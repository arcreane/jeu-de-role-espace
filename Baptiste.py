#---------------------Imports-----------------------

import tkinter as tk
import pygame
import time
import os.path
import os
from re import search

# ---------------------Music-----------------------
pygame.init()
pygame.mixer.music.load("C:/Users/rosta/AppData/Local/Programs/Python/Python39/Mainsong.wav")
pygame.mixer.music.play(-1)

# --------------------Variables----------------------
sb = pygame.mixer.Sound("C:/Users/rosta/AppData/Local/Programs/Python/Python39/bouton.wav")
chap = 0
counteraa = 0
counterda = 0
countersa = 0
counterra = 0
counteram = 0
counterdm = 0
countersm = 0
counterrmapp = 0
music_counter = 0
a = "On"
b = 0

#------------------Create folders-------------------

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

createFolder('./Armes_et_Monstres/')
createFolder('./Chapitre/')
createFolder('./Story_tools/')
createFolder('./Specialites/')
createFolder('./Texte/')

#-----------------Programme default------------------



save = 'C:/Users/rosta/AppData/Local/Programs/Python/Python39/Armes_et_Monstres'
savec = 'C:/Users/rosta/AppData/Local/Programs/Python/Python39/Chapitre'
savee = 'C:/Users/rosta/AppData/Local/Programs/Python/Python39/Texte'
savet = 'C:/Users/rosta/AppData/Local/Programs/Python/Python39/Story_tools'
saves = 'C:/Users/rosta/AppData/Local/Programs/Python/Python39/Specialites'


listdefault1 = {'attaque': 3, 'defence': 3, 'distance' : 1, 'cout' : 3}
arme1 = os.path.join(save, "Epee.py")
armedefault1 = open(arme1, "w+")
armedefault1.write("%s = %s\n" %("listdefault1", listdefault1))
armedefault1.close()

listdefault2 = { 'attaque' : 5, 'defence' : 2, 'distance': 1, 'cout' : 4}
arme2 = os.path.join(save, "Hache.py")
armedefault2  = open(arme2, "w+")
armedefault2.write("%s = %s\n" %("listdefault2" , listdefault2))
armedefault2.close()

listdefault3 = { 'attaque' : 2, 'defence' : 1, 'distance': 1, 'cout' : 2}
arme3 = os.path.join(save, "Couteau.py")
armedefault3  = open(arme3 , "w+")
armedefault3.write("%s = %s\n" %("listdefault3" , listdefault3))
armedefault3.close()

listdefault4 = { 'attaque' : 6, 'defence' : 3, 'distance': 4, 'cout' : 8}
arme4 = os.path.join(save, "Fusil.py")
armedefault4  = open(arme4 , "w+")
armedefault4.write("%s = %s\n" %("listdefault4" , listdefault4))
armedefault4.close()

listdefault5= { 'attaque' : 4, 'defence' :2 , 'distance': 2, 'cout' : 4}
arme5 = os.path.join(save, "Arc.py")
armedefault5  = open(arme5 , "w+")
armedefault5.write("%s = %s\n" %("listdefault5" , listdefault5))
armedefault5.close()

listdefault6 = { 'attaque' : 1, 'defence': 4, 'distance' : 1 ,'récompense' : 1}
monstre1 = os.path.join(save,'Gobelin.py')
monstredefault1 = open(monstre1 , "w+")
monstredefault1.write("%s = %s\n" %("listdefault6" , listdefault6))
monstredefault1.close()

listdefault7 = { 'attaque' : 2, 'defence': 4, 'distance' : 1 ,'récompense' : 2}
monstre2 = os.path.join(save,'Loup.py')
monstredefault2 = open(monstre2 , "w+")
monstredefault2.write("%s = %s\n" %("listdefault7" , listdefault7))
monstredefault2.close()

listdefault8 = { 'attaque' : 3, 'defence': 4 , 'distance' : 1 ,'récompense' : 2}
monstre3 = os.path.join(save,'Orque.py')
monstredefault3 = open(monstre3 , "w+")
monstredefault3.write("%s = %s\n" %("listdefault8" , listdefault8))
monstredefault3.close()

listdefault9 = { 'attaque' : 3, 'defence': 6, 'distance' : 1 ,'récompense' : 3}
monstre3 = os.path.join(save,'Ogre.py')
monstredefault4 = open(monstre3 , "w+")
monstredefault4.write("%s = %s\n" %("listdefault9" , listdefault9))
monstredefault4.close()

