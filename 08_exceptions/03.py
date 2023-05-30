def get_user_index():
    while True:
        try:
            id = int(input("give me id: "))
            break
        except ValueError:
            print('please try again')

    return id


def main():
    my_list = ["a", "word", 5, 18, 0, 1.15, "XX", 5.55]

    try:
        user_index = get_user_index()
        result = 1 / my_list[user_index]
        print(result)

    except ValueError:
        print("value error")

    except ZeroDivisionError:
        print("zero division error")

    except IndexError:
        print("index error")

    except TypeError:
        print('type error')

    except Exception as e:
        print("mistake:", e)


if __name__ == '__main__':
    main()