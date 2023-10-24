def caronly(km):
    cost= (km * 0.2312)* 2
    print (cost)
    return cost

def carpublic(km,cost):
    pubtotcost= (km * 0.2312+ cost)*2
    print (pubtotcost)
    return pubtotcost

def publiconly(cost):
    pubonlycost= (cost)*2
    print (pubonlycost)
    return pubonlycost

transtype= input("How did you travel to the course :\nA = caronly \nB = carpublic \nC = publiconly \n Answer: ")
if transtype == "A":
    cardist = float(input("Enter KMS Travelled: "))
    caronly(cardist)
elif transtype == "B":
    carpubdist = float(input("Enter distance to the station"))
    carpubcost = float(input("Enter cost of train and taxi"))
    carpublic(carpubdist,carpubcost)

elif transtype == "C":
    pubcost = float(input("Enter the cost of public transport: "))
    publiconly(pubcost)
    
else:
    print ("Try Again")
