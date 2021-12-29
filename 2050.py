import random  # библиотека случайных чисел
import tkinter  # библиотека форм
t2=tkinter.Tk()  # создание окно
t2.geometry("700x500")  # размер окна
t2.title("2048 Game")  # заголовок окнa
# игровое поле 4 на 4
arr = [[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
# позиции квадратов 4 на 4
poz=[[0,0,0,0]
,[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
# промежуточный массив
prarr=[[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
# проверка данных
dm=[[1,1,1,1],
[1,1,1,1],
[1,1,1,1],
[1,1,1,1]]
# цветное значени пазлов
colp={
        0:"#fffff0",
        2: "#eee4da",
        4: "#ede0c8",
        8: "#edc850",
        16: "#edc53f",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#f2b179",
        1024: "#f59563",
        2048: "#edc22e",
    }
    
# создание плитки
def init():
    for i in range(4):
        for j in range(4):
            prarr[i][j]=0
            poz[i][j]=0

# начальная плитка
def init_arr():
    for i in range(4):
        for j in range(4):
            arr[i][j]=0

# проверка заполненно ли все
def zapv ():
    movex=[-1,1,0,0]
    movey=[0,0,-1,1]
    for i in range(4):  
        for j in range(4):
            for g in range(4):
                newx=int(i+movex[g])
                newy=int(j+movey[g])
                if (newx<0 or newx>3)or(newy<0 or newy>3):
                    continue
                else:
                    if arr[i][j]==arr[newx][newy]:
                        return True
    return False



# принятие числа от 2 до 4
def random_num():
    while True:
        x1=random.randint(0,3)  
        y1=random.randint(0,3)
        if poz[x1][y1]==0:
            arr[x1][y1]=random.choice([2,4,2,2]) 
            poz[x1][y1]=1
            return   



#вверх
def put_up():
    init()  
    for i in range(4):  
        g=0
        for j in range(4):
            if arr[j][i]==0:
                continue
            else:
                prarr[g][i]=arr[j][i]
                g+=1
    for i in range(4):  #пустое значение,после объедеинения плики
        for j in range(1,4):
            if prarr[j][i]==0:
                break
            else:
                if prarr[j][i]==prarr[j-1][i]:
                    prarr[j-1][i]=prarr[j][i]+prarr[j-1][i]
                    prarr[j][i]=0
    if prarr==arr:  
        return
    init_arr()  # объединие плиток
    for i in range(4):
        g=0
        for j in range(4):
            if prarr[j][i]==0:
                continue
            else:
                arr[g][i]=prarr[j][i]
                poz[g][i]=1
                g+=1
    random_num()  # 2 или 4 генерируется случайным образом после слияния
    print_interface()  # интерфейс и отображение
    gameover()  #
    return


#вниз
def put_down():
    init()
    for i in range(4):
        g=3
        j=3
        while j>=0:
            if arr[j][i]==0:
                j-=1
                continue
            else:
                prarr[g][i]=arr[j][i]
                g-=1
                j-=1
    for i in range(4):
        j=2
        while j>=0:
            if prarr[j][i]==0:
                break
            else:
                if prarr[j][i]==prarr[j+1][i]:
                    prarr[j+1][i]=prarr[j][i]+prarr[j+1][i]
                    prarr[j][i]=0
            j-=1
    if prarr==arr:
        return
    init_arr()
    for i in range(4):
        g=3
        j=3
        while j>=0:
            if prarr[j][i]==0:
                j-=1
                continue
            else:
                arr[g][i]=prarr[j][i]
                poz[g][i]=1
                g-=1
            j-=1
    random_num()
    print_interface()
    gameover()  
    return


#интерфейс 
def print_interface():
    for i in range(4):
        for j in range(4):
            cs=colp[arr[i][j]]
            c2.create_rectangle(j*101,i*101,j*101+101,i*101+101,fill="%s"%(cs))
            if arr[i][j]!=0:  
                c2.create_text((j*101+101)-50,(i*101+101)-50,text="%d"%(arr[i][j]),font=(30))


# цвет фона
t2['bg']='#96a8df'  
c2=tkinter.Canvas(t2,width=400,height=400)  # форма 
c2.pack(side="left") 
random_num()  # рандом генерация 2 или 4 в позиции, где нет номера
for i in range(4):  
    for j in range(4):
        cs=colp[arr[i][j]]
        c2.create_rectangle(j*100,i*100,j*100+100,i*100+100,fill="%s"%(cs))  
        if arr[i][j]!=0:
            c2.create_text((j*100+100)-50,(i*100+100)-50,text="%d"%(arr[i][j]),font=("Курсив",30))  # заполнение




#влево
def put_left():
    init()
    for i in range(4):
        g=0
        for j in range(4):
            if arr[i][j]==0:
                continue
            else:
                prarr[i][g]=arr[i][j]
                g+=1
    for i in range(4):
        for j in range(1,4):
            if prarr[i][j]==0:
                break
            else:
                if prarr[i][j]==prarr[i][j-1]:
                    prarr[i][j-1]=prarr[i][j]+prarr[i][j-1]
                    prarr[i][j]=0
    if prarr==arr:
        return
    init_arr()
    for i in range(4):
        g=0
        for j in range(4):
            if prarr[i][j]==0:
                continue
            else:
                arr[i][g]=prarr[i][j]
                poz[i][g]=1
                g+=1
    random_num()
    print_interface()
    gameover()  
    return




#Направо
def put_right():
    init()
    for i in range(4):
        g=3
        j=3
        while j>=0:
            if arr[i][j]==0:
                j-=1
                continue
            else:
                prarr[i][g]=arr[i][j]
                g-=1
                j-=1
    for i in range(4):
        j=2
        while j>=0:
            if prarr[i][j]==0:
                break
            else:
                if prarr[i][j]==prarr[i][j+1]:
                    prarr[i][j+1]=prarr[i][j]+prarr[i][j+1]
                    prarr[i][j]=0
            j-=1
    if prarr==arr:
        return
    init_arr()
    for i in range(4):
        g=3
        j=3
        while j>=0:
            if prarr[i][j]==0:
                j-=1
                continue
            else:
                arr[i][g]=prarr[i][j]
                poz[i][g]=1
                g-=1
            j-=1
    random_num()
    print_interface()
    gameover()  
    return

# конец
def gameover():
    if poz==dm and zapv()==False:  # если все позиции в пазлах,то конец
        c2.create_rectangle(100,150,300,250,fill="#cc6158")
        c2.create_text(200,200,text="GаmeOver")


# кнопки
b1=tkinter.Button(t2,text="↑",font=(11),fg="black",command=put_up)  # первая кнопка 
b2=tkinter.Button(t2,text="↓",font=(11),fg="black",command=put_down)  # вторая кнопка 
b3=tkinter.Button(t2,text="←",font=(11),fg="black",command=put_left)
b4=tkinter.Button(t2,text="→",font=(11),fg="black",command=put_right)
b4.pack(side="right",anchor="center")  # позиция
b3.pack(side="right",anchor="center")
b2.pack(side="right",anchor="center")
b1.pack(side="right",anchor="center")
t2.mainloop()  