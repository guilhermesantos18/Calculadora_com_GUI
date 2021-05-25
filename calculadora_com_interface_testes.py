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
    atual = str(ecra.get())
    ecra.delete(0, END)
    ecra.insert(0, atual + adicao)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def digitar_s(subtracao):
    atual = str(ecra.get())
    ecra.delete(0, END)
    ecra.insert(0, atual + subtracao)
    # Verificar se foi atingido o número máximo de numeros no ecra
    # Se isso acontecer apaga tudo
    if len(ecra.get()) >= 25:
        ecra.delete(0, END)


def listanumeros_separados_para_um_operador(atual):
    # Verificar as posições de os operadores e adicionar os números
    # entre os operadores e guarda-los numa lista
    cont_operadores_mais = cont_operadores_menos = 0
    print(atual)
    lista_pos_operadores = []
    # Pegar todas as posições do +
    for pos in range(0, len(atual)):
        # Pegar todas as posições do +
        if atual[pos] == '+':
            cont_operadores_mais += 1
            # Contador para ajudar na adição de os números há lista entre os +
        # Pegar todas as posições do -
        elif atual[pos] == '-':
            cont_operadores_menos += 1
        lista_pos_operadores.append(pos)
    # Entra aqui se só existir +
    if cont_operadores_mais >= 1 and cont_operadores_menos == 0:
        cont_operadores_entre_primeiromais_ultimomais = 0
        lista_pos_operadores_entre_primeiromais_ultimomais = []
        # Para cada posição dos operadores, vou verificar se a sua posição,
        # É igual á posição do primeiro operador, se a posição é igual há,
        # de o último operador e se a posição dos restantes operadores está entre,
        # a primeira posição e a última posição
        for pos_mais in lista_pos_operadores:
            if pos_mais == atual.index('+'):
                listanum.append(atual[:pos_mais])
                # Entra aqui nesta situação 10+15 só existe um + e com esta condição consigu,
                # Com que adicione o número há direita do primeiro + seja adicionado há lista
                if cont_operadores_mais == 1:
                    listanum.append(atual[pos_mais + 1:])
                # Entra aqui nesta situação 10+15+16 só existem dois + e com esta condição consigu,
                # Com que adicione o número entre o primeiro mais e o último + seja adicionado há lista
                elif cont_operadores_mais == 2:
                    listanum.append(atual[pos_mais + 1:lista_pos_operadores[-1]])
            # Senão se a posição do + for maior que a primeira posição e menor que a ultima posição ou seja são
            # as posições entre a primeira e última posições
            elif atual.index('+') < pos_mais < lista_pos_operadores[-1]:
                # Entra aqui nesta situação 10+15+16+13 quando existem tres +
                if cont_operadores_mais == 3:
                    # Adicona o número há direita do primeiro +
                    listanum.append(atual[atual.index('+') + 1:pos_mais])
                    # Adiciona o número há esquerda do último +
                    listanum.append(atual[pos_mais + 1:lista_pos_operadores[-1]])
                elif cont_operadores_mais >= 4:
                    lista_pos_operadores_entre_primeiromais_ultimomais.append(pos_mais)
                    cont_operadores_entre_primeiromais_ultimomais += 1
        if cont_operadores_entre_primeiromais_ultimomais == len(lista_pos_operadores_entre_primeiromais_ultimomais):
            for pos in range(len(lista_pos_operadores_entre_primeiromais_ultimomais)):
                if lista_pos_operadores_entre_primeiromais_ultimomais[pos] == lista_pos_operadores[1]:
                    listanum.append(atual[atual.index('+') + 1:lista_pos_operadores_entre_primeiromais_ultimomais[pos]])
                if pos <= len(lista_pos_operadores_entre_primeiromais_ultimomais) - 2:
                    listanum.append(atual[lista_pos_operadores_entre_primeiromais_ultimomais[pos] + 1:lista_pos_operadores_entre_primeiromais_ultimomais[pos + 1]])
                elif pos == len(lista_pos_operadores_entre_primeiromais_ultimomais) - 1:
                    listanum.append(atual[lista_pos_operadores_entre_primeiromais_ultimomais[pos] + 1:lista_pos_operadores[-1]])
        if cont_operadores_mais >= 2:
            for pos_mais in lista_pos_operadores:
                # Se a posição de o último + for igual ao último valor de lista_pos_operadores
                # adiciona dessa posição (pos_mais) até ao fim
                if pos_mais == lista_pos_operadores[-1]:
                    listanum.append(atual[pos_mais + 1:])
    # Entra aqui se só existir -
    if cont_operadores_menos >= 1 and cont_operadores_mais == 0:
        cont_operadores_entre_primeiromenos_ultimomenos = 0
        lista_pos_operadores_entre_primeiromenos_ultimomenos = []
        # Para cada posição dos operadores, vou verificar se a sua posição,
        # É igual á posição do primeiro operador, se a posição é igual há,
        # de o último operador e se a posição dos restantes operadores está entre,
        # a primeira posição e a última posição
        for pos_menos in lista_pos_operadores:
            if pos_menos == atual.index('-'):
                listanum.append(atual[:pos_menos])
                # Entra aqui nesta situação 10-15 só existe um - e com esta condição consigu,
                # Com que adicione o número há direita do primeiro - seja adicionado há lista
                if cont_operadores_menos == 1:
                    listanum.append(atual[pos_menos + 1:])
                # Entra aqui nesta situação 10-15-16 só existem dois - e com esta condição consigu,
                # Com que adicione o número entre o primeiro mais e o último - seja adicionado há lista
                elif cont_operadores_menos == 2:
                    listanum.append(atual[pos_menos + 1:lista_pos_operadores[-1]])
            # Senão se a posição do - for maior que a primeira posição e menor que a ultima posição ou seja são
            # as posições entre a primeira e última posições
            elif atual.index('-') < pos_menos < lista_pos_operadores[-1]:
                # Entra aqui nesta situação 10-15-16-13 quando existem tres -
                if cont_operadores_menos == 3:
                    # Adicona o número há direita do primeiro -
                    listanum.append(atual[atual.index('-') + 1:pos_menos])
                    # Adiciona o número há esquerda do último -
                    listanum.append(atual[pos_menos + 1:lista_pos_operadores[-1]])
                elif cont_operadores_menos >= 4:
                    lista_pos_operadores_entre_primeiromenos_ultimomenos.append(pos_menos)
                    cont_operadores_entre_primeiromenos_ultimomenos += 1
        if cont_operadores_entre_primeiromenos_ultimomenos == len(lista_pos_operadores_entre_primeiromenos_ultimomenos):
            for pos in range(len(lista_pos_operadores_entre_primeiromenos_ultimomenos)):
                if lista_pos_operadores_entre_primeiromenos_ultimomenos[pos] == lista_pos_operadores[1]:
                    listanum.append(atual[atual.index('-') + 1:lista_pos_operadores_entre_primeiromenos_ultimomenos[pos]])
                if pos <= len(lista_pos_operadores_entre_primeiromenos_ultimomenos) - 2:
                    listanum.append(atual[lista_pos_operadores_entre_primeiromenos_ultimomenos[pos] + 1:
                                          lista_pos_operadores_entre_primeiromenos_ultimomenos[pos + 1]])
                elif pos == len(lista_pos_operadores_entre_primeiromenos_ultimomenos) - 1:
                    listanum.append(
                        atual[lista_pos_operadores_entre_primeiromenos_ultimomenos[pos] + 1:lista_pos_operadores[-1]])
        if cont_operadores_menos >= 2:
            for pos_mais in lista_pos_operadores:
                # Senão se a posição de o último - for igual ao último valor de lista_pos_operadores
                # adiciona dessa posição (pos_mais) até ao fim
                if pos_mais == lista_pos_operadores[-1]:
                    listanum.append(atual[pos_mais + 1:])
    print(listanum)


