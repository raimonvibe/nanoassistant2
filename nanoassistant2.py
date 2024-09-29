import numpy as np
import speech_recognition
import pyttsx3
from transformers import pipeline

# Initialize the speech recognizer
recognizer = speech_recognition.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the Hugging Face pipeline for text generation using the GPT-2 model
text_generator = pipeline("text-generation", model="gpt2")

def listen_to_speech():
    # Start listening to the microphone for speech input
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)  # Capture the audio input

    try:
        # Use Google's speech recognition to convert audio to text
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")  # Display the recognized text
        return text
    except speech_recognition.UnknownValueError:
        # This exception occurs if the speech is not clear or not understood
        print("Sorry, I couldn't understand the audio.")
        return None
    except speech_recognition.RequestError as e:
        # This exception occurs if there's an issue with the speech recognition service
        print(f"Could not request results from the speech recognition service; {e}")
        return None

def generate_response(question):
    # Generate a text response using the Hugging Face pipeline with GPT-2
    response = text_generator(question, max_length=100, num_return_sequences=1, temperature=1.0)[0]['generated_text']
    return response  # Return the generated response

def speak_text(text):
    # Use the text-to-speech engine to convert text to spoken words
    engine.say(text)
    engine.runAndWait()  # Wait for the speaking process to complete

def main():
    while True:
        # Listen for a question from the user
        question = listen_to_speech()

        if question:
            # Generate a response based on the recognized speech
            response = generate_response(question)
            print(f"Response: {response}")  # Display the AI's generated response
            speak_text(response)  # Speak the response using text-to-speech

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