listdefault10 = { 'attaque' : 4, 'defence': 5, 'distance' : 2 ,'récompense' : 3}
monstre5 = os.path.join(save,'Vampire.py')
monstredefault5 = open(monstre5 , "w+")
monstredefault5.write("%s = %s\n" %("listdefault10" , listdefault10))
monstredefault5.close()

#------------------Son bouton-------------------

def Sbouton():
  pygame.mixer.music.pause()
  pygame.mixer.Sound.play(sb)
  time.sleep(0.1)
  pygame.mixer.music.unpause()

#------------------Stop music-------------------

def musicstop():
  global music_counter
  if music_counter % 2 ==0:
    pygame.mixer.music.stop()
    a = "Off"
    bouton_5.configure(text=f"Sound: {a}")
  else:
    pygame.mixer.music.play()
    a = "On"
    bouton_5.configure(text=f"Sound: {a}")
  music_counter +=1

#----------------Page écriture------------------

def zone_de_texte():

    #-------------Nouvelle fenetre--------------
    texte = tk.Tk()
    texte.title("Zone de texte de l'histoire")
    texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
    texte.minsize(1080, 720)
    texte.config(background='#78597f')

    #place titre devant entrée de texte
    label_0 = tk.Label(texte, text="Titre:", font= {'Courrier',15}, bg='#78597f', fg='white')
    label_0.place(x=575 , y = 10)
    #entrée de texte pour Titre de programme
    text_0=tk.Text(texte, font=("Courrier", 15), bg='#78597f', fg='white', width=25, height=1)
    text_0.pack(pady=5)
    #entrée de texte pour zone de texte
    text_1 = tk.Text(texte, font=("Courrier", 15), bg='#78597f', fg='white', width=100, height=20)
    text_1.pack(pady=20)

    #----------Création programme écriture----------

    def files():
            text = os.path.join(savee,f"{text_0.get('1.0', 'end-1c')}.txt")
            textechange = open(text, "w+")
            textechange.write(text_1.get('1.0', 'end-1c'))
            textechange.close()

    #boutton enregistrement
    button_0=tk.Button(texte, text="Enregistrer", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [files(),Sbouton()])
    button_0.pack(pady=10)
    #bouton retour menu
    button_1 = tk.Button(texte, text="Revenir au Menu Principal", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [texte.destroy(),Sbouton()])
    button_1.pack(pady=10)
    
    texte.mainloop()

#----------------Page iventaire-----------------

