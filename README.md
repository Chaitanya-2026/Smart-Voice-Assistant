# Smart-Voice-Assistant
A Python-based Smart Voice Assistant with Speech Recognition, GPT-powered responses, Text-to-Speech, and a modern Tkinter GUI.




# ✨ Features

🎤 Voice Recognition using SpeechRecognition

🗣 Text-to-Speech with pyttsx3

🤖 AI Responses powered by OpenAI GPT

🖥 Modern GUI built with Tkinter

📜 Maintains chat history within the interface

❌ Clear chat & Exit buttons for easy control


🖼️ GUI Preview

![Voice Assistant GUI](screenshot.png)


# 🛠️ Installation

1️⃣ Clone the Repository
```
git clone https://github.com/Chaitanya-2026/voice-assistant.git

cd voice-assistant
```
2️⃣ Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac

venv\Scripts\activate      # On Windows
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Set Your OpenAI API Key
```
setx OPENAI_API_KEY "your_api_key_here"   # Windows (cmd)

export OPENAI_API_KEY="your_api_key_here" # Linux / Mac
```

▶️ Run the Project
```
python main.py
```

# 📂 Project Structure
```
📦 VoiceAssistant
 ┣ 📜 main.py              # Entry point
 ┣ 📜 gui.py               # GUI interface
 ┣ 📜 assistant.py         # Assistant logic (voice, AI, speech)
 ┣ 📜 requirements.txt     # Dependencies
 ┣ 📜 README.md            # Project documentation
 ┗ 📜 .gitignore           # Ignored files
```


⚙️ Requirements

Python 3.8+

OpenAI API Key


Libraries:

speechrecognition

pyttsx3

openai

tkinter (built-in)

Install all with:
```
pip install -r requirements.txt
```
📜 License

This project is licensed under the MIT License.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

🌟 Acknowledgements

OpenAI
 for GPT models

SpeechRecognition
 for voice input

Tkinter
 for GUI
