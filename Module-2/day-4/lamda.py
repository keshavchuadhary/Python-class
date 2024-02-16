

# def f_x(x):
#     y = x**2 + 5*x +3
#     return y


# numbers = [1,2,3,4,5,6,7,8,9,10]
# y=[f_x(x) for x in numbers]
# print(y)
# map_example = list(map(f_x, numbers))

# f_name = "This is sagarmatha colloege of sciencs and technology"
# upper_string = f_name.upper()
# upper_string_lambda = lambda x:x.upper()

# def func_upper(word):
#     if word.startswith("c"):
#         a = word.title()
#     else:
#        a= word.upper()
#     return a

# splited_list = f_name.split(" ")
# f_name_ans = list(map(func_upper,splited_list))

# print(f_name_ans)

my_string = "This is world where we live and sleep"


def func_jpt(word, index):
    if index % 2 == 0:
        result_word = word.upper()
    else:
        result_word = word.title()
    return result_word

result = [func_jpt(word,index) for index, word in enumerate(my_string.split())]
print("-".join(result))
