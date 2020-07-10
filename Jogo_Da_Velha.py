# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:59:11 2020

@author: gabri
"""
import random
import os

def display_board(board):
    print('Bem vindo ao jogo da velha!')
    for i in range(3):
        for j in range(3):
            print(board[i][j],end="")
        print()

def display_aux(ref_board):
    print()
    print("Posições a serem escolhidas:")
    for i in range(3):
        for j in range(3):
            print(ref_board[i][j],end="")
        print()
    print("-="*50)
    print()
    print("-="*50)

def player_input():
        x = int(input("Digite a posição que deseja marcar: "))
        return x

def place_marker(board, marker, position):
    if position >= 1 and position <= 3:
        i = 0
        j = position-1
    if position >= 4 and position <= 6:
        i = 1
        j = position-4
    if position >= 7 and position <= 9:
        i = 2
        j = position-7
        
    board[i][j]=board[i][j].replace(".",marker)

def win_check(board, mark):
    verificador = 0
    #Verificando as linhas:
    for i in range(3):
        for j in range(3):
            if board[i][j] == mark:
                verificador+=1
        if verificador == 3:
            return True
        verificador = 0
    #Verificando as colunas:
    for i in range(3):
        for j in range(3):
            if board[j][i] == mark:
                verificador+=1
        if verificador == 3:
            return True
        verificador = 0
    #Verificando a diagonal principal:
    for i in range(3):
        for j in range(3):
            if i==j:
                if board[i][j] == mark:
                    verificador+=1
    if verificador == 3:
        return True
    verificador = 0
    #Verificando a diagonal secundária:
    for i in range(3):
        for j in range(3):
            if j==2-i:
                if board[i][j] == mark:
                    verificador+=1
    if verificador == 3:
        return True
    verificador = 0
    return False

def choose_first():
    jogador = random.randint(1,3)
    if jogador==1:
        return "X"
    else:
        return "O"

def space_check(board, position):
    if position >= 1 and position <= 3:
        i = 0
        j = position-1
    if position >= 4 and position <= 6:
        i = 1
        j = position-4
    if position >= 7 and position <= 9:
        i = 2
        j = position-7
    if board[i][j] == ".":
        return True
    return False

def full_board_check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]==".":
                return False
    return True

def replay():
    question = input("Querem jogar novamente?['s' ou 'n']: ")
    if question == 's':
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    return False
    
def main():
    r = True
    
    while r:
        jogador1ganhou = False
        jogador2ganhou = False
        board=[[".",".","."],[".",".","."],[".",".","."]]
        ref_board=[["1","2","3"],["4","5","6"],["7","8","9"]]
        display_board(board)
        display_aux(ref_board)
        jogador1 = choose_first()
        
        if jogador1 == "X":
            jogador2 = "O"
        else:
            jogador2 = "X"
        game_on = True
        
        while game_on:
            ocupada = True
            while ocupada:
                print("Vez do jogador 1("+jogador1+"):")
                position = player_input()
            
            #Verifica se essa posição não está ocupada:
                desocupada = space_check(board, position)
                if desocupada:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    place_marker(board,jogador1,position)
                    display_board(board)
                    display_aux(ref_board)
                    ocupada = False
                else:
                    print()
                    print("Essa posição está ocupada. Tente novamente.")
            
            #Verifica se o jogador ganhou:
            ganhou = win_check(board, jogador1)
            if ganhou:
                #game_on = False
                jogador1ganhou = True
                break
            
            #Verifica se a placa está cheia:
            placacheia = full_board_check(board)
            if placacheia:
                #game_on = False
                break
            
            ocupada = True
            while ocupada:
                print("Vez do jogador 2("+jogador2+"):")
                position = player_input()
            
            #Verifica se essa posição não está ocupada:
                desocupada = space_check(board, position)
                if desocupada:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    place_marker(board,jogador2,position)
                    display_board(board)
                    display_aux(ref_board)
                    ocupada = False
                else:
                    print()
                    print("Essa posição está ocupada. Tente novamente.")
            
            #Verifica se o jogador ganhou:
            ganhou = win_check(board, jogador2)
            if ganhou:
                #game_on = False
                jogador2ganhou = True
                break
            
        if jogador1ganhou:
            print("O jogador 1 é o vencedor. Parabéns!")
        elif jogador2ganhou:
            print("O jogador 2 é o vencedor. Parabéns!")
        else:
            print("Vocês empataram!")
        
        r = replay()
main()