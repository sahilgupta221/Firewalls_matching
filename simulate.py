from time import *
from Firewall import *
from utils import*


start = clock_gettime(0)

F1 = Firewall(10,5)
F2 = Firewall(10,5)

flag=1

for rule in F2.rules:
    p=Property(rule)
    if (satisfy(F1,p)==0):
        flag=0

if(flag==0):
    print("F1 and F2 are not same")
else:
    print("F1 and F2 are same")

stop = clock_gettime(0)

print("Time taken for comparision is ",stop-start)


"""
1. Take two firewalls, F and G.
Now, we want to find a witness packet accepted by F and discarded by G.
(or vice versa, in which case, switch the names F and G.)

2. Make all accept slices of F, call them F1, F2 … 
Make all discard slices of G, call them G1, G2 … 

3. Take an accept slice Fa and a discard slice Gb.
Project Fa on base rule of Gb, to get Fab.
Project Gb on base rule of Fa, to get Gba.

4. Flip decisions for Gba. 
(After flipping, the last rule is now an accept and the rules masking it are discards).

Note that now, Fab and Gba both end in the exact same rule.
(Predicate: intersection of base rules of Fa and Gb. Decision: accept.)

6. Make one slice with all the rules from Fab (except the base rule), followed by 
all the rules from Gba (this time, including the base rule).

Now, the only packets accepted by this slice are those that :
a) are matched by the base rules in Fa and Gb, both.
b) are not masked by the non-base rules in Fa or Gb.

In other words - witness packets!

So - apply Probe (or FDD) and find witness packets for all choices of Fa and Gb.
Iff no witness packets, the two firewalls are equivalent :)
"""

start = clock_gettime(0)

F = Firewall(10,5)
G = Firewall(10,5)

slice_firewall_F = create_slice_firewall(F,1)
slice_firewall_G = create_slice_firewall(G,0)


for f in slice_firewall_F:
    for g in slice_firewall_G:
        # fab and gba
        # gba base rule ->accept and masking rules ->discard
        # find edge packet from intersection of base rules of fa and gb(same as last rules of fab and gba)
        # merge fab and gba excluding last rule of fab and including last rule of gba
        # find edge packet between probe rule of gba base rule and merge firewall.
        # check edge packet from above steps if exists then F and G are not same. make flag =0,exit from there itself.
        # if in the end flag=1 then F and G are same else not
        fab = projection_from_base_rule(f,g)
        gab = projection_from_base_rule(g,f)
        temp_gab = flip_actions(g)
        test_packet = intersection_of_base_rules(f,g)
        temp_fg_firewall = merge_two_firewall_slice(f,g)
        test_packet= test_packet+ packets_from_probe_algorithm(f,g)
        if(len(test_packet)):
            flag=0

if(flag==0):
    print("F1 and F2 are not same")
else:
    print("F1 and F2 are same")

stop = clock_gettime(0)

print("Time taken for comparision is ",stop-start)
