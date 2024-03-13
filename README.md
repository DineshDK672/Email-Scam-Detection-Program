# Email Scam Detection Program

## Overview
This Python program is designed to automate the detection of potential scam emails by searching for specific keywords or phrases within emails stored in an Excel file. The program targets emails based on their content and sender address, aiming to identify patterns indicative of scam activities. It was developed to assist the Information Security Office on campus in streamlining the email remediation process.

## Features
- Reads data from an Excel file containing multiple columns and rows of email data using the pandas library for data analysis.
- Analyzes the content of emails stored in the "Subject" column.
- Identifies sender email addresses from the "Sender address" column.
- Searches for specific keywords or phrases within email subjects.
- Marks email addresses associated with potential scam emails.
- Utilizes a threshold value to determine if marked email addresses are indicative of scam activities.

## Usage
1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
2. Clone this repository to your local machine or download the source code directly.
3. Install the required dependencies using pip:
    ```
    pip install pandas openpyxl
    ```
4. Prepare your email data in an Excel file with columns labeled "Subject" and "Sender address".
5. Modify the `keywords` variable in the script to include the specific keywords or phrases you want to search for.
6. Adjust the `threshold` value according to your scam detection criteria.
7. Run the program by executing the `scam_detection.py` script:
    ```
    python scam_detection.py
    ```
8. Review the output to identify potential scam email addresses that exceed the threshold.

## Example
Consider an Excel file `emails.xlsx` with the following structure:

| Subject                            | Sender address         |
|----------------------------------- |----------------------- |
| Urgent: Verify your account        | scam@example.com       |
| Important Notice: Security Update  | security@example.com   |
| Claim your prize now!              | prize@example.com      |
| Update your password immediately   | phishing@example.com  |

Suppose we set the `keywords` variable to `["Urgent", "Verify", "Prize", "Update"]` and the `threshold` to `1`. Running the program would mark the email address `scam@example.com` as potentially associated with scam activities.

## Contributing
Contributions are welcome! If you have any suggestions for improvements or feature requests, please feel free to open an issue or submit a pull request.
