from random import randint

class Rule:
    def __init__(self, number_of_fields,action=None,fields=None):
        if fields is None:
            self.fields = []
            for i in range(0, number_of_fields):
                p = randint(0, 100)
                if (p < 50):
                    self.fields.append([randint(0, 500), randint(500, 1000)])
                elif (p >= 50 and p <= 70):
                    self.fields.append([0, 1000])
                else:
                    single_value = randint(0, 1000)
                    self.fields.append([single_value, single_value])

            self.fields.append(action)
        else:
            self.fields=fields


class Firewall:
    def __init__(self, number_of_rules,number_of_fields,rules=None):
        if rules is None:
            self.rules = []
            self.number_of_rules = number_of_rules
            self.number_of_fields = number_of_fields
            for i in range(0, number_of_rules):
                self.rules.append(Rule(number_of_fields, randint(0, 1)))
        else:
            self.rules=rules

class Packet:
    def __init__(self, field_list,action):
        self.field=field_list

        self.field.append(action)