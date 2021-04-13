# Function Tasks
#
#
# Let's see if you can solve these word problems by creating functions.
# The function "skeleton" has been set up for you to fill in below the problem
# description, as well as example outputs of what the function should return
# given certain inputs. Best of luck, some of these will be challenging!
#
# The tasks will start off easy and proceed to get harder and harder.

# ## Task 1
#
#  Create a function that takes in two integers and returns
## a Boolean True if their sum is 10, False if their sum is something else.

def check_ten(n1,n2):
    # Code Here
    return n1+n2 == 10

#print(check_ten(8,2))


# ## Task 2
#
# Create a function that takes in two integers and returns True if their
# sum is 10, otherwise, return the actual sum value.

def check_ten_sum(n1,n2):
    # Code Here
    if n1 + n2 == 10:
        return True
    else:
        return n1 + n2


#print(check_ten_sum(9,11))

# ## Task 3
#
# Create a function that takes in a string and returns back the
# first character of that string in upper case.



def first_upper(mystring):
    # Code Here
    return mystring[0].upper()

#print(first_upper('poaspodsa'))

# ## Task 4
#
# Create a function that takes in a string and returns the last two characters.
# If there are less than two chracters, return the string:  "Error".
# Use this link if you need help/hint.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def last_two(mystring):
    # Code Here
    if len(mystring) > 2:
        return mystring[-2:]
    else:
        return "Error"

#print(last_two("sdpo"))

# ## Task 5
#
# Given a list of integers, return True if the sequence [1,2,3] is somewhere
# in the list. Hint: Use slicing and a for loop.

def seq_check(nums):
    numstring=""
    for x in nums:
        numstring = numstring + str(x)
    return '123' in numstring

#print(seq_check([1,4,2,5,7,1,2,3,5,1,6,7,8]))

# ## Task 6
#
# Given a 2 strings, create a function that returns the difference in length
# between them. This difference in length should always be a positive number
# (or just 0). Hint: Absolute Value.**



def compare_len(s1,s2):
    return abs(len(s1) - len(s2))

#print(compare_len('sds','sdd'))


# ## Task 7
#
# Given a list of integers, if the length of the list is an even number,
# return the sum of the list. If the length of the list is odd, return the max
## value in that list.



def sum_or_max(mylist):
    if len(mylist) % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)

print(sum_or_max([1,5,3,6]))