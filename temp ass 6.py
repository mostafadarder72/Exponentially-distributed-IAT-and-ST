#Exponentially distributed IAT and ST
import random
import math
from dataclasses import dataclass
from prettytable import PrettyTable


lamda = float(input("Enter the value of lamda IAT: "))
def exp_iat(lamda):
    return round(-math.log(1-random.random())/lamda)
    
lamda2 = float(input("Enter the value of lamda ST: "))
def exp_st(lamda2):
    return round(-math.log(random.random())/lamda2)
    

#for test functions IAT and ST
#print("Exponentially distributed IAT: ", round(exp_iat(lamda)))
#print("Exponentially distributed ST: ", round(exp_st(lamda2)))
@dataclass
class Row:
    IAT: int = 0
    St: int = 0
    Arrival: int = 0
    Sstart: int = 0
    Send: int = 0
    waiting: int = 0
    Qlen: int = 0
    spend_time: int =0

size = 10
simtable = []
c1 = Row()
Iat = exp_iat(lamda)
St = exp_st(lamda2)
c1.IAT = Iat
c1.ST = St
c1.Arrival = Iat
c1.Sstart = Iat
c1.Send = c1.Sstart + St
c1.waiting = 0
c1.Qlen = 0
simtable.append(c1)

# all customers
for i in range(1, size):
    c = Row()
    Iat = exp_iat(lamda)
    St = exp_st(lamda2)
    c.IAT = Iat
    c.ST = St
    c.Arrival = simtable[i - 1].Arrival + Iat
    if c.Arrival > simtable[i - 1].Send:
        c.Sstart = c.Arrival
        c.Send = c.Sstart + St
        c.waiting = 0
    else:
        c.Sstart = simtable[i - 1].Send
        c.waiting = simtable[i - 1].Send - c.Arrival
        c.Send = c.Sstart + St
    q_count = 0
    j = i-1
    while (c.Arrival < simtable[j].Sstart):
        q_count += 1
        j -= 1
    c.Qlen = q_count
    c.spend_time=c.Send-c.Arrival
    simtable.append(c)


myTable = PrettyTable(["#", "IAT", "ST", "arrival" , "sstart " ,"send", "waiting " ,"queulenth"])
i = 0
for x in simtable:
    i += 1
    # Add rows
    myTable.add_row([ i, x.IAT, x.ST, x.Arrival, x.Sstart, x.Send, x.waiting, x.Qlen])
    print(myTable)
    
    
    
    
    
    
    