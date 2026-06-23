print("\033[35m-----PERSONAL EXPENSE TRACKER-----\033[0m")

def add_Expense():
  amount=float(input("enter amount"))
  category=input("what did you spend this amount on? 🤔")
  date=input("enter date")
  print("Expense Added-\n")
  print(f"amount: {amount}")
  print(f"category: {category}")
  print(f"date: {date}")
  with open("expense.csv","a") as file:
    file.write(f"{date},{amount},{category}\n")

def show_expenses():  #add category wise displaying expenses
  print("<<<< Displaying your expenses >>>>") 
  with open("expense.csv","r") as file:
    for line in file:
      print(line.strip())

def total_spendings(): #add total spendings in one week,one month,one year, or custom
  print("<<< Displaying your total expenses >>>")
  total=0
  with open("expense.csv","r") as file:
    for line in file:
      amt=float(line.split(",")[1])
      total+=amt
  
  print(f"Total spending:{total}")

def store_dictionary():
  dictionary={}
  with open("expense.csv","r") as file:
    for line in file:
      date,amount,cat=line.strip().split(",")
      amount=float(amount)
      if cat in dictionary:   
        dictionary[cat]+=amount
      else:
        dictionary[cat]=amount
  return dictionary

def cat_summary():
  print("<<<Displaying Category Summary>>>")
  d=store_dictionary()
  for key,value in d.items():
    print(key,value)

def top_spending():
  
  d=store_dictionary()
  max_amt=0
  for key in d:
    if d.get(key)>max_amt:
      max_amt=d.get(key)
      k=key
  if not d:
    print("no expense records found")
    return
  else:
    return (f"your top spending category is: {k}, you have spent:{max_amt}")

def avg_exp():
  
  total=0
  count=0
  with open("expense.csv","r") as file:
    for line in file:
      date,amount,cat=line.strip().split(",")
      amount=float(amount)
      total+=amount
      count+=1
  if count==0:
    return("no record found")
  else:
    avg=total/count
  return(round(avg,2))
      
def monthly_summary():
  print("=== Printing Monthly Expense Summary ===")
  d={}
  with open("expense.csv","r") as file:
    for line in file:
      date,amount,category=line.strip().split(",")
      amount=float(amount)
      day,month,year=date.split("-")
      month_key=f"{month}-{year}"
      if month_key in d:
        d[month_key]+=amount
      else:
        d[month_key]=amount
  for key,value in d.items():
    print(key,value)
    
def monthly_trend():
  d={}
  with open("expense.csv","r") as file:
    for line in file:
      date,amount,category=line.strip().split(",")
      amount=float(amount)
      day,month,year=date.split("-")
      month_key=f"{month}-{year}"
      if month_key in d:
        d[month_key]+=amount
      else:
        d[month_key]=amount
  max_val=max(d,key=d.get)
  min_val=min(d,key=d.get)
  print(f"Highest Spending Month:{max_val}, your total spendings in this month:{d[max_val]}\n")
  print(f"Lowest Spending Month:{min_val}, your total spendings in this month:{d[min_val]}\n")
  
def export_report():
  with open("report.txt","w") as file:  #we open this write mode because everytime this function is called a fresh new report is generated because everything is overwritten 
    file.write("PERSONAL EXPENSE REPORT\n")
    file.write("="*30+"\n")
    avg=avg_exp()
    file.write(f"Your Average Expenses: {avg}\n")
    file.write("TOP SPENDING\n")
    top=top_spending()
    file.write(top)

  



def show_menu():
  print("\n===MENU===")
  print("1.Add Expense")
  print("2.Show my Expenses")
  print("3.Total Spendings")
  print("4.Category Summary")
  print("5.Top Spending")
  print("6.Average Expenses")
  print("7.Monthly Summary")
  print("8.Monthly Expense Trend")
  print("9.Export report")
  print("10.Exit")

def main():
  while True:
    show_menu()
    ch=int(input("How do you want to proceed?"))
    if(ch==1):
      print("welcome to your personal expense analyzer!! adding expenses :)")
      add_Expense()
    elif(ch==2):
      show_expenses()
    elif(ch==3):
      total_spendings()
    elif(ch==4):
      cat_summary()
    elif(ch==5):
      print("Calculating your top spendings.....\n")
      print(top_spending())
    elif(ch==6):
      print("***Calculating your average expenses....***\n")
      print("average expenses calculated:-",avg_exp())
    elif(ch==7):
      monthly_summary()
    elif(ch==8):
      monthly_trend()
    elif(ch==9):
      export_report()
    elif(ch==10):
      print("exiting the application....Goodbye!!")
      break
    else:
      print("Invalid Selection!! Please try again")
      
    
main()


    