def inventaire():

    #-------------Nouvelle fenetre--------------
    texte = tk.Tk()
    texte.title("Inventaire")
    texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
    texte.minsize(1080, 720)
    texte.config(background='#78597f')

    #texte indiquant armes dispo
    label_0 = tk.Label(texte, text= "\n\nLes armes disponibles sont : \nune arbalette, un arc, une épée, un couteau.", font=("Courrier", 20), bg='#78597f', fg='white')
    label_0.pack()
    

    #----------------Page arme------------------
    def armesaj():

        #-------------Nouvelle fenetre--------------
        texte = tk.Tk()
        texte.title("Arme")
        texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
        texte.minsize(1080, 720)
        texte.config(background='#78597f')

        #texte arme et atouts
        label_0 = tk.Label(texte, text= "Nom de l'arme et ses atouts", font=("Courrier", 20), bg='#78597f', fg='white')
        label_0.pack()
        #Nom de l'arme
        text_0 = tk.Text(texte, font=("Courrier", 15), bg='#78597f', fg='white', height = 1)
        text_0.pack()

        #----------Création programme armes----------
        def files():
            global counteraa
            global countersa
            global counterda
            global counterra
            listchange = {'attaque': counteraa, 'defence': counterda, 'distance' : countersa, 'récompense' : counterra}
            arme = os.path.join(save,f"{text_0.get('1.0', 'end-1c')}.py")
            armechange = open(arme, "w+")
            armechange.write("%s = %s\n" %("listchange", listchange))
            armechange.close()
            
        def restart():
            global counteraa
            global countersa
            global counterda
            global counterra
            counteraa = 0
            counterda = 0
            countersa = 0
            counterra = 0

        def clicka():
            global counteraa
            
            counteraa = counteraa + 1
            at.configure(text=f'Attack: {counteraa}')
        def clickd():
            global counterda
            counterda = counterda + 1
            de.configure(text=f'Defence: {counterda}')
        def clicks():
            global countersa
            countersa = countersa + 1
            sp.configure(text=f'Distance: {countersa}')
        def clickr():
            global counterra
            counterra = counterra + 1
            rn.configure(text=f'Cout: {counterra}')
                
        at = tk.Button(texte, text= f'Attack: {counteraa}', command = lambda:[clicka()])
        at.pack(pady= 15)
        de = tk.Button(texte, text=f'Defence: {counterda}', command = lambda:[clickd()])
        de.pack(pady=15)
        sp = tk.Button(texte, text=f'Distance: {countersa}', command = lambda:[clicks()])
        sp.pack(pady= 15)
        rn = tk.Button(texte, text=f'Cout: {counterra}', command = lambda:[clickr()])
        rn.pack(pady= 15)
        

        boutton_3=tk.Button(texte, text="Enregistrer", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),files()])
        boutton_3.pack(pady=25)
        boutton_4 = tk.Button(texte, text="Back", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),texte.destroy(), restart()])
        boutton_4.pack(pady=25)

        texte.mainloop()
      
    #boutton pour ajouter arme
    button_0 = tk.Button(texte, text="Ajouter une arme", font=("Courrier", 25), bg='white', fg='#78597f', command=lambda: [Sbouton(),armesaj()])
    button_0.pack(pady=50)
    
    #texte indiquant montres dispo
    label_1 = tk.Label(texte, text= "Les monstres disponibles sont : \n des dragons, des ogres, des gobelins, des loups, des vampires et des orques.", font=("Courrier", 20), bg='#78597f', fg='white')
    label_1.pack()

    #---------------Page monstre-----------------
    def monstreaj():

        #-------------Nouvelle fenetre--------------
        texte = tk.Tk()
        texte.title("Monstre")
        texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
        texte.minsize(1080, 720)
        texte.config(background='#78597f')

        #texte monstre et capacité
        label_0 = tk.Label(texte, text= "Nom du monstre et ses capacités", font=("Courrier", 20), bg='#78597f', fg='white')
        label_0.pack()
        #entée texte pour nom du monstre
        text_0 = tk.Text(texte, font=("Courrier", 15), bg='#78597f', fg='white', height = 1)
        text_0.pack() 

        #----------Création programme armes----------  
        def files():
            global counteram
            global countersm
            global counterdm
            global counterrm
            listchange = {'attaque': counteram, 'defence': counterdm, 'distance' : countersm, 'récompense' : counterrm}
            monstre = os.path.join(save,f"{text_0.get('1.0', 'end-1c')}.py")
            monstrechange = open(monstre, "w+")
            monstrechange.write("%s = %s\n" %("listchange", listchange))
            monstrechange.close()

        #---------Fonction restart valeurs----------
        def restart():
            global counteram
            global countersm
            global counterdm
            global counterrm
            counteram = 0
            counterdm = 0
            countersm = 0
            counterrm = 0

        # Bouton pour capacités ---> Ca va changer pour le drague
        def clicka():
            global counteram
            counteram = counteram + 1
            at.configure(text=f'Attack: {counteram}')
        def clickd():
            global counterdm
            counterdm = counterdm + 1
            de.configure(text=f'Defence: {counterdm}')
        def clicks():
            global countersm
            countersm = countersm + 1
            sp.configure(text=f'Speed: {countersm}')
        def clickr():
            global counterrm
            counterrm = counterrm + 1
            rn.configure(text=f'money won: {counterrm}')
                
        at = tk.Button(texte, text= f'Attack: {counteram}', command = lambda:[clicka()])
        at.pack(pady= 15)
        de = tk.Button(texte, text=f'Defence: {counterdm}', command = lambda:[clickd()])
        de.pack(pady= 15)
        sp = tk.Button(texte, text=f'Speed: {countersm}', command = lambda:[clicks()])
        sp.pack(pady= 15)
        rn = tk.Button(texte, text=f'Recompense: {counterrm}', command = lambda:[clickr()])
        rn.pack(pady= 15)
        
        #bouton enregistrer
        button_0=tk.Button(texte, text="Enregistrer", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),files()])
        button_0.pack(pady=25) 
        #bouton back       
        button_1 = tk.Button(texte, text="Back", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),texte.destroy(), restart()])
        button_1.pack(pady=25)

        texte.mainloop()

    #bouton ajouter monstre
    button_0 = tk.Button(texte, text="Ajouter un monstre", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),monstreaj()])
    button_0.pack(pady=50)

    #bouton menu principal
    button_1 = tk.Button(texte, text="Revenir au Menu Principal", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),texte.destroy()])
    button_1.pack(pady=25)

    texte.mainloop()

