# quiz_app.py

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A, B, C, D): ").strip().upper()
        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {question['answer']}")
    print(f"\n🎉 You got {score}/{len(questions)} correct.")

# List of quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Wordsworth", "B. William Shakespeare", "C. Charles Dickens", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    }
]

# Start the quiz
run_quiz(quiz_questions)