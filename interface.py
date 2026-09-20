from flask import Flask, request, jsonify, render_template_string
from brain import JarvisBrain

app = Flask(__name__)
brain = JarvisBrain()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JARVIS 3.2</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background: #03060a;
            color: #00e5ff;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 900px;
            margin: auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            letter-spacing: 8px;
            margin-bottom: 5px;
        }

        .status {
            text-align: center;
            color: #00ff88;
            margin-bottom: 20px;
        }

        #chat {
            height: 65vh;
            overflow-y: auto;
            background: #080d13;
            border: 1px solid #12313a;
            border-radius: 15px;
            padding: 20px;
        }

        .message {
            margin: 12px 0;
            padding: 12px;
            border-radius: 10px;
            line-height: 1.5;
        }

        .user {
            background: #10232b;
            color: white;
        }

        .jarvis {
            background: #071c20;
            color: #00e5ff;
        }

        .controls {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        input {
            flex: 1;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #16444e;
            background: #080d13;
            color: white;
            font-size: 16px;
        }

        button {
            padding: 15px 20px;
            border: none;
            border-radius: 10px;
            background: #00e5ff;
            color: black;
            font-weight: bold;
        }

        button:active {
            transform: scale(0.97);
        }
    </style>
</head>

<body>

<div class="container">

    <h1>JARVIS 3.2</h1>

    <div class="status">
        ● ONLINE
    </div>

    <div id="chat">
        <div class="message jarvis">
            JARVIS: Systems online. How can I help?
        </div>
    </div>

    <div class="controls">

        <input
            id="message"
            placeholder="Talk to Jarvis..."
            autocomplete="off"
        >

        <button onclick="sendMessage()">
            SEND
        </button>

        <button onclick="startVoice()">
            🎙
        </button>

    </div>

</div>

<script>

async function sendMessage() {

    const input = document.getElementById("message");
    const text = input.value.trim();

    if (!text) return;

    addMessage("YOU", text, "user");

    input.value = "";

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: text
            })

        });

        const data = await response.json();

        addMessage(
            "JARVIS",
            data.response,
            "jarvis"
        );

        speak(data.response);

    } catch (error) {

        addMessage(
            "JARVIS",
            "Connection error.",
            "jarvis"
        );
    }
}


function addMessage(name, text, type) {

    const chat = document.getElementById("chat");

    const message = document.createElement("div");

    message.className = "message " + type;

    message.innerHTML =
        "<strong>" +
        name +
        ":</strong> " +
        escapeHtml(text);

    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;
}


function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


function speak(text) {

    if (!("speechSynthesis" in window))
        return;

    const speech =
        new SpeechSynthesisUtterance(text);

    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}


function startVoice() {

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if (!SpeechRecognition) {

        addMessage(
            "JARVIS",
            "Voice recognition is not supported by this browser.",
            "jarvis"
        );

        return;
    }

    const recognition =
        new SpeechRecognition();

    recognition.lang = "en-IN";

    recognition.start();

    recognition.onresult = function(event) {

        const text =
            event.results[0][0].transcript;

        document.getElementById(
            "message"
        ).value = text;

        sendMessage();
    };
}


document.getElementById("message")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "response": "Please say something."
        })

    try:

        response = brain.process(message)

        return jsonify({
            "response": response
        })

    except Exception as error:

        return jsonify({
            "response": "Jarvis encountered an error."
        })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
