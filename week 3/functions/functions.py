# DRY - dont repeat yourself
# DRY - dont repeat yourself
# DRY - dont repeat yourself
# DRY - dont repeat yourself

from tkinter import N


def directions():
    print("trun left out of parking lot.")
    print("drive to stop light and turn left.")
    print("drive one mile through canfield.")
    print("starbucks is across the street from sheetz.")
    print("turn left into starbucks")

directions()

number_of_ppl = int(input("how many people are asking for directions?"))

while number_of_ppl > 0:
    print(f"{number_of_ppl} - New Directions")
    directions()
    number_of_ppl = number_of_ppl - 1