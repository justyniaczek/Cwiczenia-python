import sys
#Gra sprawdzajaca wiedze ogolna gracza

def open_file(file_name, mode):
    """Otwiera plik z pytaniami do gry"""
    try:
        the_file= open(file_name, mode)
    except IOError as e:
        print("Bład przy otwarciu pliku", file_name, "program zostanie zakonczony", e)
        input("Aby zakończyć program wciśnij enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz tekstu po sforamtowaniu go"""
    line= the_file.readline()
    line = line.replace( "/", "\n")
    return line

def next_block(the_file):
    """Zwraca kolejny blok danych z pliku"""
    category= next_line(the_file)
    question = next_line(the_file)
    answers =[]
    for i in range (4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation =next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """Wita gracza i pobiera jego nazwe"""
    print("\t\tWitaj w grze!\n")
    print("\t\t",title,"\n")

def main():
    trivia_file = open("quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score=0
    category, question, answers, correct, explanation= next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        #uzyskaj odpowiedz
        answer = input("jaka jest twoja odpowiedz")
        if answer == correct:
            score += 1
            print("Odpowiedz poprawna")
        else:
            print("Odpowiedz niepoprawna")
        print(explanation)
        print("Wynik:", score, "\n\n")
        category, question, answers, correct, explanation = next_block(trivia_file)
    trivia_file.close()
    print("To było ostatnie pytanie!")
    print("Twój końcowy wynik wynosi", score)

main()


