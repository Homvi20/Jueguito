from personaje import Personaje

class Enano(Personaje):
    
    def __init__(self, N="", R="", A="", V="", D="", B="", C=""):
        super().__init__(N, R, A, V, D, B)
        self.__cla = C


    def __str__(self):
        return super().__str__() + "Clan: - {}".format(self.__cla)
   

    def Getclan(self):
        return self.__cla
    
    def Set(self, C):
        self.__cla = C

   

    def Historia():
        print("Los Enanos sitúan el comienzo de su historia en el despertar de los primeros de su raza,\ngobernados directamente por un panteón de dioses que caminaban entre ellos.\nDe estos, los más importantes son Grungni,Grimnir y Valaya,\ny los Enanos creen que descienden directamente de estos antepasados primigenios.")

    def victoria():
        pass

    def derrota():
        pass

    def aumentarvida():
        pass