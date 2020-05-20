'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import timeit


def single_number(arr):
    start = timeit.default_timer()

    # Your code here
    # Store an array of double values seen in the loop.
    # Loop again and check if the value is in this list.
    # List comprehension to check for duplicated and remove the odd balls.
    # Can we use sets?
    dupes = {}
    for e in arr:
        if e not in dupes.keys():
            dupes[e] = 1
        else:
            dupes[e] += 1

    for key, value in dupes.items():
        if value == 1:
            final = timeit.default_timer() - start
            print(f"Time: {final:.8f}:")
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
