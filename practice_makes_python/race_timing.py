# prompt user for 10k race time
# when user returns empty string...
# display average time, then exitself.


def race_timing():
    times = []
    while True:
        time = input("Enter 10km run time: ")
        if time == "":
            break
        time = float(time)
        times.append(time)
        result = sum(times)/len(times)
    print(f"Average of {result} over {len(times)} races")


race_timing()
