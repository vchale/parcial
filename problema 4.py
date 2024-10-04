contraseña = 'admin123'
dinero = 4000
intentos = 1

# Permitir hasta 3 intentos para ingresar correctamente la contraseña
while intentos < 4:
    nombre = input('Ingrese su Nombre: ')
    clave_ingresada = input('Ingrese su clave: ')
    
    if clave_ingresada == contraseña:
        # Si la contraseña es correcta, accede al cajero
        while True:
            print(f'\nHola {nombre},\nBienvenido al Cajero BCP!!')
            print('Operaciones en Línea:')
            print('1. Ver Saldo\n2. Retirar\n3. Depositar\n4. Salir')
            opcion = input('Ingrese una opción: ')
            
            if opcion == '1':
                # Mostrar saldo
                print(f'Saldo actual: S/ {dinero}')
                
            elif opcion == '2':
                # Retiro de dinero
                monto = int(input("Ingrese el monto que desea retirar: "))
                
                if monto % 10 != 0:
                    print("Este cajero solo puede entregar billetes de 10, 20, 50, 100 y 200. Ingrese un monto válido.")
                elif monto > dinero:
                    print(f"No tiene suficiente saldo. Su saldo actual es: S/ {dinero}")
                else:
                    # Lista de las denominaciones de billetes
                    billetes = [200, 100, 50, 20, 10]
                    monto_original = monto  # Guardamos el monto original antes de descontar
                    
                    print(f"Distribución de billetes para S/ {monto_original}:")
                    
                    # Ciclo que recorre cada billete, calcula cuántos de cada uno se pueden entregar
                    for billete in billetes:
                        cantidad_billetes = monto // billete
                        if cantidad_billetes > 0:
                            print(f"{cantidad_billetes} billete(s) de S/ {billete}")
                            monto -= cantidad_billetes * billete
                    
                    # Restar el monto retirado del saldo total
                    dinero -= monto_original
                    print(f"Su nuevo saldo es: S/ {dinero}")
                    
            elif opcion == '3':
                # Depósito de dinero
                monto = int(input("Ingrese el monto que desea depositar: "))
                
                if monto <= 0:
                    print("El monto ingresado no es válido.")
                else:
                    # Aumentar el saldo con el monto depositado
                    dinero += monto
                    print(f"Ha depositado: S/ {monto}")
                    print(f"Su nuevo saldo es: S/ {dinero}")
                    
            elif opcion == '4':
                # Salir del sistema
                print("Saliendo del sistema... ¡Gracias por usar el cajero BCP!")
                break
            else:
                print("Opción no válida, por favor seleccione una opción correcta.")
                
    else:
        print(f'Datos incorrectos. Intento Número {intentos}')
        intentos += 1

print('Demasiados intentos fallidos. Intente más tarde...')
