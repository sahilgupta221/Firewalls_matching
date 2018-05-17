import copyfrom random import randrangefrom sys import argvfrom time import timemin, max = [0, 65535]class node:    def __init__(self,inid):        self.my_id = inid        self.sub = {}    def copy_subtree(self):        return copy.deepcopy(self)    def add_rule(self, newrule):        item = newrule[self.my_id]        if isinstance(item, int):            self.sub = {"RESULT":item}        else :            l1, h1 = item            oldsub = self.sub            newsub = {}            oldkeys = oldsub.keys()            sorted(oldkeys)            for old in oldkeys:                 l2,h2 = old                if (h2 < l1) or (l2 > h1): #the non overlap pieces                    newsub[(l2, h2)] = oldsub[(l2, h2)]                                    elif (l1 <= h1) and (l1 <= l2) and (l2 <= h1) and (h1 <= h2):                                        if (l1 < l2):                        newsub[(l1, l2-1)] = node(self.my_id + 1)                        newsub[(l1, l2-1)].add_rule(newrule)                                            newsub[(l2, h1)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l2, h1)].add_rule(newrule)                                        if (h1 < h2):                        newsub[(h1+1, h2)] = oldsub[(l2, h2)].copy_subtree()                    l1 = h2+1                elif (l1 <= h1) and (l1 <= l2) and (l2 <= h2) and (h2 <= h1):                    if (l1 < l2):                        newsub[(l1, l2-1)] = node(self.my_id + 1)                        newsub[(l1, l2-1)].add_rule(newrule)                    newsub[(l2, h2)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l2, h2)].add_rule(newrule)                    l1 = h2+1                elif (l1 <= h1) and (l2 <= l1) and (l1 <= h1) and (h1 <= h2):                    if (l2 < l1):                        newsub[(l2, l1-1)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l1, h1)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l1, h1)].add_rule(newrule)                    if (h1 < h2):                        newsub[(h1+1, h2)] = oldsub[(l2, h2)].copy_subtree()                    l1 = h2+1                elif (l1 <= h1) and (l2 <= l1) and (l1 <= h2) and (h2 <= h1):                    if (l2 < l1):                        newsub[(l2, l1-1)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l1, h2)] = oldsub[(l2, h2)].copy_subtree()                    newsub[(l1, h2)].add_rule(newrule)                                        l1 = h2+1            if (l1 <= h1): #something has survived                newsub[(l1, h1)] = node(self.my_id + 1)                newsub[(l1, h1)].add_rule(newrule)                l1 = h1 + 1            self.sub = newsubdef traverse(queue):    while queue:        first = queue.pop(0)        if isinstance(first, node):            print (first.my_id)            for x in first.sub:                print (x)                queue.append(first.sub[x])        else:            print ("Decision : ", first )def mycount(queue):    len = 0    while queue:        first = queue.pop(0)        if isinstance(first, node):            len += 1            for x in first.sub:                queue.append(first.sub[x])    return lenlastrule = [[min, max]]*5lastrule.append(0)def simulate(allprob, oneprob):    for loop in [4, 8, 16, 32]:        len = loop - 1        sum = 0        start = time()        num = 25        if (oneprob == 0) and (loop == 32):            num = 5        for count in range(num):            root = node(0)            root.add_rule(lastrule)            for i in range(len):                rule = []                for j in range(5):                    toss = randrange(100)                    if (toss < allprob):                         rule.append([min, max])                    elif (toss < allprob + oneprob):                        x = randrange(max + 1)                        rule.append([x, x])                    else :                        x,y = randrange(max + 1), randrange(max + 1)                        if (y < x): x,y = y,x                        rule.append([x,y])                rule.append(randrange(2))                root.add_rule(rule)            sum = sum + mycount([root])        print (allprob, oneprob, len+1, sum/num, "%.2f" %((time()-start)/num))for allprob in range(0, 40, 20):    for oneprob in range(0, 101-allprob, 20):        simulate(allprob, oneprob)