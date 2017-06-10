import math


# provides functions that returns values between [0,2]
class FunProvider:
    fun_list = ["sin", "cos", "tan", "sqrt"]

    @staticmethod
    def sin(x):
        return math.sin(x) + 1

    @staticmethod
    def cos(x):
        return math.cos(x) + 1

    @staticmethod
    def tan(x):
        return math.tan(x / 2) + 1

    @staticmethod
    def sqrt(x):
        if x < 40000:
            return math.sqrt(x) / 100
        else:
            return 2

    @staticmethod
    def get_fun_cycle_len(fun):
        fun_cycle_dict = {'sin': 2*math.pi, 'cos': 2*math.pi, 'tan': math.pi}
        return fun_cycle_dict.get(fun, 99)

    @staticmethod
    def get_fun_from_string(string):
        if string in FunProvider.fun_list:
            return getattr(FunProvider, string)
        elif str.find(string, "x") != -1:
            list_of_values = []
            max_value = 0
            min_value = 0
            for i in range(-100, 100):
                str2 = str.replace(string, "x", str(i))
                eval_value = (eval(str2))
                if eval_value > max_value:
                    max_value = eval_value
                if eval_value < min_value:
                    min_value = eval_value
                list_of_values.append(eval_value)

            # modify elements of counter domain to range [0,2]
            for index, elem in enumerate(list_of_values):
                list_of_values[index] = (elem - min_value) *\
                                        (2.0/(max_value - min_value))

            def fun_fun(x):
                if -100 <= x <= 100:
                    return list_of_values[round(x+100)]
                elif x > 100:
                    return 2
                else:
                    return 0

            return fun_fun
        else:
            print("Error in class: FunProvider method: get_fun_from_string")
            exit(3)

# my_really_fun_fun = FunProvider.get_fun_from_string("x*x+2")
# print(my_really_fun_fun(5))
