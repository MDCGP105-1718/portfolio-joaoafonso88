annual_salary = float(input("Enter your annual salary: "))
total_cost = float(input("Enter the total cost of the house: "))
portion_saved = float(input("Percentage of the monthly salary to save: "))

portion_deposit = 0.2
r = 0.04
current_savings = 0
monthly_salary = (annual_salary/12)

number_of_months = 0


while (current_savings < total_cost * portion_deposit):
    current_savings += current_savings * r / 12.0
    current_savings += monthly_salary * portion_saved
    number_of_months += 1

print("Number of months to save:", number_of_months)
