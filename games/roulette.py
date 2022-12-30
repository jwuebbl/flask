import random

def print_bets(bets):
    """ Prints the bets to console for easy debugging. """
    print("Here are the bets made by the user:")
    for bet in bets:
        print("\t" + str(bet))

def is_red_or_black_space(winning_number) -> str:
    """ Returns the string "red", "black", or "green" depending on the winning number. """
    if winning_number < 11:
        return "black" if (winning_number % 2) == 0 else "red"
    if winning_number > 10 and winning_number < 19:
        return "red" if (winning_number % 2) == 0 else "black"
    if winning_number > 18 and winning_number < 29:
        return "black" if (winning_number % 2) == 0 else "red"
    if winning_number > 28 and winning_number < 37:
        return "red" if (winning_number % 2) == 0 else "black"
    if winning_number > 36: return "green"\

def player_has_chips(account) -> bool:
    """ Returns 'True' if the player has more than 0 chips. """
    if account[4] <= 0:
        return False
    return True
    
def is_even(num):
    '''Returns True if a number is even.'''
    if num % 2 == 0:
        return True
    return False

def is_odd(num):
    '''Returns True if a number is odd.'''
    if num % 2 == 1:
        return True
    return False

def is_row_3(num):
    if num % 3 == 0:
        return True
    return False

def is_row_2(num):
    if (num % 3) - 2 == 0:
        return True
    return False

def is_row_1(num):
    if (num % 3) - 1 == 0:
        return True
    return False

def is_first_12(num):
    if num < 13:
        return True
    return False

def is_second_12(num):
    if num > 12 and num < 25:
        return True
    return False

def is_third_12(num):
    if num > 24 and num < 37:
        return True
    return False

def check_bets(bets, cursor, connection, session):
    """ Checks the player's bets and returns their updated account. """
    # Getting the user's account.
    cursor.execute("SELECT * FROM accounts WHERE username = %s", session['username'])
    connection.commit()
    account = cursor.fetchone()

    # If the player has no more chips end their betting.
    if player_has_chips == False:
        return

    # Getting the winning number.
    winning_number = random.randint(1, 38)

    # Finding the winning categories.
    red_or_black = is_red_or_black_space(winning_number)

    # checking bets.
    for bet in bets:
        users_bet = bet[0].lower()
        amount_bet = int(bet[1])
        print(bet)

        # Remove player's chips from the table, if they win a bet their chips are returned with the payout.
        cursor.execute("UPDATE accounts SET chips = chips - %s WHERE id = %s", (amount_bet, account[0]))
        connection.commit()

        # 00 or 0
        if users_bet == "00" and winning_number == 38:
            payout = amount_bet * 36
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        if users_bet == "0" and winning_number == 37:
            payout = amount_bet * 36
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        # Red or Black
        if users_bet == red_or_black:
            payout = amount_bet * 2
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        # 1 to 18
        if users_bet == "1 to 18" and winning_number < 19:
            payout = amount_bet * 2
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        # 19 to 36
        if users_bet == "19 to 36" and winning_number > 18 and winning_number < 37:
            payout = amount_bet * 2
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        # Even and Odd
        if users_bet == "EVEN" and is_even(winning_number) and winning_number < 37:
            payout = amount_bet * 2
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        if users_bet == "ODD" and is_odd(winning_number) and winning_number < 37:
            payout = amount_bet * 2
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        if users_bet == "row 3" and is_row_3(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        if users_bet == "row 2" and is_row_2(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        if users_bet == "row 1" and is_row_1(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()
        # 1st 12
        if users_bet == "1st 12" and is_first_12(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()

        # 2nd 12
        if users_bet == "2nd 12" and is_second_12(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()

        # 3rd 12
        if users_bet == "3rd 12" and is_third_12(winning_number) and winning_number < 37:
            payout = amount_bet * 3
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()

        # Individual Numbers
        if users_bet == str(winning_number):
            payout = amount_bet * 36
            cursor.execute("UPDATE accounts SET chips = chips + %s WHERE id = %s", (payout, account[0]))
            connection.commit()

    return winning_number, red_or_black