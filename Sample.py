def get_set_bits(num):

    index_set_bits = []
    idx = 0
    while(1):
        if(num%2):
            index_set_bits.append(idx)
        num = num/2
        idx += 1
        if(num == 0):
            break

    return index_set_bits

def print_subsequences(A, n):

    opsize = pow(2, n)
    for i in range(1, opsize):
        lst = get_set_bits(i)
        for each_idx in lst:
            print(A[each_idx],)
        print

if __name__ == '__main__':
    A = [1,2,3,4]
    print_subsequences(A, len(A))
