def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def generate_random_array(size, min_val, max_val):
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]

def main():
    choice = input("Хотите ввести массив вручную (1) или сгенерировать случайный (2)? ")
    if choice == "1":
        arr = list(map(int, input("Введите массив через пробел: ").split()))
    elif choice == "2":
        size = int(input("Введите размер массива: "))
        min_val = int(input("Введите минимальное значение: "))
        max_val = int(input("Введите максимальное значение: "))
        arr = generate_random_array(size, min_val, max_val)
        print("Сгенерированный массив:", arr)
    else:
        print("Некорректный ввод.")
        return
    
    sorted_arr = bubble_sort(arr)
    print("Отсортированный массив:", sorted_arr)

if __name__ == "__main__":
    main()