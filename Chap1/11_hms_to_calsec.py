print("*** Converting hh.mm.ss to seconds ***")
hours, minutes, seconds = map(int, input("Enter hh mm ss : ").split())

if minutes >= 60 :
    print(f"mm({minutes}) is invalid!")
elif hours < 0 :
    print(f"hh({hours}) is invalid!")
elif minutes < 0 :
    print(f"mm({minutes}) is invalid!")
elif seconds < 0 :
    print(f"ss({seconds}) is invalid!")
else:
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f"{hours:02}:{minutes:02}:{seconds:02} = {total_seconds:,} seconds")