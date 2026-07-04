

const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send");

function currentTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
    });
}

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;

    const timestamp = document.createElement("div");
    timestamp.className = "timestamp";
    timestamp.textContent = currentTime();

    message.appendChild(bubble);
    message.appendChild(timestamp);

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;

    return bubble;
}

async function sendMessage() {
    const question = messageInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(question, "user");
    messageInput.value = "";

    const aiBubble = addMessage("", "ai");

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            question: question,
        }),
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
        const { done, value } = await reader.read();

        if (done) break;

        aiBubble.textContent += decoder.decode(value);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

sendButton.addEventListener("click", sendMessage);

messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});