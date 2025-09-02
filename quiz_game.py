import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi",
        "explanation": "Delhi is the capital city of India."
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars",
        "explanation": "Mars appears red because of iron oxide on its surface."
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"],
        "answer": "Blue Whale",
        "explanation": "The blue whale is the largest animal ever known to have lived."
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
        "explanation": "2 + 2 equals 4."
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci",
        "explanation": "The Mona Lisa was painted by Leonardo da Vinci."
    },
    {
        "question": "Where is the Great Wall located?",
        "options": ["India", "China", "Egypt", "Mexico"],
        "answer": "China",
        "explanation": "The Great Wall is one of the most famous landmarks in China."
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["O2", "H2O", "CO2", "NaCl"],
        "answer": "H2O",
        "explanation": "Water's chemical formula is H2O."
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Tiger", "Lion", "Elephant", "Wolf"],
        "answer": "Lion",
        "explanation": "The lion is often called the King of the Jungle."
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7",
        "explanation": "There are 7 continents on Earth."
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Ganges", "Amazon", "Nile", "Yangtze"],
        "answer": "Nile",
        "explanation": "The Nile is generally considered the world's longest river."
    }
]

def print_options(opts):
    for i, opt in enumerate(opts):
        print(f"  {chr(65+i)}) {opt}")

print("Hello! Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Maybe next time!")
    quit()

print("Great! Let's start the game.")
score = 0
total_questions = len(questions)
random_questions = random.sample(questions, total_questions)

for q in random_questions:
    print("\n" + q["question"])
    shuffled_opts = random.sample(q["options"], len(q["options"]))
    print_options(shuffled_opts)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    try:
        choice = shuffled_opts[ord(answer) - 65]
        if choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
    except (IndexError, ValueError):
        print("Invalid input. No points for this question.")
    print("Explanation:", q["explanation"])

percentage = (score / total_questions) * 100

print("\nGame Over!")
print(f"Your final score is: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")
