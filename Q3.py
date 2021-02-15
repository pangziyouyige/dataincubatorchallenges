import numpy as np

# Set the random seed to reproduce results
np.random.seed(420)

# Set the bags of coins
coins = [0.01, 0.05, 0.1, 0.25, 0.5]

# Set the equal probabilities
probabilities = [1/5 for x in range(len(coins))]

# test to draw one coin from the bag
outcome = np.random.choice(coins, p=probabilities, size=1)

print("Outcome of the draw: {:.5f}".format(outcome[0]))

"""Q1: Suppose you draw 10 coins at random from the bag (assume each of the five coin types will come up with equal probability 
for each draw). What is the probability that you will be able to buy an item for $1.00?"""

# Set the cost to pay
Q1_cost = 1.00

# Initiate the numpy array to store the change you get back from the cashier
Q1_results = np.empty(50000)

# Use statistical simulation to model 10000 times, 10 draws for each time, what are the total amount for each of 10000 times
for i in range(len(Q1_results)):
    Q1_results[i] = np.sum(np.random.choice(coins, p=probabilities, size=10))

# Calculate the percentage of times that the amount is higher than 1.00, which represents the probability
Q1_probability = np.sum(Q1_results >= Q1_cost)/len(Q1_results)

print("the probability that you will be able to buy an item for $1.00 is {:.5f}".format(Q1_probability))

"""Q2:Suppose you draw 10 coins at random from the bag (assume each of the five coin types will come up with equal probability 
for each draw). What is the probability that you will be able to buy an item for $2.00?"""

# Set the cost to pay
Q2_cost = 2.00

# Initiate the numpy array to store the change you get back from the cashier
Q2_results = np.empty(50000)

# Use statistical simulation to model 10000 times, 10 draws for each time, what are the total amount for each of 10000 times
for i in range(len(Q2_results)):
    Q2_results[i] = np.sum(np.random.choice(coins, p=probabilities, size=10))

# Calculate the percentage of times that the amount is higher than 2.00, which represents the probability
Q2_probability = np.sum(Q2_results >= Q2_cost)/len(Q2_results)

print("the probability that you will be able to buy an item for $2.00 is {:.5f}".format(Q2_probability))

"""Q3:Now suppose that to pay for an item, you draw single coins one at a time from the bag (again, assume each of the five 
coin types will come up with equal probablility for each draw) until you have enough for the item and then give those coins 
to the cashier. What is the expected amount of the change you get back from the cashier when the item costs $0.25?"""

# Set the cost that need to pay
Q3_cost = 0.25

# Initiate the numpy array to store the change you get back from the cashier
Q3_results = np.empty(50000)

# Use statistical simulation to run 10000 times and get the change back for each time
for i in range(len(Q3_results)):
    amount = 0
    while amount < Q3_cost:
        outcome = np.random.choice(coins, p = probabilities, size = 1)
        amount += outcome
    Q3_results[i] = amount - Q3_cost

# expected amount of the change 
print("the expected amount of change when the item cost $0.25 is {:.5f}".format(np.mean(Q3_results)))

"""Q4: What is the standard deviation of the change you get back from the cashier when the item costs $0.25?"""

# standard deviation of the change 
print("the standard deviation of change when the item cost $0.25 is {:.5f}".format(np.std(Q3_results)))

"""Q5: What is the expected amount of the change you get back from the cashier when the item costs $1.00?"""

# Set the cost that need to pay
Q5_cost = 1.00

# Initiate the numpy array to store the change you get back from the cashier
Q5_results = np.empty(50000)

# Use statistical simulation to run 10000 times and get the change back for each time
for i in range(len(Q5_results)):
    amount = 0
    while amount < Q5_cost:
        outcome = np.random.choice(coins, p = probabilities, size = 1)
        amount += outcome
    Q5_results[i] = amount - Q5_cost

# expected amount of the change 
print("the expected amount of change when the item cost $1.00 is {:.5f}".format(np.mean(Q5_results)))

"""Q6: What is the standard deviation of the change you get back from the cashier when the item costs $1.00?"""

# standard deviation of the change 
print("the standard deviation of change when the item cost $1.00 is {:.5f}".format(np.std(Q5_results)))

"""Q7: What is the expected amount of the change you get back from the cashier when the item costs $10.00?"""

# Set the cost that need to pay
Q7_cost = 10.00

# Initiate the numpy array to store the change you get back from the cashier
Q7_results = np.empty(50000)

# Use statistical simulation to run 10000 times and get the change back for each time
for i in range(len(Q7_results)):
    amount = 0
    while amount < Q7_cost:
        outcome = np.random.choice(coins, p = probabilities, size = 1)
        amount += outcome
    Q7_results[i] = amount - Q7_cost

# expected amount of the change 
print("the expected amount of change when the item cost $10.00 is {:.5f}".format(np.mean(Q7_results)))

"""Q8: What is the standard deviation of the change you get back from the cashier when the item costs $10.00?"""

# standard deviation of the change 
print("the standard deviation of change when the item cost $10.00 is {:.5f}".format(np.std(Q7_results)))

