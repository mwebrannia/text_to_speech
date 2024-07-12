import pyttsx3

def speak_text(file_path, voice_gender='female', rate=200):
  try:
    engine = pyttsx3.init()

    #voice gender
    voices = engine.getProperty('voices')
    if voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)  # index 1 is female voice
    else:
        engine.setProperty('voice', voices[0].id)  # index 0 is male voice
        
    #speech rate
    engine.setProperty('rate', rate)

    with open(file_path, 'r') as file:
      text = file.read()

      #using the engine to say(speak) text and then stop after finishing.
      engine.say(text)
      engine.runAndWait()
      engine.stop()

  except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
  except Exception as e:
    print(f"An error occured: {e}")

file_path = "py/Apple.txt"
speak_text(file_path, voice_gender='female', rate=170)
