def tribonacci_seq(count):
    a = []
    result = 1
    for i in range(1, count + 1):
        a.append(result)
        print(result)
        result = sum(a)
        if i > 2:
            a.pop(0)


seq_length = int(input())
tribonacci_seq(seq_length)
