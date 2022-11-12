def receiving_num(num):

    for i in range(1,10):
        tmp = 6*i
        left = num-tmp
        if left%23==0:
            big_pack = int(left/23)
            print(f"big pack is {big_pack}, and small pack is {i}")


if __name__ == "__main__":
    
    receiving_num(133)