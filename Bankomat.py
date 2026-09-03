class Client:
    def __init__(self, client_id, name, pinCode, balance=0):
        self.client_id = client_id
        self.name = name
        self.PinCode = pinCode
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Сумма пополнения должна быть больше 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            
            print(f"Недостаточно средств. Баланс: {self.balance}")
        else:
            if amount <= 500:
                self.balance -= amount
                print(f"Снято {amount}. Текущий баланс: {self.balance}")
            else:
                print("Ошибка: Максимальный вывод средств должен быть не выше 500 единиц")

    def show_balance(self):
        print(f"Текущий баланс: {self.balance}")

class ATM:
    def __init__(self):
        self.clients = {}

    def add_client(self, client):
        self.clients[client.client_id] = client
        print(f"Клиент {client.name} добавлен.")

    def get_client(self, client_id):
        return self.clients.get(client_id, None)


def atm_interface():
    atm = ATM()
    while True:
        print("\n1. Добавить клиента\n2. Пополнить счет\n3. Снять деньги\n4. Показать баланс\n5. Сменить имя клиента\n6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            client_id = int(input("Введите ID клиента: "))
            name = input("Введите имя клиента: ")
            pinCode = int(input("Введите Пин-код клиента:"))
            balance = float(input("Введите начальный баланс: "))
            client = Client(client_id, name, pinCode, balance)
            atm.add_client(client)

        elif choice == "2":
            client_id = int(input("Введите ID клиента: "))
            amount = float(input("Введите сумму пополнения: "))
            client = atm.get_client(client_id)
            if client:
                pinCode = int(input("Введите Пин-код клиента:"))
                if pinCode == client.PinCode:
                    client.deposit(amount)
                else:
                    print("Неверный Пин-код")
            else:
                print("Клиент не найден.")
        
        elif choice == "3":
            client_id = int(input("Введите ID клиента: "))
            amount = float(input("Введите сумму снятия: "))
            client = atm.get_client(client_id)
            if client:
                pinCode = int(input("Введите Пин-код клиента:"))
                if pinCode == client.PinCode:
                    client.withdraw(amount)
                else:
                    print("Неверный Пин-код")
            else:
                print("Клиент не найден.")

        elif choice == "4":
            client_id = int(input("Введите ID клиента: "))
            client = atm.get_client(client_id)
            if client:
                pinCode = int(input("Введите Пин-код клиента:"))
                if pinCode == client.PinCode:
                    client.show_balance()
                else:
                    print("Неверный Пин-код")
            else:
                print("Клиент не найден.")

        elif choice == "5":
            client_id = int(input("Введите ID клиента: "))
            client = atm.get_client(client_id)
            if client:
                pinCode = int(input("Введите Пин-код клиента:"))
                if pinCode == client.PinCode:
                    newName = input("Выберите новое имя клиента:")
                    client.name = newName
                    print(f"Ваше новое имя: {client.name}")
                else:
                    print("Неверный Пин-код")
            else:
                print("Клиент не найден.")

        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

atm_interface()
