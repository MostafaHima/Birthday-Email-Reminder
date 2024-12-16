# Birthday Email Reminder

This Python project sends automatic birthday wishes to people listed in a CSV file. The application reads birthday information (names and emails) from the file, selects a personalized message from pre-written templates, and sends the birthday wishes via email using an SMTP server.

## Features

- **Automatic Birthday Notification**: The program checks if today's date matches any birthday in the CSV file.
- **Random Message Selection**: Three message templates are available, and one is chosen randomly for each birthday.
- **Email Integration**: Sends birthday emails through an SMTP server (Gmail).
- **Environment Variables**: Uses `.env` for storing sensitive information like email credentials.
- **CSV Integration**: Reads birthday data from a CSV file for easy management of contacts.

## Requirements

- Python 3.x
- `pandas` for handling CSV files
- `dotenv` for environment variable management
- `smtplib` for sending emails

## Setup

1. **Install Dependencies**:

    Create a virtual environment and install the required packages:

    ```bash
    pip install pandas python-dotenv
    ```

2. **Create a `.env` file**:

    Create a `.env` file in the root directory of your project and add your email credentials:

    ```
    MY_EMAIL=your_email@gmail.com
    MY_PASSWORD=your_email_password
    ```

3. **Prepare the `birthdays.csv` file**:

    The CSV file should have the following structure:

    ```csv
    name,month,day,email
    John,5,14,john@example.com
    Jane,12,25,jane@example.com
    ```

4. **Prepare Message Templates**:

    Add three text files (`letter_1.txt`, `letter_2.txt`, and `letter_3.txt`) in a `letter_templates/` folder. Each file should contain a birthday message with a placeholder `[NAME]` where the recipient's name will be inserted.

    Example:

    ```
    Happy Birthday [NAME]! Wishing you a wonderful day filled with joy.
    ```

## How to Use

- When you run the script, it will check if today is anyone's birthday by comparing the current date with the birthdays in the CSV file.
- If a match is found, it will send a birthday message to the corresponding email.
- The email message will be randomly selected from one of the three templates.

## Running the Script

To run the script, execute the following:

```bash
python main.py
