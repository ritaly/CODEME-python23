def my_function():
    # return 0 /10 -> zero div
    # return int('aaaa') -> value error
    # return "aaa" + 3 -> type error
    x = 10
    my_list = [1,2]
    return my_list[x]

def main():
    try:
        my_function()
    except ValueError as e:
        # handle ValueError exception
        print("Błąd wartosci")

    except (TypeError, ZeroDivisionError) as e:
        print('☀️ ->', e)

    except:
        # handle all other exceptions
        print('Nie mam pojęcia jakim jestem błędem!')

    print('🌞🌞🌞' * 10)

if __name__ == "__main__":
    main()