
import matplotlib.pyplot as plt
days = list(range(1, 32)) 
# Daily temperature data  
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]
# Create the line plot
plt.plot(days, temperature,marker='o')
# Add labels and a title
plt.xlabel("Days")
plt.ylabel("Temperature (°F)")
plt.title("Daily Temperature Over a Time in city")
plt.show()
