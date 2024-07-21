def check_element_in_list(lst, element):
    if element in lst:
        return True
    else:
        return False

# Example usage:
my_list = [1, 2, 3, 4, 5]

# Check if 3 exists in the list
element_to_check = 3
if check_element_in_list(my_list, element_to_check):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")

# Check if 10 exists in the list
element_to_check = 10
if check_element_in_list(my_list, element_to_check):
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
