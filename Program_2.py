def draw_pattern(rows):
    for i in range(rows, 0, -1):  # Loop from rows to 1 in descending order
        for j in range(1, i + 1):  # Loop from 1 to i (current row number)
            print(j, end='')  # Print numbers from 1 to i on the same line
        print()  # Move to the next line after printing each row

# Example usage:
rows = 5
draw_pattern(rows)
