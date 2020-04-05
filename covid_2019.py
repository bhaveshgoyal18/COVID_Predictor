print("             Welcome to the COVID-19 predictor..           ")
count=0
print("Q1:-Enter your Gender:-")
x = input("Male or Female:-")
print("Q2:-Enter your Age:-")
x = int(input())
if x > 50 :
    count += 2
else:
    count += 1
print("Q3:Have you any of the following disease?")
print("Heart Disease,Diabetes,Asthma,Kidney Problem")
x = input("Yes or No:-")
if x == "Yes" or x == "yes":
    count += 2
print("Q4:-Have you visited any affected country in the last 14 days?")
x = input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=2
print("Q5:-Have you come in contact with a COVID +ve patient?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=2
print("Q6:-Do you have cough?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=1
print("Q7:-Do you have cold?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=1
print("Q8:-Do you have fever?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=2
print("Q9:Do you have headache?")
x = input("Yes or No:-")
if x == "Yes" or x == "yes":
    count += 1
print("Q10:-Do you have sore throught?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=1
print("Q11:-Have you visited any hospital where COVID +ve patient is kept?")
x=input("Yes or No:-")
if x=="Yes" or x=="yes":
    count+=2
print("Q13:-Are you facing these from the last five days?")
x = input("Yes or No:-")
if x == "Yes" or x == "yes":
    count += 2
result = count   #total count =18
if result>0 and result<=4:
    print("                               VERY LOW RISK..")
    print("             Thanks for the patience for answering the questions..")
    print("                         PRAY TO GOD TO SAVE HUMANITY..")
elif result>4 and result<6:
    print("                                 LOW RISK..")
    print("             Thanks for the patience for answering the questions..")
    print("                         PRAY TO GOD TO SAVE HUMANITY..")
elif result>6 and result<=10:
    print("                             MODERATE RISK..")
    print("Thanks for the patience for answering the questions..")
    print("                         PRAY TO GOD TO SAVE HUMANITY..")
elif result>10 and result<=14:
    print("                             HIGH RISK..")
    print("                      GO FOR A COVID TEST RIGHT NOW..")
else:
    print("                             VERY HIGH RISK..")
    print("                 IMMEDIATELY GO TO A HOSPITAL OR CALL AT 104..")
    print("                    ISOLATE YOURSELF FROM OTHERs..")
