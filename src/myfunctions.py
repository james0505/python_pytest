import time
from src import CONSTANT_A
def is_windows():
    """
    Function to check if the operating system is Windows
    :param: none
    :return: True if it is Windows
    """
    time.sleep(2) # similate actions to check
    print(flush=True)
    return True

def get_operating_system():
    return "Windows" if is_windows() else "Linux"

# CONSTANT_A = 1 was defined in pytest.ini
def double():
    return CONSTANT_A*2

class Dataset:
    def __init__(self):
        self.data = None

    def load_data(self):
        time.sleep(2)
        self.data = 'slow data'
        return self.data

def slow_dataset():
    dataset = Dataset()
    return dataset.load_data()

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(get_operating_system())
    print(slow_dataset())
    print(sum_two_numbers(3, 9))
