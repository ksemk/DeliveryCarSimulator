import random

# Introduction
print("Welcome to Delivery Car Simulation")

# Defining constants of car states
INITIAL_STATE = "D0"
STATE_D1 = "D1"
STATE_D2 = "D2"
FAILURE = "F"

# Defining costs of maintenance and inspection
MAINTENANCE_COST_D1 = 250
MAINTENANCE_COST_D2 = 300
INSPECTION_COST_D1 = 200
INSPECTION_COST_D2 = 220
FAILURE_COST = 50000

# Defining parameters of transition intensity
transition_intensity01 = 1200       # Time range to go from D0 to D1
transition_intensity12 = 1000       # Time range to go from D1 to D2
transition_intensity23 = 800        # Time range to go from D2 to F
transition_intensityF = 5           # Time range to go from F to D0

# Defining variables for values summed for all simulations for chosen simulation duration
total_time_in_use = 0               # Total amount of time when cars can be used in firm 
total_time_unused = 0               # Total amount of time when cars can not be used in firm (e.g. maintenance, inspection or failure) 
total_time_overhaul = 0             # Total amount of time needed to replace cars
total_costs = 0                     # Sum of all costs spent on car maintenance and/or replacement
total_failure_costs = 0             # Sum of all costs spent on car replacement only
total_maintenance_costs = 0         # Sum of all costs spent on maintenance only
total_failure_counter = 0           # Total number of cars being in failure state
total_initial_state_counter = 0     # Numbers of times the cars was in initial state 
total_d1_state_counter = 0          # Number of times the cars was in D1 state 
total_d2_state_counter = 0          # Number of times the cars was in D2 state 


# File reader function
def read_file(file_name):
    maintenance_policy = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                maintenance_policy.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_name}' doesn't exist")
    return maintenance_policy

# To maintain the car decision probability
def inspection(state):
    if state == STATE_D1:
        print("Car inspection 1")
        return random.randint(0, 100) <= decision_probability1
    elif state == STATE_D2:
        print("Car inspection 2")
        return random.randint(0, 100) <= decision_probability2

# State update after maintenance 
def maintenance(state):
    if state == STATE_D1:
        print("The car is in state D1 and needs maintenance.")
        # After the car was in state D1 and was fixed, it goes to a better condition state (INITIAL_STATE)
        return INITIAL_STATE
    elif state == STATE_D2:
        print("The car is in state D2 and needs maintenance.")
        # After the car was in state D1 and was fixed, it goes to a better condition state (STATE_D1)
        return STATE_D1

