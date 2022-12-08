import requests
import json

def F():
    v = name.get()
    response = requests.get('https://api.github.com/users/NixOS')

    f_ = json.loads(response.text)

    y = dict.fromkeys(['company'], f_['company'])
    y2 = dict.fromkeys(['created_at'], f_['created_at'])
    y3 = dict.fromkeys(['email'], f_['email'])
    y4 = dict.fromkeys(['id'], f_['id'])
    y5 = dict.fromkeys(['name'], f_['name'])
    y6 = dict.fromkeys(['url'], f_['url'])
    j = (y,y2,y3,y4,y5,y6)




    

    if v == 'NixOS':
        with open('C:\\Users\\Nikito$\\Desktop\\vivod.json', 'w') as file:
            json.dump(j,file)
        
        
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

