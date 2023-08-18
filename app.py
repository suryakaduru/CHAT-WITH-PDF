import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplatesv1 import css, bot_template, user_template
from langchain.llms import HuggingFaceHub


def read_pdf(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text +=page.extract_text()
    return text

def split_text_into_chunks(text):
    text_splitter=CharacterTextSplitter(
        separator="/n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks=text_splitter.split_text(text)
    return chunks


def create_embeddings(text_chunks):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def build_convo_chain(vectorstore):
    llm = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"temperature":0.6, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_user_query(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header(f"Interactive PDF Assistant")
    user_question=st.text_input(f"Ask a question about your document")
    if user_question:
        handle_user_query(user_question)
    
    with st.sidebar:
        st.subheader(f"Your Documents")
        
        pdf_docs=st.file_uploader(f"Upload your PDF and click on Process",
                         accept_multiple_files=True, type='pdf')
        if st.button(f"Process"):
            with st.spinner(f"Processing"):
                try:
                #get pdf text
                    raw_text= read_pdf(pdf_docs)
                #get the chunks of text

                    text_chunks=split_text_into_chunks(raw_text)

                #create vector store

                    vectorstore=create_embeddings(text_chunks)

                #create conversation chain
                    
                    st.session_state.conversation=build_convo_chain(vectorstore)
                except Exception as e:
                    st.error(f"An Error occured")

             



if __name__ == '__main__':
    main()