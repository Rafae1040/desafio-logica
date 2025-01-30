class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        print(f"o {self.tipo} atacou usando {ataque}")


# Exemplos de uso
heroi1 = Heroi("Gandalf", 1000, "mago")
heroi1.atacar()  # Saída: o mago atacou usando magia

heroi2 = Heroi("Aragorn", 35, "guerreiro")
heroi2.atacar()  # Saída: o guerreiro atacou usando espada

heroi3 = Heroi("Bruce Lee", 32, "monge")
heroi3.atacar()  # Saída: o monge atacou usando artes marciais

heroi4 = Heroi("Hanzo", 28, "ninja")
heroi4.atacar()  # Saída: o ninja atacou usando shuriken