from personaje import Personaje

class Humano(Personaje):

    def __init__(self, N="", R="", A="", V="", D="", B="", F=""):
        super().__init__(N, R, A, V, D, B)
        self.__fam = F


    def __str__(self):
        return super().__str__() + "Familia: - {}".format(self.__fam)


    def Getfamilia(self):
        return self.__fam

    def Setfamilia(self, F):
        self.__fam = F

    
    def Historia(self):
        print("Los Humanos se les considera seres con inteligencia y con nula enpatia por lo que les rodia")

    def victoria():
        pass

    def derrota():
        pass

    def superbono():
        pass