'''Digital'''

def cal_condition(name, thai, home, age, salary, money_fak):
    '''dsad;as'''
    status = True
    if thai not in ('Yes','True'):
        status = False
    elif home not in ('Yes','True'):
        status = False
    elif age < 16:
        status = False
    elif money_fak > 500000:
        status = False
    elif salary > 840000:
        status = False

    if status:
        print(f'Congratulations! {name} is qualified to receive a digital wallet\
 amount of 10,000 baht, sponsored by all taxpayers in Thailand.')
    else:
        print(f'Unfortunately, {name} is not qualified.')

cal_condition(input(), input(), input(), float(input()), float(input()), float(input()))
