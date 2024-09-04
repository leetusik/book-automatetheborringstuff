def funca(lst):
    length = len(lst)
    result = ""
    for index, item in enumerate(lst):
        if index != length - 1:
            result += item + ", "
        else:
            result += "and " + item
    return result


spam = ["apples", "bananas", "tofu", "cats"]

print(funca([]))
