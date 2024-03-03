import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        #check if every symbol in this row are the same
        symbol = columns[0][line]
        for column in columns:     # checking of the sybol is what we want in every column
            sybol_to_check = column[line]
            if symbol != symbol_value:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)
    return winnings, winning_line
                


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = [] # column is an empty list
        current_symbols = all_symbols[:]     #add the [:] when you are making copies of a list
        for _ in range(rows):                # does the below for every row
            value = random.choice(current_symbols)
            current_symbols.remove(value) #to remove the recurring values from the list
            column.append(value) # to add the values to the column list
            
        columns.append(column) #to add the column to the columns list
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):     #for every column print the current row we are on, it is transposing
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        print() # gives a newline char after every row
    

def deposit():
    while True:
        amount = input("What would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
        while True:
            lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines.")
            else:
                print("Please enter a number.")
        return lines 

def get_bet():
        while True:
            amount = input("What would you like to bet on each line: $")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print("Amount must be between $" + MIN_BET + "- $" + MAX_BET)
            else:
                print("Please enter a number.")
        return amount

def spin():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print("You do not have enough to bet that amount! Your current balance is lower!")
        else:
            break
    #("You are betting $"+ bet + " on " + lines + " lines. Total bet is equal to: $" + total_bet)
    print(balance, lines, total_bet)
    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)
    
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_value)
    print("you won $", str(winnings))
    print("you won on lines: ", (winning_line))
    return (winning_line - total_bet)
    
    
def main():
    balance = deposit()
    while True:
        print(balance)
        spins = input("Press enter to play(q to quit)")
        if spins == "q":
            break
        balance += spin()
        print(balance)
main()
