
from operator import add
from pyspark import SparkContext
sc = SparkContext('local','test')
lst_raw_data = [1,2,3,4]

raw_rdd = sc.parallelize(lst_raw_data)

number = sc.accumulator(0)

def func(x: int):
    global number
    number += x
result_rdd = raw_rdd.foreach(func)

print(number.value)

sc.stop()
