from pyspark import SparkContext
from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()

def load_config(spark_context: SparkContext):

    spark_context._jsc.hadoopConfiguration().set('fs.s3a.access.key','Nyy86oIKdTOA4HqTAast')
    spark_context._jsc.hadoopConfiguration().set('fs.s3a.secret.key','iALsidLdjQbTNh5T3jZI870exdJa6WOiwuPAIm67')
    spark_context._jsc.hadoopConfiguration().set('fs.s3a.style.access','true')
    spark_context._jsc.hadoopConfiguration().set('fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem')
    spark_context._jsc.hadoopConfiguration().set('fs.s3a.endpoint','http://127.0.0.1:9000')
    spark_context._jsc.hadoopConfiguration().set('fs.s3a.connection.ssl.enabled','false')

load_config(spark.sparkContext)
dataframe=spark.read.json('s3a://orders/*')
dataframe.show()
average=dataframe.agg({'sales':'avg'})
average.show()