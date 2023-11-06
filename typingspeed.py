from tkinter import messagebox;
def labelSlider():
    global count,sliderwords
    text="Welcome to typing speed increaser game"
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(300,labelSlider)

def startGame(event):

    global timeleft,score,miss
    if timeleft==14:
        time()
    gamePlayDetaillabel.configure(text='')
    if(wordentry.get()==wordlabel['text']):
        score+=1
        scorelableCount.configure(text=score)
    else:
        miss+=1
        print('NOt Matched')
    random.shuffle(wordlist)
    wordlabel.configure(text=wordlist[0])
    wordentry.delete(0,END)

def time():
    global timeleft,score,miss
    if (timeleft >= 11):
        pass
    else:
        Timerleft.configure(fg="red")
    if (timeleft >= 0):
        timeleft-=1
        Timerleft.configure(text=timeleft)
        Timerleft.after(1000,time)
    else:
        gamePlayDetaillabel.configure(text='Hit={0} | Miss={1} | totalScore={2}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For Play again hit Retry')
        if rr==True:
            score=0
            timeleft=60
            miss=0
            Timerleft.configure(text=timeleft)
            wordlabel.configure(text=wordlist[0])
            scorelableCount.configure(text=0)
from tkinter import *
import random
#initialising the windows
window=Tk()
window.geometry('800x600+400+100')
window.configure(bg='powder blue')
window.title('chack your typing speed')
window.iconbitmap('spped.ico')
#////////////////////////////////////////////////
#333333333333333333333333333333333333333333333333333333333
#variabels
wordlist=['Mango','Apple','Greeps','Chuarre','Door','Tv','Laptop','Mobile']
score=0
timeleft=60
miss=0
count=0
sliderwords=''


#labels
fontlabel=Label(window,text='',font=('arial',25,'italic bold'),bg='powder blue',width=40,fg='red')
fontlabel.place(x=10,y=10)
labelSlider()
random.shuffle(wordlist)
wordlabel=Label(window,text=wordlist[0],font=('arial',25,'italic bold'),bg='powder blue',fg='black')
wordlabel.place(x=350,y=200)
scorelable=Label(window,text='your score:',font=('arial',25,'italic bold'),bg='powder blue',fg='black')
scorelable.place(x=10,y=100)

scorelableCount=Label(window,text='0',font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
scorelableCount.place(x=80,y=180)

TimerLabel=Label(window,text='Time Left:',font=('arial',25,'italic bold'),bg='powder blue',fg='black')
TimerLabel.place(x=600,y=100)

Timerleft=Label(window,text=timeleft,font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
Timerleft.place(x=640,y=180)

gamePlayDetaillabel=Label(window,text='type word and hit enter button',font=('arial',30,'italic bold'),bg='powder blue',fg='dark grey')
gamePlayDetaillabel.place(x=120,y=450)

#/////////////////////////////////
#entry box in the project
wordentry=Entry(window,justify='center',font=('arial',25,'italic bold'))
wordentry.place(x=250,y=300)
wordentry.focus_set()
############################################################
window.bind('<Return>',startGame)
window.mainloop()