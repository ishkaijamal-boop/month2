# 1-2. Создаем класс Person с методом introduce()
# class Person:
#     def __init__(self, name, birth_date, profession):
#         self.name = name
#         self.birth_date = birth_date
#         self.profession = profession
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю: {self.profession}.")
#
#
# # 3-5. Класс-наследник Classmate с уникальным атрибутом group_name и переопределенным introduce()
# class Classmate(Person):
#     def __init__(self, name, birth_date,
# profession, group_name):
#         super().__init__(name, birth_date,
# profession)
#         self.group_name = group_name
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, я одногруппник из группы {self.group_name}, я родился {self.birth_date}, работаю: {self.profession}.")
#
#
# # 3-5. Класс-наследник Friend с уникальным атрибутом hobby и переопределенным introduce()
# class Friend(Person):
#     def __init__(self, name, birth_date,
# profession, hobby):
#         super().__init__(name, birth_date,
# profession)
#         self.hobby = hobby
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name}, мое хобби - {self.hobby}, я родился {self.birth_date}, работаю: {self.profession}.")
#
#
# # --- ДОП ЗАДАНИЕ 2 ---
# # Класс BestFriend, который наследуется от Friend
# class BestFriend(Friend):
#     def __init__(self, name, birth_date, profession, hobby, shared_memory):
#         super().__init__(name, birth_date, profession, hobby)
#         self.shared_memory = shared_memory
#
#     def introduce(self):
#         # Вызываем метод родителя (Friend)
#         super().introduce()
#         # Допечатываем уникальную информацию
#         print(f"А еще у нас есть классное общее воспоминание: {self.shared_memory}!")
#
#
# print("--- ОСНОВНОЕ ЗАДАНИЕ (п. 6-7) ---")
# # 6. Создаем объекты
# classmate1 = Classmate("Бектур",
# "5.12.2000", "программистом", "Python-23")
# classmate2 = Classmate("Айгерим",
# "10.08.2001", "дизайнером", "UX/UI-12")
#
# friend1 = Friend("Алмаз",
# "2.05.1999", "аналитиком", "игра на гитаре")
# friend2 = Friend("Тимур",
# "14.11.2002", "маркетологом", "футбол")
#
# # 7. Вызываем методы
# classmate1.introduce()
# classmate2.introduce()
# friend1.introduce()
# friend2.introduce()
#
#
# print("\n--- ДОП ЗАДАНИЕ 1 (Список и цикл) ---")
# # Создаем разные объекты
# person1 = Person("Нурлан", "1.01.1995",
# "менеджером")
# # Помещаем всех в один список
# people_list = [person1, classmate1, classmate2, friend1, friend2]
#
# # Проходимся циклом и вызываем метод introduce()
# for person in people_list:
#     person.introduce()
#
#
# print("\n--- ДОП ЗАДАНИЕ 2 (BestFriend) ---")
# # Проверяем работу класса BestFriend
# best_friend = BestFriend("Максим", "20.07.1998", "IT-специалистом", "шахматы", "поездка в горы в прошлом году")
# best_friend.introduce()
