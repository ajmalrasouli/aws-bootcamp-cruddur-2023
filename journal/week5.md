# Week 5 — DynamoDB and Serverless Caching

## Required Homework/Tasks

## What is DynamoDB?
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools. DynamoDB uses a proprietary API based on JavaScript Object Notation (JSON).

#### How is data stored in DynamoDB?
Amazon DynamoDB stores data in partitions. A partition is an allocation of storage for a table, backed by solid state drives (SSDs) and automatically replicated across multiple Availability Zones within an AWS Region.

DynamoDB is a non-relational document database. DynamoDB provides faster lookup times as the data is structured in a document-based format. Additionally, DynamoDB does not require a pre-defined schema that helps scale data easily. DynamoDB comprises of three fundamental units known as table, attribute, and items.


### Amazon DynamoDB - Key Facts

|                       |                                              |
| --------------------- | -------------------------------------------- |
|Model|	Key-value Store, Document|
|Website|	aws.amazon.com/­dynamodb/|
|Type|	NoSQL
|Developed by|	Amazon|
|Initial Release Date|	January 18, 2012|
|Cloud-based|	Yes, fully managed, no servers to provision or manage|
|Runnable locally|	No (technically yes, but only for test and dev purposes)|
|Open Source|	No|
|Data scheme|	Schema-less|
|SQL Support|	Generally no, possible via AWS Athena|
|API|	Yes, RESTful HTTP API|
|Supported Languages|	Javascript, Typescript, Java, C# (.Net), Go, Php, Python, Ruby, Perl, Haskell, Erlang|
|Stored Procedures|	No|
|Triggers|	Yes, Streams|
|Consistency|	Eventual|
|Mult-master|	Yes|
|Multi-region|	Yes|
|Transactions| support	Yes, ACID|
|Backups|	Yes, including point-in-time without downtime|
|Monitoring|	Yes, with CloudWatch|
|Capacity modes|	Provisioned (with optional scaling), On-Demand|
|Encryption|	Yes, using KMS customer or AWS managed|
|Scalability|	Yes, up to 10 trillion requests per day and 20M requests per second|
|Caching|	Yes, possible using DynamoDB Accelerator (DAX)|



### Anatomy of DynamoDB
Data in DynamoDB is arranged into "Tables". Each Table consists of "Items". Each "Item" consists of "Attributes".


#### Create a DynamoDB Table Using the AWS Web Console
1. Navigate to the DynamoDB web console.
2. Click Create table.
3. Provide configuration options outlined in the lab instructions.
4. Click Create.

```sh
aws dynamodb create-table \
 --table-name Users \
 --attribute-definitions \
 AttributeName=Name,AttributeType=S \
 AttributeName=Title,AttributeType=S \
  --key-schema \ 
 AttributeName=Name,KeyType=HASH \
 AttributeName=Title,KeyType=RANGE \
 --provisioned-throughput \
 ReadCapacityUnits=10,WriteCapacityUnits=5
```
![week-5-dynamodb-1](https://user-images.githubusercontent.com/88502375/226187565-55c8c7bd-f000-402a-bc0b-216d7b680269.jpg)

![week-5-dynamodb-2](https://user-images.githubusercontent.com/88502375/226187568-4c47ea84-57e5-437e-9a79-0e42c5853fee.jpg)

![week-5-dynamodb-3](https://user-images.githubusercontent.com/88502375/226187570-d75bc764-9647-4c3a-851a-63981fda1662.jpg)


Write item to a table
```sh
aws dynamodb put-item \ --table-name Users \ --item file://item.json
```

Read item from a table
```sh
aws dynamodb get-item \ --table-name Users \ --item file://item.json
```

Delete item from a table
```sh
aws dynamodb delete-item --table-name Users --key file://key.json
```

Delete a table
```sh
aws dynamodb delete-table --table-name Users
```

List table names
```sh
aws dynamodb list-tables
```



References:
https://dynobase.dev/what-is-dynamodb/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/
