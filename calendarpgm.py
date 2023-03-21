def factorial(n):
    fact = 1
    while (n > 1):
        fact = fact * n
        n = n - 1
    return fact

def combinations(n, k):
    num = factorial(n)
    den = factorial(k) * factorial(n - k)
    return num / den


def comb_ways(a, total_num, num_choices):
    num = factorial(num_choices) * factorial(total_num - num_choices)
    den = factorial(a) * factorial(num_choices - a) * factorial(
        (total_num - num_choices) - (num_choices - a)) * factorial(num_choices - a)
    return num / den


def one_ticket_probability(total_num, tickets, num_choices, num_joker, match_num, joker_ball=False):
    outcome_numbers = combinations(total_num, num_choices)
    successful_outcome = tickets
    if joker_ball == True:
        outcome_jokerBall = num_joker
    else:
        outcome_jokerBall = (num_joker) / (num_joker - 1)
    total_outcomes = (outcome_numbers / comb_ways(match_num, total_num, num_choices)) * outcome_jokerBall
    probability_winning = (successful_outcome / total_outcomes)
    print("You're chances of winning are {:.18f}".format(probability_winning))
    print("You're chances of winning are 1 in {}".format(
        total_outcomes / successful_outcome))
    return probability_winning, (total_outcomes / successful_outcome)


total_numbers = 50  # Range
number_choices = 6  # Number of choices
total_jokerBalls = 5  # Number of joker balls
match_numbers = 6  # Countr of matched numbers
Joker_present = True  # Presence of joker ball
tickets = 1  # Total number of tickets bought

for match_numbers in range(match_numbers + 1):
    if (Joker_present):
        print("Joker Ball matches-", end=" ")
    else:
        print("Joker Ball does not match-", end=" ")
    print("Count of Numbers that matched the winning numbers = {}".format(match_numbers))
    one_ticket_probability(total_numbers, tickets, number_choices, total_jokerBalls, match_numbers, Joker_present)
