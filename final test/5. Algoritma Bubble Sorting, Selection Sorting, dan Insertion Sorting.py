# =============================================
#   Algoritma Bubble Sort, Selection Sort,
#   dan Insertion Sort
#   By: Muttia Zalzabila.S
# =============================================

# ------------------------------
# 1. Bubble Sort
# ------------------------------
def bubble_sort(data):
    arr = data.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ------------------------------
# 2. Selection Sort
# ------------------------------
def selection_sort(data):
    arr = data.copy()
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ------------------------------
# 3. Insertion Sort
# ------------------------------
def insertion_sort(data):
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ===============================
#           MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    data = [5, 3, 8, 1, 2]

    print("Data Awal =", data)
    print()

    print("Hasil Bubble Sort   =", bubble_sort(data))
    print("Hasil Selection Sort =", selection_sort(data))
    print("Hasil Insertion Sort =", insertion_sort(data))
