import speech_recognition as sr
from os import path
from pydub import AudioSegment

def transcribeFn():


        # convert mp3 file to wav                                                       
        sound = AudioSegment.from_mp3("/home/tejas/Desktop/My STuff/27-10-2022/Progress/output.wav")
        sound.export("/home/tejas/Desktop/My STuff/27-10-2022/Progress/output.wav", format="wav")


        # transcribe audio file                                                         
        AUDIO_FILE = "/home/tejas/Desktop/My STuff/27-10-2022/Progress/output.wav"

        # use the audio file as the audio source                                        
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file                  

                x = r.recognize_google(audio)
                return x

