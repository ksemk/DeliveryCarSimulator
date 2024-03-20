import random
from car import Car

# Introduction
print("Welcome to Delivery Car Simulation")

# Simulation parameters input
simulation_duration = int(input("Enter simulation duration (in iterations): "))
inspection_frequency = int(input("Enter inspection frequency: "))
inspection_counter = inspection_frequency

# Creating car object
initial_state = 100.0
reliability = int(input("Enter reliability score: "))
maintain_time = 1
gigadamagerate = int(input("Enter upper range for bigger damage: "))
car_1 = Car(initial_state, reliability, maintain_time, gigadamagerate)

# Simulation loop
for i in range(simulation_duration):
    if inspection_counter == i:
        if car_1.state <= 50:
            print("Repairing process initiated")
        inspection_counter += inspection_frequency

    if car_1.state <= 0:
        print("The car has reached a critical damage level and is broken.")
        break

    print("Car State: " + str(car_1.state) + "%")
    car_1.damage()
    rand = random.randint(0, 100)

    if rand in range(0, car_1.reliability):
        car_1.gigadamage()

# todo zużycie z upłyłem czasu (zależny od producenta)
# todo rozszerzenie na całą flotę pojazdów
