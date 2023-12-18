def balanceVictory(a, b):
    balance = int(a - b)
    return balance


def rankingClassifier(XP):
    index = 0
    a = int(0)
    b = int(0)
    c = int(10)

    while index != 11:
        if XP >= b and XP <= c:
            a += 1
            index = 11
        else:
            index += 1
            a += 1
            b += 10
            c += 10
    return a


def rankingHero(balance):
    heroClassifier = rankingClassifier(balance)

    match heroClassifier:
        case 1:
            ranking = "Ferro"
        case 2:
            ranking = "Bronze"
        case 3:
            ranking = "Prata"
        case 4:
            ranking = "Prata"
        case 5:
            ranking = "Prata"
        case 6:
            ranking = "Ouro"
        case 7:
            ranking = "Ouro"
        case 8:
            ranking = "Ouro"
        case 9:
            ranking = "Diamante"
        case 10:
            ranking = "Lendário"
        case _:
            ranking = "Imortal"

    return ranking


numVictory = int(input("Número de Vitórias: "))
numDefeat = int(input("Número de Derrotas: "))
balance = balanceVictory(numVictory, numDefeat)
ranking = rankingHero(balance)

print(f'O Herói tem de saldo de {balance} está no nível de {ranking}')

