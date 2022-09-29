from tkinter import *
from random import *
from tkinter import ttk
import webbrowser
from time import *

#шрифты
fnt_1 = "Arrial bold"
fnt_2 = "Microsoft Sans Serif"
fnt_3 = "Century"
fnt_4 = "FixedSys"
fnt_5 = "Sitka Text"

#окно для калькулятора
wnd = Tk()
wnd.geometry("500x500")
wnd.resizable(False,False)
wnd.title("Калькулятор от God)")
col = Label(wnd,text = "",width=500,height=500)
col.place(x = 0, y = 0)

#верхняя надпись
hello_user = Label(wnd,text = "\nВы используете калькулятор, написанный в 2022 году\n", font = (fnt_5,12,"bold"))
hello_user.place(x=20,y=0)

#тестовый

#строка для ввода выражения
term = Entry(wnd,width=46,font = (fnt_3,15),fg = "Black",justify = CENTER)
term.place(x=0,y=60,height = 50)

#панель для клавиш
klava = ttk.Frame(height = 300,width = 300)
klava.place(x=190,y=120)

#нужно 25 кнопок
buts_names = [str(i) for i in range(1,10)]+['0']+['+','-','/','*','abs','(',')','sin','cos',' ', 'log','exp','.','**','=']

def create_func(s):
    def click_button():
        term.insert(END,s)
    return click_button

buts = []
for i in range(25):
    buts.append(Button(klava,text=buts_names[i] ,bg = "#B3E5FC",command = create_func(buts_names[i])))
buts[19].configure(text = "__")

#разместим кнопки на панели клавиш
x1 = x2 = 0
for i in range(25):
    buts[i].configure(height = 3,width = 6)
    buts[i].place(x = x1, y = x2)
    x1 += 60
    if x1 == 300:
        x1 = 0
        x2 += 60

#Очистим строку ввода
term.delete(0, END)

#считывание значения из строки и ответ
s = ""
ans = Label(wnd,text = "Не могу посчитать",font = (fnt_1,12),relief = GROOVE,bg = "#B3E5FC",width = 18,height = 3)
def click():
    global s,ans
    s = term.get()
    if s != "":
        try:
            x = eval(s)
            tst = int(x)
            term.delete(0, END)
            term.insert(END,x)
        except:
            term.delete(0, END)
            term.insert(END,"Автору нет 18")
            ans.configure(text = "ГГ")
    ans.place(x = 12,y = 428)

#Добавим жару с рандомайзером
#панель для строк ввода и ответа
ran = ttk.Frame(height = 300,width = 170,relief = GROOVE)
ran.place(x=10,y=120)

#кнопка с инструкцией
ss = """Инструкция для этого калькулятора:

  1) клавиатура для главной строки
  2) для рандомайзера юзайте свою клаву
  3) **- это степень (3**2 == 9)
  4) не допускайте ошибок со скобками
  5) abs - модуль (abs(-2)==2)
  6) log и exp - это log и exp
  7) я сам не знаю, зачем вам мой vk
  8) этот текст можно редачить
  9) найдете баг - можете пнуть
  10) приятной работы :D"""

def get_inst():
    global ss
    msg = ttk.Frame(height = 300,width = 300)
    lble = Label(msg,text = '',font = (fnt_1,10),height = 300,width = 300,bg = "#B3E5FC")
    lble.place(x = 0, y = 0)

    txt = Text(msg,height = 20,width = 50,font = (fnt_1,10),
               bg = "#B3E5FC")
    txt.insert(0.0, ss)
    txt.place(x = 0, y = 0)
    
    ext = Button(msg,text = 'Закрыть',
                 bg=get_rgb((248, 226, 45)),
                 width = 10,
                 command = msg.destroy)
    ext.place(x = 215,y =270)
    
    msg.place(x=190,y=120)
    

def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb

instruct = Button(ran,text="Инструкция по\nприложению" ,
                      bg=get_rgb((248, 226, 45)),
                      width = 20,
                      command = get_inst)
instruct.place(x=9,y=5)

#2 строки ввода для чисел
c1 = Entry(ran,width=16,font = (fnt_2,12),justify = CENTER)
c1.place(x=10,y=60)
c1.insert(0,"1")

c2 = Entry(ran,width=16,font = (fnt_2,12),justify = CENTER)
c2.place(x=10,y=100)
c2.insert(0,"100")


#кнопка для рандома
answer = Label(ran,text = "Тут будет число",
               font = (fnt_2,12),
               justify = CENTER,
               relief = GROOVE,
               bg=get_rgb((255, 255, 255)),
               width = 17,
               height = 4)
answer.place(x=5,y=150)

def randim():
    x1 = c1.get()
    x2 = c2.get()
    try:
        c = randint(int(x1),int(x2))
        answer.configure(text = str(c))
    except:
        answer.configure(text = "Ты дурачек?")
        
rnd = Button(ran,text = 'Случайное число\nот A до B',
                 bg=get_rgb((248, 226, 45)),
                 width = 20,
                 command = randim)
rnd.place(x = 9,y=250)

def back():
    term.delete(len(term.get())-1)

Back_Space = Button(wnd,text = '<-BackSpace',bg="#B3E5FC",height = 3,width = 23,command = back)
Back_Space.place(x = 310,y = 430)


#привилегии для кнопки "="
buts[24].configure(command = click,bg=get_rgb((248, 226, 45)))


#Кнопка ссылки на меня
def get_vk():
    webbrowser.open('https://vk.com/the_last_genius', new=2)

me = Button(wnd,text = 'ВК автора',bg="#B3E5FC",height = 3,width = 15,command = get_vk)
me.place(x = 190,y = 430)

wnd.mainloop()
























