def get_number():
    try:
        number = int(input("Введите число: "))
    except Exception:
        print("Вы ввели не число. Попробуйте ещё раз!")
        number = get_number()
    return number

# def get_int_ranged_list():
#     start_range = get_number()
#     end_range = get_number()
#     my_list = list(range(start_range, end_range))
#     return my_list
    