from random import randint

class Rule:
    def __init__(self, number_of_fields,action):
        self.fields=[]
        for i in range(0, number_of_fields):
            p=randint(0,100)
            if(p<40):
                self.fields.append([randint(0, 500),randint(300, 1000)])
            elif(p>=40 and p<=60):
                self.fields.append([0, 1000])
            else:
                single_value = randint(0,1000)
                self.fields.append([single_value,single_value])




        self.fields.append(action)

    def __init__(self, fields):
        self.fields=fields