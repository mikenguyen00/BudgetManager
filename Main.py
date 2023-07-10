import Budget

outgoings = Budget.BudgetManager(2500)
outgoings.add_budget("Groceries",500)
outgoings.spend("Groceries",200)
outgoings.add_budget("Rent/Bills",1500)
outgoings.spend("Rent/Bills",1500)
outgoings.add_budget("Entertainment",500)
outgoings.spend("Entertainment",150)

outgoings.print_summary()