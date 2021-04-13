import tkinter as tk
import tkinter.font as font


def digitar_0():
    ecra.insert(30, 0)
    global valor_0
    valor_0 = str(0)
    print(valor_0)


def digitar_1():
    ecra.insert(30, 1)
    global valor_1
    valor_1 = str(1)
    print(valor_1)


def delete():
    ecra.delete(0)


def digitar_a():
    ecra.insert(30, '+')
    valor_a = '+'
    print(valor_a)
    global num_1
    if valor_a:
        num_1 = int(''.join([valor_1, valor_0]))
        print(num_1)


def res():
    global resu
    ecra.insert(30, '=')
    valor_i = '='
    print(valor_i)
    if valor_i:
        num_2 = int(''.join([valor_1, valor_0]))
        resu = num_1 + num_2
        print(resu)
    ecra.insert(30, resu)


# Configurações da janela principal, tamanho, titulo, configurações
# das linha, das colunas e da fonte
janela_principal = tk.Tk()
janela_principal.title('Calculadora')
janela_principal.columnconfigure([0, 1, 2, 3], minsize=1)
janela_principal.rowconfigure([0, 1, 2, 3, 4], minsize=37)
font = font.Font(size=10)

# Botões numéricos
btn_0 = tk.Button(text='0', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font, command=digitar_0)
btn_1 = tk.Button(text='1', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font, command=digitar_1)
btn_2 = tk.Button(text='2', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_3 = tk.Button(text='3', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_4 = tk.Button(text='4', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_5 = tk.Button(text='5', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_6 = tk.Button(text='6', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_7 = tk.Button(text='7', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_8 = tk.Button(text='8', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)
btn_9 = tk.Button(text='9', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font)

# Botões de operação
# (x - multiplacação)
# (s - subtração)
# (a - adição)
# (i - igual)
# (div - divisão)
btn_div = tk.Button(text=':', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_x = tk.Button(text='x', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_s = tk.Button(text='-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_a = tk.Button(text='+', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font, command=digitar_a)
btn_i = tk.Button(text='=', width=5, relief=tk.GROOVE, borderwidth=2, bg='#66C4F2', font=font, command=res)

# Adicionar icon ao botão delete
icon_delete = tk.PhotoImage(file='C:\Programação e Projetos\Python\Tkinter\Calculadora com interface gráfica\Icon\outline_backspace_black_24dp.gif')

# Outros Botões
# (n - positvo ou negativo)
# (v - vígula)
# (d - delete)
# (pe - parênteses esquerdo)
# (pd - parênteses direito)
btn_n = tk.Button(text='+/-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_v = tk.Button(text=',', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_d = tk.Button(text='del', width=44, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', image=icon_delete, command=delete)
btn_pe = tk.Button(text='(', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_pd = tk.Button(text=')', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)

# Ecrâ Calculadora
ecra = tk.Entry(width=25, relief=tk.GROOVE, borderwidth=2, justify=tk.RIGHT, font=font)

# Botões numéricos posicionados
btn_0.grid(row=5, column=1, ipady=5, padx=2)
btn_1.grid(row=4, column=0, ipady=5, padx=2)
btn_2.grid(row=4, column=1, ipady=5, padx=2)
btn_3.grid(row=4, column=2, ipady=5, padx=2)
btn_4.grid(row=3, column=0, ipady=5, padx=2)
btn_5.grid(row=3, column=1, ipady=5, padx=2)
btn_6.grid(row=3, column=2, ipady=5, padx=2)
btn_7.grid(row=2, column=0, ipady=5, padx=2)
btn_8.grid(row=2, column=1, ipady=5, padx=2)
btn_9.grid(row=2, column=2, ipady=5, padx=2)

# Botões de operação posicionados
btn_div.grid(row=1, column=3, ipady=5, padx=2)
btn_x.grid(row=2, column=3, ipady=5, padx=2)
btn_s.grid(row=3, column=3, ipady=5, padx=2)
btn_a.grid(row=4, column=3, ipady=5, padx=2)
btn_i.grid(row=5, column=3, ipady=5, padx=2)

# Outros Botões posicionados
btn_d.grid(row=1, column=2, ipady=4, padx=2)
btn_n.grid(row=5, column=0, ipady=5, padx=2)
btn_v.grid(row=5, column=2, ipady=5, padx=2)
btn_pe.grid(row=1, column=0, ipady=5, padx=2)
btn_pd.grid(row=1, column=1, ipady=5, padx=2)

# Posicionamento do Ecrã
ecra.place(x=17, y=7, height=25)

janela_principal.mainloop()
