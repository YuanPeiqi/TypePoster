try:
    num = int(input("请输入一个正整数"))
    if num < 0:
        raise AttributeError
    i = 1
    sum = 0
    while i <= int(num / 2):
        if num % i == 0:
            sum += i
        i += 1
    if sum == num:
        print("完美数字")
    else:
        print("不是完美数字")
except ValueError:
    print("不是有效数字")
except AttributeError:
    print("请给出一个正数")