# Simulation
def mainLoop(i):
    """
    Simulates the main loop of a delivery car simulator.

    Args:
        i (int): The duration of the simulation in time units.

    Returns:
        None

    Raises:
        None
    """

    # Definition of global variables
    global total_time_in_use, total_time_unused, total_time_overhaul, total_costs, total_failure_costs, total_maintenance_costs
    global total_failure_counter, total_initial_state_counter, total_d1_state_counter, total_d2_state_counter

    # Initialization of local simulation variables
    time_in_use = 0             # Car can be used in firm
    time_unused = 0             # General time of car being unused e.g. maintenance, inspection or failure
    time_overhaul = 0           # Time needed to replace a car after its failure
    time_of_simulation = 0      # Whole time of simulation (used + unused)
    costs = 0                   # Sum of all costs (maintenance costs, inspection costs, car replacement costs)
    failure_costs = 0           # Costs of car replacement only
    maintenance_costs = 0       # Maintenance costs only
    failure_counter = 0         # Number of cars being replaced
    initial_state_counter = 0   # Number of times a car was in initial condition
    d1_state_counter = 0        # Number of times a car was in lightly used condition
    d2_state_counter = 0        # Number of times a car was in highly used condition
    state = INITIAL_STATE       # Current state of the car
    time1t = time1i = time1m = time2t = time2i = time2m = time3t = timeF = 0    # Time variables for transitions between states

    # Main simulation loop
    while time_of_simulation < i:
        if state == INITIAL_STATE:
            # Updating state counter
            initial_state_counter += 1
            print("\nThe car is in the initial state.")

            # Time of the transition from initial state to D1 state (generates a random number from 100 to transition_intensity01)
            time1t = random.randint(100, transition_intensity01)

            # Updating time counters
            time_in_use += time1t
            time_of_simulation += time1t

            # Changing state to D1 (worse condition)
            state = STATE_D1
        elif state == STATE_D1:
            # Updating state counter
            d1_state_counter += 1
            print("\nThe car is in state D1.")

            # Time needed to inspect the car in state D1 (generates a random number from 0 to inspection_range1)
            time1i = random.randint(0, inspection_range1)
            if inspection(state):
                # If inspection decision is positive (maintenance needed), changing the state to Initial (better condition)
                state = maintenance(state)

                # Time of the maintenance needed to car repair from D1 state to initial state (generates a random number from 0 to maintenance_range1)
                time1m = random.randint(0, maintenance_range1)

                # Updating time and costs counters
                time_unused += time1m + time1i
                time_of_simulation += time1m + time1i
                costs += MAINTENANCE_COST_D1 * time1m + INSPECTION_COST_D1 * time1i
            else:
                # If inspection decision is negative (no maintenance needed), change state to D2 (worse condition)
                state = STATE_D2

                # Time of the transition from D1 state to D2 state (generates a random number from 100 to transition_intensity12)
                time2t = random.randint(100, transition_intensity12)

                # Updating time and costs counters
                time_of_simulation += time2t + time1i
                time_unused += time1i
                time_in_use += time2i
                costs += INSPECTION_COST_D1 * time1i
        elif state == STATE_D2:
            # Updating state counter
            d2_state_counter += 1
            print("\nThe car is in state D2.")

            # Time needed to inspect the car in state D2 (generates a random number from 0 to inspection_range1)
            time2i = random.randint(0, inspection_range2)
            if inspection(state):
                # If inspection decision is positive (maintenance needed), changing the state to D1 (better condition)
                state = maintenance(state)

                # Time of maintenance needed to car repair from D2 state to D1 state (generates a random number from 0 to maintenance_range1)
                time2m = random.randint(0, maintenance_range2)

                # Updating time and costs counters
                time_unused += time2m + time2i
                time_of_simulation += time2i + time2m
                costs += MAINTENANCE_COST_D2 * time2m + INSPECTION_COST_D2 * time2i
            else:
                # If inspection decision is negative (no maintenance needed), change state to Failure (worse condition)
                state = FAILURE

                # Time of the transition from D2 state to Failure state (generates a random number from 100 to transition_intensity12)
                time3t = random.randint(100, transition_intensity23)
                
                # Updating time and costs counters
                time_unused += time2i
                time_of_simulation += time2i + time3t
                time_in_use += time3t
                costs += INSPECTION_COST_D2 * time2i
        elif state == FAILURE:
            # Updating state and costs counters
            failure_costs += FAILURE_COST
            failure_counter += 1
            print("\nThe car is broken")

            # Time needed to replace the car when its cant be used due to its condition (generates a random number from 1 to transition_intensityF))
            timeF = random.randint(1, transition_intensityF)

            # Update costs and time counters
            time_overhaul += timeF
            time_of_simulation += timeF
            costs += FAILURE_COST

            # Change state to initial (replaced damaged car with a new one)
            state = INITIAL_STATE

    # Update counters for all simulations for chosen simulation duration 
    total_time_in_use += time_in_use
    total_time_unused += time_unused
    total_time_overhaul += time_overhaul
    total_costs += costs
    total_failure_counter += failure_counter
    total_initial_state_counter += initial_state_counter
    total_d1_state_counter += d1_state_counter
    total_d2_state_counter += d2_state_counter
    maintenance_costs = costs - failure_costs
    total_failure_costs += failure_costs
    total_maintenance_costs += maintenance_costs
    
    # Count average car time usage statistics for a single simulation in percents
    time_in_use_percentage = (time_in_use * 100) / time_of_simulation
    time_unused_percentage = (time_unused * 100) / time_of_simulation
    time_overhaul_percentage = (time_overhaul * 100) / time_of_simulation

    # Single simulation log
    print(f"\nSimulation finished.")
    print(f"Simulation time: {time_of_simulation}")
    print(f"Time in use: {time_in_use} ({round(time_in_use_percentage, 1)}%)")
    print(f"Time unused: {time_unused} ({round(time_unused_percentage, 1)}%)")
    print(f"Overhaul time: {time_overhaul} ({round(time_overhaul_percentage, 1)}%)")
    print(f"Total costs: {costs}")
    print(f"Failure costs: {failure_costs}")
    print(f"Maintenance costs: {maintenance_costs}")
    print(f"Number of failures: {failure_counter}")
    print(f"Number of initial states: {initial_state_counter}")
    print(f"Number of D1 states: {d1_state_counter}")
    print(f"Number of D2 states: {d2_state_counter}")

