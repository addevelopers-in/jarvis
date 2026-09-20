// ============================================================
// JARVIS 3.2
// brain.js
// Virtual Brain
// ============================================================

class JarvisBrain {

    constructor() {
        this.name = "JARVIS";
        this.history = [];
    }

    // --------------------------------------------------------
    // MEMORY
    // --------------------------------------------------------

    remember(userText, jarvisText) {

        this.history.push({
            user: userText,
            jarvis: jarvisText,
            time: new Date().toISOString()
        });

        // Keep the browser session lightweight
        if (this.history.length > 20) {
            this.history.shift();
        }
    }


    // --------------------------------------------------------
    // UNDERSTAND COMMAND
    // --------------------------------------------------------

    understand(text) {

        const original = text.trim();
        const lower = original.toLowerCase();


        // =========================
        // YOUTUBE
        // =========================

        if (lower === "open youtube" ||
            lower.includes("open youtube")) {

            return {
                type: "command",
                command: "open_youtube",
                argument: ""
            };
        }


        if (
            lower.includes("search youtube for") ||
            lower.includes("search youtube")
        ) {

            let query = lower
                .replace("search youtube for", "")
                .replace("search youtube", "")
                .trim();

            return {
                type: "command",
                command: "youtube_search",
                argument: query
            };
        }


        // =========================
        // GOOGLE
        // =========================

        if (
            lower === "open google" ||
            lower.includes("open google")
        ) {

            return {
                type: "command",
                command: "open_google",
                argument: ""
            };
        }


        if (lower.includes("search google for")) {

            let query = lower
                .replace("search google for", "")
                .trim();

            return {
                type: "command",
                command: "google_search",
                argument: query
            };
        }


        if (lower.startsWith("search for")) {

            let query = lower
                .replace("search for", "")
                .trim();

            return {
                type: "command",
                command: "google_search",
                argument: query
            };
        }


        // =========================
        // GMAIL
        // =========================

        if (
            lower === "open gmail" ||
            lower.includes("open gmail")
        ) {

            return {
                type: "command",
                command: "open_gmail",
                argument: ""
            };
        }


        if (lower.includes("search gmail for")) {

            let query = lower
                .replace("search gmail for", "")
                .trim();

            return {
                type: "command",
                command: "gmail_search",
                argument: query
            };
        }


        // =========================
        // WHATSAPP
        // =========================

        if (
            lower === "open whatsapp" ||
            lower.includes("open whatsapp")
        ) {

            return {
                type: "command",
                command: "open_whatsapp",
                argument: ""
            };
        }


        // =========================
        // TIME
        // =========================

        if (
            lower === "time" ||
            lower.includes("what time") ||
            lower.includes("current time")
        ) {

            return {
                type: "command",
                command: "get_time",
                argument: ""
            };
        }


        // =========================
        // DATE
        // =========================

        if (
            lower === "date" ||
            lower.includes("what date") ||
            lower.includes("today's date")
        ) {

            return {
                type: "command",
                command: "get_date",
                argument: ""
            };
        }


        // =========================
        // CALL
        // =========================

        if (lower.startsWith("call ")) {

            const contact = original
                .substring(5)
                .trim();

            return {
                type: "command",
                command: "call",
                argument: contact
            };
        }


        // =========================
        // CONVERSATION
        // =========================

        return {
            type: "conversation",
            command: null,
            argument: ""
        };
    }


    // --------------------------------------------------------
    // NORMAL AI-STYLE RESPONSE
    // --------------------------------------------------------

    generateResponse(text) {

        const lower = text.toLowerCase().trim();


        if (
            lower === "hello" ||
            lower === "hi" ||
            lower === "hey"
        ) {

            return "Hello. I'm Jarvis. How can I help you?";
        }


        if (lower.includes("how are you")) {

            return "I'm online and ready to help.";
        }


        if (lower.includes("who are you")) {

            return "I am Jarvis, your personal AI assistant.";
        }


        if (
            lower.includes("thank you") ||
            lower.includes("thanks")
        ) {

            return "You're welcome.";
        }


        if (lower.includes("good morning")) {

            return "Good morning. Jarvis is online.";
        }


        if (lower.includes("good night")) {

            return "Good night. I'll be here when you need me.";
        }


        if (lower.includes("jarvis")) {

            return "Yes, I'm listening.";
        }


        return (
            "I understand you. " +
            "I'm ready to connect to my generative AI system."
        );
    }


    // --------------------------------------------------------
    // PROCESS MESSAGE
    // --------------------------------------------------------

    async process(text) {

        const result = this.understand(text);


        // =========================
        // COMMAND
        // =========================

        if (result.type === "command") {

            let response = "";

            switch (result.command) {

                case "open_youtube":

                    response = "Opening YouTube.";
                    break;


                case "youtube_search":

                    response =
                        "Searching YouTube for " +
                        result.argument + ".";

                    break;


                case "open_google":

                    response = "Opening Google.";
                    break;


                case "google_search":

                    response =
                        "Searching Google for " +
                        result.argument + ".";

                    break;


                case "open_gmail":

                    response = "Opening Gmail.";
                    break;


                case "gmail_search":

                    response =
                        "Searching Gmail for " +
                        result.argument + ".";

                    break;


                case "open_whatsapp":

                    response = "Opening WhatsApp.";
                    break;


                case "get_time":

                    response =
                        "The time is " +
                        new Date().toLocaleTimeString();

                    break;


                case "get_date":

                    response =
                        "Today is " +
                        new Date().toLocaleDateString();

                    break;


                case "call":

                    response =
                        "I received your request to call " +
                        result.argument +
                        ". Phone integration will be connected later.";

                    break;


                default:

                    response = "Command received.";
            }


            // Send command to commands.js
            if (
                typeof executeCommand === "function"
            ) {

                try {

                    await executeCommand(
                        result.command,
                        result.argument
                    );

                } catch (error) {

                    console.error(
                        "Command error:",
                        error
                    );
                }
            }


            this.remember(text, response);

            return response;
        }


        // =========================
        // GENERATIVE AI RESPONSE
        // =========================

        const response =
            this.generateResponse(text);

        this.remember(text, response);

        return response;
    }
}


// ============================================================
// CREATE GLOBAL JARVIS BRAIN
// ============================================================

window.jarvisBrain = new JarvisBrain();
