from tkinter import *

def main_menu():
    #Fenster configurationen
    window = Tk()
    window.title("fodder manger mobile")
    window.geometry("300x520")
    window.maxsize(300, 520)

    #Buttons für das Hauptmenü
    storage_button= Button(window, text="Lager", height= 10, width= 20)
    storage_button.grid(row=0, column=0)

    animals_button= Button(window, text="Tiere", height= 10, width= 20)
    animals_button.grid(row=0, column=1)

    dashboard_button= Button(window, text="Dashboard", height= 10, width= 20)
    dashboard_button.grid(row=1, column=0)

    settings_button= Button(window, text="Einstellungen", height= 10, width= 20)
    settings_button.grid(row=1, column=1)



    #zeigt im ende das Fenster an
    window.mainloop()
    
main_menu()