import tkinter as tk

def create_window():
    # Crée une instance de la fenêtre
    window = tk.Tk()
    # Définit le titre de la fenêtre
    window.title("Message de bienvenue")
    # Définit la taille de la fenêtre
    window.geometry("800x600")

    # Crée un label (étiquette) pour afficher le message
    greeting = tk.Label(window, text="Bonjour à tous", font=("Arial", 24))
    # Positionne le label dans la fenêtre
    greeting.pack(expand=True)

    # Démarre la boucle principale de l'interface
    window.mainloop()

# Appelle la fonction pour créer et afficher la fenêtre
create_window()
