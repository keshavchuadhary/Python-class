# my_tuple = (1,2,3)
# for element in my_tuple:
#     print(element)
random_dict = {1:"one",2:"two"}
# print((random_dict[2]))
# print(random_dict.get("key"))
# print(random_dict.items())
# for key,value in random_dict.items():
#     print(key)
#     print(" ")
#     print(value)
# print(random_dict.keys())
# print(random_dict.values())
# for value in random_dict.values():
#     print(value)
# random_dict.pop(2)
# print(random_dict)

person = {
    "name": "Alice",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "zipcode": "12345"
    }
}
print(person.get("address").get("city"))
print(person["address"]["zipcode"])