print("\033[35m-----PERSONAL EXPENSE TRACKER-----\033[0m")

def addExpense():
  amount=float(input("enter amount"))
  category=input("what did you spend this amount on? 🤔")
  date=input("enter date")
  print("Expense Added-\n")
  print(f"amount: {amount}")
  print(f"category: {category}")
  print(f"date: {date}")

def show_menu():
  print("\n===MENU===")
  print("1.Add Expense")
  print("2.Exit")

def main():
  while True:
    show_menu()
    ch=int(input("How do you want to proceed?"))
    if(ch==1):
      print("welcome to your personal expense analyzer!! adding expenses :)")
      addExpense()
    elif(ch==2):
      print("exiting the application....Goodbye!!")
      break
    else:
      print("Invalid Selection!! Please try again")
      
    
main()


    


