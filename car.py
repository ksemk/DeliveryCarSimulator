import random


class Car:
    """
    Represents a delivery car.

    Attributes:
        state (float): The current state of the car.
        reliability (int): The reliability score of the car.
        maintain_time (int): The time interval between maintenance.
        gigadamagerate (int): The upper range for bigger damage.
    """

    def __init__(self, state, reliability, maintain_time, gigadamagerate):
        """
        Initializes a new Car instance.

        Parameters:
            state (float): The initial state of the car.
            reliability (int): The reliability score of the car.
            maintain_time (int): The time interval between maintenance.
            gigadamagerate (int): The upper range for bigger damage.
        """
        self.state = state
        self.reliability = reliability
        self.maintain_time = maintain_time
        self.gigadamagerate = gigadamagerate

    def damage(self):
        """
        Simulates regular wear and tear on the car.
        """
        self.state -= 0.5  # Adjust as per actual production rate.

    def gigadamage(self):
        """
        Simulates a significant damage occurrence on the car.
        """
        random_gigadamge = random.randint(1, self.gigadamagerate)
        self.state -= random_gigadamge
        print("A significant damage occurred: " + str(random_gigadamge) + "%")
