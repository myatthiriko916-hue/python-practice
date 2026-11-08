import random 
import webbrowser

def food_system():
    
  while True:
    
    print("==========")
    print("Welcome To Food System")
    print("==========")
    print("1.Myanmar Food")
    print("2.Thai Food")
    print("3.Korean Food")
    print("4.Chinese Food")
    
    choice = input("Choose  food category:")
    
    if   choice == "1" :
           myanmar_food()
        
    elif choice == "2" :
           thai_food()
        
    elif choice == "3" :
           korean_food()
              
    elif choice == "4" :
           chinese_food()
        
    else :
         print("Invalid Category!")
         continue 
     
    ans = input ("Do you want to order again? (y/n):")
    if ans == "y" :
        continue
    else :
        print("Thank for using Food System!")
        break 

def myanmar_food():
      
    print("Myanmar Food")
    print("1.Mohinga")
    print("2.Shan Noodle")
    print("3.Noodle Salad")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
        food = "Mohinga"
        price = 2000
    elif food_num == 2 :
        food = "Shan Noodle"
        price = 3000
       
    elif food_num == 3 :
        food = "Noodle Salad"
        price = 2000
        
    else :
        print("Invalid Food Number!")
        return
    cus_info (food, price)
     
def thai_food():
      
    print("Thai Food")
    print("1.Pad Thai")
    print("2.Tom Yum")
    print("3. Green Curry")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
        food = "Pad Tha"
        price = 6000
    elif food_num == 2 :
        food = "Tom Yum"
        price = 5000
       
    elif food_num == 3 :
        food = "Green Curry"
        price = 4500
        
    else :
        print("Invalid Food Number!")
        return
    cus_info(food,price)
     
def korean_food():
           
   print("Korean Food")
   print("1.Korean Fried Chicken")
   print("2.Kimchi Jjigae")
   print("3.Bibimbap")
         
   food_num =int (input("Choose your food:"))
         
   if food_num == 1 :
        food = "Korean Fried Chicken"
        price = 3500
   elif food_num == 2 :
        food = "Kimchi Jjigae"
        price = 3000
            
   elif food_num == 3 :
       food = "Bibimbap"
       price = 6000
             
   else :
      print("Invalid Food Number!")
      return
   cus_info(food,price)
 
def chinese_food():
      
    print("Chinese Food")
    print("1.Fried Rice")
    print("2.Hot Pot")
    print("3.Spring Rolls")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
        food = "Fried Rice"
        price = 3500
    elif food_num == 2 :
        food = "Hot Pot"
        price = 8000
       
    elif food_num == 3 :
        food = "Spring Rolls"
        price = 2000
        
    else :
        print("Invalid Food Number!")
        return
    cus_info(food,price) 

def cus_info(food,price):
    
    print("Food Name:",food)
    print("Food Price:",price,"MMK") 
   
    qty = int (input("Enter Quantity:"))
    total = price * qty 
   
    print ("Enter Customer Information")
    name = input ("Enter Your Name:")
    phone = input ("Enter Your Phone Number:")  
   
    print("==========")
    print("Ordering System")
    print("==========")
    print("Customer Name:",name)
    print("Phone Number:",phone)
    print("Food Name:",name)
    print("Food Price:",price)
    print("Quantity:",qty)
    print("Total Bill:",total,"MMK")
    
    print("Thank For Ordering!")
   
food_system()     
           