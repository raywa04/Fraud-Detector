from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Initialize Spark session
spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

# Load data from PostgreSQL
url = "jdbc:postgresql://localhost:5432/fraud_detection_db"
properties = {
    "user": "your_db_user",
    "password": "your_db_password",
    "driver": "org.postgresql.Driver"
}

df = spark.read.jdbc(url=url, table="tweets", properties=properties)

# Prepare data for ML model
assembler = VectorAssembler(inputCols=["sentiment"], outputCol="features")
data = assembler.transform(df)
data = data.select("features", col("fraud_label").alias("label"))

# Train Logistic Regression model
train, test = data.randomSplit([0.8, 0.2], seed=12345)
lr = LogisticRegression()
model = lr.fit(train)

# Evaluate model
results = model.transform(test)
evaluator = BinaryClassificationEvaluator()
accuracy = evaluator.evaluate(results)
print(f"Accuracy: {accuracy}")

# Save the model
model.write().overwrite().save("fraud_detection_model")
