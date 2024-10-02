print("*** Election ***")
num_voters = int(input("Enter a number of voter(s) : "))

votes = list(map(int, input().split()))

valid_votes = [vote for vote in votes if 1 <= vote <= 20]
if not valid_votes:
    print("*** No Candidate Wins ***")
else:
    vote_count = {}
    for vote in valid_votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

max_votes = max(vote_count.values())
winners = [candidate for candidate, count in vote_count.items() if count == max_votes]

winners.sort()

print(" ".join(map(str, winners)))