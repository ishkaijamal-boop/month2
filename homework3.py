# from datetime import datetime
#
#
# class Person:
#     def init(self, name, birth_date, occupation, higher_education):
#         self.name = name
#         self.__birth_date = birth_date
#         self.__occupation = occupation
#         self.__higher_education = higher_education
#
#     # property для профессии
#     @property
#     def occupation(self):
#         return self.__occupation
#
#     @occupation.setter
#     def occupation(self, value):
#         self.__occupation = value
#
#     # property для высшего образования
#     @property
#     def higher_education(self):
#         return self.__higher_education
#
#     @higher_education.setter
#     def higher_education(self, value):
#         self.__higher_education = value
#
#     # вычисление возраста
#     @property
#     def age(self):
#         birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
#         today = datetime.today()
#         age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
#         return age
#
#     def introduce(self):
#         edu = "есть" if self.higher_education else "нет"
#         print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. У меня {edu} высшее образование.")
#
#
# class Classmate(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, group):
#         super().init(name, birth_date, occupation, higher_education)
#         self.group = group
#
#     def introduce(self):
#         edu = "есть" if self.higher_education else "нет"
#         print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
#               f"Я учился с Айсулуу в группе {self.group}. У меня {edu} высшее образование.")
#
#
# class Friend(Person):
#     def __init__(self, name, birth_date, occupation, higher_education, hobby):
#         super().init(name, birth_date, occupation, higher_education)
#         self.hobby = hobby
#
#     def introduce(self):
#         edu = "есть" if self.higher_education else "нет"
#         print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
#               f"Мое хобби {self.hobby}. У меня {edu} высшее образование.")
#
#
# # создание объектов
# cl1 = Classmate("Иван", "20.02.2000",
# "студент", True, "11D")
# cl1.introduce()
#
# fr1 = Friend("Айбек", "20.02.2000",
# "студент", True, "футбол")
# fr1.introduce()
#
# print(fr1.age)