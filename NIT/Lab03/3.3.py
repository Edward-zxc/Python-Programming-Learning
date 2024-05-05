class HeightOutOfRangeError(Exception):
    pass
class WeightOutOfRangeError(Exception):
    pass
class InputError(Exception):
    pass

def calculate_standard_weight(height):
    if height < 30 or height > 250:
        raise HeightOutOfRangeError("身高应在30cm到250cm之间。")
    return height - 100

def check_weight_status(actual_weight, standard_weight):
    threshold = 0.05 * standard_weight
    weight_difference_value = actual_weight - standard_weight
    if abs(weight_difference_value) <= threshold:
        print("体重正常")
    elif weight_difference_value > threshold:
        print("体重超标")
    else:
        print("体重不达标")

try:
    height = float(input("请输入身高（厘米）："))
    actual_weight = float(input("请输入体重（千克）："))

    standard_weight = calculate_standard_weight(height)
    check_weight_status(actual_weight, standard_weight)

except ValueError:
    print("输入错误：请输入有效的数字。")
except HeightOutOfRangeError as e:
    print("身高异常：", e)
except WeightOutOfRangeError as e:
    print("体重异常：", e)
except InputError as e:
    print("输入异常：", e)

