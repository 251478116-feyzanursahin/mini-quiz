"""
Ogrenci: Feyzanur Sahin (251478116)
Proje: mini-quiz
"""
# V1 TASKS
# 1. "list" komutunu çalıştır
# 2. "answer" komutunu çalıştır
# 3. Dosya işlemlerini iyileştir

import sys
import os

# Bu fonksiyon quiz klasörünü ve veri dosyasını oluşturur.
# os.path.exists Python’da bir dosya veya klasörün var olup olmadığını kontrol eden bir fonksiyondur.
# sys.argv terminalden yazılan komutları programa gönderir.

def init():
    if not os.path.exists(".miniquiz"):
        os.mkdir(".miniquiz")

    path = ".miniquiz/questions.dat"

    if not os.path.exists(path):
        file = open(path, "w")
        file.close()

    return "Quiz data initialized."

# Bu fonksiyon yeni soru ekler.

def add(question, answer):

    if not os.path.exists(".miniquiz/questions.dat"):
        return "Error: Data not initialized."

    file = open(".miniquiz/questions.dat", "a")
    line = "1|" + question + "|" + answer + "\n"
    file.write(line)
    file.close()
    return "Question added"

# Fonksiyonun ana programı

def main():

    if len(sys.argv) < 2:
        print("Error: Missing parameters.")
        return

    command = sys.argv[1]
    if command == "init":
        print(init())
        return

    if command == "add":
        if len(sys.argv) < 4:
            print("Error: Missing parameters.")
            return

        question = sys.argv[2]
        answer = sys.argv[3]
        print(add(question, answer))
        return

    if command == "answer":
        if len(sys.argv) < 4:
            print("Error: Missing parameters.")
            return

        question = sys.argv[2]
        user_answer = sys.argv[3]

        path = ".miniquiz/questions.dat"

        if not os.path.exists(path):
            print("Not initialized.")
            return

        with open(path, "r") as file:
            lines = file.readlines()

            for line in lines:
                parts = line.strip().split("|")
                if parts[1] == question:
                    if parts[2].lower() == user_answer.lower():
                        print("Correct!")
                    else:
                        print("Wrong answer.")
                    return

            print("Question not found.")
        return

    if command == "list":
        path = ".miniquiz/questions.dat"

        if not os.path.exists(path):
            print("Not initialized. Run: python miniquiz.py init")
            return

        with open(path, "r") as file:
            lines = file.readlines()

            if len(lines) == 0:
                print("No questions found.")
            else:
                for line in lines:
                    parts = line.strip().split("|")
                    print("Question:", parts[1])
        return
    print("Error: Unknown command.")

main()