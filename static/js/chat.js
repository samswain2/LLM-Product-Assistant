// script.js
document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('form');
    const chatInput = document.getElementById('chat-input');
    const messagesContainer = document.querySelector('.flex-1');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userQuery = chatInput.value;
        chatInput.value = '';
        
        // Append user message
        appendMessage(userQuery, 'You');
        
        // Fetch response from server
        const response = await fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: userQuery })
        });
        const { response: assistantResponse } = await response.json();
        
        // Append assistant message
        appendMessage(assistantResponse, 'Assistant');
    });

    function appendMessage(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
        messagesContainer.appendChild(messageDiv);
    }
});
