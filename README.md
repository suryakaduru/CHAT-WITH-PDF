# CHAT-WITH-PDF


Here is the link for the app:

[link](https://chat-with-pdf-muxsqb3xxq8n5fqqjheyci.streamlit.app/)

## DEMO
  
[DEMO video](https://github.com/suryakaduru/CHAT-WITH-PDF/assets/99175643/bcc58cd4-e2d9-45b0-8c7b-44534005776b)


## How it works

The application reads the PDF and splits the text into smaller chunks that can be then fed into a LLM. It uses huggingface embeddings to create vector representations of the chunks. The application then finds the chunks that are semantically similar to the question that the user asked and feeds those chunks to the LLM to generate a response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.


## Dependencies and Installation
----------------------------
To install the PDF Chat App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
HUGGINGFACEHUB_API_TOKEN=YOUR_SECRET_KEY
```



## Usage
-----
To use the PDF Chat App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `app.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```


## References
----
1. https://github.com/alejandro-ao/langchain-ask-pdf
2. https://pastebin.com/mcHG4cY4
