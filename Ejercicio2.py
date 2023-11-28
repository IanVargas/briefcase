"""
Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.

"""
secret_number = 8

def guess_number(number) :

   if number == secret_number: 
      print("Congrats!!, secret number was", secret_number)

      
   else: 
      guess_number(int(input("Wrong number!!!, Try again:")))


number = int(input("Numero"))
guess_number(number) 