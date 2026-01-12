logs = [
    "ACTION:BUY-TICKER:AAPL-PRICE:150.2587-STATUS:SUCCESS",
    "ACTION:SELL-TICKER:TSLA-PRICE:700.1-STATUS:SUCCESS",
    "ACTION:BUY-TICKER:BTC-PRICE:45000.00-STATUS:SUCCESS"
]

for log_data in logs:
    label = 'TICKER'
    find_ticker = log_data.upper().find(label.upper())
    #Finding ticker symbols using upper and lower limit to slice out only symbol name
    if find_ticker != -1:
        ticker_lower = find_ticker + len(label) + 1
        ticker_upper = log_data.find("-PRICE", ticker_lower)
        ticker_name = log_data[ticker_lower:ticker_upper]
        print(f'Ticker found {ticker_name}')
    else:
        print('Error: Ticker Not Available')

    #Find price of ticker by reducing search area
    loc = find_ticker + (len(ticker_name) + 1)
    find_price_start_loc = 'PRICE:'
    find_price_end_loc = '-STATUS'

    #Creating upper and lower limit to slice out only numerical values
    find_price_lowerlimit = ((log_data.upper().find(find_price_start_loc.upper(), loc)) + len(find_price_start_loc))
    find_price_upperlimit = (log_data.upper().find(find_price_end_loc.upper(),find_price_lowerlimit))
    price = float(log_data[find_price_lowerlimit:find_price_upperlimit])
    print(f'Price of {ticker_name} is {price:.2f}\n')
