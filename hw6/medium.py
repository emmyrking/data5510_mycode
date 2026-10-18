# This function uses O(n)

# create list of numbers
lst = [3, 1, 4, 5, 9, 2, 6]

# define function to find second largest number in a list
def second_largest(numbers):

    # establish variables to keep track
    largest = 0
    secondLargest = 0


    # O(n)
    for num in numbers: 

        # if the number is greater than the current largest...
        if num > largest:
            
            # move current largest to second largest
            secondLargest = largest

            # replace the largest
            largest = num

        # if the number is greater than the second largest...
        elif num > secondLargest: 

            # replace the second largest
            secondLargest = num

    # return the second largest number
    return secondLargest

# call the function
my_second_largest = second_largest(lst)

# print the second largest number
print("Second Largest Number: ", my_second_largest)
