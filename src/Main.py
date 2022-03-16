#! Python 3.4
import passbild
import glob

class din():
    def __init__(self,file_input,file_destination):
        self.file_input = file_input
        self.file_destination = file_destination

    # ROSSMANN APROVED
    def zehnmalfuenfzehn(self):#10x15
        xgesamt = 1500
        ygesamt = 1000
        passbild.schleife(8,self.file_input)
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(334,430,350,450) #370 470
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,50,50,self.file_destination)#"10x15")

for i in glob.glob("*.jpg"):
    a = din(i,i)
    a.zehnmalfuenfzehn()
    print(i)
    
