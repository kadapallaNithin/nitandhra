gr_list = [{'A':["ABd","Aa","a"],'B':["Bc",'b']},{'E':['E+E',"E*E",'a']},{'S':["(L)",'a'],'L':["L,S","S"]},{'X':["XSb","Sa",'B'],'S':["Sb","XA",'a']},{'E':["E+T","E-T","T"],'T':["T*F","T/F","F"],'F':['9',"(E)"]}]
for grammer in gr_list:
    #def remove_left_recursion(grammer):
    g = dict()
    for nt in grammer:
        g[nt] = list()
        a = list()
        b = list()
        for pr in grammer[nt]:
            if pr[0] == nt:
                a.append(pr)
                #if not nt+'_' in g:
                #    g[nt+'_'] = list()
                #g[nt+'_'].append()
            else:
                b.append(pr)
        if len(a) != 0:
            g[nt+'_'] = [s[1:] for s in a]
            g[nt+'_'].append('')
            for p in b:
                g[nt].append(p+nt+'_')
        else:
            g[nt] = grammer[nt]
    print(g)
'''
if __name__ == "__main__()":
    print('HI')
    gr_list = [{'A':["ABd","Aa","a"],'B':["Bc",'b']},{'E':['E+E',"E*E",'a']},{'S':["(L)",'a'],'L':["L,S","S"]},{'X':["XSb","Sa",'B'],'S':["Sb","XA",'a']},{'E':["E+T","E-T","T"],'T':["T*F","T/F","F"],'F':['9',"(E)"]}]
    for gr in gr_list:
        print(gr)
        remove_left_recursion(gr)'''
