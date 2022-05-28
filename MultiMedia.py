import MMQuestions as mmq
from time import sleep

def main():
    print("--------------")
    print("-----QUIZ-----")
    print("--------------")
    print("Több választosnál a sorszámát kell megadni!")
    sleep(2)
    while True:
        quiz()
        again = input("Ujra? (Y/N)")
        if again.upper() == "N": break

def quiz():
    questions = mmq.questions
    for q in questions:
        if isinstance(q, mmq.Simple):
            handle_simple(q)
        elif isinstance(q, mmq.SingleChoice):
            handle_single_choice(q)
        elif isinstance(q, mmq.TrueFalse):
            handle_true_false(q)
        elif isinstance(q, mmq.Group):
            handle_group(q)

def handle_group(q):
    print(q.question)
    print(f"{q.group_name}-be kell beválogatni, a többi természetesen a másik csoportba kerülne CS-en")

    for text, ans in q.answers.items():
        answer = input(f"{text} (Y == true / N == false)")
        answer = "True" if answer.upper() == "Y" else "False"
        check_answer(answer, ans)


def handle_true_false(q):
    print(q.question)
    
    for text, ans in q.answers.items():
        answer = input(f"{text} (Y == true / N == false)")
        answer = "True" if answer.upper() == "Y" else "False"
        check_answer(answer, ans)

def handle_simple(q):
    answer = input(q.question + "\n")
    check_answer(answer, q.correct_answer)


def handle_single_choice(q):
    print(q.question)
    
    choices = "Answers: "
    for pos in range(len(q.answers)):
        choices += str(pos) + " - " + q.answers[pos]
        if pos != len(q.answers) - 1:
            choices += " | "

    answer = input(choices + "\n")
    check_answer(answer, q.correct_answer_position, q.answers[q.correct_answer_position])


def check_answer(answer, correct, toprint = None):
    if answer == str(correct):
        print("-----NOICE-----")
        for _ in range(5):
            print(".", end=" ")
            sleep(250 / 1000)
        print()
    
    else:
        if(toprint == None):
            print(f"Helyes: {correct}")
        else:
            print(f"Helyes: {toprint}")
        print("-----SADGE-----")
        
        for _ in range(5):
            print(".", end=" ")
            sleep(250 / 1000)
        print()


if __name__ == "__main__":
    main()