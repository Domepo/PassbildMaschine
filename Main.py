#! Python 3.4
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import passbild

def datei():
    zieldatei = FinalFile()
    return zieldatei
def dateiinput():
    eingabe = OpenFile()
    return eingabe

class din:

    def neunmalzwoelf():#9x12
        xgesamt = 1200
        ygesamt = 900
        passbild.schleife(6,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,380,2000)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,50,240,datei())#"9x12")

    def neunmaldreizehn():#9x13
        xgesamt = 1300
        ygesamt = 900
        passbild.schleife(6,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,420,2000)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,50,240,datei())#"9x12")

    def zehnmaldreizehn():#10x13
        xgesamt = 1300
        ygesamt = 1000
        passbild.schleife(6,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,430,480)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,50,35,datei())#"9x12"))

    def zehnmalfuenfzehn():#10x15
        xgesamt = 1500
        ygesamt = 1000
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,370,470) #370 470
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,20,40,datei())#"10x15")
#Bewerbungs foto
    # def zehnmalfuenfzehn():#10x15
    #     xgesamt = 1500
    #     ygesamt = 1000
    #     passbild.schleife(8,dateiinput())
    #     passbild.bild(xgesamt,ygesamt,255,255,255)
    #     passbild.bildperso(450,600,500,7000) #370 470
    #     passbild.bildfinal(xgesamt,ygesamt,255,255,255,20,40,datei())#"10x15")

    def elfmalfuenfzehn():#11x15
        xgesamt = 1500
        ygesamt = 1100
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,370,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,20,40,datei())#"11x15")

    def elfmalsiebszehn():#11x17
        xgesamt = 1700
        ygesamt = 1100
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,430,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,30,40,datei())#"11x15")

    def dreizehnmalsiebzehn():#13x17
        xgesamt = 1700
        ygesamt = 1300
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,420,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,46,150,datei())#"11x15")

    def dreizehnmalachtzehn():#13x18
        xgesamt = 1800
        ygesamt = 1300
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,420,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,90,150,datei())#"11x15")

    def dreizehnmalneunzehn():#13x19
        xgesamt = 1900
        ygesamt = 1300
        passbild.schleife(8,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,420,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,150,150,datei())#"11x15")


    def fuenfzehnmalzwanzig():#15x20
        xgesamt = 2000
        ygesamt = 1500
        passbild.schleife(10,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,380,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,60,250,datei())#"11x15")

    def achtzehnmalvierundzwanzig():#18x24
        xgesamt = 2400
        ygesamt = 1800
        passbild.schleife(12,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,380,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,60,400,datei())#"11x15")

    def zwanzigmalsiebunzwanzig():#20x27
        xgesamt = 2700
        ygesamt = 2000
        passbild.schleife(14,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,380,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,40,500,datei())#"11x15")

    def zwanzigmaldreizig():#20x30
        xgesamt = 3000
        ygesamt = 2000
        passbild.schleife(16,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,370,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,35,500,datei())#"11x15")

    def vierunzwanzigmaldreizig():#24x30
        xgesamt = 3000
        ygesamt = 2400
        passbild.schleife(16,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,370,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,25,700,datei())#"11x15")

    def dreizigmalachtundreizig():#30x38
        xgesamt = 3800
        ygesamt = 3000
        passbild.schleife(20,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,378,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,25,1000,datei())#"11x15")

    def dreizigmalvierzig(self):#30x40
        xgesamt = 4000
        ygesamt = 3000
        passbild.schleife(20,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,378,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,25,1000,datei())#"11x15")

    def dreizigmalfuenfunvierzig():#30x45
        xgesamt = 4500
        ygesamt = 3000
        passbild.schleife(24,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,373,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,25,1000,datei())#"11x15")

    def fuenfzigmalsiebzig():#50x70
        xgesamt = 7000
        ygesamt = 5000
        passbild.schleife(36,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,388,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,25,1900,datei())#"11x15")

    def fuenfzigmalfuenfunsiebzig():#50x75
        xgesamt = 7500
        ygesamt = 5000
        passbild.schleife(38,dateiinput())
        passbild.bild(xgesamt,ygesamt,255,255,255)
        passbild.bildperso(350,450,388,570)
        passbild.bildfinal(xgesamt,ygesamt,255,255,255,80,1900,datei())#"11x15")
#if __name__ == "__main__":
#    din.fuenfzigmalsiebzig()

OPTIONS = [
"9x12",
"9x13",
"10x13",
"10x15",
"11x15",
"11x17",
"13x17",
"13x18",
"13x19",
"15x20",
"18x24",
"20x27",
"20x30",
"24x30",
"30x38",
"30x40",
"30x45",
"50x70",
"50x75",
]
root = Tk()

def OpenFile():
    anfang = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",filetypes =(("PNG", "*.png"),("JPEG", "*.jpg"),("Text File", "*.txt")),title = "Wähle datei aus")
    return anfang
def FinalFile():
    ziel = asksaveasfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",filetypes =(("PNG", "*.png"),("JPEG", "*.jpg"),("Text File", "*.txt")),title = "Wähle datei aus")
    return ziel

def auswahl():
    print ("value is:" + variable.get())

    if variable.get() == "9x12":
        din.neunmalzwoelf()
    if variable.get() == "9x13":
        din.neunmaldreizehn()
    if variable.get() == "10x13":
        din.zehnmaldreizehn()
    if variable.get() == "10x15":
        din.zehnmalfuenfzehn()
    if variable.get() == "11x15":
        din.elfmalfuenfzehn()
    if variable.get() == "11x17":
        din.elfmalsiebszehn()
    if variable.get() == "13x17":
        din.dreizehnmalsiebzehn()
    if variable.get() == "13x18":
        din.dreizehnmalachtzehn()
    if variable.get() == "13x19":
        din.dreizehnmalneunzehn()
    if variable.get() == "15x20":
        din.fuenfzehnmalzwanzig()
    if variable.get() == "18x24":
        din.achtzehnmalvierundzwanzig()
    if variable.get() == "20x27":
        din.zwanzigmalsiebunzwanzig()
    if variable.get() == "20x30":
        din.zwanzigmaldreizig()
    if variable.get() == "24x30":
        din.vierunzwanzigmaldreizig()
    if variable.get() == "30x38":
        din.dreizigmalachtundreizig()
    if variable.get() == "30x40":
        din.dreizigmalvierzig()
    if variable.get() == "30x45":
        din.dreizigmalfuenfunvierzig()
    if variable.get() == "50x70":
        din.fuenfzigmalsiebzig()
    if variable.get() == "50x75":
        din.fuenfzigmalfuenfunsiebzig()

root.geometry('200x200') # Size 200, 200

Title = root.title( "File Opener")
label = ttk.Label(root, text ="PassbildMaschine",foreground="black",font=("Helvetica", 16))
label.pack()

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value
w = OptionMenu(root, variable, *OPTIONS)
w.pack()


button = Button(root, text="OK", command=auswahl,height = 5, width = 100,bg = "green")
button.pack()

exit = Button(root, text="Exit", command=root.destroy,height = 5, width = 100,bg = "red")
exit.pack()

root.mainloop()
