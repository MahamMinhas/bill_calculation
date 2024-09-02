 #4.	Write a program to calculate the electricity bill according to the following criteria:
# # Unit                                                     Price  
# # a.	First 100 units                                      no charge
# # b.	Next 100 units                                   Rs 5 per unit
# # c.	After 200 units                                 Rs 10 per unit

units=int(input("Enter the electricity units: "))

if(units<=0):
    print("Invalid Input")  
elif(units>0 and units<=100):
        print("No charge")
elif(units>100 and units<=200):
    Bill=(units-100)*5
    print("Bill is: ",Bill)
else:
    Bill=(100*5)+(units-200)*10
    print("Bill is: ",Bill)
