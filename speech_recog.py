# Next, import the necessary modules:
import speech_recognition as sr

# Create a Recognizer object
r = sr.Recognizer()

# Set the language of the audio
language = 'en-US'

# Create a microphone object
mic = sr.Microphone()

# Start listening for audio
print("Listening...")
with mic as source:
    audio = r.listen(source)

# Transcribe the audio
text = r.recognize_google(audio, language=language)

# Print the transcription
print(text)