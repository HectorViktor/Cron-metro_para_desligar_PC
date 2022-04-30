import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os


#definindo a janela UI 

window=tk.Tk()
window.title('ShutdownTimer')
window.geometry('420x150')



#Caixa:

hourslbl=tk.Label(window,text='Hours:',font=10)
hourslbl.grid(column=0,row=0)
minuteslbl=tk.Label(window,text='Minutes:',font=10)
minuteslbl.grid(column=0,row=1)
secondslbl=tk.Label(window,text='Seconds:',font=10)
secondslbl.grid(column=0,row=2)



#inputs:

hours=tk.IntVar()
mins=tk.IntVar()
secs=tk.IntVar()
hoursinput=tk.Entry(window,textvariable=hours,font=50)
hoursinput.grid(column=1,row=0)
minutesinput=tk.Entry(window,textvariable=mins,font=50)
minutesinput.grid(column=1,row=1)
secondsinput=tk.Entry(window,textvariable=secs,font=50)
secondsinput.grid(column=1,row=2)

h=0
m=0
s=0
timer=tk.Label(window,text='{:02d}:{:02d}:{:02d}'.format(h,m,s),font=100) #countdown label formatted
timer.grid(column=1,row=3)



#Botões:
#Primeiro, defina o que vai acontecer quando apertar START

def CDown():
    global h
    global m
    global s
    global rollback
    while h+m+s==0: #1° Processo quando o botão é pressionado, ter valores na caixa de entrada, disabilitar e configurar o cronômetro
        h=int(hoursinput.get())
        m=int(minutesinput.get())
        s=int(secondsinput.get())
        bttnSTART.configure(text='Processing...',state=tk.DISABLED)
        timer.configure(text='{:02d}:{:02d}:{:02d}'.format(h,m,s))
        tk.messagebox.showinfo('Confirm','If you continue the computer will shutdown in {:02d}:{:02d}:{:02d}'.format(h,m,s))
    if s > 0:
        s=s-1
    else:
        s=59
        if m >0:
            m=m-1
        else:
            m=59
            h=h-1
    timer.configure(text='{:02d}:{:02d}:{:02d}'.format(h,m,s))
    window.update() # Atualizar a janela para formatar o valor
    if h+m+s==0:
        window.after_cancel(CDown) # Quebra o loop quando a soma chega a zero
        os.system('shutdown -s') #Desliga o PC sem perguntar
    else:
        rollback=window.after(1000,CDown) #atrasa a função por 1000 ms e a reinicia (TIPO WHILE LOOP)



#Então, o que acontece quando o STOP for pressionado

def STOP():
    global CDown
    global h
    global m
    global s
    global rollback
    h=0
    m=0
    s=0
    window.after_cancel(rollback) #Para a contagem e reseta o crônometro.
    timer.configure(text='{:02d}:{:02d}:{:02d}'.format(h,m,s))
    bttnSTART.configure(text='Start',state=tk.ACTIVE)



# Botão UI

bttnSTART=ttk.Button(window,text='Start',command=CDown)
bttnSTART.grid(column=2,row=0)
bttnSTOP=ttk.Button(window,text='Stop',command=STOP)
bttnSTOP.grid(column=2,row=1)

window.mainloop() #mantém a janela aberta até nova ação ser realizada ou fechada#