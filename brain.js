// ============================================================
// JARVIS 3.2
// brain.js
// Local Brain — No API Required
// ============================================================

class JarvisBrain {

    constructor() {
        this.name = "JARVIS";
        this.history = [];
    }

    remember(userText, jarvisText) {

        this.history.push({
            user: userText,
            jarvis: jarvisText,
            time: new Date().toISOString()
        });

        if (this.history.length > 30) {
            this.history.shift();
        }
    }

    understand(text) {

        const original = text.trim();
        const lower = original.toLowerCase();

        // YOUTUBE
        if (lower.includes("open youtube")) {
            return {
                type: "command",
                command: "open_youtube",
                argument: ""
            };
        }

        if (lower.includes("search youtube")) {

            const query = lower
                .replace("search youtube for", "")
                .replace("search youtube", "")
                .trim();

            return {
                type: "command",
                command: "youtube_search",
                argument: query
            };
        }

        // GOOGLE
        if (lower.includes("open google")) {
            return {
                type: "command",
                command: "open_google",
                argument: ""
            };
        }

        if (lower.includes("search google")) {

            const query = lower
                .replace("search google for", "")
                .replace("search google", "")
                .trim();

            return {
                type: "command",
                command: "google_search",
                argument: query
            };
        }

        // GMAIL
        if (lower.includes("open gmail")) {
            return {
                type: "command",
                command: "open_gmail",
                argument: ""
            };
        }

        // WHATSAPP
        if (lower.includes("open whatsapp")) {
            return {
                type: "command",
                command: "open_whatsapp",
                argument: ""
            };
        }

        // TIME
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

        // DATE
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

        // CALL
        if (lower.startsWith("call ")) {

            const contact =
                original.substring(5).trim();

            return {
                type: "command",
                command: "call",
                argument: contact
            };
        }

        // NORMAL CONVERSATION
        return {
            type: "conversation",
            command: null,
            argument: ""
        };
    }


    // ==========================================
    // LOCAL RESPONSE ENGINE
    // ==========================================

    generateResponse(text) {

        const lower =
            text.toLowerCase().trim();


        if (
            lower === "hello" ||
            lower === "hi" ||
            lower === "hey"
        ) {
            return "Hello. I'm Jarvis. How can I help you?";
        }


        if (lower.includes("who are you")) {

            return (
                "I am Jarvis, your personal AI assistant."
            );
        }


        if (lower.includes("how are you")) {

            return (
                "I'm online and ready to help."
            );
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


        if (lower.includes("your name")) {

            return "My name is Jarvis.";
        }


        if (lower.includes("what can you do")) {

            return (
                "I can understand commands, open websites, " +
                "search the web, use voice input and speak responses."
            );
        }


        // Hindi responses

        if (
            lower.includes("namaste") ||
            lower.includes("नमस्ते")
        ) {

            return "Namaste! Main Jarvis hoon. Aap kya karna chahte hain?";
        }


        if (
            lower.includes("kaise ho") ||
            lower.includes("कैसे हो")
        ) {

            return "Main bilkul ready hoon. Aap bataiye.";
        }


        if (
            lower.includes("mera naam")
        ) {

            return "Aapka naam mujhe abhi bataya nahi gaya hai.";
        }


        return (
            "I can understand your command, but my " +
            "generative AI connection has not been connected yet."
        );
    }


    // ==========================================
    // MAIN PROCESSOR
    // ==========================================

    async process(text) {

        const result =
            this.understand(text);


        // COMMAND
        if (result.type === "command") {

            let response = "";


            switch (result.command) {

                case "open_youtube":

                    response =
                        "Opening YouTube.";

                    break;


                case "youtube_search":

                    response =
                        "Searching YouTube for " +
                        result.argument + ".";

                    break;


                case "open_google":

                    response =
                        "Opening Google.";

                    break;


                case "google_search":

                    response =
                        "Searching Google for " +
                        result.argument + ".";

                    break;


                case "open_gmail":

                    response =
                        "Opening Gmail.";

                    break;


                case "open_whatsapp":

                    response =
                        "Opening WhatsApp.";

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
                        result.argument + ".";

                    break;


                default:

                    response =
                        "Command received.";
            }


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


            this.remember(
                text,
                response
            );


            return response;
        }


        // CONVERSATION

        const response =
            this.generateResponse(text);


        this.remember(
            text,
            response
        );


        return response;
    }
}


// ==========================================
// GLOBAL JARVIS
// ==========================================

window.jarvisBrain =
    new JarvisBrain();
