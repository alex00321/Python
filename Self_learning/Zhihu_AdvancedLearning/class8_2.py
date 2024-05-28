final_result = {}

def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name+"销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

def middle(key):
    while True:
        # sales_sum 中的返回值是两个元素，故 final_result 中的 value 是 tuple
        final_result[key] = yield from sales_sum(key)
        print(key+"销量统计完成！！.")

def main():
    data_sets = {
        "bobby牌面膜": [1200, 1500, 3000],
        "bobby牌手机": [28,55,98,108 ],
        "bobby牌大衣": [280,560,778,70],
    }
    for key, data_set in data_sets.items():
        print("start key:", key)
        # 在 middle 方法中，调用了 yield from，从而将 yield from sales_sum(key) 的返回值和 当前的 main 函数建立了双向通道 
        m = middle(key)
        m.send(None) # 预激middle协程
        for value in data_set:
            # 不断地向 sales_sum 中发送值，值会被传到 x = yield 中（重点）
            m.send(value)   # 给协程传递每一组的值
        # 下面一行代码会导致 sales_sum 函数中 if not x: break，进而运行 return 语句，从而导致抛出 StopIteration
        m.send(None)
    print("final_result:", final_result)

if __name__ == '__main__':
    main()