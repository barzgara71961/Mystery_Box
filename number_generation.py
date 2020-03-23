import random

NUM_TRIALS = 100
winning = 0

cost = NUM_TRIALS * 5


for item in range(0, NUM_TRIALS):
    #prize = ""
    round_winning = 0

    for thing in range(0, 3):
        prize_num = random.randint(1,100)
       # prize += " "
        if 0< prize_num == 1:
            round_winning += 5
        elif 2< prize_num <= 10:
            round_winning += 2
        elif 11 < prize_num <= 50:
            round_winning += 1
        '''else:
            prize += "lead"'''

    # print("You won {} which is worth {}".format(prize,round_winning))
    winning += round_winning
print("Paid In: ${}".format(cost))
print("pay out: ${}".format(winning))

if winning > cost:
    print("you come out ${} ahead".format(winning - cost))
else:
    print("ha ha loser, you lost ${}".format(cost-winning))