#------------Page structure histoire--------------

def struct():
    #-------------Nouvelle fenetre--------------
    texte = tk.Tk()
    texte.title("Structure Histoire")
    texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
    texte.minsize(1080, 720)
    texte.config(background='#78597f')
    texte_2 = tk.Label(texte, text= "Choisissez le nombre de chapitres que vous voulez", font=("Courrier", 20), bg='#78597f', fg='white')
    texte_2.pack(pady=50)

    #---------Defintion de chapitre----------

    def chapitre():
      
      
      global chap
    #-------------Nouvelle fenetre-----------
      texte = tk.Tk()
      texte.title(f'Chapitre {chap}')
      texte.geometry("{0}x{1}+0+0".format(texte.winfo_screenwidth(), texte.winfo_screenheight()))
      texte.minsize(1080, 720)
      texte.config(background='#78597f')

      mainbox = tk.Listbox(texte, height=30)
      mainbox.pack()

    #---------------Save chapter-------------
      def files():
            chapp = os.path.join(savec,f"Chapitre {chap}.py")
            chapchange = open(chapp, "w+")
            chapchange.write("%s = %s\n" %("mainbox", mainbox)) 
            chapchange.close()

    #-------Boite avec tous les objets--------
      flist = os.listdir(save)
      flist1 = os.listdir(savee)
      flist2 = os.listdir(savet)
      flist3 = os.listdir(saves)
      

    #boite 1 avec Label
      texte_0 = tk.Label(texte, text="Liste Armes et monstres")
      texte_0.place(x = 45, y= 10)
      lbox_1 = tk.Listbox(texte, height=9)
      lbox_1.place(x=50,y=35)
      strpy = ".py"
      for item in flist:
          if item.__contains__(strpy):
              lbox_1.insert(tk.END, item)
      
      
    #boite 2 avec Label
      texte_1 = tk.Label(texte,  text="Liste de texte")
      texte_1.place(x = 72, y= 195)
      lbox_2 = tk.Listbox(texte, height=9)
      lbox_2.place(x=50,y=220)
      strtxt = ".txt"
      for item in flist1:
          if item.__contains__(strtxt):
              lbox_2.insert(tk.END, item)
      
      
    #boite 3 avec label
      texte_2 = tk.Label(texte, text="Liste des outils")
      texte_2.place(x = 70, y= 380)
      lbox_3 = tk.Listbox(texte, height=9)
      lbox_3.place(x=50,y=405)
      strtxt = ".py"
      for item in flist2:
          if item.__contains__(strtxt):
              lbox_3.insert(tk.END, item)
    
      
    #boite 4 avec label
      texte_3 = tk.Label(texte, text="Specialites")
      texte_3.place(x = 78, y= 565)
      lbox_4 = tk.Listbox(texte, height=9)
      lbox_4.place(x=50,y=590)
      strtxt = ".py"
      for item in flist3:
          if item.__contains__(strtxt):
              lbox_4.insert(tk.END, item)

      

      def select1():
          insert1 = lbox_1.get("anchor")
          mainbox.insert("anchor",insert1)
          

      def select2():
          insert2 = lbox_2.get("anchor")
          mainbox.insert("anchor",insert2)
          

      def select3():
          insert3 = lbox_3.get("anchor")
          mainbox.insert("anchor",insert3)
          

      def select4():
          insert4 = lbox_4.get("anchor")
          mainbox.insert("anchor",insert4)
          
       
      #bouton back       
      button_1 = tk.Button(texte, text="Back", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),texte.destroy()])
      button_1.place(x=500,y=700)
      #bouton enregistrer
      button_0=tk.Button(texte, text="Enregistrer", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda: [Sbouton(),files()])
      button_0.place(x=950,y=700)

      button_2=tk.Button(texte, text="Selectionner", font=("Courrier", 15), bg='white', fg='#78597f', command= lambda: [Sbouton(),select1()])
      button_2.place(x=200,y=100)

      button_3=tk.Button(texte, text="Selectionner", font=("Courrier", 15), bg='white', fg='#78597f', command= lambda: [Sbouton(),select2()])
      button_3.place(x=200,y=282)

      button_4=tk.Button(texte, text="Selectionner", font=("Courrier", 15), bg='white', fg='#78597f', command= lambda: [Sbouton(),select3()])
      button_4.place(x=200,y=464)

      button_5=tk.Button(texte, text="Selectionner", font=("Courrier", 15), bg='white', fg='#78597f', command= lambda: [Sbouton(),select4()])
      button_5.place(x=200,y=646)
          

    #---------Fonction restart chap----------
    def restart():
        global chap
        chap = 0
    #---------Fonction new chap----------    
    def newbox():
        global chap
        #---------Fonction del chap---------- 
        def prevbox():
            global chap
            box = tk.Button(texte, text='\t ', font=("Courrier", 15), bg='#78597f', fg='#78597f', command= lambda:[newbox()])      
            if 0 < chap < 9:
                box.place(x=175*chap, y=300)
            elif 8 < chap < 17:
                box.place(x=175*(chap-8), y=350)
            elif 16 < chap < 25:
                box.place(x=175*(chap-16), y=400)
            elif 24 < chap < 33:
                box.place(x=175*(chap-24), y=450)
            elif 32 < chap < 41:
               box.place(x=175*(chap-32), y=500)
            elif 40 < chap < 49:
               box.place(x=175*(chap-40), y=550)
            elif 48 < chap < 57:
               box.place(x=175*(chap-48), y=600)
            chap -= 1
            
        chap += 1
        box = tk.Button(texte, text=f'Chapitre {chap}', font=("Courrier", 15), bg='white', fg='#78597f', width= 9, command= lambda:[Sbouton(),chapitre()])
        if 0 < chap < 9:
           box.place(x=175*chap, y=300)
        elif 8 < chap < 17:
           box.place(x=175*(chap-8), y=350)
        elif 16 < chap < 25:
           box.place(x=175*(chap-16), y=400)
        elif 24 < chap < 33:
           box.place(x=175*(chap-24), y=450)
        elif 32 < chap < 41:
           box.place(x=175*(chap-32), y=500)
        elif 40 < chap < 49:
           box.place(x=175*(chap-40), y=550)
        elif 48 < chap < 57:
           box.place(x=175*(chap-48), y=600)
  

        boutton_5 = tk.Button(texte, text="Delete", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda:[prevbox()])
        boutton_5.place( x = 200, y = 700)
        
            
  
    boutton_1 = tk.Button(texte, text="Add box", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda:[newbox()])
    boutton_1.pack(pady=25)
    boutton_3 = tk.Button(texte, text="Save", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda:[Sbouton(),texte.quit()])
    boutton_3.place( x = 550, y = 700)
    boutton_4 = tk.Button(texte, text="Revenir au Menu Principal", font=("Courrier", 25), bg='white', fg='#78597f', command= lambda:[Sbouton(),texte.destroy(), restart()])
    boutton_4.place( x = 900, y = 700)

