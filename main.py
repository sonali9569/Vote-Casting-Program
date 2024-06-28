import datetime #To check the current time
import random as rand #To generate a random OTP
import smtplib #To send an email

print("Welcome to the Voting Center")
print("Voting is open from 9:00 AM to 6:00 PM")

candidates = ["Manish", "Mukesh", "Amit", "Suresh"] #Candidates for voting
print("OTP verification is required to vote")

current_hour = datetime.datetime.now().time().hour #Getting the current hour

if 9 <= current_hour <= 18: #Check if the current time is within voting hours
    voter_name = input("Enter Your Name: ")  #Voter enters their name
    voter_email = input("Enter Your Email: ") #Voter enters their email for OTP verification
    otp_code = "" #Initializing an empty string for the OTP

    for _ in range(6): #Loop to create a 6-digit OTP
        otp_code += str(rand.randint(1, 9)) #Generating a random digit between 1 and 9

    otp_message = f"Dear {voter_name}, Your OTP for voting is {otp_code}" #OTP message content
    email_subject = "OTP Verification for Voting" #Email subject
    email_content = 'Subject: {}\n\n{}'.format(email_subject, otp_message)

    mail_session = smtplib.SMTP('smtp.gmail.com', 587) #Setting up the SMTP session
    mail_session.starttls() #Starting TLS encryption
    #Ensure you have generated an app password for your Gmail account
    #https://support.google.com/accounts/answer/185833?hl=en
    mail_session.login("youremail@gmail.com", "yourapppassword") #Logging into the email account
    mail_session.sendmail('youremail@gmail.com', voter_email, email_content) #Sending the OTP email
    print("OTP has been sent!")

    entered_otp = input("Enter the OTP: ") #Voter enters the OTP
    attempts = 0 #Count the number of OTP attempts

    for _ in range(2):
        if entered_otp != otp_code: #If the entered OTP is incorrect
            print("Invalid OTP")
            otp_code = ""
            for _ in range(6): #Generate a new OTP
                otp_code += str(rand.randint(1, 9))
            otp_message = f"Dear {voter_name}, Your new OTP for voting is {otp_code}"
            email_content = 'Subject: {}\n\n{}'.format(email_subject, otp_message)
            mail_session.sendmail('youremail@gmail.com', voter_email, email_content)
            print("A new OTP has been sent")
            entered_otp = input("Enter the new OTP: ")
        if entered_otp == otp_code: #If the OTP is correct
            attempts = 1
            print("OTP verified successfully")
            break

    if attempts == 0:
        print("You have entered the wrong OTP 3 times. Please try voting again tomorrow.")
    else:
        for idx, candidate in enumerate(candidates, 1): #Display the list of candidates
            print(f"{idx}: {candidate}")
        
        selected_candidate = int(input("Enter the number corresponding to your chosen candidate: "))
        print("Your vote has been cast successfully!")
        print("Vote Details:")
        print(f"Voter: {voter_name}\nVoted for: {candidates[selected_candidate - 1]}")
        
        send_vote_details = input("Would you like to receive your vote details via email? (Enter Yes/No): ")
        send_vote_details = send_vote_details.upper()
        
        print("Thank you for voting!")
        
        if send_vote_details == "YES": #If the voter wants to receive vote details via email
            vote_details = f"Vote Details:\nVoter: {voter_name}\nVoted for: {candidates[selected_candidate - 1]}"
            email_subject = "Your Voting Details"
            email_content = 'Subject: {}\n\n{}'.format(email_subject, vote_details)
            mail_session.sendmail('youremail@gmail.com', voter_email, email_content)
            print("Vote details have been emailed to you.")
else: #If voting time is over
    print("Voting is currently closed. Please return to vote during the voting hours.")