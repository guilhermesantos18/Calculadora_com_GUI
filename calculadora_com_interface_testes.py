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
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


# Limpar o ecra da calculadora e limpar a lista
def delete():
    ecra.delete(0, END)
    listanum.clear()


def digitar_a(adicao):
    num_a = 0
    atual = ecra.get()
    ecra.delete(0, END)
    ecra.insert(0, str(atual) + adicao)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def digitar_s(subtracao):
    num_s = 1
    atual = ecra.get()
    ecra.delete(0, END)
    ecra.insert(0, str(atual) + subtracao)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def listanumeros_separados(atual):
    # Verificar as posições de os operadores e adicionar os números
    # entre os operadores e guarda-los numa lista
    print(atual)
    cont_operadores = 0
    cont_operadores_entre_primeiromais_ultimomais = 0
    lista_pos_operadores = []
    lista_pos_operadores_entre_primeiromais_ultimomais = []
    # Se existir um + em atual
    if '+' in atual:
        # Pegar todas as posições dos operadores
        for pos in range(0, len(atual)):
            if atual[pos] == '+':
                # Contador para ajudar na adição de os números há lista entre os operadores
                cont_operadores += 1
                lista_pos_operadores.append(pos)

        # Para cada posição dos operadores, vou verificar se a sua posição,
        # É igual á posição do primeiro operador, se a posição é igual há,
        # de o último operador e se a posição dos restantes operadores está entre,
        # a primeira posição e a última posição
        for pos_mais in lista_pos_operadores:
            if pos_mais == atual.index('+'):
                listanum.append(atual[:pos_mais])
                # Entra aqui nesta situação 10+15 só existe um + e com esta condição consigu,
                # Com que adicione o número há direita do primeiro + seja adicionado há lista
                if cont_operadores == 1:
                    listanum.append(atual[pos_mais + 1:])
                # Entra aqui nesta situação 10+15+16 só existem dois + e com esta condição consigu,
                # Com que adicione o número entre o primeiro mais e o último + seja adicionado há lista
                elif cont_operadores == 2:
                    listanum.append(atual[pos_mais + 1:lista_pos_operadores[-1]])
            # Senão se a posição de o último + for igual ao último valor de lista_pos_operadores
            # adiciona dessa posição (pos_mais) até ao fim
            elif pos_mais == lista_pos_operadores[-1]:
                listanum.append(atual[pos_mais + 1:])
            # Senão se a posição do + for maior que a primeira posição e menor que a ultima posição ou seja são
            # as posições entre a primeira e última posições
            elif atual.index('+') < pos_mais < lista_pos_operadores[-1]:
                # Entra aqui nesta situação 10+15+16+13 quando existem tres +
                if cont_operadores == 3:
                    # Adicona o número há direita do primeiro +
                    listanum.append(atual[atual.index('+') + 1:pos_mais])
                    # Adiciona o número há esquerda do último +
                    listanum.append(atual[pos_mais + 1:lista_pos_operadores[-1]])
                elif cont_operadores >= 4:
                    lista_pos_operadores_entre_primeiromais_ultimomais.append(pos_mais)
                    cont_operadores_entre_primeiromais_ultimomais += 1
        if cont_operadores_entre_primeiromais_ultimomais == len(lista_pos_operadores_entre_primeiromais_ultimomais):
            pos_mais_seguinte = 0
            print(len(lista_pos_operadores_entre_primeiromais_ultimomais))
            for pos in range(len(lista_pos_operadores_entre_primeiromais_ultimomais)):
                print(pos)
                pos_mais_seguinte += 1
                if pos <= len(lista_pos_operadores_entre_primeiromais_ultimomais) - 2:
                    listanum.append(atual[lista_pos_operadores_entre_primeiromais_ultimomais[pos]:lista_pos_operadores_entre_primeiromais_ultimomais[pos + pos_mais_seguinte]])
                elif pos == len(lista_pos_operadores_entre_primeiromais_ultimomais) - 1:
                    listanum.append(atual[lista_pos_operadores_entre_primeiromais_ultimomais[pos]:lista_pos_operadores[-1]])
                if pos_mais_seguinte == 1:
                    pos_mais_seguinte = 0
    print(listanum)
    print(lista_pos_operadores_entre_primeiromais_ultimomais)
    print(lista_pos_operadores)


def res():
    ecra.insert(0, '=')
    atual = str(ecra.get())
    resultado = 0
    valor_i = '='
    for a in valor_i:
        atual = atual.replace(a, '')
    listanumeros_separados(atual)
    ecra.delete(0, END)
    # for num in listanum:
    #     num = int(num)
    #     resultado += num
    # ecra.insert(0, resultado)
    # listanum.clear()
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
