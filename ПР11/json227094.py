import json
def F():
    v = name.get()
    f_json= """
    {
        'company': None
        'created_at': '2010-11-18T20:33:18Z'
        'email': None
        'id': 487568
        'name': 'Nix/Nixpkgs/NixOS'
        'url': 'https://api.github.com/users/NixOS'
    }"""

    if v == 'NixOS':
        with open('C:\\Users\\Nikito$\\Desktop\\vivod.json', 'w') as file:
            json.dump(f_json,file)
        
        
    else:
        print('Данное имя не задано')

    



import tkinter as tk 
window = tk.Tk()
window.geometry('400x300')
window.title("json") 
name = tk.Entry(window)
name.grid(padx=120, pady=15)
btn = tk.Button(window, text="click", command=F)
btn.grid(padx=90, pady=15)
window.mainloop()
F()

