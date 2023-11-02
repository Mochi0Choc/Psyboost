function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var message = messageInput.value.trim();
    if (message === "") {
        return;
    }

    var chatBox = document.getElementById("chat-box");
    var userMessageElement = document.createElement("div");
    userMessageElement.className = "user-message";
    userMessageElement.textContent = "You: " + message;
    chatBox.appendChild(userMessageElement);

    // Send the user message to the server and get a response
    fetch('/chat', {
        method: 'POST',
        body: JSON.stringify({ message: message }),  // Ensure 'message' key is present
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        var chatBotMessageElement = document.createElement("div");
        chatBotMessageElement.className = "chatbot-message";
        chatBotMessageElement.textContent = "Psyboost: " + data.response;
        chatBox.appendChild(chatBotMessageElement);

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;

        // Print entire conversation history to console (for debugging)
        console.log(data.conversation);
    });

    // Clear the message input field
    messageInput.value = "";
}
