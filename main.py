from flat import Bill, Flatmate
from report import PdfReport

# CLI inputs
bill_amount = float(input("Please enter the bill amount: "))
period_input = input("What is the bill period? (i.e. July 2024): ")
name1 = input("Enter the 1st flatmate's name: ")
name2 = input("Enter the 2nd flatmate's name: ")
days_in_house1 = int(input(f"How many days did {name1} stayed in the house during this period? "))
days_in_house2 = int(input(f"How many days did {name2} stayed in the house during this period? "))

the_bill = Bill(bill_amount, period_input)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"Bill_{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
