###Based on the code below: in the last print statement, print the following to the console: 'Toyota', 35.5, 'Chicken', 'Swiss'###

embedded_lists = [[["Number of Cars", 3],["Car Brands", "Chevy", "Toyota", "Honda"],["MPG", 18, 35.5, 12]],[["Protein", "Veggies", "Rice", "Cheese"],["Chicken", "Steak", "Pork"], ["Peppers", "Onions", "Tomatoes", "Corn"],["White", "Brown"], ["Colby", "Swiss"]]]

print(embedded_lists[0][1][2], embedded_lists[0][2][2], embedded_lists[1][1][0], embedded_lists[1][4][1])

# for i in embedded_lists:
#     print(i[1])