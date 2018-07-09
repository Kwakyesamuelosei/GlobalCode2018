
def calculate(operator,operand_1,operand_2):
    if operator == "add":
        resuts = operand_1 + operand_2
        return resuts
    elif operator == "subtract":
        resuts = operand_1 - operand_2
        return resuts
    elif operator == "multiply":
        resuts = operand_1 * operand_2
        return resuts
    elif operator == "divide":
        resuts = operand_1 / operand_2
        return resuts
    else:
        return "Operator Not Available"

print("Your result : {0}".format(calculate("gh",1,1)))
