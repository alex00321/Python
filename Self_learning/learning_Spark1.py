
from operator import add
from pyspark import SparkContext
sc = SparkContext('local','test')
logfile_rdd = sc.textFile("D:/BaiduNetdiskDownload/2.资料/data/agent.log")

mapped_rdd = logfile_rdd.map(
    lambda x: ((x.split(" ")[1],x.split(" ")[4]),1)
)

reduce_rdd = mapped_rdd.reduceByKey(add)

new_mapped_rdd = reduce_rdd.map(
    lambda x: (x[0][0],(x[0][1],x[1]))
)

group_rdd = new_mapped_rdd.groupByKey()

result_rdd = group_rdd.mapValues(
    lambda x: sorted(x,key=lambda x: x[1],reverse=True)[:3]
)
result_rdd.foreach(print)
sc.stop()
