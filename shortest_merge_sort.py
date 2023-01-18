def pick_a_pivot(arr, left, right):

    middle = left + (right - left)//2
    if arr[right] < arr[left] < arr[middle] or arr[middle] < arr[left] < arr[right]:
        return left
    elif arr[right] < arr[middle] < arr[left] or arr[left] < arr[middle] < arr[right]:
        return middle
    else:
        return right


def quick_sort(arr, left, right):
    if right - left + 1 <= 1:
        return

    x = pick_a_pivot(arr, left, right)
    arr[x], arr[right] = arr[right], arr[x]  # put pivot to the right (pivot = arr[right])
    j = left  # the place to insert value less than pivot

    # 'i' looks at all numbers in the array and compares them to pivot
    for i in range(left, right):
        if arr[i] < arr[right]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    # put pivot in its right place
    arr[right], arr[j] = arr[j], arr[right]

    # do the same sort for left side
    quick_sort(arr, left, j - 1)

    # and right side
    quick_sort(arr, j + 1, right)

    return arr

arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(arr, 0, len(arr)-1))
