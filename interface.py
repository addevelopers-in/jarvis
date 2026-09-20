import tkinter as tk
from tkinter import scrolledtext
import threading

from brain import JarvisBrain


class JarvisInterface:

    def __init__(self, root):

        self.root = root
        self.root.title("JARVIS 3.2")
        self.root.geometry("900x600")

        self.root.configure(bg="#050505")

        self.brain = JarvisBrain()

        # -------------------------------
        # TITLE
        # -------------------------------

        self.title = tk.Label(
            root,
            text="J A R V I S   3.2",
            font=("Arial", 28, "bold"),
            fg="#00e5ff",
            bg="#050505"
        )

        self.title.pack(pady=20)

        # -------------------------------
        # STATUS
        # -------------------------------

        self.status = tk.Label(
            root,
            text="● ONLINE",
            font=("Arial", 14, "bold"),
            fg="#00ff88",
            bg="#050505"
        )

        self.status.pack()

        # -------------------------------
        # CHAT WINDOW
        # -------------------------------

        self.chat = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 13),
            bg="#101010",
            fg="white",
            insertbackground="white"
        )

        self.chat.pack(
            padx=30,
            pady=20,
            fill=tk.BOTH,
            expand=True
        )

        self.chat.insert(
            tk.END,
            "JARVIS: Systems online.\n"
        )

        # -------------------------------
        # INPUT AREA
        # -------------------------------

        bottom = tk.Frame(
            root,
            bg="#050505"
        )

        bottom.pack(
            fill=tk.X,
            padx=30,
            pady=20
        )

        self.input_box = tk.Entry(
            bottom,
            font=("Arial", 14),
            bg="#151515",
            fg="white",
            insertbackground="white"
        )

        self.input_box.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            ipady=10
        )

        self.input_box.bind(
            "<Return>",
            self.send_message
        )

        self.send_button = tk.Button(
            bottom,
            text="SEND",
            font=("Arial", 12, "bold"),
            command=self.send_message,
            bg="#00e5ff",
            fg="black"
        )

        self.send_button.pack(
            side=tk.RIGHT,
            padx=(10, 0),
            ipadx=15,
            ipady=8
        )

        # -------------------------------
        # VOICE BUTTON
        # -------------------------------

        self.voice_button = tk.Button(
            root,
            text="🎙  ACTIVATE JARVIS",
            font=("Arial", 14, "bold"),
            command=self.voice_mode,
            bg="#151515",
            fg="#00e5ff"
        )

        self.voice_button.pack(
            pady=(0, 20),
            ipadx=20,
            ipady=10
        )

    # ========================================================
    # SEND MESSAGE
    # ========================================================

    def send_message(self, event=None):

        text = self.input_box.get().strip()

        if not text:
            return

        self.input_box.delete(0, tk.END)

        self.chat.insert(
            tk.END,
            f"\nYOU: {text}\n"
        )

        self.status.config(
            text="● THINKING",
            fg="#ffaa00"
        )

        threading.Thread(
            target=self.process_message,
            args=(text,),
            daemon=True
        ).start()

    # ========================================================
    # PROCESS
    # ========================================================

    def process_message(self, text):

        try:

            response = self.brain.process(text)

        except Exception as error:

            response = (
                "I encountered an error: "
                + str(error)
            )

        self.root.after(
            0,
            lambda: self.display_response(response)
        )

    # ========================================================
    # DISPLAY RESPONSE
    # ========================================================

    def display_response(self, response):

        self.chat.insert(
            tk.END,
            f"JARVIS: {response}\n"
        )

        self.chat.see(tk.END)

        self.status.config(
            text="● ONLINE",
            fg="#00ff88"
        )

    # ========================================================
    # VOICE MODE
    # ========================================================

    def voice_mode(self):

        self.status.config(
            text="● VOICE MODE",
            fg="#00e5ff"
        )

        self.chat.insert(
            tk.END,
            "\nJARVIS: Voice system will be "
            "connected in the next integration.\n"
        )

        self.chat.see(tk.END)


# ============================================================
# START JARVIS
# ============================================================

def main():

    root = tk.Tk()

    app = JarvisInterface(root)

    root.mainloop()


if __name__ == "__main__":
    main()
