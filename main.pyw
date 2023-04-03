from tkinter import *

def mouse_button_down(event) :
    global grille
    global fourmis
    global iterations
    if 0 < event.x < 500 and 0 < event.y < 500 :
        if outil.get() == "1" :
            if int((event.y//(500/taille))*taille+event.x//(500/taille)) in fourmis :
                canvas.delete(fourmis[fourmis.index(int((event.y//(500/taille))*taille+event.x//(500/taille)))+2])
                del fourmis[fourmis.index(int((event.y//(500/taille))*taille+event.x//(500/taille))) : fourmis.index(int((event.y//(500/taille))*taille+event.x//(500/taille)))+3]
            else : fourmis += [int((event.y//(500/taille))*taille+event.x//(500/taille)),b_ldf.get("active"),""]
        else :
            canvas.delete(grille[int((event.y//(500/taille))*taille+event.x//(500/taille))][1])
            grille[int((event.y//(500/taille))*taille+event.x//(500/taille))],iterations = [l_couleurs.index([b_lcouleurs.get("active").split(" ")[0],b_lcouleurs.get("active").split(" ")[2]]),canvas.create_rectangle((event.x//(500/taille))*(500/taille)+2,(event.y//(500/taille))*(500/taille)+2,(event.x//(500/taille)+1)*(500/taille)+2,(event.y//(500/taille)+1)*(500/taille)+2,fill=l_couleurs[l_couleurs.index([b_lcouleurs.get("active").split(" ")[0],b_lcouleurs.get("active").split(" ")[2]])][0],outline=l_couleurs[l_couleurs.index([b_lcouleurs.get("active").split(" ")[0],b_lcouleurs.get("active").split(" ")[2]])][0])],0
    affich()

def key_down_return(event) :
    global taille
    try :
        taille = int(entree.get())
        crea_grille()
    except : a = 0

def key_down_return2(event) :
    global limite
    try : limite = int(entree2.get())
    except : a = 0

def key_down_return3(event) :
    global l_couleurs
    l_couleurs += [["#"+entree3.get(),b_ld.get("active")]]
    crea_lcouleurs()

def key_down_return4(event) :
    global delai
    try : delai = int(entree4.get())
    except : a = 0

def suppr_outil(event) :
    global l_couleurs
    if len(l_couleurs) > 1 :
        del l_couleurs[l_couleurs.index([b_lcouleurs.get("active").split(" ")[0],b_lcouleurs.get("active").split(" ")[2]])]
        crea_lcouleurs()

def change_compteur() :
    global compteur
    compteur = 1 if compteur == 0 else 0

def clear_compteur() :
    global iterations
    iterations = 0

def change_pause() :
    global pause
    global b_pause
    pause = 1 if pause == 0 else 0
    b_pause.destroy()
    b_pause = Button(cadre,text=[" | | "," > "][pause],command=change_pause)
    b_pause.pack(side=TOP,anchor="w",padx=5,pady=5)
    if pause == 0 : mouv()

def crea_grille() :
    global grille
    global fourmis
    global iterations
    canvas.delete("all")
    grille,fourmis,iterations = [[0,canvas.create_rectangle(j*(500/taille)+2,i*(500/taille)+2,(j+1)*(500/taille)+2,(i+1)*(500/taille)+2,fill=l_couleurs[0][0],outline=l_couleurs[0][0])] for i in range (taille) for j in range (taille)],[],0
    affich()

def affich() :
    global fourmis
    global ci
    for i in range (0,len(fourmis)-2,3) :
        if fourmis[i+2] != "" : canvas.delete(fourmis[i+2])
        if fourmis[i+1] == "H" : fourmis[i+2] = canvas.create_polygon((fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,(fourmis[i]%taille+0.5)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,fill="red",outline="black")
        elif fourmis[i+1] == "B" : fourmis[i+2] = canvas.create_polygon((fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+0.5)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,fill="red",outline="black")
        elif fourmis[i+1] == "G" : fourmis[i+2] = canvas.create_polygon((fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille+0.5)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,fill="red",outline="black")
        elif fourmis[i+1] == "D" : fourmis[i+2] = canvas.create_polygon((fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille+0.5)*(500/taille)+2,(fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,fill="red",outline="black")
    try : canvas.delete(ci)
    except : a = 0
    if compteur == 1 : ci = canvas.create_text(250,10,text=str(iterations),font="Consolas 12",fill="purple")

def mouv() :
    global grille
    global fourmis
    global taille
    global iterations
    global pause
    global b_pause
    if taille < limite :
        non = 0
        for i in range (0,len(fourmis)-2,3) :
            if fourmis[i] < taille or fourmis[i] > taille**2-taille or fourmis[i]%taille == 1 or fourmis[i]%taille == taille-1 :
                non = 1
                break
        if non == 1 :
            for i in range (0,len(fourmis)-2,3) :
                fourmis[i] += 2*(fourmis[i]//taille)+taille+3
            canvas.delete("all")
            for i in range (taille) :
                grille = grille[:i*(taille+2)]+[[0,""]]+grille[i*(taille+2):i*(taille+2)+taille]+[[0,""]]+grille[i*(taille+2)+taille:]
            grille = [[0,""] for i in range (taille+2)]+grille+[[0,""] for i in range (taille+2)]
            taille += 2
            grille = [[grille[i*taille+j][0],canvas.create_rectangle(j*(500/taille)+2,i*(500/taille)+2,(j+1)*(500/taille)+2,(i+1)*(500/taille)+2,fill=l_couleurs[grille[i*taille+j][0]][0],outline=l_couleurs[grille[i*taille+j][0]][0])] for i in range (taille) for j in range (taille)]
            affich()
    i = 0
    while i < len(fourmis)-2 :
        if l_couleurs[grille[fourmis[i]][0]][1] == "G" : fourmis[i+1] = {"H" : "G","B" : "D","G" : "B","D" : "H"}[fourmis[i+1]]
        else : fourmis[i+1] = {"H" : "D","B" : "G","G" : "H","D" : "B"}[fourmis[i+1]]
        grille[fourmis[i]][0] += 1
        if grille[fourmis[i]][0] == len(l_couleurs) : grille[fourmis[i]][0] = 0
        canvas.delete(grille[fourmis[i]][1])
        grille[fourmis[i]][1] = canvas.create_rectangle((fourmis[i]%taille)*(500/taille)+2,(fourmis[i]//taille)*(500/taille)+2,(fourmis[i]%taille+1)*(500/taille)+2,(fourmis[i]//taille+1)*(500/taille)+2,fill=l_couleurs[grille[fourmis[i]][0]][0],outline=l_couleurs[grille[fourmis[i]][0]][0])
        if fourmis[i] < taille and fourmis[i+1] == "H" or fourmis[i] > taille**2-taille and fourmis[i+1] == "B" or fourmis[i]%taille == 0 and fourmis[i+1] == "G" or fourmis[i]%taille == taille-1 and fourmis[i+1] == "D" : del fourmis[i:i+3]
        else :
            fourmis[i] += {"H" : -taille,"B" : taille,"G" : -1,"D" : 1}[fourmis[i+1]]
            i += 3
    iterations += 1
    affich()
    if pause == 0 and len(fourmis) > 0 : canvas.after(delai,mouv)
    else :
        pause = 1
        b_pause.destroy()
        b_pause = Button(cadre,text=[" | | "," > "][pause],command=change_pause)
        b_pause.pack(side=TOP,anchor="w",padx=5,pady=5)

def crea_lcouleurs() :
    global b_lcouleurs
    try : b_lcouleurs.destroy()
    except : a = 0
    b_lcouleurs = Listbox(cadre4,width=30,height=8)
    for i in l_couleurs :
        b_lcouleurs.insert("end",i[0]+" : "+i[1])
    b_lcouleurs.pack(side=TOP,anchor="w",padx=0,pady=0)
    b_lcouleurs.bind("<BackSpace>",suppr_outil)

fenetre = Tk()
fenetre.title("La fourmi de Langton")
fenetre.resizable(width=False,height=False)

canvas = Canvas(fenetre,width=500,height=500,bg="white")
canvas.pack(side=LEFT,padx=5,pady=5)
canvas.bind("<Button-1>",mouse_button_down)
canvas.bind("<B1-Motion>",mouse_button_down)

cadre = LabelFrame(fenetre,padx=5,pady=5,borderwidth=0)
cadre.pack(side=LEFT,fill="both",expand="no")

cadre2 = LabelFrame(cadre,text="Largeur de l'écran :",padx=5,pady=5)
cadre2.pack(side=TOP,fill="both",expand="no")
taille = 50
entree = Entry(cadre2,width=30)
entree.pack(side=TOP,anchor="w",padx=0,pady=0)
entree.bind("<Return>",key_down_return)

cadre3 = LabelFrame(cadre,text="Limite :",padx=5,pady=5)
cadre3.pack(side=TOP,fill="both",expand="no")
limite = 50
entree2 = Entry(cadre3,width=30)
entree2.pack(side=TOP,anchor="w",padx=0,pady=0)
entree2.bind("<Return>",key_down_return2)

cadre4 = LabelFrame(cadre,text="Outils :",padx=5,pady=5)
cadre4.pack(side=TOP,fill="both",expand="no")
cadre4a = LabelFrame(cadre4,padx=0,pady=0,borderwidth=0)
cadre4a.pack(side=TOP,fill="both",expand="no")
outil,fourmis = StringVar(),[]
b_outil1,b_outil2 = Radiobutton(cadre4a,text="Fourmi",variable=outil,value=1,state=ACTIVE).pack(side=LEFT,padx=0,pady=0),Radiobutton(cadre4a,text="Case",variable=outil,value=0,state=ACTIVE).pack(side=LEFT,padx=0,pady=0)
outil.set("1")
cadre4b = LabelFrame(cadre4,padx=0,pady=0,borderwidth=0)
cadre4b.pack(side=TOP,fill="both",expand="no")
Label(cadre4b,text="Orientation de la fourmi : ").pack(side=LEFT,padx=0,pady=0)
b_ldf = Listbox(cadre4b,width=2,height=1)
for i in ["H","B","G","D"] :
    b_ldf.insert("end",i)
b_ldf.pack(side=LEFT,padx=0,pady=0)
cadre4c = LabelFrame(cadre4,padx=0,pady=0,borderwidth=0)
cadre4c.pack(side=TOP,fill="both",expand="no")
Label(cadre4c,text="#").pack(side=LEFT,padx=0,pady=0)
entree3 = Entry(cadre4c,width=10)
entree3.pack(side=LEFT,anchor="w",padx=0,pady=0)
entree3.bind("<Return>",key_down_return3)
Label(cadre4c,text=" : ").pack(side=LEFT,padx=0,pady=0)
b_ld = Listbox(cadre4c,width=2,height=1)
for i in ["G","D"] :
    b_ld.insert("end",i)
b_ld.pack(side=LEFT,padx=0,pady=0)
l_couleurs = [["#ffffff","D"],["#000000","G"]]
crea_lcouleurs()
b_clear_ecran = Button(cadre,text="Effacer",command=crea_grille).pack(side=TOP,anchor="w",padx=5,pady=5)

cadre5 = LabelFrame(cadre,text="Compteur :",padx=0,pady=0)
cadre5.pack(side=TOP,fill="both",expand="no")
compteur,iterations = 0,0
b_compteur = Checkbutton(cadre5,text="Compteur d'itérations",command=change_compteur).pack(side=LEFT,padx=5,pady=5)
b_clear_compteur = Button(cadre5,text=" X ",command=clear_compteur).pack(side=LEFT,padx=5,pady=5)

cadre6 = LabelFrame(cadre,text="Délai entre chaque itération (en ms) :",padx=5,pady=5)
cadre6.pack(side=TOP,fill="both",expand="no")
delai = 100
entree4 = Entry(cadre6,width=30)
entree4.pack(side=TOP,anchor="w",padx=0,pady=0)
entree4.bind("<Return>",key_down_return4)

pause = 1
b_pause = Button(cadre,text=" > ",command=change_pause)
b_pause.pack(side=TOP,anchor="w",padx=5,pady=5)

crea_grille()

fenetre.mainloop()