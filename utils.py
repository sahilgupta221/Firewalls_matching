from Firewall import *
from itertools import product
from Property import *

def satisfy(Frwl,p):
    #list of slice firewall.
    slice_firewall = []

    # created enemy and friend rule index as per property p
    #action index contain friend(1) and enemy(0) value same position as of rules
    enemy_action_index = []
    i=0
    for rule in Frwl.rules:
        if(rule.fields[Frwl.number_of_fields] != p.rule.fields[Frwl.number_of_fields]):
            enemy_action_index.append(i)
        i=i+1

# all enemy rules index and friend rules above it having some over lap is clubbed together
# to form a slice
    for index in enemy_action_index:
        rules=[]
        for i in range(0,index+1):
            if(i in enemy_action_index and i!=index):
                continue
            if(overlap(Frwl.rules[i],p)):
                rules.append(Frwl.rules[i])
        slice_firewall.append(Firewall(rules))



#f is list of possible edge points of various fields like f[0] contain first field edge values
        f=[]
# loop over each slice firewall and use prob algorithm to get witness packet over that slice
        for firewall in slice_firewall:
            temp_firewall = projection(firewall,p)
            f= probe_field_set(temp_firewall,p,friend_action_index)

# collect all packet in Packet list
        packet_list = fill_possible_packet(f)

# Test finally the all packets from packet list to see if any one resolve different than
# property action

    for packet in packet_list:
        for rule in Frwl.rules:
            if(packet[Frwl.number_of_fields]!=rule[Frwl.number_of_fields]):
                return 0


    return 1

# just check if rules ranges of all fields and property p ranges of all field intersect or not
def overlap(rule,p):
    for i in range(len(rule.fields)):
        if(p.rule.fields[i][0]<rule.fields[i][0]and p.rule.fields[i][1]<rule.fields[i][0]):
            return False
        if(p.rule.fields[i][0]>rule.fields[i][1] and p.rule.fields[i][1]>rule.fields[i][1]):
            return False
        if(p.rule.fields[i][0]>rule.fields[i][0] and p.rule.fields[i][1]<rule.fields[i][1]):
            return True
        if(p.rule.fields[i][0]<rule.fields[i][0]and p.rule.fields[i][1]>rule.fields[i][0]):
            return True
        if (p.rule.fields[i][0] < rule.fields[i][1] and p.rule.fields[i][1] > rule.fields[i][1]):
            return True
    return True

# actual projection of rule over p. return new constructed rule as intersection of ranges of fields
def adjust_ranges_as_per_intersections(rule,p):
    fields = []

    for i in range(len(rule.fields)):
        if(p.rule.fields[i][0]<rule.fields[i][0]and p.rule.fields[i][1]<rule.fields[i][0]):
            return Rule([])
        if(p.rule.fields[i][0]>rule.fields[i][1] and p.rule.fields[i][1]>rule.fields[i][1]):
            return Rule([])
        if(p.rule.fields[i][0]>rule.fields[i][0] and p.rule.fields[i][1]<rule.fields[i][1]):
            fields.append([p.rule.fields[i][0],p.rule.fields[i][1]])
        if(p.rule.fields[i][0]<rule.fields[i][0]and p.rule.fields[i][1]>rule.fields[i][0]):
            fields.append([rule.fields[i][0],p.rule.fields[i][1]])
        if (p.rule.fields[i][0] < rule.fields[i][1] and p.rule.fields[i][1] > rule.fields[i][1]):
            fields.append([p.rule.fields[i][0],rule.fields[i][1]])

    return Rule(fields)

# return firewall with common intersecting ranges
def projection(frwl,p):
    rule_list = []
    for i in range(len(frwl.rules)):
        rule_list.append(adjust_ranges_as_per_intersections(frwl.rules[i],p))

    return Firewall(rule_list)

# probe algorithm to get possible values at each field positions
# remember to remove elements that are out of property range generated from the process
def probe_field_set(frwl,p,friend_action_index):
    i=0
    f=[]
    for rule in frwl.rules:
        if i in friend_action_index:
            j=0
            for field in rule.fields:
                if(field[1] + 1<=p.rule.fields[1]):
                    f[j].append(field[1] + 1)
                j = j + 1
        else:
            k=0
            for field in rule.fields:
                f[k].append(field[0])
                k=k+1
        i=i+1

    return f

# cartisian product
def fill_possible_packet(field_list):
    return list(product(*field_list))