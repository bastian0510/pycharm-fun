import random

kendtePersoner = ["Nicolas Bendtner", "Bastian Seidelin"]
overskrifter = ["Scorer!", "Taber!", "Vinder!!!!!"]

print(random.choice(kendtePersoner) + " " + random.choice(overskrifter))

noegleord = ["Tårer", "Hjertesorg", "Vrede"]
digt = "Stol på mig – hvis du opsætter mål lige fra start, så undgår du masser af $emotion"

print(digt.replace("$emotion", random.choice(noegleord)))