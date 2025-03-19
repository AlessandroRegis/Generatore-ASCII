import tkinter as tk
from art import *

# Creazione della finestra principale
window = tk.Tk()
window.geometry("900x550")
window.title("Downloader Arte Ascii")
window.grid_columnconfigure(0, weight=1)

# Etichetta di benvenuto
welcome_label = tk.Label(window,
                         text="Benvenuto nel generatore ASCII. Aggiungi una parola o una frase:",
                         font=("Ubuntu", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)

# Campo di input
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)

# Funzione per generare arte ASCII
def download_ascii():
    if text_input.get():
        user_input = text_input.get()
        try:
            # Generazione dell'arte ASCII usando il modulo art
            ascii_art = text2art(user_input)  # Converte il testo in arte ASCII
        except Exception as e:
            ascii_art = f"Errore nella generazione dell'arte ASCII: {e}"
    else:
        ascii_art = "Aggiungi una parola o una frase nel campo input!"

    # Mostrare il risultato nell'interfaccia
    textwidget = tk.Text(height=20)  # Aggiunto un'altezza per gestire output più grandi
    textwidget.insert(tk.END, ascii_art)
    textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
    textwidget.configure(state='disabled')  # Per rendere il testo di sola lettura

    # Etichetta per i crediti
    credits_label = tk.Label(window, text="Un ringraziamento a PyMike, creatore del tutorial che ha permesso di creare questo programma.")
    credits_label.grid(row=4, column=0, sticky="S", padx=10)

# Bottone per avviare la generazione
download_button = tk.Button(window, text="Genera", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", padx=10, pady=10)

# Avvio del loop principale
if __name__ == "__main__":
    window.mainloop()
