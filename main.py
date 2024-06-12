import random
from car import Car

# Introduction
print("Welcome to Delivery Car Simulation")

# Defining constans
INITIAL_STATE = "D0"
STATE_D1 = "D1"
STATE_D2 = "D2"
FAILURE = "F"

# Defining costs of maintenance and inspection
MAINTENANCE_COST_D1 = 100
MAINTENANCE_COST_D2 = 200
INSPECTION_COST_D1 = 20
INSPECTION_COST_D2 = 50
FAILURE_COST = 500

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
transition_intencityF = int(maintance_policy[3])     #time range to go from F to D0
decision_probability1 = int(maintance_policy[4])
decision_probability2 = int(maintance_policy[5])
maintance_range1 = int(maintance_policy[6])          #maintance time range for state D1
maintance_range2 = int(maintance_policy[7])          #maintance time range for state D2
inspection_range1 = int(maintance_policy[8])
inspection_range2 = int(maintance_policy[9])


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
        #time2 = random.randint(0, maintance_range2)
        print("The car is in state D2 and needs maintenance.")
        return STATE_D1



# Main loop function
def mainLoop():
    time_in_use = 0
    time_unused = 0
    time_overhaul = 0
    time_of_simulation = 0
    costs = 0


    state = INITIAL_STATE
    print("Enter time:")
    i = int(input())
    while time_of_simulation < i:
        if state == INITIAL_STATE:
            print("\nThe car is in the initial state.")
            time1t = random.randint(0, transition_intencity01)
            time_in_use += time1t
            state = STATE_D1
            time_of_simulation += time1t
        elif state == STATE_D1:
            print("\nThe car is in state D1.")
            # Inspection in state D1
            time1i = random.randint(0, inspection_range1)
            if inspection(state) == True:
                state = maintenance(state)
                time1m = random.randint(0, maintance_range1)
                time_unused += time1m + time1i
                time_of_simulation += time1m + time1i
                costs += MAINTENANCE_COST_D1 * time1m + INSPECTION_COST_D1 * time1i
            else:
                state = STATE_D2
                time2t = random.randint(0, transition_intencity12)
                time_of_simulation += time2t + time1i
                time_unused += time1i
                time_in_use += time2t
                costs += INSPECTION_COST_D1 * time1i
        elif state == STATE_D2:
            print("\nThe car is in state D2.")

            # Inspection in state D2
            time2i = random.randint(0, inspection_range1)
            if inspection(state) == True:
                state = maintenance(state)
                time2m = random.randint(0, maintance_range2)
                time_unused += time2m + time2i
                time_of_simulation += time2i + time2m
                costs += MAINTENANCE_COST_D2 * time2m + INSPECTION_COST_D2 * time2i
            else:
                time3t = random.randint(0, transition_intencity23)
                time_unused += time2i
                time_of_simulation += time2i + time3t
                time_in_use += time3t
                costs += INSPECTION_COST_D2 * time2i
                state = FAILURE
        elif state == FAILURE:
            print("\nThe car is broken")
            timeF = random.randint(1, transition_intencityF)
            time_overhaul += timeF
            time_of_simulation += timeF
            costs += FAILURE_COST
            state = INITIAL_STATE

    # Print the simulation time and time in use
    time_in_use_persentage = (time_in_use * 100) / time_of_simulation
    time_unused_persentage = (time_unused * 100) / time_of_simulation
    time_overhaul_persentage = (time_overhaul * 100) / time_of_simulation
    print(f"\nSimulation finished.")
    print(f"Simulation time: {time_of_simulation}")
    print(f"Time in use: {time_in_use} ({round(time_in_use_persentage,1)}%)")
    print(f"Time unused: {time_unused} ({round(time_unused_persentage,1)}%)")
    print(f"Overhaul time: {time_overhaul} ({round(time_overhaul_persentage,1)}%)")
    print(f"Costs: {costs}")



# Call the main loop function
mainLoop()


# DATA frames, csv
# seaborn py
# overhaul