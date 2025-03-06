import statistics
def meanMedianMode(list):
    return [statistics.mean(list),statistics.median(list),statistics.mode(list)]
a,b,c=meanMedianMode([1,2,3,4,5,5,5,6,7,8,9,10,10])
print(f"Mean: {a}, Median: {b}, Mode: {c}")