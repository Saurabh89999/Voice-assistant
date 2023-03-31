import openai
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key = "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"
completion = openai.Completion()
def reply(question):
  prompt=f"Human: {question} \nAI: "
  response =completion.create(prompt=prompt, engine="text-davinci-003", stop=['\Human'], max_tokens=200 )
  answer = response.choices[0].text.strip()
  return answer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(text):
  engine.say(text)
  engine.runAndWait()

speak("Hello, How can i help you")

def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Listening....')
    audio = r.listen(source)
  try:
    print("Recognizing....")
    query = r.recognize_google(audio, language='en-in')
    print("Human said: {}\n".format(query))
  except Exception as e:
    print("Say that again....")
    return "None"
  return query

if __name__ == '__main__':
  while True:
    query = takecommand().lower()
    ans = reply(query)
    print(ans)
    speak(ans)
    if 'open youtube' in query:
      webbrowser.open('www.youtube.com')
    if 'open google' in query:
      webbrowser.open('www.google.com')
    if 'bye' in query:
      break


