String Manipulation Tool
A command-line utility for performing common string operations: length, case conversion, reversal, character counting, word counting, and word replacement.
Features
Find string length
Convert to uppercase / lowercase
Reverse a string
Count occurrences of a character
Count words
Replace a word (with existence check before replacing)
View the current (possibly modified) string at any time
Tech Stack
Python 3 (standard library only — no external dependencies)
Project Structure
.
├── string_tool.py # main script
├── requirements.txt # dependency list
│                         (none required)
└── README.md
Setup Instructions
1. Prerequisites
Python 3.8 or newer installed and available on your PATH.
2. Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
3. (Optional) Create a virtual environment
Not strictly needed since there are no third-party dependencies, but kept here for consistency with standard Python project setup:
python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
(This will effectively do nothing, since the project has no third-party dependencies — included for completeness.)
5. Run the program
python string_tool.py
You'll be prompted to enter a string, then shown a numbered menu to perform operations on it repeatedly until you choose to exit.
Usage Example
Enter a string: Hello World

--- STRING MANIPULATION TOOL ---
1. Find length
2. Uppercase
3. Lowercase
4. Reverse string
5. Count character
6. Count words
7. Replace word
8. Show current string
9. Exit

Enter your choice: 1
Length of string: 11
Known Limitations
Single string per session — to work on a new string, restart the program.
Character count (option 5) only accepts a single character by design.
No file input/output — string is entered interactively each run.
Future Improvements
Support loading text from a file.
Allow entering a new string without restarting the program.
Add unit tests for each operation.
