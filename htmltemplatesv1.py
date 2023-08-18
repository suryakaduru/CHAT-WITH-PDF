css = '''
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }

    .chat-message.user {
        background-color: #FF6B6B; /* User message color */
    }

    .chat-message.bot {
        background-color: #58B19F; /* Bot message color */
    }

    .chat-message .avatar {
        width: 20%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .chat-message .message {
        width: 80%;
        padding: 1rem;
        color: #fff;
        font-size: 0.9rem;
        line-height: 1.3;
        background-color: #1E262D;
        border-radius: 0.3rem;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/128/2593/2593627.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/128/1077/1077012.png" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
