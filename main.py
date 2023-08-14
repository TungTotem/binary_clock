import tkinter as tk
import time

# Funktion zum Konvertieren einer Dezimalzahl in eine 4-Bit-Binärzahl
def dec_to_bin(dec):
    return "{0:04b}".format(dec)

# Funktion zum Aktualisieren der Anzeigezeit
def update_time():
    current_time = time.strftime("%H:%M:%S")
    hour, minute, second = current_time.split(":")
    hour = dec_to_bin(int(hour))
    minute = dec_to_bin(int(minute))
    second = dec_to_bin(int(second))
    time_str = hour + ":" + minute + ":" + second
    time_label.config(text=time_str)
    window.after(1000, update_time)


# Erstellung des Fensters
window = tk.Tk()
window.title("Binäre Uhr")


# Label zur Anzeige der Uhrzeit
time_label = tk.Label(window, font=("Arial", 40), pady=10)
time_label.pack()

# Aktualisierung der Uhrzeit
update_time()

# Ausführung des Fensters
window.mainloop()