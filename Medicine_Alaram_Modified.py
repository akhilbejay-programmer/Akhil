import time
from datetime import datetime, timedelta
import pyttsx3
try: 
  class medical:
   def __init__(self):
     print("Welcome to medical mini agent akki,")
     self.voice("Welcome to medical mini agent akki. please enter the detaits required below",0)
     while True:
      self.name_of_medicine=input("Enter Name of the Medicine: ")
      if len(self.name_of_medicine) == 0:
        print("Please enter the name of the medicine")
        self.voice("Please enter the name of the medicine",1)
      else: 
        while True:
         try: 
          self.remainder=input(f"Enter your time for Remainding your medicine {self.name_of_medicine} as in the formate 24hrs(HH:MM:SS): ")
          self.alaram=datetime.strptime(self.remainder,"%H:%M:%S").time()
          self.next_alaram=datetime.combine(datetime.today(),self.alaram).replace(microsecond=0)
          break
         except ValueError:
           print("PLease enter the time as given above formate")
           self.voice("PLease enter the time as given above formate",0)
        break   
   def voice(self,text,voicer):
      engine = pyttsx3.init()
      voices = engine.getProperty('voices')
      engine.setProperty('voice', voices[voicer].id)
      engine.say(text)  
      engine.runAndWait()
   def logic(self):
      while True:
          self.current_time = datetime.now().replace(microsecond=0)
          print("Current Time: ",self.current_time, end="\r")
          if self.current_time > self.next_alaram:
            print("You have entered lesser time than the current time so please enter the exact time for setup your remainder")
            self.voice("You have entered lesser time than the current time so please enter the exact time for setup your remainder",1)
            break
          elif self.current_time == self.next_alaram:
            print(f"\nAlarm ringing! Now its Time for Medicine {self.name_of_medicine}...")
            for i in range(10):
               if i in [1,3,5,7,9]:
                self.voice(f"Now its time for medicine {self.name_of_medicine} ",0)
               else:
                self.voice(f"Now its time for medicine {self.name_of_medicine} ",1) 
            self.next_alaram +=timedelta(hours=self.interval)  
            print(f"Your next alaram is set for {self.next_alaram.strftime("%d-%m-%Y %H:%M:%S")}")
            self.voice(f"Your next alaram is set for {self.next_alaram.strftime("%m-%d-%Y %H:%M:%S")} so please wait for the remainder",1)
          time.sleep(1) 
   def main(self): 
    while True:
      try:
       self.no_of_times=int(input("Enter the medicine no of times in a day: "))
      except ValueError:
        print("Please enter the valid Number")
        self.voice("Please enter the valid Number",1)
        return
      if self.no_of_times > 0 and self.no_of_times < 4: 
         self.interval=24/self.no_of_times
         print("Your Setup is completed!\nThanking You!\nPlease wait for the  Remainder........................\nExiting..............")
         self.voice("Your Setup is completed! Thanking You! Please wait for the  Remainder Exiting..............",0)
         self.logic()
         break
      else:
         print("Please enter a valid Number for the medicine no of time in a day intervel[greater then 0 and lesser than 4]")
         self.voice("Please enter a valid Number for the medicine no of time in a day intervel greater then 0 and lesser than 4",1)
  obj=medical()
  while True:        
    obj.main()
except Exception as e:
  print("Something went wrong please check back",e)