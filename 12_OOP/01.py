def uppercase_decorator(text_function):
    def nested():
        txt = text_function()
        return txt.upper()

    return nested


@uppercase_decorator
def get_text():
    return "jakis tekst"

@uppercase_decorator
def get_hello():
    return "hello!"


result = get_text()
print(result)

print(get_hello())