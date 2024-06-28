# Vote-Casting-Program

This Python program simulates an electronic voting system with OTP (One-Time Password) verification. The system allows users to cast their vote for a list of candidates within a specified time frame (9:00 AM to 6:00 PM). Key features include:

- *OTP Verification*: Ensures secure voting by sending a randomly generated OTP to the user's email for verification.
- *Voting Hours Enforcement*: Allows voting only within the specified hours.
- *Candidate Selection*: Provides a list of candidates for users to select from.
- *Email Notifications*: Sends OTP and optional vote details to the user's email.
- *Secure and Reliable*: Uses SMTP for secure email communication.

## Prerequisites

- Python 3.x
- smtplib for email functionality
- A Gmail account with an app password for sending emails

## Setup

1. Clone the repository:

    sh
    git clone https://github.com/sonali9569/Vote-Casting-Program.git
    cd Vote-Casting-Program
    

2. Install the required Python packages (if any):

    sh
    pip install -r requirements.txt
    

3. Update the email and app password in the script:

    python
    mail_session.login("youremail@gmail.com", "yourapppassword")
    

4. Run the script:

    sh
    python main.py
    

## Usage Instructions

1. *Voting Time*: Ensure you are voting between 9:00 AM and 6:00 PM.
2. *Input Details*: Enter your name and email address.
3. *OTP Verification*: Check your email for the OTP, enter it in the program to verify.
4. *Select Candidate*: Choose the candidate you wish to vote for from the displayed list.
5. *Confirmation*: Optionally, receive an email confirmation with your vote details.

## Creating an Executable (Optional)

To distribute your program as an executable file, you can use pyinstaller:

1. Install PyInstaller:

    sh
    pip install pyinstaller
    

2. Create the executable:

    sh
    pyinstaller --onefile main.py
    

3. The executable will be created in the dist directory.

## Notes

- Ensure you have enabled 2-factor authentication on your Gmail account and generated an app password for sending emails. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en) to generate an app password.
- Make sure to replace "youremail@gmail.com" and "yourapppassword" in the script with your actual email and app password.

## Acknowledgments

- This program demonstrates a basic yet secure approach to electronic voting with email-based OTP verification. It is ideal for educational purposes and small-scale implementations.
