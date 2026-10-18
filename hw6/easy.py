# This function uses O(n)

# create list
lst = [5, 3, 2, 6, 89, 4, 3]

# define function sum_numbers
def sum_numbers(numbers):

    # establist variable to keep track of sum
    sum_lst = 0 

    # O(n)
    for i in numbers:

        # add each value to find the total of the list
        sum_lst += i

    # return the sum
    return sum_lst

# call the function
my_sum = sum_numbers(lst)

# print out the sum
print("Sum: ", my_sum)
    

