# Week 4 — Postgres and RDS

## Required Homework/Tasks

## What is Relational Databases?

A collection of data elements with pre-established relationships between them make up a relational database. These things are arranged in a series of tables with rows and columns. To store data about the things that will be represented in the database, tables are utilised. The actual value of an attribute is stored in a field, while each column in a database holds a specific type of data. The table's rows are a group of connected values for a single item or entity. A primary key, which is used to uniquely identify each row in a table, can be used to link rows from different tables together. Without changing the structure of the database tables itself, there are numerous ways to retrieve this data.



![download](https://user-images.githubusercontent.com/88502375/224662059-fe0580e9-e18a-4952-a386-9f2eb8a8221a.png)
#### Why use PostgreSQL?

PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help you manage your data no matter how big or small the dataset.


### Create AWS RDA cruddur instance
```
aws rds create-db-instance \
  --db-instance-identifier cruddur-db-instance \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --engine-version  14.6 \
  --master-username root \
  --master-user-password zxcvbnm321 \
  --allocated-storage 20 \
  --availability-zone us-east-1a \
  --backup-retention-period 0 \
  --port 5432 \
  --no-multi-az \
  --db-name cruddur \
  --storage-type gp2 \
  --publicly-accessible \
  --storage-encrypted \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --no-deletion-protection
```

#### Launch Postgres locally via a container!



```sh
db:
    image: postgres:13-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - '5432:5432'
    volumes: 
      - db:/var/lib/postgresql/data
```

### Create cruddur tables
```sql
CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text,
  handle text
  cognito_user_id text,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```

```sql
CREATE TABLE public.activities (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  message text NOT NULL,
  replies_count integer DEFAULT 0,
  reposts_count integer DEFAULT 0,
  likes_count integer DEFAULT 0,
  reply_to_activity_uuid integer,
  expires_at TIMESTAMP,
  created_at TIMESTAMP default current_timestamp NOT NULL
);
```


#### To connect to psql via psql client cli
```
psql -U postgres -h localhost
```

#### postgres database connected
![week-4-postgres-4](https://user-images.githubusercontent.com/88502375/224666250-edbd6868-31ef-4e9e-bdf5-7e1d67f6e15e.jpg)

#### run commands to check the database properties
![week-4-postgres-5](https://user-images.githubusercontent.com/88502375/224666274-5f89e2f2-bc29-44b5-a3c5-1429193b3280.jpg)

#### connect to cruddur database
![week-4-postgres-6](https://user-images.githubusercontent.com/88502375/224666292-abb3505d-2cbe-4316-b7c5-19afb9a8bb7c.jpg)

#### Creating environment variables for our cruddur database so, it will not ask password everytime we launch it. Also set env for our AWS RDS cruddur instance.
![week-4-postgres-7](https://user-images.githubusercontent.com/88502375/224666322-65de62aa-de06-48ba-999d-4a36bebc990d.jpg)

####  Adding Schema 
![week-4-postgres-8](https://user-images.githubusercontent.com/88502375/224666364-27711e31-bc78-4484-98b9-48caad77a280.jpg)

#### Conntecting to Cruddur database
![week-4-postgres-9](https://user-images.githubusercontent.com/88502375/224666394-b266de6b-2480-4ec2-951e-7560f0fd4e26.jpg)

#### Inserting data into our cruddur database
![week-4-postgres-10](https://user-images.githubusercontent.com/88502375/224666419-41b48efd-dc57-4992-91a4-271121482047.jpg)

#### cruddur instance on AWS RDS with Inbound rules assigned
![week-4-security-rule-13](https://user-images.githubusercontent.com/88502375/224666534-0e7ad2b3-e914-4bf3-8779-7fc6e9639ec9.jpg)


#### Make out AWS RDS instance publicly available, and giving it an IP.
![week-4-security-rule-15](https://user-images.githubusercontent.com/88502375/224674579-89f3e5df-4114-4b3b-af1b-9033d2172c95.jpg)

#### To update our security groups we can do this for access.
![week-4-db-connect-to-aws-rds-14](https://user-images.githubusercontent.com/88502375/224666567-e60ed41e-cdee-4235-80d7-d4cdaadf510b.jpg)


### AWS Lambda
AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced on November 13, 2014. Wikipedia
