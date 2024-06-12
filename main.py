import random
from car import Car

# Introduction
print("Welcome to Delivery Car Simulation")

# Defining constants
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

# Reading the maintenance policy from the config file
transition_intencity01 = 6    #time range to go from D0 to D1
transition_intencity12 = 3    #time range to go from D1 to D2
transition_intencity23 = 2   #time range to go from D2 to F
transition_intencityF = 1     #time range to go from F to D0

# Defining variables for total values
total_time_in_use = 0
total_time_unused = 0
total_time_overhaul = 0
total_costs = 0
total_failure_counter = 0
total_initial_state_counter = 0
total_d1_state_counter = 0
total_d2_state_counter = 0

# File operations
file_name = 'config.txt'

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

decision_probability1 = int(maintance_policy[0])
decision_probability2 = int(maintance_policy[1])
maintance_range1 = int(maintance_policy[2])          #maintenance time range for state D1
maintance_range2 = int(maintance_policy[3])          #maintenance time range for state D2
inspection_range1 = int(maintance_policy[4])
inspection_range2 = int(maintance_policy[5])

def inspection(state):
    if state == STATE_D1:
        print("Car inspection 1")
        return random.randint(0, 100) <= decision_probability1
    elif state == STATE_D2:
        print("Car inspection 2")
        return random.randint(0, 100) <= decision_probability2

def maintenance(state):
    if state == STATE_D1:
        print("The car is in state D1 and needs maintenance.")
        return INITIAL_STATE
    elif state == STATE_D2:
        print("The car is in state D2 and needs maintenance.")
        return STATE_D1

def mainLoop(i):
    global total_time_in_use, total_time_unused, total_time_overhaul, total_costs
    global total_failure_counter, total_initial_state_counter, total_d1_state_counter, total_d2_state_counter
    time_in_use = 0
    time_unused = 0
    time_overhaul = 0
    time_of_simulation = 0
    costs = 0
    failure_counter = 0
    initial_state_counter = 0
    d1_state_counter = 0
    d2_state_counter = 0

    state = INITIAL_STATE
    while time_of_simulation < i:
        if state == INITIAL_STATE:
            initial_state_counter += 1
            print("\nThe car is in the initial state.")
            time1t = random.randint(0, transition_intencity01)
            time_in_use += time1t
            time_of_simulation += time1t
            state = STATE_D1
        elif state == STATE_D1:
            d1_state_counter += 1
            print("\nThe car is in state D1.")
            time1i = random.randint(0, inspection_range1)
            if inspection(state):
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
            d2_state_counter += 1
            print("\nThe car is in state D2.")
            time2i = random.randint(0, inspection_range2)
            if inspection(state):
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
            failure_counter += 1
            print("\nThe car is broken")
            timeF = random.randint(1, transition_intencityF)
            time_overhaul += timeF
            time_of_simulation += timeF
            costs += FAILURE_COST
            state = INITIAL_STATE

    total_time_in_use += time_in_use
    total_time_unused += time_unused
    total_time_overhaul += time_overhaul
    total_costs += costs
    total_failure_counter += failure_counter
    total_initial_state_counter += initial_state_counter
    total_d1_state_counter += d1_state_counter
    total_d2_state_counter += d2_state_counter

    # Print the simulation time and time in use
    time_in_use_persentage = (time_in_use * 100) / time_of_simulation
    time_unused_persentage = (time_unused * 100) / time_of_simulation
    time_overhaul_persentage = (time_overhaul * 100) / time_of_simulation

    print(f"\nSimulation finished.")
    print(f"Simulation time: {time_of_simulation}")
    print(f"Time in use: {time_in_use} ({round(time_in_use_persentage, 1)}%)")
    print(f"Time unused: {time_unused} ({round(time_unused_persentage, 1)}%)")
    print(f"Overhaul time: {time_overhaul} ({round(time_overhaul_persentage, 1)}%)")
    print(f"Costs: {costs}")
    print(f"Number of failures: {failure_counter}")
    print(f"Number of initial states: {initial_state_counter}")
    print(f"Number of D1 states: {d1_state_counter}")
    print(f"Number of D2 states: {d2_state_counter}")

# Call the main loop function
sim_num = int(input("Enter the number of simulations: "))
i = int(input("Enter time:"))

for x in range(sim_num):
    mainLoop(i)

average_time_in_use = total_time_in_use / sim_num
average_costs = total_costs / sim_num

print("\nAvarage results: ")
print(f"Time in use: {total_time_in_use/sim_num}")
print(f"Time unused: {total_time_unused/sim_num}")
print(f"Overhaul time: {total_time_overhaul/sim_num}")
print(f"Costs: {total_costs/sim_num}")
print(f"Number of failures: {total_failure_counter/sim_num}")
print(f"Number of initial states: {total_initial_state_counter/sim_num}")
print(f"Number of D1 states: {total_d1_state_counter/sim_num}")
print(f"Number of D2 states: {total_d2_state_counter/sim_num}")

# Writing the results to a CSV file
with open("policy1_results.csv", "a") as file:
    file.write(f"{average_time_in_use}, {average_costs}\n")
