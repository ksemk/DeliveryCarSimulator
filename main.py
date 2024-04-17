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
maintance_probability_d1 = 0.9
maintance_probability_d2 = 0.95

simulation_time = 0
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


def inspection(state):
    if state == STATE_D1:
        random_number = random.randint(0, 10)
        if random_number <= maintance_probability_d1 * 10:
            state = INITIAL_STATE
            return True
        else:
            return False
    if state == STATE_D2:
        random_number = random.randint(0, 100)
        if random_number <= maintance_probability_d2 * 100:
            return True
        else:
            state = FAILURE
            return False


# Defining functions
def maintance(state):
    if state == STATE_D1:
        print("The car is in state D1 and needs maintenance.")
        state = INITIAL_STATE
    if state == STATE_D2:
        print("The car is in state D2 and needs maintenance.")
        state = STATE_D1