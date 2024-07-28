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
