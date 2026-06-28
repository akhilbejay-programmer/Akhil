import json
import random
import os
import pyttsx3
from collections import Counter
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE = os.path.join(BASE_DIR, "history.json")
DATABASE_FILE = os.path.join(BASE_DIR, "internal_database.json")
try:
 class product_Recommendation:
     def __init__(self):
         print("Welcome to Akhil's Product Recommendation System\nYour Recommender: akki")
         self.voice("Welcome to akhil's Product Recommendation system\nYour Recommender: akki",1)
         self.product_list={"Electronic":["Smartphone","Tablet","Smartwatch","Laptop","Desktop","Computer","Monitor","Keyboard","Mouse","Printer","Earbuds","Headphones","Bluetooth","Speaker","Soundbar","Smart TV","cctv camera","USB Flash Drive","SSD","Memory Card","Wi-Fi Router","Power Bank","Charger","USB Cable","Headset"],
                            "Fashion":["Shirts","T-Shirts","Pants","Jeans","Trousers","Shorts","Jackets","Hoodies","Sweaters","Blazers","Kurta","Suits","Sarees","Dresses","Gowns","Tops","Leggings","Skirts","kid's wear","Uniforms","shoes","Sneakers","Sandals","Slippers","boots","heels","handbags","wallets","rings","chain","luggage bage"],
                            "Kitchen":["Refrigerator","Microwave Oven","Induction Cooktop","Gas Stove","Chimney","Mixer","Grinder","Juicer","kettle","Rice Cooker","Dishwasher","Water Purifier","Frying Pan","Non-Stick Pan","Cooking Pot","Knife Set","Cutting Board","spoons","fork","Measuring Cups","Scissors","Plates","Bowls","Mugs","Glasses","Water Bottles","Flask","Dust Bin"],
                            "Home":["Air conditioner","AC","Sofa","Recliner Chair","Dining Table","Bed","Mattress","Wardrobe","Bookshelf","Wall Clock","Photo Frames","Mirrors","bed lamps","candles","lights","ceiling fan","Bedsheets","Blankets","Pillows","Pillow Covers","door mats","Vacuum Cleaner","Broomstick","Washing Machine","Air Cooler","Iron Box","heater","Sewing","Machine"],
                            "Beauty":["Face Wash","Cleanser","Moisturizer","Face Cream","Sunscreen","Face Serum","Face Mask","Lip Balm","Eye Cream","Aloe Vera Gel","Blush","Highlighter","Kajal","Eyeliner","Mascara","Eyebrow Pencil","Lipstick","Shampoo","Conditioner","Hair Oil","Hair Spray","Hair Gel","Hair Color","Hair Dryer","Hair Straightener","soap","Body Wash","Perfume","Deodorant","Shaving Cream","Trimmer","women's Sanitary Pads","Nail Cutter","Makeup Brush Set","Nail Polish","Nail Polish Remover"],
                            "Health":["Multivitamins","Vitamin C Tablets","Vitamin D Tablets","protein","energy","iron","zinc","Dumbbells","Treadmill","Exercise cycle","Jump Rope","Yoga Mat","Digital Thermometer","Blood Pressure Monitor","weight machine","first aid","Bandages","Cotton Rolls","Medical Tape","Antiseptic Solution","Hand Sanitizer","Toothbrush","Toothpaste","Mouthwash","Tongue Cleaner","Green Tea","Oats","Dry Fruits"],
                            "Sport":["Cricket Ball","Batting Gloves","Wicket Keeping Gloves","Cricket Pads","Helmet","Thigh Guard","Arm Guard","Cricket Shoes","Stumps","Football","Football Shoes","Goalkeeper Gloves","Football Jersey","Goal Net","Basketball Shoes","Shuttlecock","Badminton Net","Tennis Ball","Volleyball Net","Knee Pads","Volleyball Shoes","Table Tennis Bat","Skipping Rope","Bicycle","Cycling Helmet","Running Shoes","Track Pants","Swimming Goggles","Tent","Sleeping Bag","Water Bottle","Sports Bag"],
                            "Toys_Games":["Number Learning Board","Puzzle Sets","Building Blocks","Shape Sorter","Kit","Flash Cards","Robot Toys","Fashion Dolls","Baby Dolls","Dollhouse","RC Cars","RC Bikes","RC Boats","RC Helicopters","RC Drones","Chess","Carrom Board","Ludo","Snakes and Ladders","Business Game","Playing Cards","UNO Cards","Kite","Water Guns","Bubble Maker","Teddy Bear","Toy Piano","Toy Guitar","Toy Drum Set","Musical Keyboard","Coloring Books","Crayons","Sketch Pens","Video Game"],
                            "Automotive":["Seat Covers","Steering Wheel Cover","Car Floor Mats","Car Air Freshener","Car Charger","Sun Shades","Dashboard Camera","Car Vacuum Cleaner","Car Cover","Helmet","Riding Gloves","Bike Cover","Tank Pad","Bike Cleaning Kit","GPS Navigation Device","Reverse Parking Camera","Parking Sensors","Bluetooth Car Kit","Car Speakers","Amplifier","Engine Oil","Coolant","Brake oil","Gear Oil","Engine Cleaner","Fuel","Car Wash Shampoo","Car Tire","Bike Tire","Alloy Wheels","Wheel Covers","LED Headlights","Indicator Lights","Air Filter","Spark Plug","Battery","Side Mirrors","EV Charger","Charging Cable"],
                            "Stationery":["Ball Pens","Pencils","Erasers","Sharpeners","Markers","Highlighters","Sketch Pens","Notebooks","Writing Pads","Printer Paper","Chart Paper","Drawing Sheets","Graph Paper","Water Colors","Crayons","Paint Brushes","School Bag","Pencil Box","Geometry Box","Scale (Ruler)","Protractor","Compass Box","School Labels","Book Covers","Stapler","Paper Clips","Rubber Bands","Punch Machine","File Folders","Document Files","Pen Stand","Printer Ink","letter pad","Glue Stick","tape","Whiteboard","Notice Board","Push Pins","calculator"],
                            "Groceries":["Apple","Banana","Mango","Orange","Grapes","Pineapple","Watermelon","Papaya","Pomegranate","Guava","Tomato","Potato","Onion","Carrot","Cabbage","Cauliflower","Lady Finger","Green Chilli","Basmati Rice","Wheat Flour (Atta)","Maida","Ragi Flour","Toor Dal","Moong Dal","Chana Dal","Urad Dal","Sugar","Salt","Jaggery","Cooking Oil","Ghee","Vinegar","Baking Soda","Turmeric Powder","Red Chilli Powder","Coriander Powder","Garam Masala","Cumin Seeds","Mustard Seeds","Black Pepper","Cardamom","Cloves","Milk","Curd","Butter","Cheese","Paneer","coffee powder","tea powder","Cream"],
                            "Food":["Rice","Biryani","Fried Rice","Lemon Rice","Curd Rice","Idli","Dosa","Uttapam","Vada","Upma","Pongal","Poori","Chapati","Paratha","Naan","Roti","Samosa","Pakora","Sandwich","Burger","Pizza","Pasta","Noodles","Momos","French Fries","Manchurian","Spring Rolls","Chicken Curry","Mutton Curry","Fish Curry","Prawn Curry","Egg Curry","Paneer Butter Masala","Palak Paneer","Dal Tadka","Sambar","Rasam","Vegetable Curry","Mixed Veg Curry","Tandoori Chicken","Chicken 65","Chicken Biryani","Mutton Biryani","Veg Biryani","Fish Fry","Omelette","Boiled Eggs","Fruit Salad","Tomato Soup","Ice Cream","Cake","Gulab Jamun","Rasgulla","Laddu","Payasam","Halwa","Chocolate","Biscuit","Tea","Coffee","Milkshake","Fruit Juice"]}
         if os.path.exists(DATABASE_FILE):
          with open(DATABASE_FILE, "r") as f:
           self.internal_database = json.load(f)
         else:
          self.internal_database = {}
         if os.path.exists(HISTORY_FILE):
          with open(HISTORY_FILE,"r") as f:
           self.searching_history = json.load(f)
         else:
          self.searching_history = []
     def clear_data(self):
        with open(HISTORY_FILE, "w") as f:
         json.dump([], f)
        with open(DATABASE_FILE, "w") as f:
         json.dump({}, f)   
        self.searching_history = []
        self.internal_database = {}
     def voice(self,text,voicer):
      engine = pyttsx3.init()
      voices = engine.getProperty('voices')
      engine.setProperty('voice', voices[voicer].id)
      engine.say(text)  
      engine.runAndWait()     
     def logic(self,product):
         self.searching_history.append(product)
         with open(HISTORY_FILE, "w") as f:
            json.dump(self.searching_history, f,indent=4)
         found=False
         for category , products in self.product_list.items():
             if product in [single_item.lower() for single_item in products]:
                 print(f"Your Recommendation System akki is Activated.................\nYour Search {product} is a product belongs to {category} category \nThere are many products in category: {category}\nHere is your Related Product:")
                 self.voice(f"Your Recommendation System akki is Activated.................\nYour Search {product} is a product belongs to {category} category \nThere are many products in category: {category}\nHere is your Related Product",1)
                 for i, item in enumerate(products, start=1):
                     print(f"{item:<25}", end="")
                     if i % 6 == 0:
                         print()
                 found=True
                 break   
         if not found:
             found_internal=False
             for category_internal, product_internal in self.internal_database.items():
                if product.lower() in [p.lower() for p in product_internal]:
                 print(f"Your product {product} is found in your previous history\nUnder the Category: {category_internal}")
                 self.voice(f"Your product {product} is found in your previous history\nUnder the Category {category_internal}",1)
                 found_internal=True
                 break
             if not found_internal:
                 print("Sorry your search Not Found in my Data Base")
                 self.voice("Sorry your search Not Found in my Data Base",1)
                 while True:
                  self.voice("Please help me to train this System. so enter the name of category for your search",0)
                  self.category_storage=input("Please help me to train this System. so enter the name of category for your search: ").lower()
                  if len(self.category_storage)!=0:
                      print("Your System is trained successfully Thanks for your help")
                      self.voice("Your System is trained successfully Thanks for your help",1)
                      if self.category_storage not in self.internal_database:
                          self.internal_database[self.category_storage] = []
                      if product.lower() not in [p.lower() for p in self.internal_database[self.category_storage]]:
                          self.internal_database[self.category_storage].append(product)
                      with open(DATABASE_FILE, "w") as f:
                          json.dump(self.internal_database, f,indent=4)
                          break
                  else:
                      print("Please enter a category to store the data")
                      self.voice("Please enter a category to store the data",1)
             print(f"Your Recommendation System akki is Activated...........\nHere is given all categories list so choose one to view there products,\n{self.product_list.keys()}")
             self.voice(f"Your Recommendation System akki is Activated...........\nHere is given all categories list so choose one to view there products,\n{self.product_list.keys()}",0)
             while True: 
              found=False
              self.voice("Enter your category name",1)
              self.category_option=input("Enter your category name: ")
              if len(self.category_option) !=0:
               for category, products in self.product_list.items():
                   if self.category_option.lower() in category.lower():
                       found=True
                       print(f"Here is your list of products in category {category}: ")
                       self.voice(f"Here is your list of products in category {category}",0)
                       for i, item in enumerate(products, start=1):
                           print(f"{item:<25}", end="")
                           if i % 6 == 0:
                               print()
                       break
               if not found:
                print("You have entered Invalid category. Please choose one from the list above")
                self.voice("You have entered Invalid category. Please choose one from the list above",1)
                continue 
               break
              else:
                 print("Your category name is empty")
                 self.voice("Your category name is empty",0)     
         print()
     def search_history(self):
        print("Your Agent akki is Activated.........")
        self.voice("Your Agent akki is Activated.........",1)
        if len(self.searching_history)==0:
           print("Your New user, so You have no previous data in search history")
           self.voice("Your New user, so You have no previous data in search history",0)
        else:
           print("Here is your search history: ")
           self.voice("Here is your search history",1)
           history = Counter(self.searching_history)
           for product, count in history.items():
            print(f"{product} : {count}times searched",end=", ")
     def recommandation(self):
        if len(self.searching_history)==0:
           print("Your new user, so you have no previous data to recommend the products. Enter \"yes\" for akki to suggest you the products")
           self.voice("Your new user, so you have no previous data to recommend the products. so enter yes for akki to suggest you the products",1)
           while True:
            self.voice("Enter your option",0)
            user_ans=input("Enter your option: ")
            if len(user_ans)!=0:
             if user_ans.lower() in ["yes","y"]:
                    category = random.choice(list(self.product_list.keys()))
                    products_store = self.product_list[category]
                    print(f"Your Recommendation System akki is Activated.................\nI suggested products from my favorite category {category}\nThere are many products in category: {category}\nHere is your Related Product: ")
                    self.voice(f"Your Recommendation System akki is  Activated.................\nI suggested products from my favorite category {category}\nThere are many products in category: {category}\nHere is your Related Product",1)
                    for i, item in enumerate(products_store, start=1):
                        print(f"{item:<25}", end="")
                        if i % 6 == 0:
                            print()
                    print()
                    break
             elif user_ans.lower() in ["no","n"]:
                print("First go to option 1 and search for the products then you will get the recommendation\nThanking you.............")
                self.voice("First go to option 1 and search for the products then you will get the recommendation\nThanking you.............",1)
                break
            else:
                print("Please enter \"Yes\" or \"No\"")
                self.voice("Please enter Yes or No",1)
        if not self.searching_history:
          return        
        self.frequency=Counter(self.searching_history)
        product, _ =self.frequency.most_common(1)[0]  
        self.product_list_values=[] 
        for products in self.product_list.values():
           self.product_list_values.extend(product_items.lower() for product_items in products)
        if product in self.product_list_values:
           for category , products_store in self.product_list.items():
              product = product.lower()
              if product in [single_store_item.lower() for single_store_item in products_store]:
                 print(f"Your Recommendation System akki is Activated.......................\nAccording to your previous search, I found Your favorite Search \"{product}\" is a product belongs to \"{category}\" category \nThere are many products in category: {category}\nHere is your Related Product:")
                 self.voice(f"Your Recommendation System akki is Activated.................\nAccording to your previous search, I found Your favorite Search {product} is a product belongs to {category} category \nThere are many products in category: {category}\nHere is your Related Product",0)
                 for i, item in enumerate(products_store, start=1):
                     print(f"{item:<25}", end="")
                     if i % 6 == 0:
                         print()
                 break
           print()
        else:
            category = random.choice(list(self.product_list.keys()))
            products_store = self.product_list[category]
            print(f"Your Recommendation System akki is Activated.................\nI suggested products from my favorite category \nThere are many products in category: {category}\nHere is your Related Product: ")
            self.voice(f"Your Recommendation System akki is Activated.................\nI suggested products from my favorite category. \nThere are many products in category: {category}\nHere is your Related Product",0)
            for i, item in enumerate(products_store, start=1):
                 print(f"{item:<25}", end="")
                 if i % 6 == 0:
                     print()            
     def main(self):
         print("Main Menu:\n1.Search a product\n2.Your Search History\n3.Your Recomandation\n4.Clear your system data")
         self.voice("Here is your Main Menu:\n1 for Search a product\n2 for Your Search History\n3 for Your Recomandation\n4 for Clear your system data",0)
         while True:
          try:
             self.voice("Enter Your option from above",1)
             choice=int(input("Enter Your option from above: "))
             break
          except ValueError:
             print("Please enter a valid input")
             self.voice("Please enter a valid input",0)            
         match choice:
             case 1:
                 while True:
                  self.voice("Please enter Name of the product for search",0)
                  self.product =input("Please enter Name of the product for search: ").lower()
                  if len(self.product)!=0:
                     self.logic(self.product)
                     break
                  else:
                     print("Your product should'nt be empty for search")
                     self.voice("Your product should'nt be empty for search",1)
             case 2:
                 self.search_history()
             case 3:
                 self.recommandation()
             case 4:
                 print("Your data will be delete permanently and your system akki will be reset")
                 self.voice("Your data will be delete permanently and your system akki will be reset, \nEnter yes for deletion process",0)
                 while True:
                  data_input=input("Enter \"yes\" for deletion process: ")
                  if len(data_input)!=0:
                   if data_input.lower() in ["yes","y"]:
                    print("Your deletion procss begin please wait...............")
                    self.voice("Your deletion process begin please wait...............",1)
                    self.clear_data()
                    print("Your data is successfully deleted, your system akki is newly born")
                    self.voice("Your data is deleted successfully, your system akki is newly born",0)
                   else:
                      print("You have taken Good Decision my Cheif")
                      self.voice("You have taken good decision my chief",1) 
                   break 
                  else:
                     print("Please Enter \"Yes\" or \"No\"")
                     self.voice("Please enter Yes or No",0)
             case _:
                 print("Please enter your option between (1 to 4)only, Now your system akki is going back")
                 self.voice("Please enter your option between (1 to 4)only, Now your system akki is going back",1)          
 obj= product_Recommendation()
 while True:
  obj.main()
  print("\nSearch for Another Product\n")
  obj.voice("Search for Another Product",1)
except Exception as e:
   print("Something went wrong please try again or contact the Developer Akhil................")