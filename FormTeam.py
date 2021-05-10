def formTeam(d, t, n):
    dev_arr = [0]*(d-1)
    test_arr = [0]*(t-1)
    dev_arr[0] = 1
    test_arr[0] = 1
    for i in range(1, n):
        d_sum = sum(dev_arr) % 1000000007
        t_sum = sum(test_arr) % 1000000007
        dev_arr = [t_sum] + dev_arr
        test_arr = [d_sum] + test_arr
        dev_arr.pop()
        test_arr.pop()

    return (sum(dev_arr) + sum(test_arr)) % 1000000007
