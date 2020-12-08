import os 
import psutil 
from gtts import gTTS 
from time import sleep

 

if __name__ == "__main__":
    battery = psutil.sensors_battery() 
    language = 'en'
    if(((battery.percent) < 11) and ((battery.power_plugged) == False)):
        plugInText = f"Only {battery.percent} percent battery is available. Please connect to charger immediately."
        myobj = gTTS(text=plugInText, lang=language, slow=False) 
        myobj.save("plugInText.mp3")
        os.system("mpg321 plugInText.mp3") 
        sleep(10)
        os.remove("plugInText.mp3")
    elif(((battery.percent) == 100) and ((battery.power_plugged) == True)):
        plugOutText = f"Battery fully charged. Please remove the charger immediately."
        myobj = gTTS(text=plugOutText, lang=language, slow=False) 
        myobj.save("plugOutText.mp3")
        os.system("mpg321 plugOutText.mp3") 
        sleep(10)
        os.remove("plugOutText.mp3")
