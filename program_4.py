# Title: Week 7 Program 4 
# Author: Michael Beaudet
# Date 3/7/25

import math

def distance(point1, point2):
# Define each point
    x1, y1, z1 = point1
    x2, y2, z2 = point2
# Calculate the distance
    distance_calculation = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 -z1) ** 2)
    
    return distance_calculation

def main():
    try: 
# Get the user's input as a tuples and use split() to separate each number
        point1 = tuple(map(float, input("Enter the coordinates for the first point (x1, y1, z1): ").split()))
        point2 = tuple(map(float, input("Enter the coordinates for the second point (x2, y2, z2): ").split()))
# Display the results
        print(f"The distance between the points is: {distance(point1, point2)}")
# Display an error if the user's inputs are invalid    
    except ValueError:
        print("Invalid input. Please enter the coordinates properly")
# Call the main function
if __name__ == "__main__":
    main()