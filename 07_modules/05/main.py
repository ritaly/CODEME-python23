from areas import count_rectangle_area, count_circle_area, count_square_area

def get_user_rooms():
    rooms = {
        "square": [],
        "circle": [],
        "rectangle": []
    }

    while True:
        options = """ Dostępne kształty pokoi
        1 - kwadrat
        2 - koło
        3 - prostokąt
        0 - jeśli chcesz zakońćzyć dodawnie pokoi
        """
        print(options)
        room_type = input('Jaki rodzaj pokoju chcesz dodać (1,2,3)')

        if room_type == '1':
            a = float(input("Jakiej długości jest ściana[m]:"))
            rooms['square'].append(a)
        elif room_type == '2':
            r = float(input("Jaki promien pokoju [m]:"))
            rooms['circle'].append(r)
        elif room_type == '3':
            a = float(input("Jakiej długości jest ściana A [m]:"))
            b = float(input("Jakiej długości jest ściana B [m]:"))
            rooms['rectangle'].append([a, b])
        elif room_type == '0':
            break
        else:
            print("Nie znam takiego kształtu, SPRÓBUJ JESZCZE RAZ")

    return rooms


def main():
    # rooms = {
    #     "square": [4, 5, 6],
    #     "circle": [3, 4],
    #     "rectangle": [[3, 4], [4, 5], [1, 2]]
    # }
    rooms = get_user_rooms()
    print(rooms)

    total = 0

    for shape, space in rooms.items():
        if shape == "square":
            for wall in space:
                total += count_square_area(wall)

        if shape == "circle":
            for radius in space:
                total += count_circle_area(radius)

        if shape == 'rectangle':
            for walls in space:
                a, b = walls
                total += count_rectangle_area(a, b)


    print("Powierzchnia całkowita", total)




if __name__ == '__main__':
    main()
