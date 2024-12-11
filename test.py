import tkinter as tk

def create_warning_window():
    # Créer la fenêtre principale
    window = tk.Tk()
    
    # Définir les dimensions et le titre de la fenêtre
    window.geometry("400x200")
    window.title("Attention")

    # Changer la couleur de fond en rouge
    window.configure(bg="red")

    # Ajouter un texte au centre de la fenêtre
    label = tk.Label(window, text="Nous avons le contrôle de votre PC", font=("Arial", 16, "bold"), fg="white", bg="red")
    label.pack(expand=True)

    # Empêcher la redimension de la fenêtre
    window.resizable(False, False)

    # Lancer la boucle principale
    window.mainloop()

# Appeler la fonction pour créer la fenêtre
create_warning_window()
