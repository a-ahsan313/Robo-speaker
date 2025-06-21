import os
def speak(text):
    # use only for windows
    os.system(f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"') 

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1. Created by Ahsan")
    while True:
        question = input("Enter what you want me to speak(or 'q' to quit): ")
        if question.lower() == 'q':
            break 
        speak(question)    