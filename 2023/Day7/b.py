with open("./2023/Day7/input.txt", "r") as f:
    lines = f.read().splitlines()

cards = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}

bids = {}

five, four, full_house, three, two_pair, one_pair, high_card = [[] for _ in range(7)]

from collections import Counter


def rank(hand):
    count = Counter(hand)

    if count["J"] > 0:
        most = count.most_common(1)[0][0]
        if most == "J":
            most = count.most_common(2)[1][0]
        count[most] += count["J"]
        count.pop("J")

    match len(count):
        case 5:
            high_card.append(hand)
        case 4:
            one_pair.append(hand)
        case 3:
            if count.most_common(1)[0][1] == 2:
                two_pair.append(hand)
            else:
                three.append(hand)
        case 2:
            if count.most_common(2)[0][1] == 4:
                four.append(hand)
            else:
                full_house.append(hand)
        case 1:
            five.append(hand)
        case _:
            print(hand, count)
            raise Exception("WTF???")


def order(hands, level):
    if len(hands) < 2:
        return hands

    grouped = sorted(hands, key=lambda x: cards[x[level]], reverse=True)
    sort = []
    i = 0

    while i < len(grouped):
        cur = [grouped[i]]
        j = i + 1
        while j < len(grouped) and grouped[j][level] == grouped[i][level]:
            cur.append(grouped[j])
            j += 1
        sort.append(cur)
        i = j  # Move to the next group of hands

    # Recurse for each group if necessary
    for k in range(len(sort)):
        if len(sort[k]) > 1:
            sort[k] = order(sort[k], level + 1)

    return [item for sublist in sort[::-1] for item in sublist]


for i, line in enumerate(lines):
    hand, bid = line.split()
    # the order will be fixed at the end
    if hand == "JJJJJ":
        hand = "AAAAA"

    bids.update({hand: int(bid)})
    rank(hand)

cur_rank = 1
ans = 0

for hands in [high_card, one_pair, two_pair, three, full_house, four, five]:
    ranked = order(hands, 0)
    if ranked[-1] == "AAAAA":
        # Put "AAAAA" at the start since it's actually meant to be "JJJJJ"
        ranked = [ranked[-1]] + ranked[:-1]

    print(ranked)
    for hand in ranked:
        print(cur_rank, hand, bids[hand])
        ans += cur_rank * bids[hand]
        cur_rank += 1

print(ans)
