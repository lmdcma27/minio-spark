from pyspark import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Spark S3 Example") \
    .config("spark.hadoop.fs.s3a.access.key", "Nyy86oIKdTOA4HqTAast") \
    .config("spark.hadoop.fs.s3a.secret.key", "iALsidLdjQbTNh5T3jZI870exdJa6WOiwuPAIm67") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://192.168.49.2:31662") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()



dataframe = spark.read.json('s3a://orders/company_sales.json')

print('2')

average = dataframe.agg({'sales': 'avg'})
print('3')

average.show()
