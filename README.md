Nakula: Twitter Reader and stream producer!
======

Python Library Installation
------------
The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install tweepy
    pip install kafka-python


Configuration
------------
Set environment variables below:

- export TWITTER_CONSUMER_KEY='your twitter-consumer-key'
- export TWITTER_CONSUMER_SECRET='your twitter-consumer-secret'
- export TWITTER_ACCESS_TOKEN='your twitter-access-token'
- export TWITTER_ACCESS_SECRET='your twitter-access-secret'


Kafka Service Installation
------------
You better to switch to java8 to avoid this kind of error:
https://stackoverflow.com/questions/36970622/kafka-unrecognized-vm-option-printgcdatestamps

- sudo add-apt-repository ppa:webupd8team/java
- sudo apt update; sudo apt install oracle-java8-installer
- sudo apt install oracle-java8-set-default

Download Kafka-Zookeeper
------------
wget https://www-us.apache.org/dist/zookeeper/current/zookeeper-3.4.12.tar.gz  
tar -zxf zookeeper-3.4.12.tar.gz  
cd zookeeper-3.4.12  

Create Configuration File
-----
$ vi conf/zoo.cfg

tickTime=2000 
dataDir=/path/to/zookeeper/data  
clientPort=2181  
initLimit=5  
syncLimit=2

Start Zookeeper
----
bin/zkServer.sh start
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic hello-kafka


Download Kafka
----
wget http://archive.apache.org/dist/kafka/0.9.0.0/kafka_2.11-0.9.0.0.tgz  
tar -zxf kafka_2.11-0.9.0.0.tgz  
cd kafka_2.11-0.9.0.0  

Start Service
----
cd src  
python twit_reader.py

To Consume via cmd directly
---
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic hello-kafka
