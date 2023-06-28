import matplotlib as plt 
import yfinance as yf
import datetime as dt

print("WELCOME TO STOCK ANALYZER!")
def user_input():
    symbol=input(f"Input symbol here: ")
    enter_date = input("Please enter start and end date in ISO format (YYYY-MM-DD,YYYY-MM-DD), or press enter for defaults: ")
    date_split = enter_date.split(",") 
    if enter_date: 
        else: None
    
    if date_split:
        start_date = dt.strptime(date_split[0], "%Y-%m-%d")
        finish_date = dt.strptime(date_split[1], "%Y-%m-%d") 
        if len(date_split) > 1:
            else: None
    else:
        start_date = end_date = None
    return symbol, start_date, finish_date


def download_data(symbol, start_date, finish_date):
    data = yf.download(symbol, start=start_date, end=finish_date)
    data.drop(["Close"], axis=1, inplace=True)
    return data


def analyzing_data(data, column_name, symbol):
    columns = ('Open':'O'), ('High':'H'), ('Low': 'L'), ('Close': 'C'), ('Volume': 'V')
    column_data = data [c[0]
    if c[1].upper() == column_name.upper()].iloc[:, 0]
    option_type = input("Please choose raw (R) or percent change (P): ")
    if option_type.upper() == "R":
        pass
    elif option_type.upper() == "P":
        column_data = column_data.pct_change()
    else:
        print("Choice is invalid, please try again")

    print(f"Descriptive Statistics for {symbol}:")
    print(f"Count: {column_data.count()}")
    print(f"Mean: {column_data.mean()}")
    print(f"St.Dev: {column_data.std()}")
    print(f"Min {column_data.min()}")
    print(f"25% {column_data.quantile(0.25)}")
    print(f"50% {column_data.quantile(0.5)}")
    print(f"75% {column_data.quantile(0.75)}")
    print(f"Max {column_data.max()}")
    print(f"dtype: {column_data.dtype}")


def first_page():
    symbol, start_date, end_date = user_input()
    data = download_data(symbol, start_date, end_date)
    print("Available data to analyze:")
    print("(O)pen")
    print("(H)igh")
    print("(L)ow")
    print("(C)lose")
    print("(V)olume")
    print("(E)xit")
    while True:
        column_name = input("Choose which data to analyze: ")
        if column_name.upper() == "E":
            break
        try:
            analyzing_data(data, column_name, symbol)
        except IndexError:
            print("This is invalid, try again")

def continue_analyzing():
    choice = input("Would you like descriptives for another column? (Y/N): ")
    return choice.upper() == "Y"

def graph_type():
    print("Available plots:")
    print("1 - Area")
    print("2 - Histogram")
    print("3 - Line")
    graph_type = int(input("Select which plot type you would like to view: "))
    return graph_type

def create_graphs(data, column_name, graph_type, symbol):
    columns = ('Open':'O'), ('High':'H'), ('Low': 'L'), ('Close': 'C'), ('Volume': 'V')
    col_data = data[[c[0] for c in columns if c[1].upper() == column_name.upper()]].iloc[:, 0]

    change_type = input("Choose raw (R) or percent change (P) data for the graph: ")
    if change_type.upper() == "P":
        col_data = col_data.pct_change()

    plt.figure()
    if graph_type == 1:
        plt.stackplot(col_data.index, col_data, colors=["blue"], edgecolor="yellow", linewidth=1)
        plt.title(f"Plot of {symbol} {column_name} prices")
    elif graph_type == 2:
        col_data.plot.hist(bins=50, color="red", edgecolor="pink")
        plt.title(f"Histogram of {symbol} {column_name} prices")
    elif graph_type == 3:
        col_data.plot.line(color="purple", linewidth=2)
        plt.title(f"Line plot of {symbol} {column_name} prices")
    else:
        print("This is invalid, please try again")
        return

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

def main_page_input():
    symbol, start_date, end_date = user_input()
    data = get_data(symbol, start_date, end_date)
    print("Data Analyzing:")
    print("(O)pen")
    print("(H)igh")
    print("(L)ow")
    print("(C)lose")
    print("(V)olume")
    print("(E)xit")
    while True:
        column_name = input("Choose which data to analyze: ")
        if column_name.upper() == "E":
            break
        try:
            analyzing_data(data, column_name, symbol)
        except IndexError:
            print("Invalid choice, please try again")
        if not continue_analyzing():
            break

    while True:
        graph_type = graph_type()
        print("Available data to analyze:")
        print("(O)pen")
        print("(H)igh")
        print("(L)ow")
        print("(C)lose")
        print("(V)olume")
        print("(E)xit")
        column_name = input("What column should be plotted?: ")
        if column_name.upper() == "E":
            break
        create_graphs(data, column_name, graph_type, symbol)


if __name__ == "__main__":
    first_page()