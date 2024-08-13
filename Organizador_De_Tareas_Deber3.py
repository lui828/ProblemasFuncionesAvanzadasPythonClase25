tareas = []

def agregar_tarea(tarea):
    tareas.append({"tarea": tarea, "completada": False})

def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
        return
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['tarea']} - {estado}")

def completar_tarea(numero_tarea):
    if 0 < numero_tarea <= len(tareas):
        tareas[numero_tarea - 1]["completada"] = True
    else:
        print("Número de tarea no válido.")

def eliminar_tarea(numero_tarea):
    if 0 < numero_tarea <= len(tareas):
        tareas.pop(numero_tarea - 1)
        print("Tarea eliminada.")
    else:
        print("Número de tarea no válido.")

# Ejemplo de uso
while True:
    print("\n1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Escribe la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        mostrar_tareas()
        numero_tarea = int(input("Número de tarea a completar: "))
        completar_tarea(numero_tarea)
    elif opcion == "4":
        mostrar_tareas()
        numero_tarea = int(input("Número de tarea a eliminar: "))
        eliminar_tarea(numero_tarea)
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")