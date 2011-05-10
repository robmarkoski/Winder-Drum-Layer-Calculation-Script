#Enter Drum
import math
import sys
"""
drumw = int(input("Enter Drum Width (mm): "))
drumd = int(input("Enter Drum Diameter (mm): "))
drumf = int(input("Enter Drum Flange Diameter (mm): "))
ropel = int(input("Enter Rope Length (m): "))
roped = int(input("Enter Rope Diameter (mm): "))
grooved = input("Is the drum grooved? Y or N : ")
"""

drumw = 1016 #Drum Width
drumd = 508 #Drum Diameter
drumf = 966 #Drum Flange Height
ropel = 500 #Length of Rope
roped = 24 #Diameter of Rope
grooved = "Y" #Is drum grooved?

def get_max_width(table1,index1):
    """Get max width given column index"""
    return max([len(format(row1[index1])) for row1 in table])



def printoutput(tdata):
    colpad = []
    out = sys.stdout
    for i in range(len(tdata[0])):
        colpad.append(get_max_width(table,i))
    for row in tdata:
        for i in range(0,len(row)):
            col = format(row[i]).center(colpad[i]+1)
            print(col, end=" | ",file=out)
        print(file=out)
    return

length = 0
cuml = 0
flangd = 0
pcd = 0
layer = 1 

roped2 = roped * 1.02 #Include for rope stretch.
layerb = round(drumw/roped2) #Estimate amount of layers on bottom layer of drum
aroped = drumw/layerb #average diameter of rope
coils = round(drumw/aroped)
delta = (aroped**2- aroped**2/4)**0.5
table = [["Layer","Length (m)","PCD (mm)","Coils","Cumulative Length (m)"]]
print("delta: {: .2f}".format(delta))

while (cuml < ropel):	
    if (layer == 1):
        pcd = round(drumd + aroped,2)
        length = round(pcd/1000 * 3.14159 * coils,2)

        cuml = length
        table.append([layer,length,pcd,coils,cuml])
        layer = 2
    
    else:
        pcd = round(pcd + delta,2)
        if (layer % 2):
            coils = coils -1
        else:
            coils = coils +1
        length = round(pcd/1000 * 3.14159 * coils,2)
        cuml = round(cuml + length,2)
        if (cuml > ropel):
            ropeleft = round(ropel - (cuml - length),2)
            coils = round(ropeleft / (pcd/1000 * 3.14159),0)
            cuml = round(ropel,2)
        
        table.append([layer,length,pcd,coils,cuml])
        layer = layer +1

printoutput(table)


    
