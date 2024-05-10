def quiz(questions):
    score = 0
    total_questions = len(questions)
    
    for question, options, correct_answer in questions:
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
            user_answer_index = int(user_answer) - 1
            if options[user_answer_index] == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {correct_answer}")
        else:
            print("Invalid input. Skipping this question.")

    print(f"Quiz completed! Your score: {score}/{total_questions}")

if __name__ == "__main__":
    
    questions = [
        ("When was the Jallianwala massacre happen?", ["1919", "1911", "1906", "1945"], "1919"),
        ("Who give to slogan 'करो या मरो'?", ["Motilal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Bhagat Singh"], "Mahatma Gandhi"),
        ("Who wrote 'The Golden Threshold'?", ["Rajendra Prasad", "Jawaharlal Nehru", "Sarojini Naidu", "Dr. BR Ambedkar"], "Sarojini Naidu"),
        ("Who was the first Prime Minister of independent India?", ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Maulana Abul Kalam Azad", "Dr. BR Ambedkar"], "Jawaharlal Nehru"),
        ("The Indian National Congress was founded in which year?", ["1905", "1885", "1920", "1942"], "1885"),
        ("Who was the last viceroy of India?", ["Lord Mountbatten", "Lord Curzon", "Lord Dalhousie", "Lord Irwin"], "Lord Mountbatten"),
        
    ]

    quiz(questions)
