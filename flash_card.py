"""
一个实用的闪卡记忆工具将实现德国科学家塞巴斯蒂安·莱特纳提出的间隔重复的概念。该系统建议以增加的时间间隔复习卡片，分为以下几步
首先，你创建3-5个盒子存放闪卡，使用时间间隔来标记每个盒子，以显示卡片应该复习的频率。例如最难记的每天复习，其次每2天一次。
接下来，你开始学习和整理闪卡，经历多个学习周期。
在第一个周期中，你的所有卡片都在第一盒里。你回答这些卡片上的问题。如果你答对了，卡片会移到第二盒。答错了，卡片会留在第一盒。
当你进入第二个周期时，你回答第一盒和第二盒卡片上的问题。答对了，卡片会移到第三盒。答错了，卡片会留在第一盒。
在第三个周期中，你学习所有三盒里的卡片。同样，答错卡片移回第一盒。答对卡片移到下一盒。对于答对了在已经第三盒的卡片，从数据库删除。
如果你想更详细地了解这种方法，可以参考 MindEdge 文章。https://www.mindedge.com/learning-science/the-leitner-system-how-does-it-work/

A practical flashcard memorization tool implements the spaced repetition concept proposed by German scientist Sebastian Leitner. 
The system suggests reviewing cards at increasing intervals, divided into the following steps:
First, you create 3-5 boxes to hold flashcards, and use time intervals to mark each box, indicating how frequently each card should be reviewed. 
For example, the hardest ones are reviewed every day, the next box every 2 days, and so on.
Next, you begin studying and organizing the flashcards, going through several study cycles.
In the first cycle, all your cards are in the first box. You answer the questions on these cards. If you get it right, the card moves to the second box; if wrong, it stays in the first box.
When you enter the second cycle, you answer the cards in the first and second boxes. If correct, the card moves to the third box; if wrong, it goes back to the first box.
In the third cycle, you study cards in all three boxes. Similarly, a wrong answer sends a card back to the first box, and a correct answer moves it to the next box. If you answer correctly for a card already in the third box, delete it from the database.
If you want to know more about this method, see the MindEdge article: https://www.mindedge.com/learning-science/the-leitner-system-how-does-it-work/
"""

# flash_card.py
from db import SessionLocal
from models import Base, FlashCard

# flash_cards = {}


def insert_data(question, answer):
    """
    插入数据到数据库表中
    Insert data into the database table
    """
    #  创建一个会话
    #  Create a session
    session = SessionLocal()

    try:
        new_data = FlashCard(question=question, answer=answer) # type: ignore
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
    Get data from the database table
    """
    #  创建一个会话
    #  Create a session
    session = SessionLocal()

    try:
        return session.query(FlashCard).all()
    finally:
        session.close()


def delete_flashcard(question):
    """
    删除数据
    Delete data
    """
    #  创建一个会话
    #  Create a session
    session = SessionLocal()

    try:
        flash_card = session.query(FlashCard).filter(FlashCard.question == question).first() # type: ignore
        if flash_card:
            session.delete(flash_card)
            session.commit()
        else:
            print("Flashcard not found.")
    except:
        session.rollback()
        raise
    finally:
        session.close()


def edit_flashcard(question, rep_count=None):
    """
    编辑数据
    Edit data
    """
    #  创建一个会话
    #  Create a session
    session = SessionLocal()

    try:
        flash_card = session.query(FlashCard).filter(FlashCard.question == question).first() # type: ignore
        if flash_card:
            if rep_count is not None:
                flash_card.rep_count = rep_count
            else:
                new_question = input(f"current question: {flash_card.question}\nplease write a new question:\n> ")
                if new_question:
                    flash_card.question = new_question
                print()
                new_answer = input(f"current answer: {flash_card.answer}\nplease write a new answer:\n> ")
                if new_answer:
                    flash_card.answer = new_answer
                print()
            session.commit()
        else:
            print("Flashcard not found.")
    except:
        session.rollback()
        raise
    finally:
        session.close()


def update_flashcards(question):
    """
    如果前一步输入 u ，程序应打印以下更新子菜单（4）。
    press "d" to delete the flashcard:
    press "e" to edit the flashcard:
    即 d 删除当前的闪卡， e 选项提供编辑当前闪卡的方式。
    
    对于 e 选项 首先，我们需要编辑问题：
    current question: <question>
    please write a new question: 
    问题编辑完成后，继续编辑答案：
    current answer: <answer>
    please write a new answer:
    如果用户将问题或答案字段留空，保持原始问题或答案值不变。

    当用户按错键时，在练习（3）和更新（4）菜单中输出 <wrong key> is not an option 消息
    程序的其他部分应按前一阶段的方式运行。

    If "u" is entered in the previous step, the program should print the following update submenu (4):
    press "d" to delete the flashcard:
    press "e" to edit the flashcard:
    That is, "d" deletes the current flashcard, and "e" allows editing the current flashcard.

    For the "e" option, first, we edit the question:
    current question: <question>
    please write a new question:
    After editing the question, continue to edit the answer:
    current answer: <answer>
    please write a new answer:
    If the user leaves the question or answer field empty, the original value remains unchanged.

    When the user presses the wrong key, print <wrong key> is not an option in both practice (3) and update (4) menus.
    The rest of the program should function as in the previous stage.
    """
    while True:
        print("press \"d\" to delete the flashcard:")
        print("press \"e\" to edit the flashcard:")
        choice = input('> ')
        if choice == 'd':
            print()
            delete_flashcard(question)
            break
        elif choice == 'e':
            print()
            edit_flashcard(question)
            break
        else:
            print(f"{choice} is not an option")
            continue


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

    If you enter 1, the program should print the following submenu (2):
    1. Add a new flashcard
    2. Exit

    By selecting "Add a new flashcard," the user is prompted to enter Question and Answer.
    Both Question and Answer must be non-empty; otherwise, continue waiting for input.
    After entry, the program returns automatically to submenu (2). Repeat this process whenever a new card is added.

    Question:
    > What is the capital city of Brazil?
    Answer:
    > Brasilia

    If input is invalid, output: {wrong key} is not an option, and wait for correct input.
    """
    print("1. Add a new flashcard")
    print("2. Exit")
    choice = input("> ")
    if choice == '1':
        print()
        question, answer = '', ''
        while not question:
            question = input("Question:\n> ").strip()
        while not answer:
            answer = input("Answer:\n> ").strip()
            print()
        # flash_cards[question] = answer
        insert_data(question, answer)
        add_flashcards()
    elif choice == '2':
        print()
        main()
    else:
        print(f"{choice} is not an option\n")
        add_flashcards()


