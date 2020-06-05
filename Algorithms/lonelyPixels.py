print(mat[i][j],p,x)                          if mat[i][j] == p:
                if x == -1:                                       x = i
                    print(x)
                else:
                    print('b')
                    break
        lnlcols.append(x)
    return lnlcols
def lonelyPixels(mat,p):
    lnlrows = lonelyPixel_rows(mat,p)
    lnlcols = lonelyPixel_cols(mat,p)             r = list()                                    for i in lnlrows:
        for j in lnlcols:                                 if lnlrows[i] != -1 and lnlcols[j] != -1:
                r.append((i,j))
    return r
print(lonelyPixels(mat,1))
