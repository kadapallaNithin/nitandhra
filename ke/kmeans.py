import random as rand
import matplotlib.pyplot as plt
%matplotlib inline

def dist(A,B): # distance between points A(x1,y1) and B(x2,y2)
    return ((A[0] - B[0])**2 + (A[1]-B[1])**2)**(0.5)

def cluster(ds,centroidsArr):
    clusters = list()
    k = len(centroidsArr)
    for i in range(k):
        clusters.append([])
    for i in range(len(ds)): # put each element into corresponding k-means cluster
        #find to which cluster it is close
        mDist = dist(ds[i],centroidsArr[0]) #assume 1st cluster is closest
        closeTo = 0
        for j in range(0,k): #check whether it is closer than seen closest cluster
            di = dist(ds[i],centroidsArr[j])
            if mDist > di:
                mDist = di
                closeTo = j
        clusters[closeTo].append(ds[i]) #append to closest cluster
    return clusters
def centroids(clusters):
    centroidsArr = list()
    for i in range(len(clusters)):
        clustxSum = clusters[i][0][0]
        clustySum = clusters[i][0][1]
        for j in range(1,len(clusters[i])):
            clustxSum += clusters[i][j][0]
            clustySum += clusters[i][j][1]
        centroidsArr.append((clustxSum/len(clusters[i]) , clustySum/len(clusters[i])))
    #print(centroidsArr)
    return centroidsArr
def k_means_c(ds,k,centroidsArr): # input - array of data points ,'k' #output - k-means clusters
    
    flag = True;
    i = 0
    centroidArr1 = list()
    while( flag ):
        if i % 2 == 0:
            clus = cluster(ds,centroidsArr)
            centroidsArr1= centroids(clus)
            plt.plot([co[0] for co in centroidsArr],[co[1] for co in centroidsArr],'ro')
            #print(centroidsArr1)
            #plt.scatter([co[0] for co in centroidsArr1 ],[co[1] for co in centroidsArr1],'ro')
        else:
            clus = cluster(ds,centroidsArr1)
            centroidsArr = centroids(clus)
            plt.plot([co[0] for co in centroidsArr1],[co[1] for co in centroidsArr1],'ro')
            #plt.scatter(centroidsArr,'ro')
            #print(centroidsArr)
            #print(centroidsArr1)
            #flag = Falseik
        #print(clus)
        for c in clus:
            plt.scatter([co[0] for co in c],[co[1] for co in c])
        plt.show()
        #print(input())
        flag = (centroidsArr != centroidsArr1)
        i+=1
        #print(input())
    if i % 2 == 0:
        return (centroidsArr,clus)
    return (centroidArr1,clus)
def k_means(ds,k):
    centroidsArr = list()
    rand.shuffle(ds) #can be optimized in next version
    for i in range(k): # choose k centroids from randomised ds
        centroidsArr.append(ds[i])
    return k_means_c(ds,k,centroidsArr)
ds = [[0.196705753183788,0.266174967499455]
,[0.413286989521383,0.355828352990633]
,[0.338435546719209,0.435738258997923]
,[0.103801517189990,0.164344805836115]
,[0.159052363075132,0.325059012698889]
,[0.0669054926780630,0.487418074001379]
,[0.335731444739015,0.0379836806470678]
,[0.285495537731203,0.293509583541386]
,[0.0848835330132443,0.206943248886680]
,[0.0738278885758684,0.154568213233134]
,[0.238039859133728,0.131917020763398]
,[0.454051208253475,0.379383132540102]
,[0.276087513357917,0.497607990564876]
,[0.0164699463749383,0.0932857220706846]
,[0.0269314632177781,0.390572634267382]
,[0.402531614279451,0.0978989905133660]
,[0.225687427351724,0.496179486589963]
,[0.191323114779979,0.401130784882144]
,[0.394821851844845,0.212113354951653]
,[0.182143434749897,0.364431934025687]
,[1.49835358252355,1.40350138880436]
,[1.80899026719904,1.93497908617805]
,[1.35650893348105,1.47948454563248]
,[1.07324343448981,1.23179161166312]
,[1.59099145527485,1.39629024850978]
,[1.91018783072814,1.70507747511279]
,[1.19376593616661,1.55855903456055]
,[1.43236779153440,1.75663070089437]
,[1.7491597290680,1.99548105855526]
,[1.03918448664758,1.96243140436663]
,[1.94632498980548,1.53506710525616]
,[1.76367332366376,1.96387012997171]
,[1.55882055050956,1.11562587918126]
,[1.18384294446577,1.05144829323021]
,[1.49794881501895,1.30434894563657]
,[1.51784560023405,1.58019183314271]
,[1.99424301064405,1.53096445233828]
,[1.85485168309068,1.90120809265314]
,[1.96240393971197,1.54055042517024]
,[1.67894100897703,1.43198061085668]]
k = 2
clust =  k_means(ds,k) #cluster(ds,centroids())
