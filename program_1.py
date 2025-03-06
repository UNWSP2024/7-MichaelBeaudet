# Title: Week 7 Program 1
# Author: Michael Beaudet
# Date: 3/6/25

def rainfall_calculation():
    months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    rainfall = []
# Get rainfall for each month
    for month in months:
        rainfall.append(float(input(f"Enter the rainfall for {month}: ")))
# Calculate each measurement
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    most_rainfall = max(rainfall)
    least_rainfall = min(rainfall)
# Get the max and minimum rain values
    highest_month = months[rainfall.index(most_rainfall)]
    lowest_month = months[rainfall.index(least_rainfall)]
# Display the measurements
    print(f"The total rainfall was: {total_rainfall:.2f} inches")
    print(f"The average rainfall for every month was: {average_rainfall:.2f}")
    print(f"The month with the most rain was: {highest_month} and it rained: {most_rainfall:.2f}")
    print(f"The month with the least rain was: {lowest_month} and it only rained: {least_rainfall:.2f}")

if __name__ == "__main__":
    rainfall_calculation()