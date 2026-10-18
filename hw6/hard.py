# This function uses O(n)

# establish list
lst = [5, 3, 2, 6, 89, -4, 3]

# define function to find the difference of the max and min numbers in a list
def number_difference(numbers):

    # establish variables to keep track
    my_max = numbers[0]
    my_min = numbers[0]

    # O(n)
    for num in numbers: 

        # if the number is greater than the current maximum...
        if num > my_max:

            # replace the maximum
            my_max = num

        # if the number is less than the current minimum...
        if num < my_min:

            # replace the minimum
            my_min = num

    # find the greatest difference
    my_difference = my_max - my_min
    return my_difference

# call the function
the_difference = number_difference(lst)

# print out findings
print(the_difference)