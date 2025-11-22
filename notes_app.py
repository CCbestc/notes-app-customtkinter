import customtkinter as ctk
import json
from datetime import datetime

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Logiciel de Notes")
        self.root.geometry("600x500")

        # Configuration de l'apparence
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Liste pour stocker les notes
        self.notes = []

        # Interface
        self.create_widgets()

    def create_widgets(self):
        # Frame pour la liste des notes
        self.notes_frame = ctk.CTkFrame(self.root)
        self.notes_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Liste des notes
        self.notes_listbox = ctk.CTkTextbox(self.notes_frame, wrap="word")
        self.notes_listbox.pack(fill="both", expand=True)

        # Frame pour les boutons et la saisie
        self.input_frame = ctk.CTkFrame(self.root)
        self.input_frame.pack(pady=10, padx=10, fill="x")

        # Champ de saisie
        self.note_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Écrivez votre note ici...")
        self.note_entry.pack(side="left", fill="x", expand=True, padx=5)

        # Boutons
        self.add_button = ctk.CTkButton(self.input_frame, text="Ajouter", command=self.add_note)
        self.add_button.pack(side="left", padx=5)

        self.save_button = ctk.CTkButton(self.input_frame, text="Sauvegarder", command=self.save_notes)
        self.save_button.pack(side="left", padx=5)

        self.load_button = ctk.CTkButton(self.input_frame, text="Charger", command=self.load_notes)
        self.load_button.pack(side="left", padx=5)

    def add_note(self):
        note_text = self.note_entry.get()
        if note_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note = f"{timestamp} - {note_text}\n"
            self.notes.append(note)
            self.notes_listbox.insert("end", note)
            self.note_entry.delete(0, "end")

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)
        print("Notes sauvegardées !")

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
            self.notes_listbox.delete("1.0", "end")
            for note in self.notes:
                self.notes_listbox.insert("end", note)
        except FileNotFoundError:
            print("Aucune note sauvegardée trouvée.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = NoteApp(root)
    root.mainloop()