from personaje import Personaje

class Elfo(Personaje):

    def __init__(self, N="", R="", A="", V="", D="", B="",Re="" ):
        super().__init__(N, R, A, V, D, B)
        self.__rei = Re


    def __str__(self):
        return super().__str__() + "Reino: - {}".format(self.__rei)


    def Getreino(self):
        return self.__rei

    def Setreino(self, Re):
        self.__rei = Re


    def Historia(self):
        print("Los Elfos se les considera seres con poderes mágicos y belleza sobrenatural que pueden ayudar o molestar a los humanos.")

    def victoria():
        pass

    def derrota():
        pass

    def quitavida():
        pass