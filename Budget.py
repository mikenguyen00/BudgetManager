class BudgetManager:    
    def __init__(self,amount):
        self.intial=amount
        self.budget={}
        self.expenditure={}

    def add_budget(self,name, amount):
        if name in self.budget:
            raise ValueError("Budget Exists")
        if amount > self.intial:
            raise ValueError("Insufficient Funds")
        self.budget[name]=amount
        self.intial-=amount
        self.expenditure[name]=0
        return self.intial

    def spend(self,name,amount):
        if name not in self.expenditure:
            raise ValueError("No Name exist in Expenditure")
        self.expenditure[name]+=amount
        budgeted=self.budget[name]
        spent=self.expenditure[name]
        return budgeted - spent

    def print_summary(self):
        print("Budget               Budgeted    Spent   Remaining")
        print("----------------     ---------- -------- ---------")
        total_budgeted=0
        total_spent=0
        total_remaining=0
        for name in self.budget:
            budgeted = self.budget[name]
            spent = self.expenditure[name]
            remaining=budgeted-spent
            print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f}, {remaining:10.2f}')
            total_budgeted += budgeted
            total_spent+=spent
            total_remaining+=remaining
        print("----------------     ---------- -------- ---------")
        print(f'{"Total":15s}, {total_budgeted:10.2f}, {total_spent:10.2f}, {total_budgeted-total_spent:10.2f}')

