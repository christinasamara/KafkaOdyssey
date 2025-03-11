# KafkaOdyssey
Kafka-Spark-MongoDB

# Big Data Traffic Explorer 🚦  

A real-time traffic data processing pipeline using **Kafka, Apache Spark, and MongoDB**.  
This project simulates vehicle movement, processes streaming data, and stores the results for analysis.  

## Project Overview  
This project is part of the **Big Data Applications** course at the University of Patras. It involves:  
- Simulating traffic data using the **UXSIM simulator**  
- Streaming vehicle positions via **Kafka**  
- Processing real-time data with **Apache Spark**  
- Storing raw & processed data in **MongoDB**  
- Running queries to analyze traffic trends  

## Tech Stack  
- **Python**  
- **Kafka**
- **Apache Spark**
- **MongoDB**
- **Jupyter Notebooks**

1. **Set up dependencies**  
   - Install Java 8+, Python 3.8+, Jupyter, Kafka, Spark, MongoDB  
2. **Start Kafka & Create a Topic**  
   ```sh
   bin/zookeeper-server-start.sh config/zookeeper.properties  
   bin/kafka-server-start.sh config/server.properties  
   bin/kafka-topics.sh --create --topic vehicles --bootstrap-server localhost:9092
   
   python producer.py  # Sends vehicle data to Kafka
   python consumer.py  # Reads from Kafka
   spark-submit sparkjob.py  # Processes data
   spark-submit mongo_spark.py  # Stores in MongoDB

   python check_mongo.py  # Querying the DB

🚦Driving Forward
