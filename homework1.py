a=int(input("Give me 1st number:"))
b=int(input("Give me 2nd number:"))

all_a=id(a)
print("location of 1st number:",all_a)

hex_b=id(b)
print("location of 2nd number:",hex_b)

a1=a+b
print("Addition:",a1)

a2=a*b
print("Multiplication:",a2)

if a > b:
    a3=a-b
    print("Subtration:",a3)
    a4=a//b
    print("Division:",a4)
    
if a < b:
 a3=b-a
 print("Addition:",a3)
 
 a4=b//a
 print("Division:",a4)
 
 all_a1=id(a1)
 print("location of addition:",all_a1)
 
 all_a2=id(a2)
 print("Location of multiplication:",all_a2)
 
 all_a3=id(a3)
 print("Location of substration:",all_a3)
 
 all_a4=id(a4)
 print("Location of division:",all_a4)
 
 hex_a1=id(a1)
 print("Location of addition :",hex_a1)
 
 hex_a2=id(a2)
 print("Location of multiplication:",hex_a2)
 
 hex_a3=id(a3)
 print("Location of substration:",hex_a1)
 
 hex_a4=id(a4)
 print("Location of division:",hex_a1)
 
    
    