def sumNumber(sum):
    if sum ==1:
        return 1
    #print(sum)
    return sum + sumNumber(sum-1)

print(sumNumber(4))