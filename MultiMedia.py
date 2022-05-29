import random
import copy
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
        if again.upper() != "Y": break

def quiz():
    questions = mmq.questions
    random.shuffle(questions)
    for q in questions:
        if isinstance(q, mmq.Simple):
            handle_simple(q)
        elif isinstance(q, mmq.SingleChoice):
            handle_single_choice(q)
        elif isinstance(q, mmq.TrueFalse):
            handle_true_false(q)
        elif isinstance(q, mmq.Group):
            handle_group(q)
        elif isinstance(q, mmq.Sequence):
            handle_sequence(q)
        elif isinstance(q, mmq.MultiGroup):
            pass
            # handle_multigroup(q)

def handle_multigroup(q):
    print(q.question)

    correct_answers = q.answers
    # keys to list
    remaining = [*copy.deepcopy(q.answers)]
    random.shuffle(remaining)
    
    if q.single_answer_per_group:
        for pos in range(len(q.groups)):
            choices = "Answers: "
            for apos in range(len(remaining)):
                choices += str(apos) + " - " + remaining[apos]
                if apos != len(remaining) - 1:
                    choices += " | "
            
            print(choices)
            answer = input(q.groups[pos] + " : ")
            try:
                pass
            except:
                pass



    else:
        pass


def handle_sequence(q):
    print(q.question)
    correct_order = q.answers
    random_ordered_answers = copy.deepcopy(q.answers)
    random.shuffle(random_ordered_answers)

    choices = "Answers: "
    for pos in range(len(random_ordered_answers)):
        choices += str(pos) + " - " + random_ordered_answers[pos]
        if pos != len(q.answers) - 1:
            choices += " | "

    print(choices)
    answer_list = input("A válaszokhoz tartozó számokat szóközzel elválasztva írd be!").split(" ")
    answers_num = 0
    answers = []
    for pos in range(len(answer_list)):
        # these are strings, so it will work on '0' as well
        if not answer_list[pos]: continue
        try:
            if answers_num >= len(correct_order): raise IndexError()
            num = answer_list[pos]
            answers.append(random_ordered_answers[int(num)])
            answers_num += 1
        except IndexError:
            print("!!!Too many answers!!!")
            print("----------------------")
            return
        except ValueError:
            print("!!!Not every answer was a number!!!")
            print("-----------------------------------")
            return
    
    check_answer(answers, correct_order)


def handle_group(q):
    print(q.question)
    print(f"{q.group_name}-be kell beválogatni, a többi természetesen a másik csoportba kerülne CS-en")

    for text, ans in q.answers.items():
        print(f"{q.group_name}")
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
    if isinstance(answer, list) and isinstance(correct, list):
        if answer == correct:
            print("-----NOICE-----")
            dot_print()
        else:
            if toprint == None :
                print(f"Helyes: {correct}")
            else:
                print(f"Helyes: {toprint}")
            print("-----SADGE-----")
            
            dot_print()
    
    elif answer == str(correct):
        print("-----NOICE-----")
        dot_print()
    
    else:
        if toprint == None :
            print(f"Helyes: {correct}")
        else:
            print(f"Helyes: {toprint}")
        print("-----SADGE-----")
        
        dot_print()

def dot_print():
    for _ in range(5):
        print(".", end=" ")
        sleep(250 / 1000)
    print()


if __name__ == "__main__":
    main()