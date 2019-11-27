def all_in(subset,list_ip):
    trth = True
    i = 0
    while trth  and i < len(subset):
#        if not subset[i] in list_ip:
#            trth = False
        trth =  False
        for el in list_ip:
            if el == subset[i]:
                trth = True
        i += 1
    return trth
#all_in([(1),(8),(5)],[1,3,6,4,5])# == True

def sup(subsets,dataset,min_sup_count):
    fr = list()
    for st in subsets:
        count = 0
        for trns in dataset:
            if all_in(st,trns):
                count+=1
        if count >= min_sup_count:
            fr.append([st,count])
    return fr
#sup([[['E', 'K'], 4], [['E', 'O'], 3], [['E', 'Y'], 3], [['K', 'O'], 3], [['K', 'Y'], 3]],ds,1)# == [['d', 2]]

def sup1(dataset):# 1
    l = list()
    for s in dataset:
        for e in s:
            f = [c[1] for c in l if c[0] == e]
            if len(f) == 0:
                l.append([e,1])
            elif len(f) == 1:
                l[l.index([e,f[0]])][1] += 1
            else :
                print("Error in your code")
    return l 
#sup1(["MONKEY","DONKEY","KEY","COOKIE"])#[['M', 1],['O', 4],['N', 2],['K', 4],['E', 4],['Y', 3],['D', 1],['C', 1],['I', 1]

def apriori_gen(c):
    c = [x[0] for x in c]
    if len(c) > 0:
        li = list()
        x = len(c[0])
        for i in range(len(c)):
            for j in range(i+1,len(c)):
                tr = True
                l = list()
                for k in range(x-1):
                    if tr and c[i][k] == c[j][k]:
                        l.append(c[i][k])
                    else:
                        tr = False
                if tr:
                    l.append(c[i][x-1])
                    l.append(c[j][x-1])
                    li.append(l)
    return li
#apriori_gen([['MO', 1],['ML', 4],['NM', 2],['KL', 4],['EM', 4],['YK', 3],['KD', 1],['CN', 1],['IO', 1]])
#apriori_gen([[['E', 'K'], 4], [['E', 'O'], 3], [['E', 'Y'], 3], [['K', 'O'], 3], [['K', 'Y'], 3]])

def apriori(ds,min_sup,min_con):
    min_sup = min_sup*len(ds)/100
    sup0 = sup1(ds)
    flag = True
    i = 1
    while flag:
        sup0.sort(key=lambda x:x[1])
        sup0.reverse()
        while len(sup0) > 0 and sup0[-1][1] < min_sup:
            sup0.pop()
        #sup0 = [c[0] for c in sup0]
        #sup0 = apriori_gen([c[0] for c in sup0],i)
        sup0 = sup([x for x in apriori_gen([c[0] for c in sup0])],ds,3)
        if i % 2 == 0:
            flag = False
        i += 1
        print(sup0)
ds = ["MONKEY","DONKEY","KEY","COOKIE"]
apriori(ds,26,3)

def apriori(ds,min_sup,min_con):
    min_sup = min_sup*len(ds)/100
    sup0 = sup(ds)
    a = [1]
    for i in a:
        sup0.sort(key=lambda x:x[1])
        sup0.reverse()
        while len(sup0) > 0 and sup0[-1][1] < min_sup:
            sup0.pop()
        
    print(sup0)
apriori(["MONKEY","DONKEY","KEY","COOKIE"],26,3)
