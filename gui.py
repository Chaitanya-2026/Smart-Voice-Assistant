import tkinter as tk
from tkinter import scrolledtext
from assistant import AssistantController


class VoiceAssistantWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("🎤 Smart Voice Assistant")
        self.root.geometry("550x650")
        self.root.configure(bg="#1e1e2e")

        # Controller
        self.controller = AssistantController()

        # Title Label (fixed at top center)
        self.title_label = tk.Label(
            root,
            text="🤖 Smart Voice Assistant",
            font=("Helvetica", 20, "bold"),
            fg="cyan",
            bg="#1e1e2e"
        )
        self.title_label.pack(pady=(15, 5))

        # Status Label (below title)
        self.status_label = tk.Label(
            root,
            text="Idle",
            font=("Helvetica", 12, "italic"),
            fg="lightgreen",
            bg="#1e1e2e"
        )
        self.status_label.pack()

        # Scrollable Chat Area
        self.text_box = scrolledtext.ScrolledText(
            root,
            wrap="word",
            bg="#2e2e3e",
            fg="white",
            font=("Consolas", 12),
            height=20
        )
        self.text_box.pack(expand=True, fill="both", padx=15, pady=15)

        # Button Frame
        button_frame = tk.Frame(root, bg="#1e1e2e")
        button_frame.pack(pady=10)

        self.listen_button = tk.Button(
            button_frame, text="🎙️ Ask", command=self.listen_and_process,
            bg="#009688", fg="white", font=("Helvetica", 12, "bold"), width=12
        )
        self.listen_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(
            button_frame, text="🧹 Clear", command=self.clear_text,
            bg="#FFA500", fg="white", font=("Helvetica", 12, "bold"), width=12
        )
        self.clear_button.grid(row=0, column=1, padx=5)

        self.exit_button = tk.Button(
            button_frame, text="❌ Exit", command=root.quit,
            bg="#E53935", fg="white", font=("Helvetica", 12, "bold"), width=12
        )
        self.exit_button.grid(row=0, column=2, padx=5)

    def append_log(self, text, speaker="System"):
        """Add text with label (User/Assistant/System)"""
        self.text_box.insert(tk.END, f"{speaker}: {text}\n")
        self.text_box.see(tk.END)

    def clear_text(self):
        self.text_box.delete("1.0", tk.END)

    def listen_and_process(self):
        """Listen, process, show in GUI, and speak every time."""
        self.update_status("Listening...", "yellow")

        user_text = self.controller.listen()
        if user_text:
            self.append_log(user_text, "You")
            self.update_status("Thinking...", "orange")

            response = self.controller.process(user_text)
            self.append_log(response, "Assistant")

            # Always speak response
            self.update_status("Speaking...", "cyan")
            self.controller.speak(response)

        self.update_status("Idle", "lightgreen")

    def update_status(self, message, color):
        """Update the separate status label below the fixed title"""
        self.status_label.config(text=message, fg=color)
        self.root.update_idletasks()
