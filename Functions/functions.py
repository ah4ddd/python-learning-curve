def calculate_average(sales_list):
    total = sum(sales_list)
    average = total / len(sales_list)
    return average

daily_sales = [10, 15, 20]
avg = calculate_average(daily_sales)
print(f"Average: {avg}")
