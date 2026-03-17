# class Contact:
#     def __init__(self, name, phone_number, contact_id):
#         self.id = contact_id
#         self.name = name
#         self.phone_number = phone_number
#
#     @classmethod
#     def validate_phone_number(cls, phone_number):
#         if phone_number.isdigit() and len(phone_number) == 10:
#             return True
#         return False
#
#
# class ContactList:
#     last_id = 0
#     all_contacts = []
#
#     @classmethod
#     def add_contact(cls, name, phone_number):
#         if Contact.validate_phone_number(phone_number):
#             cls.last_id += 1
#             contact = Contact(name, phone_number, cls.last_id)
#             cls.all_contacts.append(contact)
#             print(f"Контакт {name} добавлен. ID: {contact.id}")
#         else:
#             print("Неверный номер телефона")
#
#     @classmethod
#     def remove_contact(cls, contact_id):
#         for contact in cls.all_contacts:
#             if contact.id == contact_id:
#                 cls.all_contacts.remove(contact)
#                 print(f"Контакт с ID {contact_id} удалён")
#                 return
#         print("Контакт не найден")
#
#
# # пример использования
# print(ContactList.last_id)  # 0
#
# ContactList.add_contact("Ivan",
# "1234567890")
# ContactList.add_contact("Anna",
# "9876543210")
#
# print(ContactList.last_id)  # 2
#
# ContactList.remove_contact(1)