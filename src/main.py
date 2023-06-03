def distribute_expenses(participants_f, expenses_f):
    num_participants = len(participants_f)
    total_expenses = sum(expenses_f)
    average_expense = total_expenses / num_participants
    balance = {participant: (average_expense*cost_factor) - expenses_f[i] for i, (participant, cost_factor) in enumerate(participants_f.items())}

    transactions_f = []

    iterations = 0
    max_iterations = num_participants ** 2  # Set a maximum number of iterations

    while any(v > 0.009 for v in balance.values()) and iterations < max_iterations:
        max_creditor = max(balance, key=balance.get)
        max_debtor = min(balance, key=balance.get)

        if balance[max_creditor] > abs(balance[max_debtor]):
            amount_f = abs(balance[max_debtor])
            balance[max_creditor] -= amount_f
            balance[max_debtor] = 0
        else:
            amount_f = balance[max_creditor]
            balance[max_creditor] = 0
            balance[max_debtor] += amount_f

        transaction = (max_debtor, max_creditor, amount_f)
        transactions_f.append(transaction)

        iterations += 1

    return transactions_f


if __name__ == '__main__':
    nights = 3
    participants_with_nights = {
        "K": 3,
        "V": 3,
        "Bu": 3,
        "Bo": 3,
        "Kr": 3,
        "Br": 3,
        "A": 1
    }
    expenses = [
        364.26,
        253.73,
        52.92,
        33.0,
        22.5,
        20.0,
        0.0
    ]
    sum_personnights = sum(participants_with_nights.values())
    participants_with_costfactor = {
        p: n / sum_personnights * len(participants_with_nights) for p, n in participants_with_nights.items()
    }

    transactions = distribute_expenses(participants_with_costfactor, expenses)

    print(f"Split costs:")
    for debtor, creditor, amount in transactions:
        print(f"{debtor} gets €{amount:.2f} from {creditor}")