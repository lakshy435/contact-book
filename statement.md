 Project Statement: Simple Contact Book Application

 1. Project Title
Simple Contact Book Application (CLI)

 2. Course Context
This project serves as a practical application assignment, focusing on fundamental programming concepts, modular design, and data persistence, relevant to the course on [**Insert Course Name/Code Here, e.g., Introduction to Programming/CS101**].

 3. Real-World Problem / Need
The core problem addressed is the need for efficient, non-internet-dependent management of a small list of contacts. While modern systems offer complex solutions, this project fills the gap for a minimalistic, reliable utility built directly on basic programming constructs.

 4. Scope and Functionality
The application is a Command-Line Interface (CLI) utility designed to manage contact records.

# Implemented Functions (CRUD Operations)
* **Create (Add Contact):** Captures Name, Phone Number (integer), and Email (optional).
* **Read (View Contacts):** Displays all saved contact entries.
* **Search:** Allows retrieval of a specific contact by Name.
* **Delete:** Removes a contact entry permanently by Name.

# Technical Limitations
The current scope is limited to exact name matching for Search/Delete and does not include advanced features like:
* Editing existing contacts.
* Input validation (e.g., checking for non-numeric input in phone field).
* Case-insensitive searching.

 5. Technical Design and Implementation
The solution employs a Top-Down, modular design approach to separate concerns and enhance code readability.

A. Core Data Structure
The contact data is managed using a **Python Dictionary**.
* **Key:** The contact's **Name** (string).
* **Value:** A nested dictionary containing the fields `"phone"` (integer) and `"email"` (string).

 B. Persistence Mechanism
The built-in **`json` module** is used for data persistence.
* The `load_contact()` function handles reading the dictionary from the `contacts.json` file. A `try-except` block handles the initial scenario where the file does not exist, initializing an empty dictionary.
* The `save_contacts()` function is called immediately after any modification (Add or Delete) to ensure data is written back to `contacts.json`, guaranteeing data integrity upon exit.

 C. Modular Design
Each primary operation (Add, View, Search, Delete) is encapsulated in its own function. This makes the code easy to test, debug, and expand, adhering to the principles of good software engineering.

 6. Development Adherence
The project development strictly followed the prescribed development process:
1.  **Problem Definition:** Defined simple contact management.
2.  **Requirement Analysis:** Identified the need for CRUD and persistence.
3.  **Top-Down Design:** Implemented distinct, modular functions (`add_contact`, `load_contact`, etc.).
4.  **Algorithm Development:** Utilized dictionary lookups for efficient retrieval and deletion.
5.  **Implementation:** Coded in Python using the standard library.
6.  **Testing and Refinement:** Verified successful execution of all menu options and correct JSON file I/O.

 7. Declaration
I declare that this project, including all source code and documentation in this repository, is my own original work and has been developed without the use of external Large Language Models (LLMs) or generative AI tools. All principles of academic honesty have been strictly adhered to.


[lakshya singh]
[25bai10855]
[Date of Submission-24/11/2025]
