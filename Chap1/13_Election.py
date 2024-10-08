# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

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
