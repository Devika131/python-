
import matplotlib.pyplot as plt

categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars 

expenses = [1200, 400, 200, 150, 250]

#create Bar Plot:

plt.bar(categories, expenses)

#Add Labels And a Titles
plt.xlabel("categories")
plt.ylabel("expenses")
plt.title("monthly expenses in different spending categories")
plt.show()
