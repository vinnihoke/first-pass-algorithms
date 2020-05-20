'''
Input: a List of integers
Returns: a List of integers
'''
import math


def product_of_all_other_numbers(arr):
    # Your code here
    cursor = 0
    size = len(arr)
    output = [0] * size

    def recursive_helper(mod_arr):
        nonlocal cursor
        if cursor == size:
            return
        else:
            # Break apart the head from everything else.
            head, *tail = mod_arr

            # Set the output at index cursor to math.prod(tail)
            output[cursor] = math.prod(tail)

            # Increment cursor
            cursor += 1

            #  Swap first and last
            popped = mod_arr.pop(mod_arr.index(head))
            mod_arr.append(popped)

            # Re-run with the mod_arr
            recursive_helper(mod_arr)

    recursive_helper(arr)

    # Wrong implementation.
    # def recursive_helper(mod_arr):
    #     nonlocal cursor
    #     if cursor == size:
    #         return
    #     else:
    #         head, *tail = mod_arr
    #         arr[0] = math.prod(tail)
    #         popped = mod_arr.pop(mod_arr.index(head))
    #         mod_arr.append(popped)
    #         cursor += 1
    #         recursive_helper(mod_arr)
    # recursive_helper(arr)
    return output

    # Head is now the first variable in the list, tail is the rest.
    # I need to replace each index in the array by multiplying everything else in the array.
    # If i can increment head each time.


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 7, 3, 4]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    #        9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
