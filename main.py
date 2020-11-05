from agent import *
zero = Agent(0)
one = Agent(1)
two = Agent(2)
agents = [zero, one, two]
option_0 = (1,2,4)
option_1 = (1,2,3)
Agent.options.append(option_0)
Agent.options.append(option_1)


#### testing first part of exercise ####
for op in range(2):
    print("option "+ str(op) + ": " +str(Agent.options[op]))
print("******* RESULTS *******")

if isParetoImprovement(agents, 0, 1):
    print("option 0 is a preto improvement to option 1")
else:
    print("option 0 is not a preto improvement to option 1")
if isParetoImprovement(agents, 1, 0):
    print("option 1 is a preto improvement to option 0")
else:
    print("option 1 is not a preto improvement to option 0")


option_0 = (1,3,3)
option_1 = (2,1,5)
option_2 = (3,2,5)
option_3 = (4,5,1)
option_4 = (5,4,1)

Agent.options.clear()
Agent.options.append(option_0)
Agent.options.append(option_1)
Agent.options.append(option_2)
Agent.options.append(option_3)
Agent.options.append(option_4)
alloptions = [0,1,2,3,4] # op.1 is not  pareto optimal because of opt.2
# alloptions = [0,1,3,4] # now (after removing op.2) op.1 is pareto optimal
### testing second part of exercise ###
print()
print("Phase 2:\n")
for op in alloptions:
    print("option "+ str(op) + ": " +str(Agent.options[op]))
print("******* RESULTS *******")
for op in alloptions:
    if isParetoOptimal(agents, op, alloptions):
        print("option "+str(op) +" is pareto optimal!")

