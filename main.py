import random
from car import Car

# Introduction
print("Welcome to Delivery Car Simulation")

# Defining constans
INITIAL_STATE = "D0"
STATE_D1 = "D1"
STATE_D2 = "D2"
FAILURE = "F"

# Defining variables
file_name = 'config.txt'
#maintance_probability_d1 = 0.9
#maintance_probability_d2 = 0.95


#simulation_time = 0
#Reading from file
def read_file(file_name):
    maintance_policy = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                maintance_policy.append(line.strip())
    except FileNotFoundError:
        print(f"Plik '{file_name}' nie istnieje")

    return maintance_policy

maintance_policy = read_file(file_name)
#Parameters
transition_intencity01 = int(maintance_policy[0])
transition_intencity12 = int(maintance_policy[1])
transition_intencity23 = int(maintance_policy[2])
decision_probability1 = int(maintance_policy[3])
decision_probability2 = int(maintance_policy[4])
maintance_range1 = int(maintance_policy[5])
maintance_range2 = int(maintance_policy[6])

def inspection(state):
    if state == STATE_D1:
        random_number = random.randint(0, 100)
        if random_number <= decision_probability1:
            print("Car inspection")
            return True
        else:
            return False
    if state == STATE_D2:
        random_number = random.randint(0, 100)
        if random_number <= decision_probability2:
            print("Car inspection")
            return True
        else:
            return False

# Defining functions
def maintance(state):
    if state == STATE_D1:
        print("The car is in state D1 and needs maintenance.")
        state = INITIAL_STATE
    elif state == STATE_D2:
        print("The car is in state D2 and needs maintenance.")
        state = STATE_D1



# Main loop
def mainLoop():
    state = INITIAL_STATE
    while state != FAILURE:
        if state == INITIAL_STATE:
            print("The car is in the initial state.")
            state = STATE_D1
        elif state == STATE_D1:
            print("The car is in state D1.")
            if inspection(state):
                maintance(state)
            else:
                state = STATE_D2
        elif state == STATE_D2:
            print("The car is in state D2.")
            if inspection(state):
                maintance(state)
            else:
                state = FAILURE

mainLoop()