import random 
import webbrowser

def myanmar_food():
      
    print("\n===Myanmar Food===\n")
    print("1.Mohinga , 2000MMK")
    print("2.Shan Noodle ,3000MMK ")
    print("3.Noodle Salad , 2000MMK")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
        cus_info ("Mohinga" , 2000)
        
    elif food_num == 2 :
        cus_info ("Shan Noodle" , 3000)
        
    elif food_num == 3 :
        cus_info ("Noodle Salad" , 2000)
        
    else :
        print("Invalid Food Number!")

def thai_food():
      
    print("\n===Thai Food===\n")
    print("1.Pad Thai , 5000MMK")
    print("2.Tom Yum , 6000MMK")
    print("3.Green Curry , 5000MMK")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
          cus_info ("Pad Thai" , 5000)
        
    elif food_num == 2 :
         cus_info ("Tom Yum" , 6000)
       
    elif food_num == 3 :
        cus_info ("Green Curry" , 5000)
        
    else :
        print("Invalid Food Number!")
        
def korean_food():
           
   print("\n===Korean Food===\n")
   print("1.Korean Fried Chicken , 3500MMK ")
   print("2.Kimchi Jjigae , 4000MMK")
   print("3.Bibimbap , 4500MMK")
         
   food_num =int (input("Choose your food:"))
         
   if food_num == 1 :
          cus_info ("Korean Fried Chicken" , 3500)
        
   elif food_num == 2 :
         cus_info ("Kimchi Jjigae" , 4000)       
            
   elif food_num == 3 :
         cus_info ("Bibimbap" , 4500)
              
   else :
      print("Invalid Food Number!")        

def chinese_food():
      
    print("\n===Chinese Food===\n")
    print("1.Fried Rice , 3500")
    print("2.Hot Pot , 8500")
    print("3.Spring Rolls , 2500")
    
    food_num =int (input("Choose your food:"))
    
    if food_num == 1 :
        cus_info("Fried Rice", 3500)
        
    elif food_num == 2 :
        cus_info ( "Hot Pot" , 8000)
       
    elif food_num == 3 :
        cus_info ("Spring Rolls" ,2000)
        
    else :
        print("Invalid Food Number!")

def payment_method():
       
     print("\n===Payment Method===\n") 
     print("1.Cash")
     print("2.KPay")
     print("3.WavePay")
     
     payment = int(input ("Choose your payment type:"))
     
     if payment == 1 :
          return "Cash"
     
     elif payment == 2 :
         return "KPay"
     
     elif payment == 3 :
          return "WavePay"
     
     else :
         print("Invalid Payment Method!")

def cus_info(food,price):
    
    print ("Enter Customer Information")
    name = input ("Enter Your Name:")
    phone = input ("Enter Your Phone Number:") 
    qty = int (input("Enter Quantity:"))
    total = price * qty 
    payment = payment_method()
   
    print("==========")
    print("Ordering System")
    print("==========")
    print("Customer Name:", name)
    print("Phone Number:", phone)
    print("Food Name:", name)
    print("Food Price:", price)
    print("Quantity:", qty)
    print("Total Bill:", total , "MMK")
    print("Payment Method:", payment)
    print("Thank For Ordering!\n")     

def food_system():
    
  while True: 
      
    print("==========")
    print("Welcome To Food System")
    print("==========")
    print("1.Myanmar Food")
    print("2.Thai Food")
    print("3.Korean Food")
    print("4.Chinese Food")
    
    choice = int(input("Choose  food category:"))
    
    if   choice == 1 :
           myanmar_food()
        
    elif choice == 2 :
           thai_food()
        
    elif choice == 3 :
           korean_food()
              
    elif choice == 4 :
           chinese_food()
           
    else :
           print("Invalid Category!") 
           
    ans = input("Do you want to order again?(y/n):")
    if ans!='y' :
        print("Thanks For Using Food System !")
        break
    else :
        print()       
           
food_system()      