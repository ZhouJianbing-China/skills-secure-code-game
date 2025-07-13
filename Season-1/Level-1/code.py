'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')
MAX_ITEM_AMOUNT = 100000 # maximum price of item in the shop
MAX_QUANTITY = 100 # maximum quantity of an item in the shop
MIN_QUANTITY = 0 # minimum quantity of an item in the shop
MAX_TOTAL = 1e6 # maximum total amount accepted for an order

def validorder(order: Order):
    payment = Decimal('0')
    receive = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            print("payment "+ item.description)
            if (-MAX_ITEM_AMOUNT < item.amount < MAX_ITEM_AMOUNT):
                payment += Decimal(str(item.amount))
        elif item.type == 'product':
            print("product "+ item.description)
            if(-MAX_ITEM_AMOUNT < item.amount < MAX_ITEM_AMOUNT and MIN_QUANTITY<item.quantity <MAX_QUANTITY):
                receive -= Decimal(str(item.amount)) * Decimal(str(item.quantity))
        else:
            return "Invalid item type: %s" % item.type
    if abs(payment) > MAX_TOTAL or receive > MAX_TOTAL:
        return "Total amount payable for an order exceeded"
    
    if abs(payment) != abs(receive):
        print(payment + receive)
        return "Order ID: %s - Payment imbalance: $%0.02f" % (order.id, payment + receive)
    else:
        return "Order ID: %s - Full payment received!" % order.id