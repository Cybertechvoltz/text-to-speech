from gtts
import gTTs
from playsound
import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTs(text = "enter text to convert to mp3",
          convert into audio file",
	   lang= language,slow=false)
sp.save(audio)