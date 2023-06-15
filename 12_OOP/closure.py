def closure():
    txt = 'la'
    def inside(number):
        return txt * number
    return inside


func_internal = closure()
result = func_internal(2)
print(result)

# def closure(txt):
#     def inside(number):
#         return txt * number
#     return inside
#
#
# func_internal = closure('lala')
# result = func_internal(2)
# print(result)