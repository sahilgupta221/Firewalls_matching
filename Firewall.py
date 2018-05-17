from Rule import *
from random import randint

class Firewall:
    def __init__(self, number_of_rules,number_of_fields):
        self.rules=[]
        self.number_of_rules=number_of_rules
        self.number_of_fields= number_of_fields
        for i in range(0, number_of_rules):
            self.rules.append(Rule(number_of_fields,randint(0, 2)))

    def __init__(self, rules):
        self.rules=rules