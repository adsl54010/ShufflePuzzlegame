import array
import random
import datetime
import math


def getopenlist(gamemap):
    gamemapopen=gamemap;
    zero=gamemap.index(0)
    h=0
    if (zero%3 == 0):
        print ("是第一列喔")
        if (zero<=2):
            print ("是第一排喔")
            f = open('openlist.txt','w')   #寫OPENLIST
            gamemapopen[int(zero)],gamemapopen[1]=gamemapopen[1],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)>0):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[3]=gamemapopen[3],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        elif (zero<=5):
            print ("是第二排喔")
            f = open ('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[0]=gamemapopen[0],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[4]=gamemapopen[4],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[6]=gamemapopen[6],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        else:
            print ("是第三排喔")
            f = open ('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[3]=gamemapopen[3],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[7]=gamemapopen[7],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
    elif (zero%3 == 1):
        print ("是第二列喔")
        if (zero<=2):
            print ("是第一排喔")
            f = open ('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[0]=gamemapopen[0],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[4]=gamemapopen[4],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[2]=gamemapopen[2],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        elif (zero<=5):
            print ("是第二排喔")
            f = open ('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[1]=gamemapopen[1],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[3]=gamemapopen[3],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[5]=gamemapopen[5],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[7]=gamemapopen[7],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        else:
            print ("是第三排喔")
            f = open('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[4]=gamemapopen[4],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[6]=gamemapopen[6],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[8]=gamemapopen[8],gamemapopen[int(zero)]#
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
    else:
        print ("是第三列喔")
        if (zero<=2):
            print ("是第一排喔")
            f = open ('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[1]=gamemapopen[1],gamemapopen[int(zero)] #1
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[5]=gamemapopen[5],gamemapopen[int(zero)] #2
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        elif (zero<=5):
            print ("是第二排喔")
            f = open('openlist.txt','w')
            gamemapopen[int(zero)],gamemapopen[2]=gamemapopen[2],gamemapopen[int(zero)]  #1
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[4]=gamemapopen[4],gamemapopen[int(zero)]#2
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[8]=gamemapopen[8],gamemapopen[int(zero)]#3
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
        else:
            print ("是第三排喔")
            f = open('openlist.txt','w')   #寫OPENLIST
            gamemapopen[int(zero)],gamemapopen[5]=gamemapopen[5],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            gamemapopen[int(zero)],gamemapopen[7]=gamemapopen[7],gamemapopen[int(zero)]
            g= open('gamemap.txt','r')
            gamemap=g.readline()
            gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
            g.close()
            i=0
            h=0
            if (kicksame(gamemapopen)==1):
                while i< len(gamemapopen):
                    if ((gamemapopen[i]) != (i+1)):
                       h=h+int(math.sqrt(abs(gamemapopen[i]-((i+1)%9))))
                    i=i+1
                f.write(str(h))
                i=0
                while i< len(gamemapopen):
                    f.write(str(gamemapopen[i]))
                    i=i+1
                f.write("\n")
            gamemapopen=gamemap
            f.close()
    print("\n")



def getcloselist(gamemap,h,k):
    midans=""
    f = open('closelist.txt','r')
    midans=f.readlines()
    f.close()

    min=9
    i=0
    f = open('openlist.txt','r')   #寫OPENLIST
    closelist = (f.readline())
    gamemapclose=closelist
    while closelist!="":
        if int(closelist[0]) <= min:
            gamemapclose=""
            min = int(closelist[0])
            while i <= 9:
                gamemapclose=gamemapclose+closelist[i+1]
                i=i+1
        i=0
        closelist = (f.readline())
    i=0
    h=0
    while i< 9:
        if (int(gamemapclose[i]) != (i+1)):
           h=h+int(math.sqrt(abs(int(gamemapclose[i])-((i+1)%9))))
        i=i+1
    f.close()
    f = open('closelist.txt','w')
    f.writelines(midans)
    f.write(gamemapclose[0])
    f.write(" ")
    f.write(gamemapclose[1])
    f.write(" ")
    f.write(gamemapclose[2])
    f.write("\n")
    f.write(gamemapclose[3])
    f.write(" ")
    f.write(gamemapclose[4])
    f.write(" ")
    f.write(gamemapclose[5])
    f.write("  h = ")
    f.write(str(h))
    f.write ("     step = ")
    f.write(str(k))
    f.write("\n")
    f.write(gamemapclose[6])
    f.write(" ")
    f.write(gamemapclose[7])
    f.write(" ")
    f.write(gamemapclose[8])
    f.write("\n")
    f.write("--------------------------")
    f.write("\n")
    g= open('gamemap.txt','w')
    gamemap=gamemapclose
    i=0
    while i<9:
        g.write(str(gamemap[i]))
        i=i+1
    g.close()
    gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])

    i=0
    while i<(len(gamemapclose)-1):
        if (i%9==0):
            f.write("3,3,")
            f.write(gamemapclose[i])
        else:
            f.write(",")
            f.write(gamemapclose[i])
        i=i+1
    f.write("\n")
    f.write("\n")
    f.close()
    return(h)

def kicksame(samemap):
    f = open("closelist.txt",'r')
    i=1
    j=0
    same= f.readline()
    while same!="":
        if ((i%6)==5):
            sameple=array.array('B',[int(same[4]),int(same[6]),int(same[8]),int(same[10]),int(same[12]),int(same[14]),int(same[16]),int(same[18]),int(same[20])])
            if samemap==sameple:
                return (0)
        same= f.readline()
        i=i+1
        j=j+1
    f.close()
    return(1)


def A(gamemap):    #A*演算法
    h=0
    k=1
    i=0
    while i< 9:
        if (int(gamemap[i]) != (i+1)%9):
           h=h+int(math.sqrt(abs(gamemap[i]-((i+1)%9))))
        i=i+1
    f = open('closelist.txt','w')
    f.write(str(gamemap[0]))
    f.write(" ")
    f.write(str(gamemap[1]))
    f.write(" ")
    f.write(str(gamemap[2]))
    f.write("\n")
    f.write(str(gamemap[3]))
    f.write(" ")
    f.write(str(gamemap[4]))
    f.write(" ")
    f.write(str(gamemap[5]))
    f.write("  h = ")
    f.write(str(h))
    f.write ("     step = ")
    f.write("0")
    f.write("\n")
    f.write(str(gamemap[6]))
    f.write(" ")
    f.write(str(gamemap[7]))
    f.write(" ")
    f.write(str(gamemap[8]))
    f.write("\n")
    f.write("--------------------------")
    f.write("\n")
    i=0
    while i<9:
        if (i%9==0):
            f.write("3,3,")
            f.write(str(gamemap[i]))
        else:
            f.write(",")
            f.write(str(gamemap[i]))
        i=i+1
    f.write("\n")
    f.write("\n")
    f.close()
    i=0
    if h==0:
        f = open('closelist.txt','w')
        while i<9:
            if (i==0):
                f.write("\n")
                f.write("3,3,")
                f.write(str(gamemap[i]))
            else:
                f.write(",")
                f.write(str(gamemap[i]))
            i=i+1
        f.close()
    while h>1:
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('B',[int(gamemap[0]),int(gamemap[1]),int(gamemap[2]),int(gamemap[3]),int(gamemap[4]),int(gamemap[5]),int(gamemap[6]),int(gamemap[7]),int(gamemap[8])])
        g.close()
        getopenlist(gamemap)
        h=(getcloselist(gamemap,h,k))
        k=k+1
        i=i+1

def kicksame3(samemap):
    f = open("closelist.txt",'r')
    i=1
    j=0
    n=0
    same= f.readline()
    sameple=""
    samemapstr=""
    while n<15:
        samemapstr=samemapstr+" "+str(samemap[n])
        n=n+1
    n=0
    while same!="":
        if ((i%6)==5):
            m=4
            game=""
            sameple=""
            while (m<48):
                if (same[m]!="," ):
                    game=game+same[m]
                elif(same[m]!="\n"):
                    sameple=sameple+str(ten(str(threefive(game))))
                    game=""
                if(m==47):
                    sameple=sameple+str(ten(str(threefive(game))))
                m=m+1
            while n<30: 
                if (samemapstr[n]==sameple[n]):
                    n=n+1
                    if (n==30):
                        return (0)
                else:
                    n=0
                    break;
        same= f.readline()
        i=i+1
        j=j+1
    f.close()
    return(1)

def getopenlist3(gamemap):
    ans=array.array('u',["1","2","3","4","5","6","7","8","9","A","B","C","D","E","0"])
    gamemapopen=gamemap;
    zero=gamemap.index("0")
    h=0
    if (zero == 0):
        print ("是1-1喔")
        f = open('openlist.txt','w')   #寫OPENLIST
        gamemapopen[int(zero)],gamemapopen[1]=gamemapopen[1],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[5]=gamemapopen[5],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif (zero==5):
        print ("是1-2喔")
        f = open ('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[0]=gamemapopen[0],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[6]=gamemapopen[6],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[10]=gamemapopen[10],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif(zero==10):
        print ("是1-3喔")
        f = open ('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[5]=gamemapopen[5],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[11]=gamemapopen[11],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif (zero>=1 and zero<=3):
        print ("是2,3,4-1")
        f = open ('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[int(zero)-1]=gamemapopen[int(zero)-1],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)+5]=gamemapopen[int(zero)+5],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)+1]=gamemapopen[int(zero)+1],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif (zero>5 and zero<9):
        print ("是2,3,4-2喔")
        f = open ('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[int(zero)-5]=gamemapopen[int(zero)-5],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)-1]=gamemapopen[int(zero)-1],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)+1]=gamemapopen[int(zero)+1],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero+5)]=gamemapopen[int(zero)+5],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif(zero>10 and zero<14):
        print ("是2,3,4-3喔")
        f = open('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[int(zero)-5]=gamemapopen[int(zero)-5],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)-1]=gamemapopen[int(zero)-1],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[int(zero)+1]=gamemapopen[int(zero)+1],gamemapopen[int(zero)]#
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif(zero==4):
        print ("是5-1")
        f = open ('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[3]=gamemapopen[3],gamemapopen[int(zero)] #1
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[9]=gamemapopen[9],gamemapopen[int(zero)] #2
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif (zero==9):
        print ("是5-2喔")
        f = open('openlist.txt','w')
        gamemapopen[int(zero)],gamemapopen[4]=gamemapopen[4],gamemapopen[int(zero)]  #1
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[8]=gamemapopen[8],gamemapopen[int(zero)]#2
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[14]=gamemapopen[14],gamemapopen[int(zero)]#3
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    elif(zero==14):
        print ("是5-3喔")
        f = open('openlist.txt','w')   #寫OPENLIST
        gamemapopen[int(zero)],gamemapopen[9]=gamemapopen[9],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        gamemapopen[int(zero)],gamemapopen[13]=gamemapopen[13],gamemapopen[int(zero)]
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        i=0
        h=0
        if (kicksame3(gamemapopen)>0):
            while i< len(gamemapopen):
                if ((gamemapopen[i]) != ans[i]):
                   h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemapopen[i]))-int(show((i+1)))))))
                i=i+1
            f.write(str(threefive(str(h))))
            i=0
            while i< len(gamemapopen):
                f.write(str(gamemapopen[i]))
                i=i+1
            f.write("\n")
        gamemapopen=gamemap
        f.close()
    print("\n")

def getcloselist3(gamemap,h,k):
    ans=array.array('u',["1","2","3","4","5","6","7","8","9","A","B","C","D","E","0"])
    midans=""
    f = open('closelist.txt','r')
    midans=f.readlines()
    f.close()
    
    min=15
    i=0
    f = open('openlist.txt','r')   #寫OPENLIST
    closelist = (f.readline())
    gamemapclose=closelist
    while closelist!="":
        if int(str(show(closelist[0]))) <= min:
            gamemapclose=""
            min = int(str(show(closelist[0])))
            while i <= 15:
                gamemapclose=gamemapclose+closelist[i+1]
                i=i+1
        i=0
        closelist = (f.readline())
    i=0
    h=0
    while i< 15:
        if (str(gamemapclose[i]) != ans[i]):
            h=h+int(math.sqrt(math.sqrt(abs(int(fivethree(gamemapclose[i]))-int(fivethree((ans[i])))))))
        i=i+1
    f.close()
    f = open('closelist.txt','w')
    f.writelines(midans)
    f.write(str(show(gamemapclose[0])))
    f.write(" ")
    f.write(str(show(gamemapclose[1])))
    f.write(" ")
    f.write(str(show(gamemapclose[2])))
    f.write(" ")
    f.write(str(show(gamemapclose[3])))
    f.write(" ")
    f.write(str(show(gamemapclose[4])))
    f.write("\n")
    f.write(str(show(gamemapclose[5])))
    f.write(" ")
    f.write(str(show(gamemapclose[6])))
    f.write(" ")
    f.write(str(show(gamemapclose[7])))
    f.write(" ")
    f.write(str(show(gamemapclose[8])))
    f.write(" ")
    f.write(str(show(gamemapclose[9])))
    f.write(" ")
    f.write("  h=")
    f.write(str(h))
    f.write ("     step = ")
    f.write(str(k))
    f.write("\n")
    f.write(str(show(gamemapclose[10])))
    f.write(" ")
    f.write(str(show(gamemapclose[11])))
    f.write(" ")
    f.write(str(show(gamemapclose[12])))
    f.write(" ")
    f.write(str(show(gamemapclose[13])))
    f.write(" ")
    f.write(str(show(gamemapclose[14])))
    f.write("\n")
    f.write("--------------------------")
    f.write("\n")
    g= open('gamemap.txt','w')
    gamemap=gamemapclose
    i=0
    while i<15:
        g.write(str(gamemap[i]))
        i=i+1
    g.close()
    gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])

    i=0
    while i<(len(gamemapclose)-1):
        if (i%15==0):
            f.write("5,3,")
            f.write(show(gamemapclose[i]))
        else:
            f.write(",")
            f.write(show(gamemapclose[i]))
        i=i+1
    f.write("\n")
    f.write("\n")
    f.close()
    return(h)

def threefive(game):   #判斷是什麼因為有0~14 要把10~14變成英文
    if(game=="10"):
        return("A")
    elif(game=="11"):
        return("B")
    elif(game=="12"):
        return("C")
    elif(game=="13"):
        return("D")
    elif(game=="14"):
        return("E")
    else:
        return(game)

def fivethree(ten):
    if (ten=="A"):
        return("10")
    elif(ten=="B"):
        return("11")
    elif(ten=="C"):
        return("12")
    elif(ten=="D"):
        return("13")
    elif(ten=="E"):
        return("14")
    else:
        return(ten)

def ten(ten):
    if (ten=="A"):
        return(" "+ten)
    elif(ten=="B"):
        return(" "+ten)
    elif(ten=="C"):
        return(" "+ten)
    elif(ten=="D"):
        return(" "+ten)
    elif(ten=="E"):
        return(" "+ten)
    else:
        return(ten)
        

def show(num):
    if(num=="A"):
        return("10")
    elif(num=="B"):
        return("11")
    elif(num=="C"):
        return("12")
    elif(num=="D"):
        return("13")
    elif(num=="E"):
        return("14")
    else:
        return(" "+str(num))
def A3(gamemap):    #3*5的A行演算法
    h=0
    k=1
    i=0
    ans=array.array('u',["1","2","3","4","5","6","7","8","9","A","B","C","D","E","0"])
    while i< 15:
        if (gamemap[i]!=ans[i]):
           h=h+int(math.sqrt(math.sqrt(abs(int(show(gamemap[i]))-(i+1)))))
        i=i+1
    f = open('closelist.txt','w')
    f.write(str(show(gamemap[0])))
    f.write(" ")
    f.write(str(show(gamemap[1])))
    f.write(" ")
    f.write(str(show(gamemap[2])))
    f.write(" ")
    f.write(str(show(gamemap[3])))
    f.write(" ")
    f.write(str(show(gamemap[4])))
    f.write("\n")
    f.write(str(show(gamemap[5])))
    f.write(" ")
    f.write(str(show(gamemap[6])))
    f.write(" ")
    f.write(str(show(gamemap[7])))
    f.write(" ")
    f.write(str(show(gamemap[8])))
    f.write(" ")
    f.write(str(show(gamemap[9])))
    f.write(" ")
    f.write("  h=")
    f.write(str(h))
    f.write ("     step = ")
    f.write("0")
    f.write("\n")
    f.write(str(show(gamemap[10])))
    f.write(" ")
    f.write(str(show(gamemap[11])))
    f.write(" ")
    f.write(str(show(gamemap[12])))
    f.write(" ")
    f.write(str(show(gamemap[13])))
    f.write(" ")
    f.write(str(show(gamemap[14])))
    f.write("\n")
    f.write("--------------------------")
    f.write("\n")
    i=0
    z=250
    while i<15:
        if (i%15==0):
            f.write("5,3,")
            f.write(show(gamemap[i]))
        else:
            f.write(",")
            f.write(show(gamemap[i]))
        i=i+1
    f.write("\n")
    f.write("\n")
    f.close()
    i=0
    '''if h==0:
        f = open('closelist.txt','w')
        while i<15:
            if (i==0):
                f.write("\n")
                f.write("5,3,")
                f.write(show(gamemap[i]))
            else:
                f.write(",")
                f.write(show(gamemap[i]))
            i=i+1
        f.close()'''
    while h>=1 :  #原來 h>1
        g= open('gamemap.txt','r')
        gamemap=g.readline()
        gamemap=array.array('u',[gamemap[0],gamemap[1],gamemap[2],gamemap[3],gamemap[4],gamemap[5],gamemap[6],gamemap[7],gamemap[8],gamemap[9],gamemap[10],gamemap[11],gamemap[12],gamemap[13],gamemap[14]])
        g.close()
        getopenlist3(gamemap)
        h=(getcloselist3(gamemap,h,k))
        k=k+1
        i=i+1
        z=z-1

starttime = datetime.datetime.now()#long running
f = open('Shuffle Puzzle game.txt','r')    #讀取
start=(f.readline())                                  #將讀到的資料放入START
f.close();

print (start)
print ("開始")
f= open('closelist.txt','w')                        #清空之前的Close list
f.write("")
f.close()

i=4                                         #用來將讀到的資料轉換成STRING因為前面的是代表3*3的方格所以不要從4開始取
game = ""
if(start[0]=="3"):
    while (i<22):
        game= game + start[i]+" "
        i=i+2
    gamemap=array.array('B',[int(game[0]),int(game[2]),int(game[4]),int(game[6]),int(game[8]),int(game[10]),int(game[12]),int(game[14]),int(game[16])])
    f= open('gamemap.txt','w')
    i=0
    while i<9:
        f.write(str(gamemap[i]))
        i=i+1
    f.close()
    A(gamemap)
else:
    gamemap=""
    while (i<38):
        if (start[i]!=',' ):
            game=game+start[i]

        else:
            gamemap=gamemap+threefive(game)
            game=""
        if(i==37):
            gamemap=gamemap+threefive(game)
        i=i+1
    f= open('gamemap.txt','w')
    i=0
    while i<15:
        f.write(str(gamemap[i]))
        i=i+1
    f.close()
    A3(gamemap)


endtime = datetime.datetime.now()
print (endtime-starttime)
name=input("按一下離開")
