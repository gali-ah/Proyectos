from StackHanoi import Stack

print("\n¡Vamos a jugar a las torres de Hanoi!")

#Crear las pilas
stacks = []  # Lista vacía para almacenar las pilas

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# Añadir las pilas a la lista
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Configurar el juego
num_disks = int(input("¿Con cuántos discos quieres jugar? "))

# Asegurarse de que el número de discos sea al menos 3
while num_disks < 3:
    num_disks = int(input("Ingresa un número mayor o igual a 3\n"))

# Agregar discos a la pila izquierda
for i in range(num_disks, 0, -1):
    left_stack.push(i)

# Calcular la cantidad de movimientos óptimos
num_optimal_moves = 2 ** num_disks - 1

# Imprimir el número de movimientos óptimos
print("\nLo más rápido que puedes resolver este juego es en {0} movimientos".format(num_optimal_moves))

# Obtener entrada del usuario

def get_input():
    choices = ['L', 'M', 'R']  # Letras iniciales de las pilas

    while True:
        # Imprimir las opciones
        for i in range(len(stacks)):
            name = stacks[i].get_name()  # Obtener el nombre de la pila
            letter = choices[i]  # Obtener la letra correspondiente
            print(f"Escribe {letter} para {name}")

        # Obtener la entrada del usuario
        user_input = input("").strip().upper()  # Leer la entrada y convertirla a mayúsculas

        # Verificar si la entrada es válida
        if user_input in choices:
            # Encontrar y devolver la pila correspondiente
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]  # Devolver la pila seleccionada
        else:
            print("Entrada no válida. Intenta de nuevo.")

# Jugando el juego

num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Pilas actuales...")
    for stack in stacks:
        stack.print_items()  # Imprimir los elementos de cada pila

    while True:
        print("\n¿Desde qué pila quieres mover un disco?\n")
        from_stack = get_input()  # Obtener la pila de origen

        print("\n¿A qué pila quieres mover el disco?\n")
        to_stack = get_input()  # Obtener la pila de destino

        # Verificar si el movimiento es válido
        if from_stack.get_size() == 0:
            print("\n\nMovimiento no válido. Inténtalo de nuevo.")
        elif (to_stack.get_size() == 0 or 
              from_stack.peek() < to_stack.peek()):
            # Mover el disco
            disk = from_stack.pop()  # Extraer el disco de from_stack
            to_stack.push(disk)  # Empujar el disco a to_stack
            num_user_moves += 1  # Incrementar el contador de movimientos
            break  # Salir del bucle interno
        else:
            print("\n\nMovimiento no válido. Inténtalo de nuevo.")

# Al finalizar el juego
print(f"\n\nCompletaste el juego en {num_user_moves} movimientos y el número óptimo de movimientos es {num_optimal_moves}.")