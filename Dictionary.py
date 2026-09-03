Users = {1:"Andrey", 2:"Vlad", 3:"Dima"}
Users.update({3:"Alexey", 4:"Max"})
Users[2] = "Vladislav"
print(Users)


Users_Info = {
    "Andrey": {"Age": 16, "Email": "Andrey@gmail.com"},
    "Vlad": {"Age": 15, "Email": "Vlad@mail.ru"}
}

for key in Users_Info:
    print("Name:", key, "\n", " Age:", Users_Info[key]["Age"], "\n", " Email:", Users_Info[key]["Email"])