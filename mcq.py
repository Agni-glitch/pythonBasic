questions = [
    ["What is the capital of France?", "Paris", "Berlin", "London", "Madrid", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Jupiter", "Mars", "Saturn", 3],
    ["Who wrote 'Romeo and Juliet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "Leo Tolstoy", 2],
    ["Which is the smallest prime number?", "0", "1", "2", "3", 2],
    ["What is the chemical symbol for water?", "H2O", "O2", "CO2", "HO", 0],
    ["Which number is considered unlucky in many cultures?", "3", "7", "13", "8", 2],
    ["What is the largest ocean on Earth?", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", "Pacific Ocean", 3],
    ["Which country hosted the 2016 Summer Olympics?", "Brazil", "China", "USA", "UK", 0],
    ["What is the powerhouse of the cell?", "Nucleus", "Mitochondria", "Ribosome", "Cell Wall", 1],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 2],
    ["Which animal is known as the 'King of the Jungle'?", "Elephant", "Tiger", "Lion", "Bear", 2],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Granite", 2],
    ["Which programming language is known for its use in web development?", "Python", "Java", "HTML", "C++", 2],
    ["What is the square root of 64?", "6", "8", "10", "12", 1],
    ["In which year did World War I begin?", "1912", "1914", "1916", "1918", 1]
]
levels=[1000,2000,3000,5000,10000,20000,30000,50000,75000,100000,200000,300000,500000,1000000]
for q in range(0,len(questions)-1):
    question=questions[q]
    print(f"Question of Rs.{levels[q]}")
    print(f"{question[0]}")
    print(f"a.{question[1]} b.{question[2]} c.{question[3]} d.{question[4]}")
    ip=int(input("Answer: (1-4)"))
    if(ip==question[5]):
        print(f"You won Rs.{levels[q]}")
    else:
        break