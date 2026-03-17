
# class Animal:
#     def __init__(self, name, age):
#         self.__name = name      # приватный атрибут
#         self.__age = age        # приватный атрибут
#
# #геттер
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
# #сеттер
#     def set_name(self, name):
#         self.__name = name
#
#     def set_age(self, age):
#         self.__age = age
#
# #звуки
#     def make_sound(self):
#         print("Животное издает звук")
#
# #класс наследников Dog
# class Dog(Animal):
#     def make_sound(self):
#         print("Гав-гав")
#
#
# #класс наследников Gat
# class Cat(Animal):
#     def make_sound(self):
#         print("Мяу-мяу")
#
#
# #обьекты
# dog = Dog("Bobik", 3)
# kitty = Cat("Kisa", 1)
#
#
# dog.make_sound()
# kitty.make_sound()
#
# #работа с геттарами
# print(dog.get_name(), dog.get_age())
# print(kitty.get_name(), kitty.get_age())
#
#
# kitty.set_age(2)
#
# print(kitty.get_age())
