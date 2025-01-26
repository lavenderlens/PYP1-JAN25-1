total = 0

def add(num):
    global total
    total += num
def sub(num):
    global total
    total -= num
def mul(num):
    global total
    if total != 0:
        total *= num #long hand is total = total * num
def div(num):
    global total
    if total != 0:
        total /= num

def equals():
    global total
    return_value = total
    total = 0
    return return_value

if __name__ == "__main__":
    # we can test our procedural code here
    # and it will not run if funcs imported elsewhere
    add(5)
    sub(2)
    mul(3)
    div(9)
    print(result := equals())
    print(total)

    # expect 1.0