# Main menu
program_status = True
while program_status:
    print("1. Set simulation parameters and run the simulation")
    print("2. Exit")
    option = int(input("Choose an option: "))
    if option == 1:
        # Initial values for data generation
        current_policy = sim_num = min_simulation_time = max_simulation_time = dots_num = 0

        # Choosing maintenance policy
        while current_policy != 1 and current_policy != 2 and current_policy != 3:
            current_policy = int(input("Choose the policy: "))
            if current_policy != 1 and current_policy != 2 and current_policy != 3:
                print("\nWrong option, please try again!\n")

        # Choosing number of simulations to run for a single dot on the plot to minimize the impact of the simulation uncertainty 
        while sim_num <= 0:
            sim_num = int(input("Enter the number of simulations: "))
            if sim_num <= 0:
                print("\nWrong option, please try again!\n")

        # Defining minimal value of a single simulation time
        while min_simulation_time <= 0:
            min_simulation_time = int(input("Enter the minimum time range of simulation: "))
            if min_simulation_time <= 0:
                print("\nWrong option, please try again!\n")

        # Defining maximal value of a single simulation time
        while max_simulation_time <= 0 or max_simulation_time < min_simulation_time:
            max_simulation_time = int(input("Enter the maximum time range of simulation: "))
            if max_simulation_time <= 0 or max_simulation_time < min_simulation_time:
                print("\nWrong option, please try again!\n")

        # Defining the number of dots to use in a plot
        while dots_num <= 0:
            dots_num = int(input("Enter the number of points for chart: "))
            if dots_num <= 0:
                print("\nWrong option, please try again!\n")

        # Counting the gap between the dots on a plot
        leap = int((max_simulation_time - min_simulation_time) / dots_num)

        # Reading maintenance policy from the file
        if current_policy == 1:
            filename = "DeliveryCarSimulator\simulation_results\policy1_results.csv"
            with open(filename, "w") as file:
                file.write("")  # This clears the content of the file.
            maintenance_policy = read_file("DeliveryCarSimulator\maintenance_policies\policy1.txt")
        elif current_policy == 2:
            filename = "DeliveryCarSimulator\simulation_results\policy2_results.csv"
            with open(filename, "w") as file:
                file.write("")  # This clears the content of the file.
            maintenance_policy = read_file("DeliveryCarSimulator\maintenance_policies\policy2.txt")
        elif current_policy == 3:
            filename = "DeliveryCarSimulator\simulation_results\policy3_results.csv"
            with open(filename, "w") as file:
                file.write("")  # This clears the content of the file.
            maintenance_policy = read_file("DeliveryCarSimulator\maintenance_policies\policy3.txt")

        # Saving values of the policies into variables
        decision_probability1 = int(maintenance_policy[0])    # maintenance probability range for state D1
        decision_probability2 = int(maintenance_policy[1])    # maintenance probability range for state D2
        maintenance_range1 = int(maintenance_policy[2])       # maintenance time range for state D1
        maintenance_range2 = int(maintenance_policy[3])       # maintenance time range for state D2
        inspection_range1 = int(maintenance_policy[4])        # inspection time range for state D1
        inspection_range2 = int(maintenance_policy[5])        # maintenance time range for state D2

        # Running the simulation
        for time in range(min_simulation_time, max_simulation_time, leap):
            for simulation in range(sim_num):
                mainLoop(time)

            # Counting average values for simulation log
            average_time_in_use = total_time_in_use / sim_num
            average_costs = total_costs / sim_num
            average_failure_costs = total_failure_costs / sim_num
            average_maintenance_costs = total_maintenance_costs / sim_num

            # Simulation log for a single dot on a plot
            print("\nAverage results: ")
            print(f"Time in use: {total_time_in_use / sim_num}")
            print(f"Time unused: {total_time_unused / sim_num}")
            print(f"Overhaul time: {total_time_overhaul / sim_num}")
            print(f"Costs: {total_costs / sim_num}")
            print(f"Number of failures: {total_failure_counter / sim_num}")
            print(f"Number of initial states: {total_initial_state_counter / sim_num}")
            print(f"Number of D1 states: {total_d1_state_counter / sim_num}")
            print(f"Number of D2 states: {total_d2_state_counter / sim_num}")
            print(f"Failure costs: {total_failure_costs / sim_num}")
            print(f"Maintenance costs: {total_maintenance_costs / sim_num}")

            # Write the results to the chosen CSV file
            with open(filename, "a") as file:
                file.write(f"{average_time_in_use}, {average_costs}, {average_failure_costs}, {average_maintenance_costs}\n")

            # Setting initial values to variables for the next simulation
            average_time_in_use = 0
            average_costs = 0
            total_time_in_use = 0
            total_time_unused = 0
            total_time_overhaul = 0
            total_costs = 0
            total_failure_counter = 0
            total_initial_state_counter = 0
            total_d1_state_counter = 0
            total_d2_state_counter = 0
            total_failure_costs = 0
            total_maintenance_costs = 0
    
    # Exit the program
    elif option == 2:
        program_status = False
    else:
        print("\nWrong option, please try again!\n")
