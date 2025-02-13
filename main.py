import random
import json

with open("verbes.json", "r", encoding="utf-8") as file:
    conjugaisons  = json.load(file)


# Liste des temps verbaux
temps = ["présent", "passé composé", "imparfait", "futur", "plus-que-parfait"]


def generer_options(verbe, temps, correcte):
    options = [correcte]
    while len(options) < 4:
        autre_temps = random.choice(temps)
        autre_conjugaison = random.choice(conjugaisons[verbe][autre_temps])
        if autre_conjugaison != correcte and autre_conjugaison not in options:
            options.append(autre_conjugaison)
    random.shuffle(options)
    return options

def jouer():
    score = 0
    for _ in range(10):
        verbe = random.choice(list(conjugaisons.keys()))
        temps_choisi = random.choice(temps)
        conjugaison_correcte = random.choice(conjugaisons[verbe][temps_choisi])

        print(f"\nQuelle est la conjugaison correcte pour '{verbe}' au {temps_choisi} ?")
        options = generer_options(verbe, temps, conjugaison_correcte)

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choix = int(input("Votre choix : ")) - 1
        if choix < 0 or choix >= len(options):
            print("Choix invalide.")
            continue

        if options[choix] == conjugaison_correcte:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Faux. La réponse correcte est: {conjugaison_correcte}")

    print(f"Votre score : {score}/10")

def jouer2():
    score = 0
    pronoms = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]
    for _ in range(10):
        verbe = random.choice(list(conjugaisons.keys()))
        temps_choisi = random.choice(temps)
        index_pronom = random.randint(0, 5)
        conjugaison_correcte = conjugaisons[verbe][temps_choisi][index_pronom]
        pronom = pronoms[index_pronom]

        print(f"Quelle est la conjugaison correcte pour '{verbe}' au {temps_choisi} pour '{pronom}' ?")
        options = generer_options(verbe, temps, conjugaison_correcte)

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choix = int(input("Votre choix : ")) - 1
        if choix < 0 or choix >= len(options):
            print("Choix invalide.")
            continue

        if options[choix] == conjugaison_correcte:
            print("Correct !")
            score += 1
        else:
            print(f"Faux. La réponse correcte est : {conjugaison_correcte}")

    print(f"Votre score : {score}/10")


def main():
    while True:
        print("\nMenu Principal")
        print("1. Jouer")
        # print("2. Jouer 2")
        print("2. Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            jouer2()
        elif choix == "2":
        #     jouer2()
        # elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
