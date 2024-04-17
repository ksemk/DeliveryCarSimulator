import random


class Car:
    """
    Represents a delivery car.

    Attributes:
        state (string): The current state of the car.
    """

    def __init__(self, state):
        """
        Initializes a new Car instance.

        Parameters:
            state (string): The initial state of the car.

        """
        self.state = state
