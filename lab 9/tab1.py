
# Лабораторная работа №9
# Тема: Связные списки (Linked Lists)


# Задача 1. Создание узла
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Задачи 2–10. Класс связного списка
class LinkedList:
    def __init__(self):
        self.head = None

    # Задача 3. Добавление элемента в начало
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Задача 4. Добавление элемента в конец
    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Задача 5. Вывод всех элементов
    def display(self):
        current = self.head

        if current is None:
            print("Список пуст")
            return

        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next

        print()

    # Задача 6. Поиск элемента
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False

    # Задача 7. Удаление первого элемента
    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("Список пуст, удалять нечего")

    # Задача 8. Подсчёт количества элементов
    def count(self):
        current = self.head
        total = 0

        while current is not None:
            total += 1
            current = current.next

        return total

    # Задача 10. Разворот связного списка
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


# Задача 1. Создание и связывание нескольких узлов
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print("Задача 1. Связанные узлы:")
current = node1
while current is not None:
    print(current.data, end=" ")
    current = current.next
print("\n")


# Задача 2. Создание пустого списка
linked_list = LinkedList()
print("Задача 2. Создан пустой список")


# Задача 3. Добавление в начало
linked_list.add_first(10)
linked_list.add_first(20)
linked_list.add_first(30)

print("\nЗадача 3. Добавление в начало:")
linked_list.display()  # 30 -> 20 -> 10


# Задача 4. Добавление в конец
linked_list.add_last(40)
linked_list.add_last(50)

print("\nЗадача 4. Добавление в конец:")
linked_list.display()  # 30 -> 20 -> 10 -> 40 -> 50


# Задача 5. Вывод списка
print("\nЗадача 5. Элементы списка:")
linked_list.display()


# Задача 6. Поиск элемента
print("\nЗадача 6. Поиск элемента:")
number = 20

if linked_list.search(number):
    print(f"Элемент {number} найден")
else:
    print(f"Элемент {number} не найден")

print("Поиск числа 100:", linked_list.search(100))


# Задача 7. Удаление первого элемента
print("\nЗадача 7. Удаление первого элемента:")
print("До удаления:")
linked_list.display()

linked_list.remove_first()

print("После удаления:")
linked_list.display()


# Задача 8. Подсчёт количества элементов
print("\nЗадача 8. Количество элементов:")
print("Количество элементов:", linked_list.count())


# Задача 9. Ввод пяти чисел от пользователя
print("\nЗадача 9. Введите 5 чисел:")
user_list = LinkedList()

for i in range(5):
    number = int(input(f"Введите число {i + 1}: "))
    user_list.add_last(number)

print("Ваш связный список:")
user_list.display()


# Задача 10. Разворот связного списка
print("\nЗадача 10. Разворот списка:")
print("Исходный список:")
user_list.display()

user_list.reverse()

print("Список после разворота:")
user_list.display()
