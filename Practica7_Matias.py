import random

while True:

    name = input("\n\tEnter your name --> ")
    
    file_name = 'practica7' + str(name) + '.txt'
    f = open(file_name, 'w')
    i = range(1,1000000)
    code = print(f"\n\n\t\t ===> {name} = {random.choice(i)}")
    f.write(str(code))

    again = input("\n\tWould you like to check another person's code? --> (y/n)").lower()
    if again.startswith("n"):
        print("Goodbye\n\nBe safe!")
        f.close()
        break