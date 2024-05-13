from gurobipy import *
from numpy import *

m1 = Model(name = "Question 2")

data = array([   [1,-1,2],
                 [1,0,-1],
                 [2,1,3],
                 [6,-1,4]])


#Decision Variables
x_12 = m1.addVar(vtype = "B", name = f"x_12")
x_14 = m1.addVar(vtype = "B", name = f"x_14")
x_23 = m1.addVar(vtype = "B", name = f"x_23")
x_25 = m1.addVar(vtype = "B", name = f"x_25")
x_36 = m1.addVar(vtype = "B", name = f"x_36")
x_45 = m1.addVar(vtype = "B", name = f"x_45")
x_47 = m1.addVar(vtype = "B", name = f"x_47")
x_56 = m1.addVar(vtype = "B", name = f"x_56")
x_58 = m1.addVar(vtype = "B", name = f"x_58")
x_69 = m1.addVar(vtype = "B", name = f"x_69")
x_78 = m1.addVar(vtype = "B", name = f"x_78")
x_710 = m1.addVar(vtype = "B", name = f"x_710")
x_89 = m1.addVar(vtype = "B", name = f"x_89")
x_811 = m1.addVar(vtype = "B", name = f"x_811")
x_912 = m1.addVar(vtype = "B", name = f"x_912")
x_1011 = m1.addVar(vtype = "B", name = f"x_1011")
x_1112 = m1.addVar(vtype = "B", name = f"x_1112")

#Objective Function
object = data[0,0] + data[0,1]* x_12 + data[1,0]* x_14 + data[0,2]* x_23 +data[1,1]* x_25 +data[1,2]* x_36 +data[1,1]* x_45 \
+ data[2,0]* x_47 +data[1,2]* x_56 + data[2,1]* x_58 + data[1,2]* x_69 + data[2,1]* x_78 + data[3,0]* x_710 + data[2,2]* x_89 + \
data[3,1]* x_811 + data[3,2]* x_912 + data[3,1]* x_1011 + data[3,2]* x_1112

m1.setObjective(object, GRB.MAXIMIZE)

#Constraints 
m1.addConstr(x_12 + x_14 == 1)
m1.addConstr(x_23 + x_25 == x_12)
m1.addConstr(x_36 == x_23)
m1.addConstr(x_45 + x_47 == x_14)
m1.addConstr(x_56 + x_58 == x_25 + x_45)
m1.addConstr(x_69 == x_36 + x_56)
m1.addConstr(x_78 + x_710 == x_47)
m1.addConstr(x_89 + x_811 == x_58 + x_78)
m1.addConstr(x_912 == x_69 + x_89)
m1.addConstr(x_1011 == x_710)
m1.addConstr(x_1112 == x_1011 + x_811)


m1.optimize()

#Variable values
for v in m1.getVars():
    print(f"{v.varName} = {v.X}")

#Objective function value

print("Optimal Objective Value of the Problem:", m1.objVal)

