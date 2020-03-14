kør_program = True

while kør_program:
    num1 = float(input("tal 1?"))
    regneart = input("skriv regneart * / - + ** %")
    num2 = float(input("tal 2? "))

    if regneart =="+":
        print(num1 + num2)
    elif regneart == "-":
        print(num1 - num2)
    elif regneart == "/":
        if num2 ==0:
            print("man kan ikke dividere med nul!")
        else:
            print(num1 / num2)
    elif regneart == "*":
        print(num1 * num2)
    elif regneart == "**":
        print(num1 ** num2)
    else:
        print("forkert regneart")
    fortsæt = input("vil du gerne fortsætte j eller n: ")
    if fortsæt == "j":
        kør_program = True
    elif fortsæt == "n":
        kør_program = False

    fortsæt = input("vil du regne alle regnearter med dine tal? ")
    if fortsæt == "j":
        print(num1 + num2)
        print(num1 - num2)
        print(num1 * num2)

print("øv! du sluttede lommeregnere")
