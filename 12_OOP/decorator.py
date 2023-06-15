def hau_decorator(func_as_param):
    def hau_inside():
        print('hau~' * 10)
        func_as_param()
        print('hau~' * 10)

    return hau_inside

@hau_decorator
def describe_dog():
    print("Pies to najwspanialszy przyjaciel człowieka")
@hau_decorator
def show_text():
    print("Lubię placki")

show_text()
describe_dog()
