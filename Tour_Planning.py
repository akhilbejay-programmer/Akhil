import pyttsx3
try:
    class tour_planning_agent():
        def __init__(self):
            print("Welcome to Indian Government Tourist Planning agent akki,")
            self.voice("Welcome to Indian Government Tourist Planning agent akki",1)
            self.india={"Andhra Pradesh":{"Tirumala Temple":1500,"Araku Valley":2000,"Borra Caves":1500,"Gandikota":1500,"Lambasingi":1500,"Belum Caves":1200,"Srisailam":1500,"Rushikonda Beach":1000,"Yarada Beach":1000,"Horsley Hills":1500},"Telangana":{"Charminar":1500,"Golconda Fort":1500,"Ramoji Film City":3000,"Yadadri Temple":1500,"Nagarjuna Sagar":2000},"Tamil Nadu":{"Meenakshi Amman Temple":1500,"Ooty":2500,"Kodaikanal":2500,"Rameswaram":2000,"Mahabalipuram":2000},"Karnataka":{"Mysore Palace":1500,"Hampi":2000,"Coorg":2000,"Jog Falls":2000,"Gokarna":2000},"Kerala":{"Munnar":2000,"Alappuzha":2500,"Thekkady":2000,"Kovalam Beach":2000,"Wayanad":2000},"Arunachal Pradesh":{"Tawang Monastery":2500,"Sela Pass":2000,"Ziro Valley":2000,"Namdapha National Park":2500,"Bomdila":2000},"Assam":{"Kaziranga National Park":2500,"Kamakhya Temple":1500,"Majuli":1500,"Manas National Park":2500,"Haflong":2000},"Bihar":{"Mahabodhi Temple":1500,"Nalanda University Ruins":1500,"Rajgir":1500,"Vaishali":1500,"Vikramshila Ruins":1500},
                   "Chhattisgarh":{"Chitrakote Falls":1500,"Tirathgarh Falls":1500,"Kanger Valley National Park":2000,"Barnawapara Wildlife Sanctuary":2000,"Bhoramdeo Temple":1500},"Goa":{"Baga Beach":2000,"Calangute Beach":2000,"Fort Aguada":1500,"Dudhsagar Falls":2500,"Basilica of Bom Jesus":1500},"Gujarat":{"Statue of Unity":2000,"Gir National Park":2500,"Rann of Kutch":2000,"Somnath Temple":1500,"Dwarkadhish Temple":1500},"Haryana":{"Kurukshetra":1500,"Sultanpur National Park":1500,"Morni Hills":2000,"Pinjore Gardens":1500,"Damdama Lake":1500},"Himachal Pradesh":{"Shimla":2000,"Manali":2500,"Dharamshala":2000,"Spiti Valley":3000,"Kasol":2000},"Jharkhand":{"Hundru Falls":1500,"Dassam Falls":1500,"Betla National Park":2000,"Parasnath Hill":1500,"Patratu Valley":1500},"Madhya Pradesh":{"Khajuraho Group of Monuments":2000,"Kanha National Park":2500,"Sanchi Stupa":1500,"Bhimbetka Rock Shelters":1500,"Pachmarhi":2000},"Maharashtra":{"Gateway of India":1500,"Ajanta Caves":2000,"Ellora Caves":2000,"Mahabaleshwar":2000,"Lonavala":2000},
                   "Manipur":{"Loktak Lake":2000,"Keibul Lamjao National Park":2000,"Kangla Fort":1500,"Shree Govindajee Temple":1000,"Andro Village":1500},"Meghalaya":{"Double Decker Living Root Bridge":2000,"Nohkalikai Falls":2000,"Umiam Lake":2000,"Mawlynnong":2000,"Dawki":2000},"Mizoram":{"Reiek":2000,"Vantawng Falls":2000,"Phawngpui":2500,"Tam Dil":2000,"Solomon's Temple":1500},"Nagaland":{"Kohima War Cemetery":1500,"Dzukou Valley":2500,"Khonoma":2000,"Japfu Peak":2500,"Shilloi Lake":2000},"Odisha":{"Jagannath Temple":1500,"Konark Sun Temple":2000,"Chilika Lake":2000,"Lingaraja Temple":1500,"Udayagiri and Khandagiri Caves":1500},"Punjab":{"Golden Temple":1500,"Jallianwala Bagh":1500,"Wagah Border":1500,"Anandpur Sahib":1500,"Rock Garden":1500},"Rajasthan":{"Hawa Mahal":2000,"Amber Fort":2000,"City Palace":2000,"Jaisalmer Fort":2500,"Ranthambore National Park":3000},"Sikkim":{"Tsomgo Lake":2500,"Nathula Pass":3000,"Yumthang Valley":3000,"Pelling":2500,"Rumtek Monastery":2000},"Tripura":{"Ujjayanta Palace":1500,"Neermahal":2000,"Unakoti":2000,"Sepahijala Wildlife Sanctuary":2000,"Jampui Hills":2500},"Puducherry":{"Promenade Beach":1500,"Sri Aurobindo Ashram":1500,"Auroville":2000,"Paradise Beach":2000,"French Quarter":1500},
                   "Uttar Pradesh":{"Taj Mahal":2000,"Varanasi Ghats":1500,"Ayodhya":1500,"Fatehpur Sikri":2000,"Mathura":1500},"Uttarakhand":{"Nainital":2000,"Mussoorie":2000,"Kedarnath Temple":3000,"Rishikesh":2000,"Jim Corbett National Park":3000},"West Bengal":{"Darjeeling":2500,"Sundarbans National Park":3000,"Victoria Memorial":1500,"Kalimpong":2500,"Digha":2000},"Andaman and Nicobar Islands":{"Cellular Jail":2000,"Radhanagar Beach":2500,"Ross Island":2000,"Elephant Beach":2500,"Baratang Island":2500},"Chandigarh":{"Rock Garden":1500,"Sukhna Lake":1500,"Rose Garden":1500,"Capitol Complex":1500,"Government Museum and Art Gallery":1500},"Dadra and Nagar Haveli and Daman and Diu":{"Devka Beach":1500,"Jampore Beach":1500,"Diu Fort":2000,"Naida Caves":2000,"Vanganga Lake Garden":1500},"Delhi":{"Red Fort":1500,"Qutub Minar":1500,"India Gate":1500,"Lotus Temple":1500,"Akshardham":2000},"Jammu and Kashmir":{"Dal Lake":2500,"Gulmarg":3000,"Pahalgam":2500,"Sonamarg":3000,"Vaishno Devi Temple":2000},"Ladakh":{"Pangong Lake":3000,"Nubra Valley":3000,"Leh Palace":2000,"Magnetic Hill":2000,"Khardung La":3000},"Lakshadweep":{"Agatti Island":3000,"Bangaram Island":3500,"Kadmat Island":3000,"Kavaratti":3000,"Minicoy Island":3500}}
        def voice(self,text,voicer):
           engine=pyttsx3.init()
           voices=engine.getProperty('voices')
           engine.setProperty('voice',voices[voicer].id)
           engine.say(text)
           engine.runAndWait()
        def tourist_places(self):
            print("Your Indian Tour Guide akki is activated...........")
            self.voice("Your Indian Tour Guide akki is activated...........",1)
            found=False
            print("Here is All states(28) & Teritories(8) in India: ")
            self.indian_states=[self.states for self.states,self.places in self.india.items()]
            for i,space in enumerate(self.indian_states,start=1):
                print(f"{i:2}.{space:<35}",end="")
                if i % 4 == 0:
                    print()
            while True:
             self.state_input=input("Enter the State in India you want to plan a tour: ").strip().lower()
             if len(self.state_input)!=0:
              found=False
              for self.states,self.places in self.india.items():
                  if self.state_input == self.states.strip().lower():
                      print(f"Here is your list of Tourist places in your tour destination {self.state_input}:")
                      for self.single_place,self.budget in self.places.items():
                          print(f"*{self.single_place}")
                          found=True
                      while True:
                       self.option=input("Enter YES for Budget of your Tour Destination: ").lower()
                       if len(self.option)!=0:
                        if self.option in ["yes","y"]:
                            self.trip_budget=sum(self.places.values())
                            print(f"Here is your 1 day Budget for your trip in {self.state_input} : {self.trip_budget} approx + travelling charges")
                        else:
                           print("Your input shows your are Not Intrested to go Forword.............")
                           self.voice("Your input shows your are Not Intrested to go Forword.............",0)
                        return
                       else:
                          print("Your option should'nt be empty")
                          self.voice("Your option should'nt be empty",0)
              if not found:
               print("No matching Indian state found")
               self.voice("No matching Indian state found",1)     
             else:
                print("Your input state should'nt be Empty")   
                self.voice("Your input state should'nt be Empty",0)
        def make_plan(self):
            print("Your Indian Tour Guide akki is activated.............")
            self.voice("Your Indian Tour Guide akki is activated.............",0)
            while True:
             try:
              self.tour_budget=round(float(input("Enter the Budget for your trip in India: ")))
              self.final_budget=self.tour_budget
              while True:
               self.state_input=input("Enter the State in India you want to plan a tour: ").strip().lower()
               if len(self.state_input)!=0:
                for self.states,self.places in self.india.items():
                 if self.state_input == self.states.strip().lower():
                     if self.tour_budget >=0 and self.tour_budget >= min(self.places.values()):
                      print(f"Here is your Tour plan in {self.state_input} with {self.tour_budget}")
                      for place, budget in sorted(self.places.items(), key=lambda x:(x[1],x[0])):
                       if budget <= self.tour_budget:
                        self.tour_budget-=budget
                        print(f"*{place} -- ₹{budget}\nYour balance budget is {self.tour_budget}rs")
                       else:
                        break
                      print("This is the best plan within your budget.")
                      self.voice("This is the best plan within your budget",0)
                      if self.tour_budget > min(self.places.values()):
                          print("Your current balance is higher than the least budget trip so are you interest to plan another one more")
                          self.voice("Your current balance is higher than the least budget trip so are you interest to plan another one more then give the input below",1)
                          while True:
                           self.retry_option=input("Enter yes for re plan another trip: ").lower()
                           if len(self.retry_option)!=0:
                            if self.retry_option in ["yes","y"]:
                             self.retry=True
                            else:
                              self.retry=False 
                              print("Your input show your No Intrested to go Forword\nThank you !............")
                              self.voice("Your input show your No Intrested to go Forword\nThank you !............",1)
                            break
                           else:
                              print("Your option should'nt be empty")
                              self.voice("Your option should'nt be empty",1)
                      else:
                         self.retry=False
                break 
               else:
                  print("Your input state should'nt be empty")  
                  self.voice("Your input state should'nt be empty",1)    
              break 
             except ValueError:
                print("please enter a valid input budget")
                self.voice("please enter a valid input budget",1)
            for self.states,self.places in self.india.items():
             if self.tour_budget >=0 and self.state_input == self.states.strip().lower() and self.final_budget <min(self.places.values()):
                 print(f"Your budget {self.tour_budget}rs is too low............\nMinimum budget required is ₹{min(self.places.values())}")
                 self.voice(f"Your budget {self.tour_budget}rs is too low............\nMinimum budget required is ₹{min(self.places.values())}",0)
                 break
             elif self.tour_budget <=0:
                print("Your budget should be Greater than \"0(Zero)\"")
                self.voice("Your budget should be Greater than \"0\"",1)
                break
            if self.state_input not in [self.states.strip().lower() for self.states,self.places in self.india.items()]:
                print("No matching Indian state found")
                self.voice("No matching Indian state found",1)
        def main(self):
            print("1.View all Tourist Places\n2.Make my plan")
            while True:
             try:
              choice=int(input("Enter your option: "))
              match choice:
                  case 1:
                      self.tourist_places()
                      print("\nThank you for visting India")
                  case 2:
                      self.retry=True
                      while self.retry:
                       self.make_plan()
                  case _:
                      print("Please enter a valid input as (1 or 2)")
                      self.voice("Please enter a valid input as (1 or 2)",0)
              break
             except ValueError:
                print("please enter the Valid Number as Above")
                self.voice("please enter the Valid Number as Above",0)
    obj=tour_planning_agent()
    while True:
     obj.main()                
except Exception as e:
    print("Something went wrong please try again or contact the Developer Akhil Bejay",e)