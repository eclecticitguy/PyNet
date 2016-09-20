#!/usr/bin/env python

'''
2. Write a function that converts a list to a dictionary where the
index of the list is used as the key to the new dictionary (the
function should return the new dictionary).
'''

def list_to_dict(a_list):

    # Initialize blank dict
    return_dict = {}

    # Enumerate and loop through list parameter
    for k, v in enumerate(a_list):
        # For every list element, set dictionary key to list index and dictionary value to list value
        return_dict[k] = v

    # Return completed dictionary
    return return_dict

# Initialize test list
test_list = [1, 3, 5, 'a', 'b', 'c']

# Call function 'list_to_dict' using test list and print the output to STDOUT
print list_to_dict(test_list)
