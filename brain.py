"""
JARVIS 3.2
Virtual Brain
"""

from commands import execute_command


# ============================================================
# JARVIS BRAIN
# ============================================================

class JarvisBrain:

    def __init__(self):
        self.name = "JARVIS"
        self.history = []

    # --------------------------------------------------------
    # Remember conversation during the current session
    # --------------------------------------------------------

    def remember(self, user_text, jarvis_text):
        self.history.append({
            "user": user_text,
            "jarvis": jarvis_text
        })

        # Keep the session lightweight
        if len(self.history) > 20:
            self.history.pop(0)

    # --------------------------------------------------------
    # Detect simple commands
    # --------------------------------------------------------

    def understand(self, text):

        text = text.lower().strip()

        # YouTube
        if "open youtube" in text:
            return "open_youtube", ""

        if "youtube" in text and (
            "search" in text or
            "find" in text or
            "look for" in text
        ):
            query = text

            for phrase in [
                "search youtube for",
                "search youtube",
                "find on youtube",
                "look for on youtube"
            ]:
                query = query.replace(phrase, "")

            return "youtube_search", query.strip()

        # Google
        if "open google" in text:
            return "open_google", ""

        if "search google for" in text:
            query = text.replace(
                "search google for", ""
            ).strip()

            return "google_search", query

        if text.startswith("search for "):
            query = text.replace(
                "search for", ""
            ).strip()

            return "google_search", query

        # Gmail
        if "open gmail" in text:
            return "open_gmail", ""

        if "search gmail for" in text:
            query = text.replace(
                "search gmail for", ""
            ).strip()

            return "gmail_search", query

        # WhatsApp
        if "open whatsapp" in text:
            return "open_whatsapp", ""

        # Time
        if "what time" in text or text == "time":
            return "get_time", ""

        # Date
        if "what date" in text or text == "date":
            return "get_date", ""

        # Call
        if text.startswith("call "):
            contact = text.replace(
                "call", "", 1
            ).strip()

            return "call", contact

        return None, ""

    # --------------------------------------------------------
    # Generate normal AI-style responses
    # --------------------------------------------------------

    def generate_response(self, text):

        text_lower = text.lower().strip()

        if text_lower in ["hello", "hi", "hey"]:
            return "Hello. I'm Jarvis. How can I help you?"

        if "how are you" in text_lower:
            return "I'm running perfectly and ready to help."

        if "who are you" in text_lower:
            return (
                "I am Jarvis, your personal AI assistant."
            )

        if "thank you" in text_lower or "thanks" in text_lower:
            return "You're welcome."

        if "good morning" in text_lower:
            return "Good morning. Jarvis is online."

        if "good night" in text_lower:
            return "Good night. I'll be here when you need me."

        return (
            "I understand what you're saying. "
            "My generative AI system can handle "
            "more advanced conversations once connected."
        )

    # --------------------------------------------------------
    # Main processing function
    # --------------------------------------------------------

    def process(self, text):

        command, argument = self.understand(text)

        # If it is an executable command
        if command:

            result = execute_command(
                command,
                argument
            )

            if command == "open_youtube":
                response = "Opening YouTube."

            elif command == "open_google":
                response = "Opening Google."

            elif command == "open_gmail":
                response = "Opening Gmail."

            elif command == "open_whatsapp":
                response = "Opening WhatsApp."

            elif command == "google_search":
                response = (
                    f"Searching Google for {argument}."
                )

            elif command == "youtube_search":
                response = (
                    f"Searching YouTube for {argument}."
                )

            elif command == "gmail_search":
                response = (
                    f"Searching Gmail for {argument}."
                )

            elif command == "get_time":
                response = f"The time is {result}."

            elif command == "get_date":
                response = f"Today is {result}."

            elif command == "call":
                response = (
                    f"I received your request to call "
                    f"{argument}. Phone integration is "
                    f"being connected."
                )

            else:
                response = "Command completed."

            self.remember(text, response)

            return response

        # Otherwise treat it as conversation
        response = self.generate_response(text)

        self.remember(text, response)

        return response


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    jarvis = JarvisBrain()

    print("JARVIS 3.2 BRAIN ONLINE")
    print("Type 'exit' to stop.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Jarvis: Goodbye.")
            break

        response = jarvis.process(user_input)

        print("Jarvis:", response)
