import random
import json

with open("verbes.json", "r", encoding="utf-8") as file:
    conjugaisons = json.load(file)


# Liste des temps verbaux
temps = ["présent", "passé composé", "imparfait", "futur",
         "plus-que-parfait", "conditionnel présent", "conditionnel passé"]
d = {"a": 1, "b": 2, "c": 3, "d": 4}
accents = {'Aigu': ['é'], 'Grave ': ['à', 'è', 'ù'], 'Circonflexe ': [
    'â', 'ê', 'î', 'ô', 'û'], 'Tréma': ['ë', 'ï', 'ü'], 'Cédille': ['ç']}


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

        print(
            f"\nQuelle est la conjugaison correcte pour '{verbe}' au {temps_choisi} ?")
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

        print(
            f"\nQuelle est la conjugaison correcte pour '{verbe}' au {temps_choisi} pour '{pronom}' ?")
        options = generer_options(verbe, temps, conjugaison_correcte)

        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choix = int(input("Votre choix : ")) - 1
        if choix < 0 or choix >= len(options):
            print("Choix invalide.")
            continue

        if options[choix] == conjugaison_correcte:
            print("✅ Correct !")
            score += 1
        else:
            print(f"❌ Faux. La réponse correcte est : {conjugaison_correcte}")

    print(f"Votre score : {score}/10")


def jouer_trois():
    score = 0
    pronoms = ["je", "tu", "il/elle", "nous", "vous", "ils/elles"]
    for _ in range(10):
        verbe = random.choice(list(conjugaisons.keys()))
        temps_choisi = random.choice(temps)
        index_pronom = random.randint(0, 5)
        conjugaison_correcte = conjugaisons[verbe][temps_choisi][index_pronom]
        pronom = pronoms[index_pronom]

        print(
            f"\n Quelle est la conjugaison correcte pour '{verbe}' au {temps_choisi} pour '{pronom}' ?")
        prem_choix = input("Votre choix :")
        if prem_choix == ":qa":
            print("Au revoir !")
            break
        elif prem_choix == conjugaison_correcte:
            print("✅ Correct !")
            score += 1
        else:
            print(
                f"❌ Faux. La réponse correcte est : {conjugaison_correcte}")
    print(f"Votre score : {score}/10")


def mots_jouer():
    score = 0
    with open("translate.json", "r", encoding="utf-8") as file:
        mots = json.load(file)
    for _ in range(10):
        mot = random.choice(list(mots.keys()))
        vrai_mots_anglais = mots[mot].split(',')
        print(f"Quelle est la traduction anglaise de « {mot} »?")
        resp = input("Votre choix: ")
        if resp == ":qa":
            print("Au revoir !")
            break
        if len(vrai_mots_anglais) > 1:
            found = False
            for mot in vrai_mots_anglais:
                if resp == mot.strip():
                    print("✅ Correct !")
                    score += 1
                    found = True
            if not found:
                print(
                    f"❌ Faux. La réponse correcte est : {vrai_mots_anglais}")
        else:
            if resp == vrai_mots_anglais[0]:
                print("✅ Correct !")
                score += 1
            else:
                print(
                    f"❌ Faux. La réponse correcte est : {vrai_mots_anglais}")
    print(f"Votre score : {score}/10")


def main():
    while True:
        print("\nMenu Principal")
        print("1. Jouer")
        print("2. Jouer (Dur)")
        print("3. Mots Jouer")
        print("4. Quitter")

        choix = input("Votre choix : ")
        acc = list(accents.values())
        print(f"Accents: {list(accents.values())}")
        if choix == "1":
            jouer2()
        elif choix == "2":
            jouer_trois()
        elif choix == "3":
            mots_jouer()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
