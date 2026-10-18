num1=int(input("Give me first number:"))
num2=int(input("Give me second number:"))
op=input("Give me your function:(+,-,*,/):")

all_num1=id(num1)
print("location of first number:",all_num1)
all_num2=id(num2)
print("location of second number:",all_num2)

hex_num1=id(num1)
print("location of first number:",hex_num1)
hex_num2=id(num2)
print("location of first number:",hex_num2)

def add(num1,num2):
    print(num1+num2)
    
def sub(num1,num2):
    if num1>num2:
        print(num1-num2)
    elif num2>num1:   
        print(num2-num1)
    
def multi(num1,num2):
    print(num1*num2)
    
def div(num1,num2):
    if num1>num2:
        print(num1/num2)
    elif num2>num1:   
        print(num2/num1)
        
if op=="+":    
    add(num1,num2)
     
elif op=="-":
     sub(num1,num2)
           
elif op=="*":
     multi(num1,num2)
       
elif op=="/":
     div(num1,num2)
