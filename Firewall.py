from Rule import *
from random import randint

class Firewall:
    def __init__(self, number_of_rules,number_of_fields):
        self.rules=[]
        for i in range(0, number_of_rules):
            self.fields.append(Rule(number_of_fields,randint(0, 2)))