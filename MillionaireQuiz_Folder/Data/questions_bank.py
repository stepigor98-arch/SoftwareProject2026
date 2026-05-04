# Contains seed questions used to fill the database on first run


from typing import Dict, List                   # Each question is represented as a dictionary with keys




# text(text type): question text, options(list of strings): list of 4 answer options, correct(int): index of the correct option (0-3), level(str): difficulty level, category(str): question category

QUESTION_SEED: List[Dict] = [
    # --- EASY ---
    {"text": "What color is the sky on a clear day?", "options": ["Blue", "Green", "Red", "Black"], "correct": 0, "level": "easy", "category": "General"},
    {"text": "How many days are there in a week?", "options": ["5", "6", "7", "8"], "correct": 2, "level": "easy", "category": "General"},
    {"text": "Which animal is known for meowing?", "options": ["Dog", "Cat", "Cow", "Horse"], "correct": 1, "level": "easy", "category": "General"},
    {"text": "Which one is a fruit?", "options": ["Carrot", "Potato", "Apple", "Onion"], "correct": 2, "level": "easy", "category": "General"},
    {"text": "What is the opposite of 'hot'?", "options": ["Warm", "Cold", "Wet", "Dry"], "correct": 1, "level": "easy", "category": "General"},
    {"text": "Which planet do we live on?", "options": ["Mars", "Earth", "Venus", "Jupiter"], "correct": 1, "level": "easy", "category": "General"},
    {"text": "What is 10 + 5?", "options": ["12", "13", "14", "15"], "correct": 3, "level": "easy", "category": "Math"},
    {"text": "Which one is a primary color?", "options": ["Purple", "Orange", "Red", "Pink"], "correct": 2, "level": "easy", "category": "General"},
    {"text": "How many minutes are there in one hour?", "options": ["30", "45", "60", "90"], "correct": 2, "level": "easy", "category": "Math"},
    {"text": "Which season comes after spring?", "options": ["Winter", "Summer", "Autumn", "None"], "correct": 1, "level": "easy", "category": "General"},
    {"text": "What do we call a baby cat?", "options": ["Puppy", "Kitten", "Cub", "Foal"], "correct": 1, "level": "easy", "category": "General"},
    {"text": "Which shape has three sides?", "options": ["Square", "Triangle", "Circle", "Rectangle"], "correct": 1, "level": "easy", "category": "Math"},
    {"text": "Which one is used to write on a computer?", "options": ["Keyboard", "Spoon", "Shoes", "Plate"], "correct": 0, "level": "easy", "category": "IT"},


    # --- MEDIUM ---
    {"text": "Which ocean is the largest on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "correct": 3, "level": "medium", "category": "Geography"},
    {"text": "Which gas do plants mostly use for photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], "correct": 2, "level": "medium", "category": "Science"},
    {"text": "Which country is famous for the Eiffel Tower?", "options": ["Italy", "France", "Spain", "Germany"], "correct": 1, "level": "medium", "category": "Geography"},
    {"text": "In computing, what does 'CPU' stand for?", "options": ["Central Processing Unit", "Computer Power User", "Core Program Utility", "Central Performance Upload"], "correct": 0, "level": "medium", "category": "IT"},
    {"text": "Which language uses the word 'Hola' for 'Hello'?", "options": ["Spanish", "French", "German", "Japanese"], "correct": 0, "level": "medium", "category": "Languages"},
    {"text": "Which of these is NOT a programming language?", "options": ["Python", "Java", "HTML", "Ruby"], "correct": 2, "level": "medium", "category": "IT"},
    {"text": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "correct": 2, "level": "medium", "category": "Geography"},
    {"text": "Which instrument typically has six strings?", "options": ["Violin", "Flute", "Guitar", "Drum"], "correct": 2, "level": "medium", "category": "Music"},
    {"text": "Which country has the city of Rome as its capital?", "options": ["Spain", "Italy", "Greece", "Portugal"], "correct": 1, "level": "medium", "category": "Geography"},
    {"text": "What is the chemical symbol for water?", "options": ["O2", "CO2", "H2O", "NaCl"], "correct": 2, "level": "medium", "category": "Science"},
    {"text": "Which planet is known as the Red Planet?", "options": ["Mars", "Mercury", "Saturn", "Neptune"], "correct": 0, "level": "medium", "category": "Science"},
    {"text": "In music, how many notes are there in a standard major scale?", "options": ["5", "6", "7", "8"], "correct": 2, "level": "medium", "category": "Music"},
    {"text": "Which file extension is commonly used for Python files?", "options": [".java", ".py", ".html", ".sql"], "correct": 1, "level": "medium", "category": "IT"},


    # --- HARD ---
    {"text": "Which data structure works in 'Last In, First Out' (LIFO) order?", "options": ["Queue", "Stack", "Tree", "Graph"], "correct": 1, "level": "hard", "category": "IT"},
    {"text": "Which HTTP method is typically used to update an existing resource?", "options": ["GET", "POST", "PUT", "TRACE"], "correct": 2, "level": "hard", "category": "IT"},
    {"text": "Which of these is a common SQL aggregate function?", "options": ["MERGE", "COUNT", "JOIN", "INDEX"], "correct": 1, "level": "hard", "category": "Databases"},
    {"text": "What is the base-2 number system called?", "options": ["Decimal", "Binary", "Hexadecimal", "Octal"], "correct": 1, "level": "hard", "category": "IT"},
    {"text": "Which of these best describes 'encapsulation' in OOP?", "options": ["Hiding data inside a class", "Running code faster", "Using only functions", "Copying objects automatically"], "correct": 0, "level": "hard", "category": "OOP"},
    {"text": "In networking, what does 'DNS' do?", "options": ["Encrypts files", "Translates domain names to IP addresses", "Blocks ads", "Increases CPU speed"], "correct": 1, "level": "hard", "category": "Networking"},
    {"text": "Which of these is a valid IPv4 address format?", "options": ["256.10.10.10", "192.168.1.1", "192.168.1", "192.168.1.1.1"], "correct": 1, "level": "hard", "category": "Networking"},
    {"text": "Which Git command uploads commits to a remote repository?", "options": ["git push", "git pull", "git clone", "git init"], "correct": 0, "level": "hard", "category": "IT"},
    {"text": "Which SQL clause is used to filter groups created by GROUP BY?", "options": ["WHERE", "HAVING", "ORDER BY", "LIMIT"], "correct": 1, "level": "hard", "category": "Databases"},
    {"text": "Which network protocol is commonly used to securely browse websites?", "options": ["HTTP", "FTP", "HTTPS", "SMTP"], "correct": 2, "level": "hard", "category": "Networking"},
    {"text": "In Python, what is the output type of the expression: type([])?", "options": ["list", "<class 'list'>", "array", "tuple"], "correct": 1, "level": "hard", "category": "Python"},
    {"text": "Which of these is NOT a normal form in database design?", "options": ["1NF", "2NF", "3NF", "4PF"], "correct": 3, "level": "hard", "category": "Databases"},
    {"text": "In OOP, what is polymorphism mainly about?", "options": ["One class can have only one method", "Same interface, different implementations", "Data stored in tables", "Functions must be global"], "correct": 1, "level": "hard", "category": "OOP"},

    # --- EXPERT ---
    {"text": "In Big-O notation, what is the time complexity of binary search in a sorted array?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "correct": 1, "level": "expert", "category": "IT"},
    {"text": "In Python, which keyword creates a generator (instead of returning a full list at once)?", "options": ["yield", "return", "break", "pass"], "correct": 0, "level": "expert", "category": "Python"},
    {"text": "Which SQL statement permanently removes rows from a table?", "options": ["SELECT", "UPDATE", "DELETE", "GRANT"], "correct": 2, "level": "expert", "category": "Databases"},
    {"text": "Which SQL join returns all rows from the left table and only matching rows from the right table?", "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN"], "correct": 1, "level": "expert", "category": "Databases"},
    {"text": "In TCP/IP, which part ensures reliable delivery with acknowledgements and retransmissions?", "options": ["IP", "UDP", "TCP", "ICMP"], "correct": 2, "level": "expert", "category": "Networking"},
    {"text": "In Big-O notation, what is the average time complexity of quicksort?", "options": ["O(n)", "O(n log n)", "O(log n)", "O(n^2)"], "correct": 1, "level": "expert", "category": "IT"},
    {"text": "Which isolation level in databases is the strongest (most strict) in terms of preventing anomalies?", "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"], "correct": 3, "level": "expert", "category": "Databases"},
    {"text": "In Python, what does the 'GIL' mainly affect?", "options": ["File permissions", "Network speed", "CPU-bound threading concurrency", "Database indexing"], "correct": 2, "level": "expert", "category": "Python"},

]   
