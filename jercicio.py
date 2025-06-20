num_1 = float(input("primer numero a consultar: "))

num_2 = float(input("que operacion vas hacer? (+,-,/,*): "))

operador = input("que operacion vas a hacer? (+,-,/,*): ")

if operador == "+":
    print("resultado", num_1 + num_2)
elif operador == "-":
    print("resultado", num_1 - num_2)
elif operador == "*":
    print("resultado", num_1 * num_2)
elif operador == "/":
    if num_1 != 0:|
        print("resultado", num_1 / num_2)
    else:
        print("resuiltado no valido")