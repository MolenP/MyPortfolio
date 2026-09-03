import random
import time

Registered_Users = {"m":{"Password":"1"}}
Cards = []

def Login():
    while True:
        try:
            act = int(input("Enter your act(1 - Login; 2 - Register; 0 - Exit):"))
        except:
            print("Invalid input")
            continue

        if act == 1:
            #Login---------------------------------------------------

            while True:
                print("For cancel you need to type '0'")
                login = input("Enter your login:")

                if not login.isascii():
                    print("ERROR: Your login have an unsupported characters, try again")
                    continue

                if login == "0":
                    break

                #Password---------------------------------------------------
                
                password = input("Enter your password:")

                if not password.isascii():
                    print("ERROR: Your password have an unsupported characters, try again")
                    continue

                if login in Registered_Users and Registered_Users[login]["Password"] == password:
                    print("Log in Succes")
                    return login
                else:
                    print("Invalid Login or Password")
                    continue
            continue
        

        elif act == 2:
            #Login--------------------------------------------------- 

            while True:
                print("For cancel you need to type '0'")
                login = input("Enter your login:")

                if not login.isascii():
                    print("ERROR: Your login have an unsupported characters, try again")
                    continue
                
                if login in Registered_Users:
                    print("ERROR: Your login is already used, try again")
                    continue

                if login == "0":
                    break

                #Password---------------------------------------------------

                while True:
                    print("For cancel you need to type '0'")
                    password = input("Enter your password:")

                    if password == "0":
                        break

                    if not password.isascii():
                        print("ERROR: Your password have an unsupported characters, try again")
                        continue

                    if len(password) < 5:
                        print("ERROR: Your password must be longer than 4 symbols")
                        continue

                    print("Register is succes")
                    Registered_Users.update({login:{"Password":password}})
                    break
                break
            continue
        elif act == 0:
            exit()
        else:
            print("Invalid input")
            continue


user = Login()
Questions_count = 0
for item in Cards:
    if item["Owner"] == user:
        Questions_count += 1

while True:
    try:
        act2 = int(input(f"Hello, {user}, what do you want?(1-Cards; 2-Quiz; 0-Log Out):")) 
    except:
        print("Invalid input")
        continue

    if act2 == 0:
        user = Login()
        Questions_count = 0
        for item in Cards:
            if item["Owner"] == user:
                Questions_count += 1
        continue

    elif act2 == 1:
        try:
            cards_act = int(input("Select your act(1 - Create new card; 2 - Delete card; 3 - Check list of cards):"))
        except:
            print("Invalid input")
            continue

        if cards_act == 1:
            new_card_question = input("Enter your new question:")
            Questions_count += 1
            Cards.append({
                "Number":Questions_count,
                "Owner":user,
                "Question":new_card_question,
                "RightAnswer":"",
                "WrongAnswer":[],
                "Answers":[],
                "AnswersCount":0
            })
            
            while True:
                try:
                    new_card_answers_count = int(input("How many answers do you want?(2-4):"))
                except:
                    print("ERROR: Invalid input")
                    continue

                if new_card_answers_count > 4:
                    print("ERROR: You cant create more than 4 answers")
                    continue

                if new_card_answers_count < 2:
                    print("ERROR: You cant create less than 2 answers")
                    continue
                
                for i in range(new_card_answers_count):
                    if i == 0:
                        new_card_right_answer = input(f"Enter right answer:")
                        for item in Cards:
                            if item["Number"] == Questions_count:
                                item["RightAnswer"] = new_card_right_answer
                                item["Answers"].append(new_card_right_answer)

                    if i >= 1:
                        new_card_wrong_answer = input(f"Enter {i} wrong answer:")
                        for item in Cards:
                            if item["Number"] == Questions_count:
                                item["WrongAnswer"].append(new_card_wrong_answer)
                                item["Answers"].append(new_card_wrong_answer)
                                item["AnswersCount"] = new_card_answers_count
                
                print("Card created succesful")
                break
            continue
        
        elif cards_act == 2:
            users_Questions = []
            for item in Cards:
                if item["Owner"] == user:
                    users_Questions.append(item)

            if len(users_Questions) > 0:
                for item in users_Questions:
                    print("-------------")
                    for key, value in item.items():
                        print(f"{key}:{value}")
                while True:
                    try:
                        choice = int(input("Select number of question that you want to delete:"))
                        break
                    except:
                        print("ERROR: Invalid input")

                isFound = False        
                for item in users_Questions:
                    if item["Number"] == choice:
                        Cards.remove(item)
                        print("Card deleted")
                        Questions_count -= 1
                        isFound = True
                
                if isFound == False:
                    print("ERROR: The number of question you wrote was not found")

            else:
                print("ERROR: No card has been found")
                continue

        elif cards_act == 3:
            users_Questions = []
            for item in Cards:
                if item["Owner"] == user:
                    users_Questions.append(item)

            if len(users_Questions) > 0:
                for item in users_Questions:
                    print("-------------")
                    for key, value in item.items():
                        print(f"{key}:{value}") 
            else:
                print("ERROR:No cards has been found")

             

    elif act2 == 2:
        users_Questions = []
        for item in Cards:
            if item["Owner"] == user:
                users_Questions.append(item)

        if len(users_Questions) > 0:
            while True:
                print("Welcome to Quiz! Answer the questions. \nBe aware, you have a limited time, 30 seconds per question. \nYou should write number of answer")
                try:
                    count = int(input("How many questions do you want:"))
                    break
                except:
                    print("Invalid input")

            if count > len(users_Questions):
                print("ERROR: You don't have that many questions")
                continue
            elif count <= 0:
                print("ERROR: The count of questions can't be less than 0 or be 0")
                continue
            else:
                Points = 0
                questions = random.sample(users_Questions, count)
                for i in range(count):
                    start_time = time.time()
                    print("-------------------------")
                    print(f"#{i + 1}. {questions[i]['Question']}")
                    answers = random.sample(questions[i]["Answers"], questions[i]["AnswersCount"])
                    
                    for ii in range(questions[i]["AnswersCount"]):
                        answer_number = ii + 1
                        print(f"{answer_number}. {answers[ii]}")
                    while True:
                        while True:
                            try:
                                Otvet = int(input("Your Answer:"))
                                break
                            except:
                                print("ERROR: Invalid input")
                                continue
                        end_time = time.time()
                        spent_time = end_time - start_time
                        if spent_time > 30:
                            print(f"Time's up! The correct answer is << {questions[i]['RightAnswer']} >>, you don't get a point:(")
                            continue
                        if Otvet < 1 or Otvet > len(answers):
                            print(f"Answer number can be only 1-{questions[i]["AnswersCount"]}")
                            continue
                        break
                    if answers[Otvet - 1] == questions[i]["RightAnswer"]:
                        Points += 1
                        print("Correct Answer!")
                    else:
                        print("Incorrect Answer")
                print(f"Your score: {Points}/{count}")
        else:
            print("ERROR: No cards has been found")
            continue