def interchange_first_last(lst):
    if len(lst) < 2:
        return lst  # if the list has less than 2 elements, no change needed
    
    # Swap first and last elements
    lst[0], lst[-1] = lst[-1], lst[0]
    
    return lst

# Example usage:
input_list = [12, 35, 9, 56, 24]
print("Original List:", input_list)
interchanged_list = interchange_first_last(input_list[:])  # pass a copy to avoid modifying original list
print("Interchanged List:", interchanged_list)
