#juego piedra papel o tijera
import random

options = ('piedra', 'papel', 'tijera')
computerWins = 0
userWins = 0
rounds = 1
while True:
  print('* ' *10)
  print('ROUND' , rounds)
  print('* ' *10)
  print('computer wins: ', computerWins)
  print('User Wins: ', userWins)
  
  user_option = input('piedra, papel o tijera: ')
  user_option = user_option.lower()
  rounds+=1

  #validar si usuario ingresa una opcion no valida
  if not user_option in options:
    print('Opcion no valida.')
    continue
  #random de opciones
  computerOption = random.choice(options)
  print('user elije => ', user_option)
  
  print('computer elije => ', computerOption)
  
  if user_option == computerOption:
    print('EMPATE')
  elif user_option == 'piedra':
    if computerOption == 'tijera':
      print('Piedra gana a tijera')
      print('User gana')
      print()
      userWins +=1;
    else:
      print('Papel gana a piedra')
      print('Computer gana')
      print()
      computerWins +=1
  elif user_option == 'papel':
    if computerOption == 'piedra':
      print('Papel gana a piedra')
      print('User gana')
      print()
      userWins+=1
    else:
      print('Tijera gana a papel')
      print('Computer gana')
      print()
      computerWins+=1
  elif user_option == 'tijera':
    if computerOption == 'papel':
      print('tijera gana a papel')
      print('User gana')
      print()
      userWins+=1
    else:
      print('Piedra gana a tijera')
      print('Computer gana')
      print()
      computerWins+=1
#Definir ganador y romper ciclo
  if computerWins == 2:
    print('El Ganador es el Computer!')
    print(f'Sus victorias son: {computerWins} ')
    break
  if userWins == 2:
    print('El Ganador es el User')
    print(f'Sus victorias son: {userWins} ')
    break