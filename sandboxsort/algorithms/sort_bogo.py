import random


def calculate(inputData: list = None) -> list:
    """Calculate

    Parameters
    ----------
    na : None

    Returns
    -------
    list
        The sorted list
    """

    # Stolen from: https://en.wikipedia.org/wiki/Bogosort
    # Generate random data if none provided
    if not inputData:
        size = 10
        min_val = 1
        max_val = 100
        inputData = [random.randint(min_val, max_val) for _ in range(size)]

    # Confirm Sort
    def is_sorted(random_array):
        for i in range(1, len(random_array)):
            if random_array[i] < random_array[i - 1]:
                return False
        return True

    # Perform Bogo sort
    def bogo_sort(random_array):
        while not is_sorted(random_array):
            random.shuffle(random_array)
        return random_array

    print(f'Unsorted list: {inputData}')
    sortedData = bogo_sort(inputData)
    print(f'Sorted array: {sortedData}')
    return sortedData


if __name__ == "__main__":
    print('Calculating Solutions...')
    calculate()
