# 03-125: Dunder __repr__

class Invoice:
    def __init__(self, invoice_id, client, total):
        self.invoice_id = invoice_id
        self.client = client
        self.total = total

    def __str__(self):
        return f'\nInvoice # {self.invoice_id}:\nFrom {self.client}.\nTotal ammount: {self.total} €'
    
    # __repr__
    def __repr__(self):
        return f'\nInvoice <value: invoice_id: {self.invoice_id}, client: {self.client}, total: {self.total}'
    
inv_client_1 = Invoice('INV-000354724','Google', 500.00)
print(str(inv_client_1))
print(repr(inv_client_1))       # Invoice <value: invoice_id: INV-000354724, client: Google, total: 500.0