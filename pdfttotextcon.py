import PyPDF3
import re
# import io
import spacy
import pandas as pd
from spacy.matcher import Matcher
from tabula import read_pdf , convert_into
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf ,SQLContext
from pyspark.sql.functions import trim

# df = read_pdf('Assignment-1.pdf')
convert_into("Assignment-1.pdf", "test.csv", output_format="csv")
convert_into("Assignment-1.pdf", "test_all.csv", output_format="csv",pages="3")

spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
# sc=spark.sparkContext
df=spark.read.option("inferSchema","true").csv("test.csv")
# print(df_all)
df = df.withColumn("Name", trim(df._c0))

arr=["Title","First name","Surname","Company name","Address line 1","Address line 2","Address line 3", "Town/city","Country"]
arr_val=[]
for i in arr:
    result_df=df.filter(df['_c0']==i)
    arr_val.append(result_df.toPandas()._c1.iloc[-1])
# print(arr_val)

Name=''
for element in arr_val[0:3]:
    if isinstance(element, str):
        Name+=element + ' '
Company_name=arr_val[3]
Address=''
for element in arr_val[4:8]:
    if isinstance(element, str):
        Address+=element+' '
# name = ''.join(a for a in arr_val)
# print(name)
print("Name :",Name)
print("Company Name :", Company_name)
print("Address : ", Address)


df_all=spark.read.option("inferSchema","true").csv("test_all.csv")
# df_all = df_all.withColumn("Name", trim(df._c0))
result_df=df_all.filter(df_all['_c0']=="Description of proposed materials and finishes:")
print("Material :")
print(result_df.toPandas()._c1.values)