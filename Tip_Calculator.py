# THIS IS A TIP CALCULATOR PROGRAM

print("++++++++++ TIP CALCULATOR ++++++++++")
bill=float(input("what was the total bill? $"))
tip_percentage=int(input("how much tip would you like to give? 5, 10, or 15?"))
number_of_persons=int(input("How many people to split the bill?"))

'''here i need to find the tip amount 
   bill_amount=4
   tip=10%
   tip_amout is 4/100*10 =0.4 '''
tip_amount=(bill / 100 )*tip_percentage
# add the tip amount to the bill
bill+=tip_amount
splited_amount= bill/number_of_persons
print("Each person should pay: $",round(splited_amount,2))
