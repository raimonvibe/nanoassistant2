
# *NanoAssistant2: Your Funny AI Buddy*

**Tired of always getting the "right" answers?** Want to have a chat with an AI that’s just as quirky as your best friend? Then NanoAssistant2 is the perfect project for you! 🤖✨

Inspired by: [NanoAssistant by reese3222](https://github.com/reese3222/nanoassistant)

## ***What's NanoAssistant2?***
NanoAssistant2 is a voice assistant project that uses **GPT-2** for generating responses, meaning you’ll get some hilariously offbeat answers that are guaranteed to make you smile. We use the **Hugging Face pipeline** to power GPT-2, and the project supports **voice input/output** using `speech_recognition` and `pyttsx3`, making it feel like you’re chatting with a real AI buddy!

## **How to Get Started**

### 1. Install Python 3.11
Make sure you have Python 3.11 installed on your system. Follow the steps below based on your operating system:

- **Windows (using PowerShell)**:
    ```powershell
    winget install Python.Python.3.11
    ```

- **macOS (using Homebrew)**:
    ```bash
    brew install python@3.11
    ```

- **Linux (Ubuntu/Debian)**:
    ```bash
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.11 python3.11-venv
    ```

### 2. Create a Virtual Environment
Navigate to your project directory and create a virtual environment using Python 3.11:
```bash
python3.11 -m venv venv
```
Activate the virtual environment:
- **Windows**:
    ```powershell
    .\venv\Scripts\Activate
    ```
- **macOS and Linux**:
    ```bash
    source venv/bin/activate
    ```

### 3. Clone the Repository
```bash
git clone https://github.com/raimonvibe/nanoassistant2.git
```

### 4. Install Dependencies
Navigate into the project directory and install the necessary dependencies inside the virtual environment:
```bash
cd nanoassistant2
pip install -r requirements.txt
```

### 5. Run the Script
Start the voice assistant by running:
```bash
python nanoassistant2.py
```

## ***Why It's Fun to Use***
- 😆 **Funny conversations**: GPT-2 can sometimes give unexpected and hilarious responses, making each interaction unique.
- 🎤 **Voice input/output**: Speak to NanoAssistant2 and have it speak back – no need for boring text chats!
- ✨ **Super customizable**: You can tweak the code to adjust the responses, speed, and style to fit your preferences.

## **Tips for Best Experience**
- **Use clear and simple prompts** to get the funniest responses. The more straightforward your question, the more creative GPT-2 gets!
- Want more randomness? **Adjust the "temperature" parameter** in the `generate_response` function. Increasing this value will make responses more unpredictable! 🔥
- If the responses are slow, consider **running the project on a machine with more processing power** or using a smaller model.

## ***Troubleshooting***
- **Audio Issues?** Ensure your microphone is connected and recognized by your system. You may need to check your system’s audio settings or permissions.
- **Slow responses?** Try reducing the `max_length` parameter in the `generate_response` function or running it on a more capable machine.

## **Have Fun!** 🎉
This project is all about having a good time and enjoying the quirky interactions with your AI buddy. Don’t take it too seriously – that’s what makes NanoAssistant2 so special!
