while True:
    print("""
    dime, ¿que quieres hacer?
    1)sumar los dos numeros 
    2)restar los dos numeros
    3)multiplicar los dos 
    4)sacar promedio
    5)apagar calculadora 
    """)
    opcion= int(input("elige una opcion:"))

    if opcion ==1:
        n1 = int(input("introduce tu primer numero:"))
        n2 = int(input("introduce tu segundo numero:"))

        sum=n1+n2
        print("el resultado es:",sum)
    elif opcion ==2:
        r1 = int(input("introduce tu primer numero:"))
        r2 = int(input("introduce tu primer numero:"))
        resta=n1-r2
        print("el resultado es:",resta)
    elif opcion == 3:
        m1 = int(input("introduce tu primer numero:"))
        m2 = int(input("introduce tu segundo numero:"))

        multi=m1*m2
        print("el resultado es:",multi)
    elif opcion == 4:
        p1 = float(input("introduce tu primera nota:"))
        p2 = float(input("introduce tu segunda nota:"))
        p3 = float(input("ingrese tu tercera nota:"))

        prom =(p1+p2+p3)/3
        if prom>6:
            print("aprovaste con una exelente nota tu promedio es:",prom)
        elif prom>=4:
            print("aprovaste apenas con un promedio de:",prom)
        elif prom<3.9:
            print("reprovaste",prom)
    elif opcion == 5:
        print("hasta pronto")
        break
    else:
        print("opcion incorrecta")



