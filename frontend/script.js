console.log("script.js loaded");
const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send");

const uploadButton = document.getElementById("upload");
const pdfInput = document.getElementById("pdf-file");
const uploadStatus = document.getElementById("upload-status");

// Stores the conversation history for the current chat session.
const conversationHistory = [];

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
    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";

    addMessage(question, "user");
    conversationHistory.push({
        role: "user",
        content: question,
    });
    messageInput.value = "";
    messageInput.focus();

    const aiBubble = addMessage("", "ai");

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question: question,
                history: conversationHistory,
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
        conversationHistory.push({
            role: "assistant",
            content: aiBubble.textContent,
        });
        console.log(conversationHistory);
        sendButton.disabled = false;
        sendButton.textContent = "Send";
    } catch (error) {
        aiBubble.textContent = "❌ Unable to connect to the server.";
        console.error(error);
        sendButton.disabled = false;
        sendButton.textContent = "Send";
    }
}

async function uploadPDF() {
    console.log("Upload button clicked");

    const file = pdfInput.files[0];
    console.log(file);

    if (!file) {
        alert("Please choose a PDF first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    console.log("Sending request...");
    
    uploadButton.disabled = true;
    uploadButton.textContent = "Uploading...";
    uploadStatus.textContent =`⏳ Uploading ${file.name}...`;
    const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
    });

    console.log(response);

    if (!response.ok) {
        console.log(await response.text());
        uploadStatus.textContent = "❌ Upload failed.";
        uploadButton.disabled = false;
        uploadButton.textContent = "Upload PDF";
        return;
    }

    const result = await response.json();
    console.log(result);

    uploadStatus.textContent = `${file.name} uploaded successfully.`;
    pdfInput.value = "";
    uploadButton.disabled = false;
    uploadButton.textContent = "Upload PDF";
}


sendButton.addEventListener("click", sendMessage);
uploadButton.addEventListener("click", uploadPDF);

messageInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});
