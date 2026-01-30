📖 Introduction

A Queue is a fundamental linear data structure that follows the FIFO (First In, First Out) principle.
The element added first is removed first, similar to a queue of people waiting in line.

This project provides a clear and easy-to-understand implementation of a Queue to help learners grasp its working principles.

❓ What is a Queue?

A Queue supports operations where:

Insertion happens at the rear

Deletion happens from the front

📌 FIFO Rule:

First element inserted → First element removed

⭐ Features

Simple and readable implementation

Supports basic queue operations

Beginner-friendly structure

Easy to extend (Circular Queue / Priority Queue)

Useful for DSA learning and interviews

🧠 Types of Queue

Simple Queue

Circular Queue

Priority Queue

Deque (Double-Ended Queue)

⚙️ Queue Operations
Operation	Description
Enqueue	Insert an element at the rear
Dequeue	Remove an element from the front
Peek / Front	View the front element
IsEmpty	Check if queue is empty
IsFull	Check if queue is full (array-based)
🧩 Implementation

This Queue can be implemented using:

Arrays

Linked Lists

(Choose based on your project requirements.)

▶️ Usage

Typical steps:

Create a Queue

Add elements using enqueue()

Remove elements using dequeue()

Check front element using peek()

🧪 Example
Enqueue: 10, 20, 30
Queue: [10, 20, 30]

Dequeue:
Removed → 10
Queue: [20, 30]

🧠 Applications of Queue

CPU scheduling

Printer queue

Breadth-First Search (BFS)

Request handling in servers

Call center systems

📁 Project Structure
Queue/
├── src/
│   ├── Queue.js        # Queue implementation
│   └── index.js        # Driver code
├── README.md
└── package.json

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/Raj-Kumar-Chaurasiya/DSA-Queue

2️⃣ Navigate to project folder
cd queue

3️⃣ Install dependencies (if any)
npm install

4️⃣ Run the project
node src/index.js

⏱️ Time Complexity
Operation	Complexity
Enqueue	O(1)
Dequeue	O(1)
Peek	O(1)
🤝 Contributing

Contributions are welcome!
Steps:

Fork the repository

Create a new branch

Commit your changes

Submit a pull request

📄 License

This project is licensed under the MIT License.

© 2025 Raj Kumar Chaurasiya
