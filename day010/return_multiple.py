# functions with outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        print("You didn't provide valid inputs.")
        return format_name(input("First name: "), input("Last name: "))
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Full name: {formated_f_name} {formated_l_name}'

print(format_name(input("First name: "), input("Last name: ")))