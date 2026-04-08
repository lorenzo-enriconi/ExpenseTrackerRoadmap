\# 💸 Expense Tracker



A simple command-line expense tracker built with Python. Add, update, delete, and view your expenses — all stored in a local text file. Built as part of the https://roadmap.sh/projects/expense-tracker backend projects challenge.



\---



\## Features



\- ➕ Add expenses with description, amount, and month

\- ✏️ Update existing expenses

\- 🗑️ Delete expenses with automatic ID re-numbering

\- 📋 View all recorded expenses

\- 📅 Filter expenses by month



\---



\## Requirements



\- Python \*\*3.10 or higher\*\* (required for `match/case` syntax)

\- No external libraries needed — uses only the Python standard library



\---



\## Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/lorenzo-enriconi/ExpenseTrackerRoadmap

```



\### 2. Run the program



```bash

python main.py

```



That's it. No installation or setup required.



\---



\## How It Works



When you run the program, a menu is displayed in the terminal:



```

1\. Add Expense

2\. Update Expense

3\. Delete Expense

4\. View Expenses

5\. View Monthly Expenses

6\. Exit

```



Enter the number corresponding to the action you want to perform and follow the prompts.



\### Data Storage



All expenses are saved to a file called `expenses.txt` in the same directory as the script. The file is created automatically on the first expense added.



Each line in the file follows this format:



```

{id} - {description}: {amount} ({month})

```



\*\*Example:\*\*



```

1 - Rent: 1200.0 (January)

2 - Internet: 120.0 (January)

3 - Groceries: 350.0 (February)

```



\### Auto ID System



IDs are \*\*position-based\*\*, not permanently stored. This means:



\- IDs always start at `1`

\- When an expense is deleted, all subsequent IDs are automatically recalculated

\- There are no gaps in the ID sequence



\*\*Example:\*\* If you delete expense `1`, the former expense `2` becomes `1`, `3` becomes `2`, and so on.



\---



\## Usage Example



```

Enter your choice: 1

Enter the expense amount: 150.00

Enter the expense description: Electricity bill

Enter the month of the expense: March



Enter your choice: 4



1 - Electricity bill: 150.0 (March)



Enter your choice: 3

Enter the ID of the expense to delete: 1



Enter your choice: 4

No expenses found.

```



\---



\## Project Structure



```

expense-tracker/

├── expense\_tracker.py   # Main application file

├── expenses.txt         # Auto-generated data file (created on first run)

└── README.md

```



\---



\## Roadmap / Possible Improvements



\- \[ ] Export expenses to CSV

\- \[ ] Summary report with total spending per month

\- \[ ] Category support

\- \[ ] Search expenses by keyword



\---



\## License



This project is open source and available under the \[MIT License](LICENSE).

