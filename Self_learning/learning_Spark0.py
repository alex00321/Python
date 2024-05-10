from operator import add
from pyspark import SparkContext
sc = SparkContext('local','test')
lst_raw_data = ["hello scala","hello spark"]

raw_rdd = sc.parallelize(lst_raw_data)

flat_rdd = raw_rdd.flatMap(
    lambda x:x.split(" ")
)

mapped_rdd = flat_rdd.map(
    lambda x: (x,1)
)
#mapped_rdd.cache()
mapped_rdd.persist()
reduced_rdd = mapped_rdd.reduceByKey(add)
print(reduced_rdd.collect())
#################################
print("##################################")

groupby_rdd = mapped_rdd.groupByKey()

groupby_rdd.foreach(print)
