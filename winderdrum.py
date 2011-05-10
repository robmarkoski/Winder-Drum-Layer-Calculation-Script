#Enter Drum
import math
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

def printoutput(layer, length, pcd, coils, cuml):
	print("| {:d} | {:.2f} | {:.2f} | {:.2f} | {:.2f} |".format(layer,length,pcd,coils,cuml))

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

print("delta: {: .2f}".format(delta))
print("| Layer | Length | PCD | Coils | Cumulative Length |")
while (cuml < ropel):
    if (layer == 1):
        table = ""
        pcd = drumd + aroped
        length = pcd/1000 * 3.14159 * coils
        cuml = length
        printoutput(layer,length,pcd,coils,cuml)
        layer = 2
        
    else:
        pcd = pcd + delta
        if (layer % 2):
            coils = coils -1
        else:
            coils = coils +1
        length = pcd/1000 * 3.14159 * coils
        cuml = cuml + length
        if (cuml > ropel):
            ropeleft = ropel - (cuml - length)
            coils = round(ropeleft / (pcd/1000 * 3.14159))
            cuml = ropel
        print("{:d} | {:.2f} | {:.2f} | {:.2f} | {:.2f}".format(layer,length,pcd,coils,cuml))
        layer = layer +1
        



    
