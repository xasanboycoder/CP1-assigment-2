def classify(value):
    if value < 48:
        return "Below range"
    elif value <= 52:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total / count
n = int(input("Enter the number of cables: "))
total = 0
below = 0
in_range = 0
above = 0
for _ in range(n):
    length = int(input("Enter the cable length: "))
    result = classify(length)
    print(result)

    total += length

    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range += 1
    else:
        above += 1
average = calculate_average(total, n)
print(f"Total length: {total} cm")
print(f"Average length: {average} cm")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")