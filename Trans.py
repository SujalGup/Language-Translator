from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES

root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.title("Project--Language Translator")
root.config(bg = 'light blue')

#heading
Label(root, text = "LANGUAGE TRANSLATOR", font = "cascadia 20 bold", bg='white smoke').pack()
Label(root,text ="PROJECT BY Sujal Gupta", font = 'calibri 20 bold', bg ='white smoke' , width = '22').pack(side = 'bottom')



#INPUT AND OUTPUT TEXT WIDGET
Label(root,text ="Input", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)


Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)
 


##################
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=20,y=60)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(root, values= language, width =22)
dest_lang.place(x=890,y=60)
dest_lang.set('choose output language')
########################################  Define function #######

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)
   



##########  Translate Button ########
trans_btn = Button(root, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'teal', activebackground = 'sky blue')
trans_btn.place(x = 490, y = 180)


root.mainloop()
