# flash_card.py

flash_cards = {}


def add_flashcards():
    """
    如果输入 1 ，程序应打印以下子菜单（2）。
    1. Add a new flashcard
    2. Exit

    通过选择 Add a new flashcard 选项，用户将被提示输入 Question 和 Answer 。
    您的问题和答案必须是非空值。否则，等待输入。
    输入完成后，程序将自动返回子菜单（2）。每次用户想要添加新卡片时，重复此过程。

    Question:
    > What is the capital city of Brazil?
    Answer:
    > Brasilia

    如果输入错误，输出以下消息： {wrong key} is not an option 。等待正确的输入。
    """
    print("1. Add a new flashcard")
    print("2. Exit")
    choice = input("> ")
    print()
    if choice == '1':
        question, answer = '', ''
        while not question:
            question = input("Question:\n> ").strip()
        while not answer:
            answer = input("Answer:\n> ").strip()
            print()
        flash_cards[question] = answer
        print()
        add_flashcards()
    elif choice == '2':
        main()
    else:
        print(f"{choice} is not an option\n")
        add_flashcards()


def practice_flashcards():
    """
    主菜单（1）中的 Practice flashcards 选项应打印所有已添加的问题和答案。
    如果没有卡片，打印 There is no flashcard to practice! 并返回主菜单（1）

    你的闪卡应该在屏幕上按以下方式显示：
    Question: {your question}
    Please press "y" to see the answer or press "n" to skip:

    如果输入 y ，程序应输出 Answer: {your answer} 并转到下一张闪卡。
    如果没有更多闪卡要显示，则返回主菜单（1）。
    如果输入 n ，则跳转到下一张闪卡。如果没有更多闪卡要显示，则返回主菜单（1）。
    如果输入错误，输出以下消息： {wrong key} is not an option 。等待正确的输入。
    """
    if not flash_cards:
        print("There is no flashcard to practice!\n")
        main()
    else:
        for question, answer in flash_cards.items():
            print(f"Question: {question}")
            user_input = input('Please press "y" to see the answer or press "n" to skip:\n> ')
            print()
            if user_input.lower() == "y":
                print(f"Answer: {answer}\n")
            elif user_input.lower() == "n":
                print()
            else:
                print(f"{user_input} is not an option\n")
        main()


def main():
    """
    当程序启动时，它应该打印以下菜单。这是我们主菜单（1）：
    1. Add flashcards
    2. Practice flashcards
    3. Exit

    如果输入错误，输出以下消息： {wrong key} is not an option 。等待正确的输入。
    不要忘记告别消息。每次用户退出程序时，输出 Bye!
    """
    print("1. Add flashcards")
    print("2. Practice flashcards")
    print("3. Exit")
    choice = input("> ")
    print()
    if choice == '1':
        add_flashcards()
    elif choice == '2':
        practice_flashcards()
    elif choice == '3':
        print("Bye!")
        print()
    else:
        print(f"{choice} is not an option\n")
        main()

main()
