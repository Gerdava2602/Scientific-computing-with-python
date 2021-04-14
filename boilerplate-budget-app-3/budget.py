class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self,amount, description=""):
    ledger_object = dict()
    ledger_object["amount"] = amount
    ledger_object["description"] = description
    self.ledger.append(ledger_object)

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      ledger_object = dict()
      ledger_object["amount"] = -amount
      ledger_object["description"] = description
      self.ledger.append(ledger_object)
      return True
    return False

  def check_funds(self, amount):
    total = 0
    for o in self.ledger:
      total += o["amount"]
    if total >= amount:
      return True
    return False

  def get_balance(self):
    return sum([l["amount"] for l in self.ledger])

  def transfer(self, amount, budget):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to "+(budget.name))
      budget.deposit(amount, "Transfer from "+(self.name))
      return True
    return False

  def __str__(self):
    title = "*"*int(15-len(self.name)/2) + self.name + "*"*int(15-len(self.name)/2)+"\n"

    items = ""
    total = 0
    for l in self.ledger:
      if len(l["description"])>23:
        items += l["description"][:23]
      else:
        items += l["description"] + " "*(23- len(l["description"]))
      items += " " + str("{:.2f}".format(l["amount"])) + "\n"
      total += l["amount"]
    
    total = "Total: "+str("{:.2f}".format(total))

      
    return "".join([title, items, total])

def create_spend_chart(categories):
  chart = "Percentage spent by category\n"
  n = 100
  total = 0
  percent = dict()
  for c in categories:
      actual = -sum([o["amount"] for o in c.ledger if o["amount"] < 0])
      total += actual
      percent[c.name] = actual
  for c in categories:
    percent[c.name] = round(percent[c.name]/total*100)
    if percent[c.name] % 10 > 7:
      percent[c.name] += percent[c.name] % 10
    else:
      percent[c.name] -= percent[c.name] % 10
  


  while n >= 0:
    chart += " "*(3-len(str(n))) + str(n)+"| "
    for c in categories:
      if percent[c.name] >= n:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"
    n -= 10
  
  chart += " "*4 + "-"*(len(categories)*3+1)+"\n"

  for i in range(max([len(f.name) for f in categories])):
    chart += " "*5
    for c in categories:
      if i < len(c.name):
        chart += c.name[i]
      else:  
        chart +=" "
      chart += " "*2
    chart += "\n"
  return chart[:-1]
  