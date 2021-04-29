import tkinter as tk
from tkinter import END
import tkinter.font as font

listanum = []


# Configurações da janela principal, tamanho, titulo, configurações
# das linha, das colunas e da fonte
janela_principal = tk.Tk()
janela_principal.title('Calculadora')
janela_principal.columnconfigure([0, 1, 2, 3], minsize=1)
janela_principal.rowconfigure([0, 1, 2, 3, 4], minsize=37)
# Não permitir que a janela seja extendida
janela_principal.resizable(False, False)
font = font.Font(size=10)
# Ecrâ Calculadora
ecra = tk.Entry(width=25, relief=tk.GROOVE, borderwidth=2, justify=tk.RIGHT, font=font)


def inserir_numeros(numero):
    atual = ecra.get()
    ecra.delete(0, END)
    ecra.insert(0, str(atual) + str(numero))


def delete():
    ecra.delete(0, END)


def digitar_a(adicao):
    num_a = 0
    atual = ecra.get()
    ecra.delete(0, END)
    ecra.insert(0, str(atual) + adicao)
    atual_a = ecra.get()
    for num in atual_a:
        if num == '+':
            num_a += 1
    print(num_a)
    if num_a >= 1:
        um_a(num_a)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def digitar_s(subtracao):
    num_s = 1
    atual = ecra.get()
    ecra.delete(0, END)
    ecra.insert(0, str(atual) + subtracao)
    for num in atual:
        if num == '-':
            num_s += 1
    if num_s == 1:
        um_s(num_s)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def um_a(num_a):
    global index_a1
    if num_a == 1:
        atual = str(ecra.get())
        index_a1 = atual.index('+')
        listanum.append(atual[:index_a1])
        listanum.append('+')
    elif num_a > 1:
        atual = str(ecra.get())
        index_a2 = atual.index('+')
        listanum.append(atual[index_a1+1:index_a2])
        listanum.append('+')
    print(listanum)


def um_s(num_s):
    if num_s == 1:
        atual = str(ecra.get())
        print(atual)
        index_s = atual.index('-')
        listanum.append(atual[:index_s])
    print(listanum)



def res():
    resultado = 0
    ecra.insert(0, '=')
    valor_i = '='

    # if numero_a >= 1:
    #     print('ola')
    #     for num in numeros:
    #         if num.isnumeric():
    #             listanum.append(int(num))
    #         elif num == '+':
    #             listanum.append(num)

    print(listanum)
    # numero_i = numeros.count('=')
    # if numero_i == 1:
    #     for a in valor_i:
    #         numeros = numeros.replace(a, '')
    #         listanum.append(int(numeros))
    # ecra.delete(0, END)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


# Botões numéricos
btn_0 = tk.Button(text='0', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(0))
btn_1 = tk.Button(text='1', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(1))
btn_2 = tk.Button(text='2', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(2))
btn_3 = tk.Button(text='3', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(3))
btn_4 = tk.Button(text='4', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(4))
btn_5 = tk.Button(text='5', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(5))
btn_6 = tk.Button(text='6', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(6))
btn_7 = tk.Button(text='7', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(7))
btn_8 = tk.Button(text='8', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(8))
btn_9 = tk.Button(text='9', width=5, relief=tk.GROOVE, borderwidth=2, bg='white', font=font,
                  command=lambda: inserir_numeros(9))

# Botões de operação
# (x - multiplacação)
# (s - subtração)
# (a - adição)
# (i - igual)
# (div - divisão)
btn_div = tk.Button(text=':', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_x = tk.Button(text='x', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_s = tk.Button(text='-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font, command=lambda: digitar_s('-'))
btn_a = tk.Button(text='+', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font, command=lambda: digitar_a('+'))
btn_i = tk.Button(text='=', width=5, relief=tk.GROOVE, borderwidth=2, bg='#66C4F2', font=font, command=res)

# Adicionar icon ao botão delete
icon_delete = tk.PhotoImage(
    file='C:\Programação e Projetos\Python\Tkinter\Calculadora_com_GUI\Icon\outline_backspace_black_24dp.gif')

# Outros Botões
# (n - positvo ou negativo)
# (v - vígula)
# (d - delete)
# (pe - parênteses esquerdo)
# (pd - parênteses direito)
btn_n = tk.Button(text='+/-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_v = tk.Button(text=',', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_d = tk.Button(width=44, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', image=icon_delete, command=delete)
btn_pe = tk.Button(text='(', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_pd = tk.Button(text=')', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)

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
