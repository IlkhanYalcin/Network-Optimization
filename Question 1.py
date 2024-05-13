from gurobipy import *
import numpy as np


m1 =Model("Warm-up Question")

# Ranges

variables = range(0,3)


# Decision Variables

x1 = m1.addVar( vtype = GRB.INTEGER , name = "x1")
x2 = m1.addVar( vtype = GRB.INTEGER , name = "x2")
x3 = m1.addVar( vtype = GRB.INTEGER , name = "x3")


# Objective Function 

##(1)
obj = 78*x1 + 63*x2 + 94*x3
m1.setObjective(obj, GRB.MAXIMIZE)

#Subject To

##(2)
m1.addConstr(2*x1 + x2 + 4*x3 <= 51)
m1.addConstr(x1 + 3*x2 + 2*x3 <= 41)
m1.addConstr(x1 + x2 >= 14)


m1.optimize()


#Variable values
for v in m1.getVars():
    print(f"{v.varName} = {v.X}")


#Objective function value
print("Optimal Objective Value of the Problem:", m1.objVal)