import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date


# 1. Open the CSV file
with open('employees.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # 3. Loop through the rows and print out name and age
    for row in reader:
        birth_year = int(row['date_of_birth'][:4])
        age = 2023 - birth_year
        print(row['name'], age)
        
        # 4. Calculate the average age
        if 'ages' not in locals():
            ages = [age]
        else:
            ages.append(age)
    avg_age = sum(ages) / len(ages)
    print(f"Average age: {avg_age:.2f}")
    
    # 5. Function to find employee with highest salary
    def find_highest_salary(file):
        with open(file, 'r') as f:
            reader = csv.DictReader(f)
            highest_salary = 0
            highest_salary_employee = None
            for row in reader:
                salary = int(row['salary'])
                if salary > highest_salary:
                    highest_salary = salary
                    highest_salary_employee = row['name']
            return highest_salary_employee
        
    # 9. Write modified data back to new CSV file
    def write_to_csv(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
    
    # 6. Use pandas to read the CSV file into a DataFrame
    df = pd.read_csv('employees.csv')
    
    # 7. Sort the DataFrame by salary in descending order and print the top 5 employees
    top_employees = df.sort_values('salary', ascending=False).head()
    print(top_employees)
    
    # 8. Use matplotlib to create a bar chart of the number of employees in each department
    department_counts = df['department'].value_counts()
    department_counts.plot(kind='bar')
    plt.title('Number of Employees by Department')
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.show()
