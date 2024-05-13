from gurobipy import *
from numpy import *


#Assumptions
## 1- If you have the full capacity while visiting a city, you can take the special person with you, with the detail of one of the 
#people you took have to be left behind. So you gain the function, but the people carried will remain the same.

## 2 - When the program visits Cremona, it will receive 0 person because of Yiğit.

## 3 - When the capacity is full, program can still visit the neighboring cities but does not pick people, as desired.

#Model
m1 = Model(name = "Question 3")

#ranges 
cities = range(1,13)

#Data & Parameters
human_lim = 82 * 7 #574


city_names = {1:"Pavia", 2:"Lodi",3:"Milan",4:"Varese",
              5:"Como",6:"Monza",7:"Lecco",8:"Sondrio",
              9:"Bergamo",10:"Brescia",11:"Mantua",12:"Cremona"}

city_pop = {1 : 86,
            2 : 23,
            3 : 326,
            4 : 89,
            5 : 60,
            6 : 86,
            7 : 34,
            8 : 18,
            9 : 111, #Assuming Yiğit is Effective in this region
            10: 127,
            11: 41,
            12: 0}

neighbors = {
    1: [2, 3],
    2: [3, 9],
    3: [4,6],
    4: [5, 6],
    5: [6, 7, 8],
    6: [8,12],
    7: [8,9],
    8: [10],
    9: [10,12],
    10: [11,12],
    11: [12],
    12: [12]
}


#Decision Variables

x = m1.addVars(cities, vtype = "B", name = f"city {cities}")
carrier = m1.addVar(vtype = "B")
carried =m1.addVar(vtype = GRB.INTEGER)

#objective function

objective = carried
#(1)
m1.setObjective(objective, GRB.MAXIMIZE)



#Constraints
##(2)
m1.addConstr(x[1] == 1, name = "Nodes has to be started at 1")

##(3)
###Assuming that doctor lives in Milan
m1.addConstr(x[3] == 1) 

##(4)
m1.addConstr(quicksum(x[i] for i in cities) == 7, name = "visit 7 nodes")

##(5)
m1.addConstr(carrier <= x[5])



##(6)
#m1.addConstr(quicksum(city_pop[i] * x[i] for i in cities) >= carried)   

##(7)
m1.addConstr(carried <= human_lim + 78 * carrier) 

##(8)
for i in cities:
    m1.addConstr(quicksum(x[i] for i in neighbors[i]) >=  x[i])


m1.optimize()


#Variable values
for v,i in zip(m1.getVars(), range(1,13)):
    print(f"{city_names[i]} = {v.X}")

#Objective function value

print("Optimal Objective Value of the Problem:", m1.objVal)



