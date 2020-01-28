import math
def naive_bayes(x,offst):
    pk = 'RID'
    clas = 'class'
    cl = df[[clas,pk]].groupby(clas).count()
#cl.loc['no']
#cl.index
    total = 0
    parti = dict()
    for i in cl.index:
        print(cl.loc[i][pk])
        total += cl.loc[i][pk]
        parti[i] = df[df[clas]==i]
    pr = dict()
    prn = dict()
    for part in parti:
        print()
        lp = 0
        p = 1
        for atr in x :
        #print(parti[part][[atr,pk]].groupby(atr).count().loc[x[atr]][pk],cl.loc[part][pk])
            lp += math.log10(parti[part][[atr,pk]].groupby(atr).count().loc[x[atr]][pk]/cl.loc[part][pk])
            p *= parti[part][[atr,pk]].groupby(atr).count().loc[x[atr]][pk]/cl.loc[part][pk]
        pr[part] = 10**(lp)*(cl.loc[part][pk]/total)
        prn[part] = p*(cl.loc[part][pk]/total)
    return pr,prn
