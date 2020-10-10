# Chapter 8: Database

# Part 1: Amazon Relational Database Service

## Unmanaged vs Managed Services

### Unmanaged

- Scaling, fault tolerance and availability managed by you

### Managed

- Scaling, fault tolerance and availability are typically built into the service

## Challenges of Running Your Own Relational Database

- OS installation and patches
- Software installation and patches
- Server maintenance and energy footprint
- Database backups and high availability
- Data security
- Limits on scalability

## Amazon RDS

- Managed service that sets up and operates a relational database in the cloud
- Cost-efficient and resizable capacity while automating time-consuming admin tasks

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_141544.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_141544.png)

## On-Premises vs EC2 Instance vs RDS

- On-premises you are responsible for everything from optimizing applications, patching and setting up hardware, managing network and power
- EC2 instance you need to patch OS and handle software and backup operations
- RDS or Aurora will automatically scale your database, patch, manage backups and ensure high availability

### RDS

- You manage application optimization
- AWS manages:
    - OS installation and patches
    - Database software installation and patches
    - Database backups
    - High availability
    - Scaling
    - Power and racking and stacking servers
    - Server maintenance

## RDS Instances

### Engines

- MySQL
- Amazon Aurora
- Microsoft SQL server
- PostgreSQL
- MariaDB
- Oracle

### DB Instance Class

- CPU
- Memory
- Network Performance

### DB Instance Storage

- Magnetic
- General purpose SSD
- Provisioned IOPS

## RDS in a VPC

- RDS operates the same regardless of it is in a VPC
- However, best to isolate in a private subnet so Internet cannot access it

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142208.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142208.png)

### High Availability with Multi-AZ Design

- RDS can be configured for multi-AZ design with high availability
- After the design is configured, RDS automatically generates a standby copy of the database instance in another AZ within the same VPC
- After seeding the database copy, it is regularly synced and replicated onto the standby copy

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142353.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142353.png)

## RDS Read Replicas

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142726.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_142726.png)

### Features

- Offers asyncrhonous replication
- Can be promoted to master if needed

### Functionality

- Use for read-heavy database workloads
- Offload read queries from master to reduce load on master
- Can be created in a different Region to satisfy disaster recovery or reduce latency

## RDS Use Cases

### Web and Mobile Applications

- High throughput
- Massive storage scalability
- High availability

### Ecommerce Applications

- Low cost database
- Data security
- Fully managed solution

### Mobile and Online Games

- Rapidly grow capacity
- Automatic Scaling
- Database Mirroring

### When to Use RDS?

- Complex transactions or complex queries
- A medium to high query or write rate, up to 30k IOPS
- No more than a single worker node or shard
- High durability

### When to not use RDS?

- Massive read/write rates
- Sharding due to high data size or throughput demands
- Simple GET or PUT requests and queries that a NoSQL database can handle
- Relational database management system customization, when you need your own customization outside of RDS limitations
- In these scenarios, consider DynamoDB or EC2 instead based on suitability

## RDS Billing

- Clock hour billing incur charges when resources are running
- Database characteritics such as engine, size and memory class
- DB purchase type, on-demand or reserved instances
- Number of DB instances provisioned to handle loads

## RDS Storage

### Provisioned Storage

- No charge for backup storage of up to 100% of provisioned database storage for an active database instance
- After db instance is terminated, backup storage billed per GB per month

### Additional Storage

- Charge per GB per month
- Backup storage in addition to provisioned storage

## RDS Deployment Type and Data Transfer

### Request

- The number of input and output requests made to the database

### Deployment Type

- Storage and I/O charges vary depending on how you deploy
- Single AZ/Multiple AZ

### Data Transfer

- No charge for inbound data transfer
- Tiered charges for outbound data transfer

# Part 2: Amazon DynamoDB

## What is Amazon DynamoDB?

- Fast and flexible NoSQL Database service for any scale
- Virtually unlimited storage
- Items can have differing attributes
- Low-latency queries
- Scalable read/write throughput

## DynamoDB Core Components

- Tables, items and attributes are the core DynamoDB components
- Supports two different kinds of primary keys, Partition keys and partition and sort key

## Partitioning

- As data grows, table is partitioned by key
- Query by key to find items efficiently
- Scan to find items by any attributes, but slower

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_145804.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_145804.png)

## Keys

- Single Key — One partition key
- Compound Key — Partition key and Sort key to form the primary key

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_145947.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_145947.png)

## DynamoDB Features

- Runs exclusively on SSDs
- Supports document and key-value store models
- Replicates your tables automatically across your choice of AWS regions
- Works well for mobile, web, gaming and IOT and others
- Is accessible via console, CLI and API calls
- Has no limits on table size or throughput and has low latency

# Part 3: Amazon Redshift

## What is Amazon Redshift?

- A fast and powerful, fully managed data warehouse that is simple and cost-effective to set up
- Allows you to run complex analytic queries against petabytes of structured data

## Amazon Redshift Abilities

### Redshift Automation and Scaling

- Redshift Manages, Monitors and Scales automatically

### Redshift Compatibility

- Compatible with tools like SQL, Java Database, Open Database Connectivity connectory and enables you to use SQL clients and BI tools of your choice

## Redshift Use Cases

### Enterprise Data Warehouse

- Migrate at a pace where customers are comfortable with
- Experiment without large upfront cost of commitment
- Respond faster to business needs

### Big Data

- Low price point for small customers
- Managed service for ease of deployment and maintenance
- Focus more on data and less on database management

### SaaS

- Scale the data warehouse capacity as demand grows
- Add analytic functionality to applications
- Reduce hardware and software costs

## Redshift Features

- Fast and fully managed data warehouse service
- Easily scale with no downtime
- Columnar storage and parallel processing architecture
- Automatically and continuously monitors cluster
- Encryption built-in

# Part 4: Amazon Aurora

## What is Amazon Aurora?

- Enterprise-class relational database
- Compatible with MySQL or PostgreSQL
- Automate time-consuming tasks like patching and backups

## Amazon Aurora Service Benefits

- Fast and highly available
- Simple and resilient with redo log from every read operation
- Compatible and managed service
- Pay-as-you-go

## Aurora Features

- High performance and scalability
- High availability and durability
- Multiple levels of security
- Compatible with MySQL and PostgreSQL
- Fully Managed

# Right Tools for the Right Job

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151017.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151017.png)

# Database Case Studies

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151752.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151752.png)

- Configuration Database — RDS or Aurora
- Metadata Database — DynamoDB

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151759.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151759.png)

- RDS or Aurora

![Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151806.png](Chapter%208%20Database%2006cfc7a634ca45c5baed139b6316e2e6/Annotation_2020-06-29_151806.png)

- RDS or Aurora