def practice_flashcards():
    """
    主菜单（1）中的 Practice flashcards 选项应打印所有已添加的问题和答案。
    如果没有卡片，打印 There is no flashcard to practice! 并返回主菜单（1）

    在用户从上一阶段输入 Practice flashcards 键后弹出的菜单中添加新功能。我们称之为练习菜单（3）：
    Question: {your question}
    press "y" to see the answer:
    press "n" to skip:
    press "u" to update:

    如果输入 y ，程序应输出 Answer: {your answer} 
    在显示每个问题后，你需要询问用户他们的答案是否正确。为此，我们需要创建另一个菜单，我们称之为学习菜单（5）：
    press "y" if your answer is correct:
    press "n" if your answer is wrong:
    然后转到下一张闪卡。
    如果没有更多闪卡要显示，则返回主菜单（1）。
    如果输入 n ，则跳转到下一张闪卡。如果没有更多闪卡要显示，则返回主菜单（1）。
    如果输入错误，输出以下消息： {wrong key} is not an option 。
    程序的其他部分应按前一阶段的方式运行。

    The "Practice flashcards" option in the main menu (1) should print all added questions and answers.
    If there are no cards, print "There is no flashcard to practice!" and return to the main menu (1).

    After the user enters "Practice flashcards," a new feature appears in the popup menu, called the practice menu (3):
    Question: {your question}
    press "y" to see the answer:
    press "n" to skip:
    press "u" to update:

    If the input is "y", the program should output "Answer: {your answer}".
    After showing each question, you need to ask the user whether their answer was correct, using a study menu (5):
    press "y" if your answer is correct:
    press "n" if your answer is wrong:
    Then move to the next flashcard.
    If there are no more flashcards to display, return to the main menu (1).
    If the input is "n", skip to the next flashcard. If there are no more, return to the main menu (1).
    If the input is invalid, output: {wrong key} is not an option.
    The rest of the program should function as in the previous stage.
    """
    flash_cards = get_data()
    if not flash_cards:
        print("There is no flashcard to practice!\n")
        main()
    else:
        for flash_card in flash_cards:
            print()
            print(f"Question: {flash_card.question}")
            while True:
                user_input = input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n> ')
                if user_input.lower() == "y":
                    print(f"Answer: {flash_card.answer}\n")
                    while True:
                        user_input = input('press "y" if your answer is correct:\npress "n" if your answer is wrong:\n> ')
                        if user_input.lower() == "y":
                            flash_card.rep_count += 1
                            edit_flashcard(flash_card.question, rep_count=flash_card.rep_count)
                            if flash_card.rep_count == 4:
                                delete_flashcard(flash_card.question)
                            print()
                            break
                        elif user_input.lower() == "n":
                            flash_card.rep_count = 1
                            print()
                            break
                        else:
                            print(f"{user_input} is not an option\n")
                            continue
                    break
                elif user_input.lower() == "n":
                    print()
                    break
                elif user_input.lower() == "u":
                    update_flashcards(flash_card.question)
                    break
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

    When the program starts, it should print the following menu. This is our main menu (1):
    1. Add flashcards
    2. Practice flashcards
    3. Exit

    If the input is invalid, output: {wrong key} is not an option. Wait for correct input.
    Don't forget the farewell message. Each time the user exits, output "Bye!"
    """
    while True:
        print("1. Add flashcards")
        print("2. Practice flashcards")
        print("3. Exit")
        choice = input("> ")
        if choice == '1':
            add_flashcards()
            break
        elif choice == '2':
            practice_flashcards()
            break
        elif choice == '3':
            print()
            print("Bye!")
            break
        else:
            print(f"{choice} is not an option\n")


main()
