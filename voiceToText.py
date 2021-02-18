import speech_recognition as sr
import pyaudio as pa
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()


with sr.Microphone() as source : 
    print('speak now')
    global audio1
    audio1 = r3.listen(source)
print('thing is: '+r3.recognize_google(audio1))
if 'edureka' in r2.recognize_google(audio1):
    r2 = sr.Recognizer()
    url = 'https://www.edureka.co/'
    with sr.Microphone() as source:
        print('search your query')
        audio2 = r2.listen(source)
        try: 
            get = r2.recognize_google(audio2)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
            
    

            
        
    