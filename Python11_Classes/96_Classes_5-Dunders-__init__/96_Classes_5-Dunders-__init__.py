# 03-124: Dunder __init__ + __str__


# __init__

class Invoice:
  def __str__(self):
    return "This is the invoice class!"


inv = Invoice()
print(str(inv))



# __init__ + __str__ constructors

class Invoice:
    def __init__(self, invoice_id, client, total):
        self.invoice_id = invoice_id
        self.client = client
        self.total = total

    def __str__(self):
        return f'\nInvoice # {self.invoice_id}:\nFrom {self.client}.\nTotal ammount: {self.total} €'
    
inv_client_1 = Invoice('INV-000354724','Google', 500.00)

print(str(inv_client_1))