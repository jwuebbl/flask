import random


def print_bets(bets):
    """ Prints the bets to console for easy debugging. """
    print("Here are the bets made by the user:")
    for bet in bets:
        print("\t" + str(bet))

def is_red_or_black_space(winning_number):
    """ Returns the string "red", "black", or "green" depending on the winning number. """
    if winning_number < 11:
        return "black" if (winning_number % 2) == 0 else "red"
    if winning_number > 10 and winning_number < 19:
        return "red" if (winning_number % 2) == 0 else "black"
    if winning_number > 18 and winning_number < 29:
        return "black" if (winning_number % 2) == 0 else "red"
    if winning_number > 28 and winning_number < 37:
        return "red" if (winning_number % 2) == 0 else "black"
    if winning_number > 36: return "green"
    
def check_bets(bets, cursor, connection, session):
    """ Checks the player's bets and returns their updated account. """
    # Getting the user's account.
    cursor.execute("SELECT * FROM accounts WHERE username = %s", session['username'])
    connection.commit()
    account = cursor.fetchone()
    # Getting the winning number.
    winning_number = random.randint(1,38)
    # Finding the winning categories.
    red_or_black = is_red_or_black_space(winning_number)
    # checking bets.
    for bet in bets:
        users_bet = bet[0].lower()
        amount_bet = bet[1]
        print("\t\tUser's bet:    " + bet[0].lower() + ". \t\tAmount bet: " + bet[1])
        print("\t\tWinning Color: " + red_or_black)
        if users_bet == red_or_black:
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (amount_bet, account[0]))
            connection.commit()
        else:
            cursor.execute("UPDATE accounts SET chips = chips - %s WHERE id = %s", (amount_bet, account[0]))
            connection.commit()