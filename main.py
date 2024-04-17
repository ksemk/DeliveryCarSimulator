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



#Reading from file
def read_file(file_name):
    maintance_policy = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                maintance_policy.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist")

    return maintance_policy

maintance_policy = read_file(file_name)

#Parameters
transition_intencity01 = int(maintance_policy[0])    #time range to go from D0 to D1
transition_intencity12 = int(maintance_policy[1])    #time range to go from D1 to D2
transition_intencity23 = int(maintance_policy[2])    #time range to go from D2 to F
decision_probability1 = int(maintance_policy[3])
decision_probability2 = int(maintance_policy[4])
maintance_range1 = int(maintance_policy[5])          #maintance range for state D1
maintance_range2 = int(maintance_policy[6])          #maintance range for state D2

def inspection(state):
    if state == STATE_D1:
        print("Car inspection 1")
        random_number = random.randint(0, 100)
        if random_number <= decision_probability1:
            return True
        else:
            return False
    if state == STATE_D2:
        print("Car inspection 2")
        random_number = random.randint(0, 100)
        if random_number <= decision_probability2:
            return True
        else:
            return False

# Defining functions
def maintenance(state):
    if state == STATE_D1:
        print("The car is in state D1 and needs maintenance.")

        return INITIAL_STATE
    elif state == STATE_D2:
        time2 = random.randint(0, maintance_range2)
        print("The car is in state D2 and needs maintenance.")
        return STATE_D1



# Main loop function
def mainLoop():
    simulation_time = 0
    time_in_use = 0
    time_unused = 0
    state = INITIAL_STATE
    while state != FAILURE:
        if state == INITIAL_STATE:
            print("\nThe car is in the initial state.")
            time1t =random.randint(0, transition_intencity01)
            simulation_time += time1t
            time_in_use += time1t
            state = STATE_D1
        elif state == STATE_D1:
            print("\nThe car is in state D1.")
            time2t = random.randint(0, transition_intencity12)
            simulation_time += time2t
            time_in_use += time2t
            if inspection(state) == True:
                state = maintenance(state)
                time1m = random.randint(0, maintance_range1)
                simulation_time += time1m
                time_unused += time1m
            else:
                state = STATE_D2
        elif state == STATE_D2:
            print("\nThe car is in state D2.")
            time3 = random.randint(0, transition_intencity23)
            simulation_time += time3
            time_in_use += time3
            if inspection(state) == True:
                state = maintenance(state)
                time2m = random.randint(0, maintance_range2)
                simulation_time += time2m
                time_unused += time2m
            else:
                state = FAILURE

    # Print the simulation time and time in use
    print(f"\nSimulation finished.")
    print(f"Simulation time: {simulation_time}")
    print(f"Time in use: {time_in_use}")
    print(f"Time unused: {time_unused}")



# Call the main loop function
mainLoop()
