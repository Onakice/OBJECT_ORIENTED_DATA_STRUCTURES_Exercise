bid_input = input("Enter All Bid : ")
bid_list = bid_input.split()

bids = [int(num) for num in bid_list]

if len(bids) < 2:
    print("not enough bidder")
else:
    sorted_bids = sorted(bids, reverse=True)
    max_bids = sorted_bids[0]
    second_bids = sorted_bids[1]

    if max_bids == second_bids:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {max_bids} need to pay {second_bids}")