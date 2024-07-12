def get_fibonacci(n):
    Sum = 1
    series = [1]
    for i in range(n):
        series.append(Sum)
        Sum+=series[i]
    return Sum   
