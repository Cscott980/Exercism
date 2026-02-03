def exchange_money(budget, exchange_rate):
    return budget/exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value
    pass


def get_value_of_bills(denomination, number_of_bills):
    return number_of_bills * denomination


def get_number_of_bills(amount, denomination):
    return int(amount / denomination)


def get_leftover_of_bills(amount, denomination):
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_decimal = spread / 100
    effective_rate = exchange_rate * (1 + spread_decimal)
    exchanged = budget / effective_rate
    return int(exchanged // denomination * denomination)
    
    
    
