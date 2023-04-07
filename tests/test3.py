# import rest of the libraries
import speech_recognition as sr


listener = sr.Recognizer()
print('Listening for a command...')

with sr.Microphone() as source:
    print("Say something!")
    listener.pause_threshold = 1
    print("Say something! 2") 
    listener.adjust_for_ambient_noise(source)
    print("Say something! 3") 
    input_speech = listener.listen(source)
    print('Im here')

try:
    print('Recognizing speech...')
    query = listener.recognize_google(input_speech, language='en-US')
    print(f'The input speech was: {query}')
except Exception as exception:
    print('I did not quite catch that')
    print(exception)
    print('None') 