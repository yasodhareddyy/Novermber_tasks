import random

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[random.randint(0,len(arr)-1)]
    less=[x for x in arr if x[1]<pivot[1] ]
    equal=[x for x in arr if x[1]==pivot[1] ]
    greater=[x for x in arr if x[1]>pivot[1] ]

    return quick_sort(less)+equal+quick_sort(greater)


stock_data=[]

for i in range(10):
    symbol="stock"+str(i)
    performance=random.uniform(-1.0,1.0)
    stock_data.append((symbol,performance))
    stock_data=quick_sort(stock_data)

    top_performing_stock_data=stock_data[:5]
    print("Top-performing stocks:")
    for stock in top_performing_stock_data:
        print(f"{stock[0]}:{stock[1]}")








"""

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    less = [x for x in arr if x[1] < pivot[1]]
    equal = [x for x in arr if x[1] == pivot[1]]
    greater = [x for x in arr if x[1] > pivot[1]]

    return quick_sort(greater) + equal + quick_sort(less)

# Initialize an empty list to store stock data (symbol, performance).
stock_data = []

# Simulate receiving real-time stock data (symbol, performance change) continuously.
for _ in range(10):
    symbol = "Stock" + str(_)
    performance = random.uniform(-1.0, 1.0)  # Simulated performance change.
    stock_data.append((symbol, performance))

    # Sort the list using Quick Sort.
    stock_data = quick_sort(stock_data)

    # Ensure that only the top N performing stocks are maintained.
    top_performing_stocks = stock_data[:5]  # Adjust this number as needed.

    # Print the current top-performing stocks.
    print("Top-performing stocks:")
    for stock in top_performing_stocks:
        print(f"{stock[0]}: {stock[1]}")

# Continue to receive and process new stock data as it arrives in real-time.

"""