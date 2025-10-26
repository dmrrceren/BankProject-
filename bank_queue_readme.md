# Bank Queue System – Priority Queue with Circular Linked Lists

## Description
This project simulates a **bank queue system** using **priority queues** implemented with **circular linked lists**.  
Customers are assigned one of three priority levels: **0 (Low)**, **1 (Medium)**, **2 (High)**.  
High-priority customers are served first, followed by medium and low-priority customers.

## Features
- Add new customers to the queue with a selected priority level.
- Serve customers based on their priority level (dequeue).
- Display the current state of all queues.
- Interactive command-line interface.

## Implementation
- Programming Language: **Python 3**  
- Data Structure: **Circular Linked List** for each priority queue  
- Priority Handling: Customers in higher priority queues are served first.  
- Object-Oriented Design: Classes `Node`, `CircularQueue`, and `BankQueue` are used.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/dmrrceren/BankProject-.git
```
2. Navigate to the project folder:
```bash
cd BankProject-
```
3. Ensure Python 3 is installed:
```bash
python --version
```

## Usage
Run the program:
```bash
python main.py
```
In the interactive menu you can:
1. Add a new customer (`enqueue`)  
2. Serve a customer (`dequeue`)  
3. Display all queues  
4. Exit the program  

Example:
```
=== Bank Queue System ===
1 - Add customer
2 - Serve customer
3 - Show queues
4 - Exit
Choice: 1
Customer name: Alice
Select priority: 0 - Low | 1 - Medium | 2 - High
Priority: 2
Alice added to the 2nd (High) priority queue.
```

## License
This project is **open-source** and available for educational purposes.

## Author
**Ceren Demirer**

