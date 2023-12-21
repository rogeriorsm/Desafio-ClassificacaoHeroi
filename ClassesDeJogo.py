class Hero:
    def __init__(self, name, age, type, power):
        self.name = name
        self.age = age
        self.type = type
        self.power = power


    def Attack(self, type, power):
        self.power = power
        self.type = type
        print(f'O {self.type} atacou usando {self.power}')

def typeHero(a):
    match a:
        case 1:
            tHero = "mago"
        case 2:
            tHero = "guerreiro"
        case 3:
            tHero = "monge"
        case 4:
            tHero = "ninja"
        case _:
            tHero = "Esse Herói não existe."
    return tHero


def setPower(type):
    if type == "mago":
        power = "usou mágia"
    elif type == "guerreiro":
        power = "usou espada"
    elif type == "monge":
        power = "usou artes marciais"
    elif type == "ninja":
        power = "usou shuriken"
    else:
        power = "Esse herói não existe!!!"

    return power


print("Vamos iniciar o jogo...")
print("")
name = str(input("Digite o nome do Herói: "))
age = int(input("Digite a idade do herói: "))
print("Escolha o tipo do seu herói:")
escolha = int(input("1 = Mago; 2 = Guerreiro; 3 = Monge; 4 = Ninja;   " ))

tHero = typeHero(escolha)
powerHero = setPower(tHero)
person = Hero(name, age, tHero, powerHero)
person.Attack(tHero, powerHero)



