"""
Ejercicio: Gestión de una lista de tareas

Imagina que estás creando una aplicación para gestionar tareas pendientes. 
Necesitas crear un programa en Python que te permita realizar las siguientes acciones:

    Crear una lista vacía para almacenar las tareas.
    Añadir nuevas tareas a la lista.
    Mostrar la lista de tareas actual.
    Marcar una tarea como completada (eliminarla de la lista).
    Ordenar la lista de tareas alfabéticamente.
"""

task_lists = [' Task 1', 'Task 2']


# new task on last items
new_task = input("Please, describe the new task: ")
task_lists.append(new_task)
print(f"New task, '{new_task}', has been included.")
print('\n' + str(task_lists) )

# Printing tasks list
print('\n' + str(task_lists) )

# Ordering alphabetically
# print('\nAlphabetically sorted task list: ' + str(task_lists.sorted()) )

# Removing a task using non-zero index to non-zero
print('\n' + str(task_lists) )
task_index = input('\n' + 'Select a task index to be removed: ')
task_lists.pop({int(task_index) - 1})


# def addingTasks(task_list):
#     for _ in range():
#         task_lists.insert({index}, '{task}')

# print(task_lists)

# del task_lists[-1]
# print(task_lists)

# task_lists.append('f')
# print(task_lists)