// ============================================================
// JARVIS 3.2
// commands.js
// Command & Action Engine
// ============================================================

async function executeCommand(command, argument) {

    switch (command) {

        // =========================
        // YOUTUBE
        // =========================

        case "open_youtube":
            window.open("https://www.youtube.com", "_blank");
            break;

        case "youtube_search":
            if (argument) {
                const youtubeURL =
                    "https://www.youtube.com/results?search_query=" +
                    encodeURIComponent(argument);

                window.open(youtubeURL, "_blank");
            }
            break;


        // =========================
        // GOOGLE
        // =========================

        case "open_google":
            window.open("https://www.google.com", "_blank");
            break;

        case "google_search":
            if (argument) {
                const googleURL =
                    "https://www.google.com/search?q=" +
                    encodeURIComponent(argument);

                window.open(googleURL, "_blank");
            }
            break;


        // =========================
        // GMAIL
        // =========================

        case "open_gmail":
            window.open("https://mail.google.com", "_blank");
            break;

        case "gmail_search":
            if (argument) {
                const gmailURL =
                    "https://mail.google.com/mail/u/0/#search/" +
                    encodeURIComponent(argument);

                window.open(gmailURL, "_blank");
            }
            break;


        // =========================
        // WHATSAPP
        // =========================

        case "open_whatsapp":
            window.open("https://web.whatsapp.com", "_blank");
            break;


        // =========================
        // TIME
        // =========================

        case "get_time":
            console.log(
                "Current time:",
                new Date().toLocaleTimeString()
            );
            break;


        // =========================
        // DATE
        // =========================

        case "get_date":
            console.log(
                "Current date:",
                new Date().toLocaleDateString()
            );
            break;


        // =========================
        // CALL
        // =========================

        case "call":

            if (argument) {

                const phoneNumber =
                    argument.replace(/[^0-9+]/g, "");

                if (phoneNumber) {
                    window.location.href =
                        "tel:" + phoneNumber;
                } else {
                    console.log(
                        "A phone number is required for calling."
                    );
                }

            }

            break;


        // =========================
        // UNKNOWN COMMAND
        // =========================

        default:

            console.log(
                "Unknown Jarvis command:",
                command,
                argument
            );
    }
}


// Make the function available globally
window.executeCommand = executeCommand;
