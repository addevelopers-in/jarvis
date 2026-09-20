import webbrowser
import urllib.parse
from datetime import datetime


def open_url(url):
    try:
        webbrowser.open(url)
        return True
    except Exception:
        return False


def open_youtube():
    return open_url("https://www.youtube.com")


def open_google():
    return open_url("https://www.google.com")


def open_gmail():
    return open_url("https://mail.google.com")


def open_whatsapp():
    return open_url("https://web.whatsapp.com")


def google_search(query):
    if not query:
        return False

    query = urllib.parse.quote_plus(query)
    return open_url(
        f"https://www.google.com/search?q={query}"
    )


def youtube_search(query):
    if not query:
        return False

    query = urllib.parse.quote_plus(query)
    return open_url(
        f"https://www.youtube.com/results?search_query={query}"
    )


def gmail_search(query):
    if not query:
        return open_gmail()

    query = urllib.parse.quote_plus(query)
    return open_url(
        f"https://mail.google.com/mail/u/0/#search/{query}"
    )


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%d %B %Y")


def call_contact(contact):
    return {
        "action": "call",
        "contact": contact,
        "status": "phone_bridge_pending"
    }


def send_whatsapp(contact, message):
    return {
        "action": "whatsapp",
        "contact": contact,
        "message": message,
        "status": "phone_bridge_pending"
    }


def execute_command(command, argument=""):

    command = command.lower().strip()
    argument = argument.strip()

    if command == "open_youtube":
        return open_youtube()

    if command == "open_google":
        return open_google()

    if command == "open_gmail":
        return open_gmail()

    if command == "open_whatsapp":
        return open_whatsapp()

    if command == "google_search":
        return google_search(argument)

    if command == "youtube_search":
        return youtube_search(argument)

    if command == "gmail_search":
        return gmail_search(argument)

    if command == "get_time":
        return get_time()

    if command == "get_date":
        return get_date()

    if command == "call":
        return call_contact(argument)

    return False
