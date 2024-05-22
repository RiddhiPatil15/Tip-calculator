print("Hello, welcome to tip caluculator!")
bill = float(input("What is the total bill?\nRupees "))
people = int(input("How many people to split the bill?\n"))
tip = int(input("What percentage tip would you like to give, 5%, 10%, or 12%?\n"))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person, 2)
# or final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: Rupees {final_amount}")