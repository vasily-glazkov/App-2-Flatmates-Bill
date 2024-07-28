import os.path
import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and a period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill, mate2):
        weight = self.days_in_house / (self.days_in_house + mate2.days_in_house)
        return round(weight * bill.amount, 1)


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates
    such as their names, their due amounts and the period of the
    bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, mate1, mate2, bill) -> None:
        flatmate1_pay = str(round(mate1.pays(bill, mate2), 1))
        flatmate2_pay = str(round(mate2.pays(bill, mate1), 1))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Adding image into pdf file
        pdf.image("./files/house.png", w=40, h=40)

        # Insert title
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Helvetica', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Helvetica', size=12)
        pdf.cell(w=100, h=25, txt=mate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=mate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))


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
