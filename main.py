price = 100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

price(f"The Down Payment is :{down_payment}")