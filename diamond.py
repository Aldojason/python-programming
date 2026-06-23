rows = int(input("Enter number of rows: "))

# Upper half (including middle row)
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars.strip())

# Lower half
for i in range(rows - 1, 0, -1):
    spaces = " " * (rows - i)
    stars = "* " * i
    print(spaces + stars.strip())
