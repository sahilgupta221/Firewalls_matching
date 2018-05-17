
class Packet:
    def __init__(self, field_list,action):
        self.field=field_list

        self.field.append(action)