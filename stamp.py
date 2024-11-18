'''stamp'''

def transaction():
    '''transaction'''
    num_items = int(input())
    unit_price = int(input())
    discount_units = int(input())
    bulk_units = int(input())
    bulk_discount = int(input())
    total_price = 0
    discount_remaining = 0
    total_items = 0

    for _ in range(num_items):
        purchased = int(input())

        if discount_remaining <= purchased:
            total_items += purchased - discount_remaining
            total_price += ((purchased - discount_remaining) // unit_price) * discount_units
            discount_remaining = (total_price // bulk_units) * bulk_discount
        else:
            leftover = 0 if not purchased % bulk_discount else 1
            discount_remaining -= ((purchased // bulk_discount) + leftover) * bulk_discount

        total_price -= (total_price // bulk_units) * bulk_units

    total_price += (discount_remaining // bulk_discount) * bulk_units if bulk_discount else 0
    print(total_items)
    print(total_price)

transaction()
