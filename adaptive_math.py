import addition_module, subtraction_module, multiplication_module, division_module

print("""
which of the following modules would you like to do?

addition
subtraction
multiplication
division
""")
ask = input()
if ask == 'addition':
    addition_module.addit()
elif ask == 'subtraction':
    subtraction_module.subtraction()
elif ask == 'multiplication':
    multiplication_module.multiplication()
elif ask == 'division':
    division_module.division()
