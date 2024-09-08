import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Funkcja do tworzenia plików z określoną zawartością
def create_file(file_path, content=""):
    with open(file_path, 'w') as file:
        file.write(content)

# Funkcja do tworzenia struktury folderów i plików
def create_fivem_project():
    # Pobierz dane od użytkownika
    folder_name = entry_folder_name.get()
    folder_location = entry_folder_location.get()

    if not folder_name or not folder_location:
        messagebox.showerror("Error", "Please provide a folder name and location.")
        return

    # Tworzenie głównego folderu projektu
    project_path = os.path.join(folder_location, folder_name)
    os.makedirs(project_path, exist_ok=True)

    # Tworzenie folderów 'client' i 'server'
    client_folder = os.path.join(project_path, 'client')
    server_folder = os.path.join(project_path, 'server')
    os.makedirs(client_folder, exist_ok=True)
    os.makedirs(server_folder, exist_ok=True)

    # Tworzenie plików 'main.lua' w folderach 'client' i 'server'
    create_file(os.path.join(client_folder, 'main.lua'), 'ESX = exports["es_extended"]:getSharedObject()')
    create_file(os.path.join(server_folder, 'main.lua'), 'ESX = exports["es_extended"]:getSharedObject()')

    # Tworzenie pliku 'fxmanifest.lua' w głównym folderze
    fxmanifest_content = """fx_version 'cerulean'
game 'gta5'
lua54 'yes'
author 'Biqydu'

shared_scripts {'config.lua'}
      
server_scripts {
  'server/*.lua',
  'config.lua',
}
      
client_scripts {
  'client/*.lua',
  'config.lua',
}
"""
    create_file(os.path.join(project_path, 'fxmanifest.lua'), fxmanifest_content)

    # Tworzenie pliku 'config.lua' w głównym folderze
    config_content = """Config = {}"""
    create_file(os.path.join(project_path, 'config.lua'), config_content)

    messagebox.showinfo("Success", f"FiveM project was created in the location: {project_path}")

def choose_location():
    folder_selected = filedialog.askdirectory()  # Otwiera okno dialogowe wyboru folderu
    entry_folder_location.delete(0, tk.END)
    entry_folder_location.insert(0, folder_selected)

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title("Create project Fivem")

# Etykiety i pola tekstowe
tk.Label(root, text="Folder name:").grid(row=0, column=0, padx=10, pady=10)
entry_folder_name = tk.Entry(root, width=40)
entry_folder_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Folder location:").grid(row=1, column=0, padx=10, pady=10)
entry_folder_location = tk.Entry(root, width=40)
entry_folder_location.grid(row=1, column=1, padx=10, pady=10)

# Przycisk wyboru lokalizacji
button_choose_location = tk.Button(root, text="Select a location", command=choose_location)
button_choose_location.grid(row=1, column=2, padx=10, pady=10)

# Przycisk do tworzenia projektu
button_create = tk.Button(root, text="Create a project", command=create_fivem_project)
button_create.grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
