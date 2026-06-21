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
      
  

  


def show_menu():
  print("\n===MENU===")
  print("1.Add Expense")
  print("2.Show my Expenses")
  print("3.Total Spendings")
  print("4.Exit")

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
      print("exiting the application....Goodbye!!")
      break
    else:
      print("Invalid Selection!! Please try again")
      
    
main()


    


