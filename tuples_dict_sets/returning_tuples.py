def calculate_payment(hours,rate):
    subtotal = hours * rate
    tax = subtotal * 0.10
    total = subtotal + tax
    return (subtotal, tax, total)

def generate_invoice(name,projects):
    print(f"Invoice for {name}\n" + "-"* 100)
    grand_total = 0
    for project_name, hours, rate in projects:
        subtotal, tax, total = calculate_payment(hours,rate)
        grand_total += total

        print(f"{project_name}")
        print(f"Hours Worked: {hours}")
        print(f"Hourly Rate:${subtotal:.2f}")
        print(f"Tax:(10%): ${tax:.2f}")
        print(f"Total: ${total:2f}\n")

    return name, len(projects), grand_total

projects = (
    ("website Design", 20, 120),
    ("Ui mockup", 15, 150),
    ("Brand Logo", 10, 75)
)

summary = generate_invoice("Ahad", projects)

name, total_projects, grand_total = summary

print("summary".center(41,"-"))
print(f"Freelancer{name}")
print(f"Projects Completed: {total_projects}")
print(f"Grand Total: ${grand_total:.2f}")
