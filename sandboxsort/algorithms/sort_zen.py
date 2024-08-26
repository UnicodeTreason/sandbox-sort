import random


def sort(inputData: list = None) -> list:
    """Calculate Zen Sort

    Parameters
    ----------
    inputData : list
        The unsorted list

    Returns
    -------
    list
        The sorted list
    """

    # Generate random data if none provided
    if not inputData:
        size = 10
        min_val = 1
        max_val = 100
        inputData = [random.randint(min_val, max_val) for _ in range(size)]

    print('Zen Sort')
    print(f'Unsorted list: {inputData}')
    print(f'Sorted array: {inputData}')
    return inputData


if __name__ == "__main__":
    print('Direct Call')
    sort()
