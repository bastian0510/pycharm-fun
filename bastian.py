kendtperson = input("skriv en kendt person: ")

print("du ser en " + kendtperson + " som gerne vil have dig ind i et rum!")

valg1 = input("vælg a. og gå ind i rumet b. sige nej og gå")

if valg1 == "a":
    print("du overlevde")
    print("du møder en gammel mand på gaden!")
    valg2 = input("a. du gå med ham en i hans bil elller b. ringer til politiet")
    if valg2 == "b":
        print("manden bliver sændt i fængsel")
    else:
        print("du bliver ikke kidnappede")
else:
    print("du blev kidnappede og spillet er slut")
