import pandas as pd


df = pd.read_csv(r'C:\Users\Anilc\OneDrive\Desktop\Python\Data\details.csv')

print("DataFrame Head:")

mean_salary = df['salary'].mean()
print("\nMean Salary:", mean_salary)


median_salary = df['salary'].median()
print("Median Salary:", median_salary)

mode_salary = df['salary'].mode()
print("Mode Salary:", mode_salary[0])
