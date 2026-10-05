print("===================================")
print("       STUDY ASSISTANT CHATBOT")
print("===================================")
print("Ask me a study question.")
print("Type 'bye' to exit.")
print()

while True:
    question = input("You: ").lower().strip()

    if question == "bye":
        print("Bot: Goodbye! Keep studying and do your best!")
        break

    elif "what is python" in question:
        print("Bot: Python is a high-level, interpreted programming language.")

    elif "what is java" in question:
        print("Bot: Java is an object-oriented, class-based programming language.")

    elif "what is dbms" in question:
        print("Bot: DBMS stands for Database Management System. It is used to store, manage, and retrieve data.")

    elif "what is operating system" in question or "what is os" in question:
        print("Bot: An Operating System is system software that manages computer hardware and software resources.")

    elif "what is computer network" in question:
        print("Bot: A computer network is a group of connected computers that communicate and share resources.")

    elif "what is data structure" in question:
        print("Bot: A data structure is a way of organizing and storing data so it can be used efficiently.")

    elif "what is algorithm" in question:
        print("Bot: An algorithm is a step-by-step procedure used to solve a problem.")

    elif "what is oops" in question or "what is oop" in question:
        print("Bot: OOP stands for Object-Oriented Programming. It uses concepts such as classes, objects, inheritance, polymorphism, abstraction, and encapsulation.")

    elif "what is inheritance" in question:
        print("Bot: Inheritance allows one class to acquire the properties and methods of another class.")

    elif "what is polymorphism" in question:
        print("Bot: Polymorphism means one interface can be used for different implementations.")

    elif "what is database" in question:
        print("Bot: A database is an organized collection of data that can be stored, managed, and retrieved.")

    elif "what is sql" in question:
        print("Bot: SQL stands for Structured Query Language. It is used to communicate with and manage relational databases.")

    elif "how to study" in question:
        print("Bot: Make a study timetable, understand concepts, practice questions, and revise regularly.")

    elif "exam" in question:
        print("Bot: For exams, focus on important topics, practice previous questions, revise regularly, and manage your time.")

    elif "hello" in question or "hi" in question:
        print("Bot: Hello! I am your Study Assistant. Ask me a study question.")

    elif "thank" in question:
        print("Bot: You're welcome! Keep learning!")

    else:
        print("Bot: I don't have an answer for that question yet.")
        print("Bot: Try asking about Python, Java, DBMS, OS, Networks, OOP, or Data Structures.")

print()
print("Study session ended.")