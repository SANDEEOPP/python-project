#LMS Assignment2
########################################
req_incomstart=10000
req_incomend=20000
req_Cscorestart=600
req_Cscoreend=900
req_interestrateform=2.0
req_interestrateTo=5.0

def approve_loan(income, credit_score, interest):
    if income >= req_incomstart and income <= req_incomend and credit_score >= req_Cscorestart and credit_score <= req_Cscoreend and interest >= req_interestrateform and interest <= req_interestrateTo  :
        return "Approved"
    else:
        return "Denied"
# Customer Inputs
# ###################
income = float(input("What is your annual income   ="))
credit_score = float(input("What is your credit score   = "))
interest = float(input("What is your expected intrest rate ="))

result = approve_loan(income, credit_score, interest)
print(result)
# Save input data to a text file
with open("BankofAmerica.txt", "a") as file:
    file.write(f"Income: {income}, Credit Score: {credit_score}, interest: {interest}, Result: {result}\n")