# Verificar operadores para que quando o usuário digitar por exemplo,
# 3+-* ou seja digitar mais de 1 operador para realizar a conta aparecer
# no ecra 'Número Inválido'
def verificar_operadores(atual):
    lista_pos_operadores = []
    for pos in range(0, len(atual)):
        if atual[pos] == '-' or atual[pos] == '+' or atual[pos] == '*' or atual[pos] == '/':
            lista_pos_operadores.append(pos)
    print(lista_pos_operadores)
    for pos_operadores in lista_pos_operadores[:-1]:
        if atual[pos_operadores + 1] == '+' or atual[pos_operadores + 1] == '-':
            ecra.insert(0, 'Número Inválido')


def res():
    ecra.insert(0, '=')
    atual = str(ecra.get())
    resultado = 0
    valor_i = '='
    for a in valor_i:
        atual = atual.replace(a, '')

    listanumeros_separados_para_um_operador(atual)
    ecra.delete(0, END)
    verificar_operadores(atual)
    if '+' in atual:
        for num in listanum:
            num = int(num)
            resultado += num
    elif '-' in atual:
        resultado = int(listanum[0])
        for num in listanum[1:]:
            num = int(num)
            resultado -= num
    ecra.insert(0, resultado)

    listanum.clear()
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
btn_div = tk.Button(text='/', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_x = tk.Button(text='x', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font)
btn_s = tk.Button(text='-', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font, command=lambda: digitar_s('-'))
btn_a = tk.Button(text='+', width=5, relief=tk.GROOVE, borderwidth=2, bg='#C4CBCA', font=font, command=lambda: digitar_a('+'))
btn_i = tk.Button(text='=', width=5, relief=tk.GROOVE, borderwidth=2, bg='#66C4F2', font=font, command=res)

# Adicionar icon ao botão delete
icon_delete = tk.PhotoImage(
    file='C:\Programação e Projetos\Linguagens que mais uso e trabalho\Python\Tkinter\Calculadora_com_GUI\Icon\outline_backspace_black_24dp.gif')

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
