import random

numbers = [random.randint(-60, 100) for x in range(50)]

# first task
def first_task():
    prod = 1
    for num in numbers:
        prod *= num
    return prod

# second task
def second_task():
    dividable_7_5 = []
    for y, num in enumerate(numbers):
        if num % 5 == 0 or num % 7 == 0:
            dividable_7_5.append(y)
    return dividable_7_5

# third task
def third_task():
    dividable_3_AND5 = []
    for y, num in enumerate(numbers):
        if num % 3 == 0 and num % 7 == 0:
            dividable_3_AND5.append(y)
    return dividable_3_AND5

# fourth task
def fourth_task():
    all_neg = all(num < 0 for num in numbers)
    return all_neg

# fifth task
def fifth_task():
    between_1_10 = any(1 <= num <= 10 for num in numbers)
    return between_1_10

# sixth task
def sixth_task():
    dividable_18 = sum(1 for num in numbers if num % 18 == 0)
    return dividable_18

# seventh task
def seventh_task():
    min_num = numbers.index(min(numbers))
    return min_num

# eight task
def eight_task():
    sqr_dividable_17_18 = []
    for num in numbers:
        sqr = num**2
        if sqr % 17 == 0 and sqr % 18 == 0:
            sqr_dividable_17_18.append(sqr)
    return sqr_dividable_17_18

# ninth task
def ninth_task():
    neg_w_pos_nbs = False
    for x in range(1, len(numbers) - 1):
        if numbers[x] < 0 and numbers[x - 1] > 0 and numbers[x + 1] > 0:
            neg_w_pos_nbs = True
            break
    return neg_w_pos_nbs

# tenth_task
def tenth_task():
    strictly_inc = all(numbers[x] < numbers[x + 1] for x in range(len(numbers) - 1))
    return strictly_inc

# eleventh_task
def eleventh_task():
    even_nums = [num for num in numbers if num % 2 == 0]
    odd_nums = [num for num in numbers if num % 2 != 0]
    return even_nums, odd_nums

# Collecting results
results = {
    "Szorzatok": first_task(),
    "5-tel vagy 7-tel oszthatóak": second_task(),
    "Első 3-al és 7-tel osztható": third_task(),
    "Mind negatív(?)": fourth_task(),
    "1 és 10 közötti": fifth_task(),
    "Mennyi 18-al osztható": sixth_task(),
    "Legkisebb": seventh_task(),
    "Négyzetszám osztható 17-tel és 18-al": eight_task(),
    "Negatív pozitív szomszédokkal": ninth_task(),
    "Monoton növekvő": tenth_task(),
    "Páros számok": eleventh_task()[0],  # Even numbers
    "Páratlan számok": eleventh_task()[1],  # Odd numbers
}

# Printing the results
for task, result in results.items():
    print(f"{task}: {result}")