#$implementar una calculadora que pida dos numeros y una operacion, vamos a usar la figura de swich... case y luego

num_1 = float(input("primer numero a consultar: "))

num_2 = float(input("que operacion vas hacer? (+,-,/,*): "))

#como asi switch y case 
# switch y case es una forma diferente de escribir, donde se evalua un parametro, booleano, y bse va a direccionar inmediatamente segun los casos definidos

match operador:
    case "+":
        print("resultado", num_1 + num_2)
    case "-":
        print("resultado", num_1 - num_2)
    case "/":
        print("resultado", num_1 * num_2)
    case "/":
        if num_2 != 0:
            print("resultado", num_1 / num_2)
        else:
            print("resultado no valido")
    case _:
        print("resultado no valido")