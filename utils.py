from Firewall import *
from Property import *

def satisfy(Frwl,p):
    #list of slice firewall.
    slice_firewall = []

    # created enemy and friend rule index as per property p
    #action index contain friend(1) and enemy(0) value same position as of rules
    friend_action_index = []
    i=0
    for rule in Frwl.rules:
        if(rule.fields[Frwl.number_of_fields] == p.rule.fields[Frwl.number_of_fields]):
            friend_action_index.append(i)
        i=i+1

# all enemy rules index and friend rules above it having some over lap is clubbed together
# to form a slice
    pre_index=0
    for index in friend_action_index:
        rules=[]
        for i in range(pre_index,index+1):
            if(overlap(Frwl.rules[i],p)):
                rules.append(Frwl.rules[i])
        slice_firewall.append(Firewall(rules))
        pre_index = index+1



#f is list of possible edge points of various fields like f[0] contain first field edge values
        f=[]
# loop over each slice firewall and use prob algorithm to get witness packet over that slice
        for firewall in slice_firewall:
            temp_firewall = projection(firewall,p)
            f= probe_field_set(temp_firewall,p)

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
    return 0


# return firewall with common intersecting ranges
def projection(frwl,p):
    return 0

# probe algorithm to get possible values at each field positions
# remember to remove elements that are out of property range generated from the process
def probe_field_set(frwl,p):
    return 0

# cartisian product
def fill_possible_packet(field_list):
    return 0