import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

answer_count = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}. {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["User Choice"] = user_choice
    if question["User Choice"] == question["correct answer"]:
        print("Correct Answer!")
        answer_count += 1
    else:
        print("Wrong Answer!")

for question in data:
    message = f"{index + 1}- Your answer: {question['User Choice']}, Correct answer: {question['correct answer']} "
    print(message)

print(f"{answer_count} / {len(data)}")