#---------------Main page éditer------------------

window = tk.Tk()
window.title("Menu principal")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.minsize(1080, 720)
window.config(background='#78597f')
frame = tk.Frame(window, bg='#78597f')

texte_1 = tk.Label(frame, text="\nÉditez votre histoire. \nTout d'abord, vous allez devoir gérer \nl'inventaire des armes et des monstres, ainsi que les zones de textes.", font=("Courrier", 19), bg='#78597f', fg='white')
texte_1.pack()
bouton_1 = tk.Button(frame, text="Gérer l'inventaire des armes et des monstres", font=("Courrier", 25), bg='white', fg='#78597f', command=lambda:[Sbouton(),inventaire()])
bouton_1.pack(pady=30)
bouton_2 = tk.Button(frame, text="Gérer les zones de texte", font=("Courrier", 25), bg='white', fg='#78597f', command=lambda:[Sbouton(),zone_de_texte()])
bouton_2.pack(pady=30)
bouton_3 = tk.Button(frame, text="Gérer les étapes de l'histoire", font=("Courrier", 25), bg='white', fg='#78597f', command=lambda:[Sbouton(),struct()])
bouton_3.pack(pady=30)
bouton_4=tk.Button(frame, text="Fermer", font=("Courrier", 25), bg='white', fg='#78597f', command=lambda:[Sbouton(),pygame.mixer.music.stop(),window.destroy()])
bouton_4.pack(pady= 40)
  
bouton_5=tk.Button(window, text=f"Sound: {a}", font=("Courrier", 10), bg='white', fg='#78597f', command=lambda:[musicstop()])
bouton_5.place(x=10,y=10)


#--------------Création de l'image---------------

width = 400
height = 200
image = tk.PhotoImage(file="C:/Users/rosta/AppData/Local/Programs/Python/Sparte.png").zoom(14).subsample(30)
canvas = tk.Canvas(window, width=width, height=height, bg='#78597f', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack()
frame.pack()

window.mainloop()
