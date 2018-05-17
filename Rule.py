from random import randint

class Rule:
    def __init__(self, number_of_fields,action):
        self.fields=[]
        for i in range(0, number_of_fields):
            self.fields.append([randint(0, 1000),randint(0, 1000)])

        self.fields.append(action)

    def __init__(self, fields):
        self.fields=fields