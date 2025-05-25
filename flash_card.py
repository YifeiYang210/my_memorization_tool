# flash_card.py
from db import SessionLocal
from models import Base, FlashCard

# flash_cards = {}


def insert_data(question, answer):
    """
    插入数据到数据库表中
    """
    #  创建一个会话
    session = SessionLocal()

    try:
        new_data = FlashCard(question=question, answer=answer)  # type: ignore
        session.add(new_data)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def get_data():
    """
    从数据库表中获取数据
    """
    #  创建一个会话
    session = SessionLocal()

    try:
        return session.query(FlashCard).all()
    finally:
        session.close()



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
        # flash_cards[question] = answer
        insert_data(question, answer)
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
    flash_cards = get_data()
    if not flash_cards:
        print("There is no flashcard to practice!\n")
        main()
    else:
        for flash_card in flash_cards:
            print(f"Question: {flash_card.question}")
            user_input = input('Please press "y" to see the answer or press "n" to skip:\n> ')
            print()
            if user_input.lower() == "y":
                print(f"Answer: {flash_card.answer}\n")
            elif user_input.lower() == "n" or user_input.lower() == "s":
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
    while True:
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")
        choice = input("> ")
        print()
        if choice == '1':
            add_flashcards()
            break
        elif choice == '2':
            practice_flashcards()
            break
        elif choice == '3':
            print("Bye!")
            print()
            break
        else:
            print(f"{choice} is not an option\n")


main()
