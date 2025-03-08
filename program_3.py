# Title: Week 7 Program 3
# Author: Michael Beaudet
# Date: 3/7/25

def main():
# Initialize the all_entered_values list
    all_entered_values = []
# Create a while loop 
    while True:
# Get the year
        year = input("Enter the year or type done to finish: ")
        if year.lower() == 'done':
            break
        try:
            year = int(year)
# Get the state
            state = input("Enter the state's name: ")
# Get the population
            population = int(input("Enter the population: "))
# Put the results into the list
            all_entered_values.append([year, state, population])
# Display and error if the user does a wrong input
        except ValueError:
            print("Invalid input. Please enter the proper values.")
# Get the year that the user whats to sum
    year_to_sum = int(input("Enter the year to sum the populations for: "))
# Call the data
    sum_population_for_year(all_entered_values, year_to_sum)

def sum_population_for_year(all_entered_values, year_to_sum):
# Initialaze total_population 
    total_population = 0
# Create the loop 
    for input in all_entered_values:
        year, state, population = input 
        if year == year_to_sum:
# Add the population
            total_population += population
# Display the results
    print(f"The total population for the year {year_to_sum} is: {total_population}")

# Call the main function
if __name__ == '__main__':
    main()