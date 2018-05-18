from Allclassescollection import *
import copy

###################################################################################

def create_slice_firewall(firewall,split_action):
    slice_firewall = []

    # created enemy and friend rule index as per property p
    # action index contain friend(1) and enemy(0) value same position as of rules
    friend_action_index = []
    i = 0
    for rule in firewall.rules:
        if (rule.fields[firewall.number_of_fields] == split_action):
            friend_action_index.append(i)
        i = i + 1

        # all enemy rules index and friend rules above it having some over lap is clubbed together
        # to form a slice
    for index in friend_action_index:
        rules = []
        for i in range(0, index + 1):
            if (i in friend_action_index and i != index):
                continue
            if (is_overlap(firewall.rules[i], firewall.rules[index])):
                rules.append(firewall.rules[i])
        slice_firewall.append(Firewall(0,0,rules))

    return slice_firewall


def is_overlap(firewall_rule,base_rule):
    for i in range(len(firewall_rule.fields)-1):
        if(base_rule.fields[i][0]<firewall_rule.fields[i][0] and base_rule.fields[i][1]<firewall_rule.fields[i][0]):
            return False
        if(base_rule.fields[i][0]>firewall_rule.fields[i][1] and base_rule.fields[i][1]>firewall_rule.fields[i][1]):
            return False
        if(base_rule.fields[i][0]>firewall_rule.fields[i][0] and base_rule.fields[i][1]<firewall_rule.fields[i][1]):
            return True
        if(base_rule.fields[i][0]<firewall_rule.fields[i][0] and base_rule.fields[i][1]>firewall_rule.fields[i][0]):
            return True
        if(base_rule.fields[i][0]<firewall_rule.fields[i][1] and base_rule.fields[i][1]>firewall_rule.fields[i][1]):
            return True
    return True

def re_adjust_ranges_as_per_intersections(firewall_rule,base_rule):
    fields = []
    if firewall_rule.fields is not None and isinstance(base_rule.fields, int)== False and isinstance(firewall_rule.fields, int):
        for i in range(len(firewall_rule.fields) - 1):
            if (base_rule.fields[i][0] < firewall_rule.fields[i][0] and base_rule.fields[i][1] <
                firewall_rule.fields[i][0]):
                return Rule(0)
            elif (base_rule.fields[i][0] > firewall_rule.fields[i][1] and base_rule.fields[i][1] >
                firewall_rule.fields[i][1]):
                return Rule(0)
            elif (base_rule.fields[i][0] > firewall_rule.fields[i][0] and base_rule.fields[i][1] <
                firewall_rule.fields[i][1]):
                fields.append([base_rule.fields[i][0], base_rule.fields[i][1]])
            elif (base_rule.fields[i][0] < firewall_rule.fields[i][0] and base_rule.fields[i][1] >
                firewall_rule.fields[i][0]):
                fields.append([firewall_rule.fields[i][0], base_rule.fields[i][1]])
            elif (base_rule.fields[i][0] < firewall_rule.fields[i][1] and base_rule.fields[i][1] >
                firewall_rule.fields[i][1]):
                fields.append([base_rule.fields[i][0], firewall_rule.fields[i][1]])

        fields.append(firewall_rule.fields[len(firewall_rule.fields) - 1])

    return Rule(0,0,fields)

def projection_from_base_rule(f,g):
    rule_list = []
    for i in range(len(f.rules)):
        rule_list.append(re_adjust_ranges_as_per_intersections(f.rules[i],g.rules[len(g.rules)-1]))

    return Firewall(0,0,rule_list)

def flip_actions(g):
    rule_list = []
    for i in range(len(g.rules)):
        temp = copy.deepcopy(g.rules[i])
        if len(temp.fields)>0:
            temp.fields[len(temp.fields)-1]=0 if temp.fields[len(temp.fields)-1]==1 else 1
        rule_list.append(temp)
    return Firewall(0,0,rule_list)

def merge_two_firewall_slice(f,g):
    f_new = projection_from_base_rule(f, f)
    g_new = projection_from_base_rule(g, g)
    f_new.rules.remove(f_new.rules[len(f_new.rules)-1])
    rules = f_new.rules+g_new.rules
    merged_firewall = Firewall(0,0,rules)
    return merged_firewall

def packets_from_probe_algorithm(firewall):
    base_rule=firewall.rules[len(firewall.rules)-1]

    # f is list of possible edge points of various fields like f[0] contain first field edge values
    f=[]
    for rule in firewall.rules:
        if len(rule.fields) !=0:
            if rule.fields[len(rule.fields) - 1] == base_rule.fields[len(base_rule.fields) - 1]:
                j = 0
                for field in rule.fields:
                    if field is not None and isinstance(field, int)== False:
                        if (field[1] + 1 <= base_rule.fields[1]):
                            f[j].append(field[1] + 1)
                        j = j + 1

            else:
                k = 0
                for field in rule.fields:
                    if field is not None and isinstance(field, int)== False:
                        f[k].append(field[0])
                        k = k + 1

    return f

#############################################################################
