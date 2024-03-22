import random

def generate_random_number(start, end):
    return random.randint(start, end)

def binary_search(target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if mid == target:
            return mid
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def play_game():
    start_range = 1
    end_range = 100
    secret_number = generate_random_number(start_range, end_range)
    attempts = 0
    max_attempts = 10

    print("Selamat datang di Game Tebak Angka!")
    print("Komputer telah memilih sebuah angka di antara", start_range, "dan", end_range)

    while attempts < max_attempts:
        guess = int(input("Masukkan tebakan Anda: "))

        if guess < start_range or guess > end_range:
            print("Tebakan Anda di luar jangkauan yang ditentukan. Coba lagi.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Selamat! Anda menebak angka dengan benar dalam", attempts, "percobaan.")
            return

        if guess < secret_number:
            print("Tebakan Anda terlalu rendah.")
        else:
            print("Tebakan Anda terlalu tinggi.")

    print("Sayang sekali, Anda telah melebihi batas percobaan.")
    print("Angka yang benar adalah", secret_number)

play_game()
