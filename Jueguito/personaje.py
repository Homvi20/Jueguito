class Personaje():

    def __init__(self ,N="",R="",A="", V="",D="",B="" ):
        self.__nom = N
        self.__raz = R
        self.__arm = A
        self.__vid = V
        self.__dañ = D
        self.__bon = B



    def __str__(self):
        return "Nombre: - {} - Raza: - {} - Arma: - {} - Vida: - {} - Daño: - {} - Bonificacion: - {}".format(self.__nom,self.__raz,self.__arm,self.__vid,self.__dañ,self.__bon)



    def Getnombre(self):
        return self.__nom

    def Getraza(self):
        return self.__raz

    def Getarma(self):
        return self.__arm
    
    def Getvida(self):
        return self.__vid

    def Getdaño(self):
        return self.__dañ
    
    def Getbonificacion(self):
        return self.__bon

    

    def Setnombre(self,N):
        self.__nom = N

    def Setraza(self,R):
        self.__raz = R

    def Setarma(self,A):
        self.__arm = A

    def Set(self,V):
        self.__vid = V

    def Setdaño(self,D):
        self.__dañ = D

    def Setbonificacion(self,B):
        self.__bon = B


    
    def Historia(self):
        if self.__raz == "Enano":
            print("Los Enanos sitúan el comienzo de su historia en el despertar de los primeros de su raza,\ngobernados directamente por un panteón de dioses que caminaban entre ellos.\nDe estos, los más importantes son Grungni,Grimnir y Valaya,\ny los Enanos creen que descienden directamente de estos antepasados primigenios.")

        if self.__raz == "Elfo":
            print("Los Elfos se les considera seres con poderes mágicos y belleza sobrenatural que pueden ayudar o molestar a los humanos.")

        if self.__raz == "Humano":
            print("Los Humanos se les considera seres con inteligencia y con nula enpatia por lo que les rodia")

    def victoria():
        pass

    def derrota():
        pass