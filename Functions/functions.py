def function_a():
    print("A starts")
    function_b()
    print("A ends")

def function_b():
    print("B starts")
    function_c()
    print("B ends")

def function_c():
    print("C runs")

function_b()

def check_age(age):
    if age < 18:
        return "Too young"
    elif age > 65:
        return "Senior"
    else:
        return "Adult"

    print("This never runs!")  # Dead code!

result = check_age(25)
print(result)
