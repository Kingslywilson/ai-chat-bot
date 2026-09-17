const chat = document.getElementById("chat");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send");


async function sendMessage() {

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage("user", message);
    messageInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "Sending...";


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong");
        }

        addMessage("bot", data.response);


    } catch (error) {

        addMessage(
            "bot",
            "Sorry, something went wrong. Please try again."
        );

        console.error(error);

    } finally {

        sendButton.disabled = false;
        sendButton.textContent = "Send";

        messageInput.focus();

    }
}

function addMessage(type, text) {

    const messageDiv = document.createElement("div");

    messageDiv.className = `message ${type}`;

    const name =
        type === "user"
            ? "You"
            : "Assistant";


    const strong = document.createElement("strong");
    strong.textContent = name + ":";


    const paragraph = document.createElement("p");
    paragraph.textContent = text;


    messageDiv.appendChild(strong);
    messageDiv.appendChild(paragraph);


    chat.appendChild(messageDiv);

    chat.scrollTop = chat.scrollHeight;
}

sendButton.addEventListener(
    "click",
    sendMessage
);

messageInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();

        }

    }
);
