from collections import defaultdict

def getNetProfit(events):
    stock_quantity = defaultdict(int)
    stock_price = {}
    net_profit = 0
    result = []

    for event in events:
        event_list = event.split()
        event_type = event_list[0]

        match event_type:
            case "BUY":
                stock_name = event_list[1]
                quantity = int(event_list[2])
                stock_quantity[stock_name] += quantity
            case "SELL":
                stock_name = event_list[1]
                quantity = int(event_list[2])
                stock_quantity[stock_name] -= quantity
            case "CHANGE":
                price_change = int(event_list[2])
                stock_price[stock_name] += price_change
                net_profit += price_change * stock_quantity.get(stock_name)
            case "QUERY":
                result.append(net_profit)

    return result

