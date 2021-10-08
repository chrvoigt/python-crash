import sys
import pyttsx3

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('pip3 install pyttsx3')
    sys.exit()
'''
sqnj
skqmld
sqkdjoj
'''
tts = pyttsx3.init()  # Initialize the TTS engine.

print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('Input: ')
    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say it.