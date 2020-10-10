# Module 3: AWS Global Infrastructure Overview

# Learning Outcome

- AWS Global Infrastructure
- AWS Service and service category overview
- Identify the differences between AWS Regions, Availability Zones and edge locations

---

# Part 1: AWS Global Infrastructure

# AWS Global Infrastructure

- Designed and built to deliver a flexible, reliable, scalable and secure cloud computing environment with high quality global network performance

## AWS Region

- An AWS Region is a geographical area
- Data replication across Regions is controlled by you
- Communication between Regions uses AWS backbone network infrastructure
- Each region provides full redundancy and connectivity to the network
- A region usually has two or more Availability Zones

### Factors When Selecting A Region

- Data governance and legal requirements
- Proximity and latency to customers
- Services available in the region
- Costs which vary by region

## Availability Zone

- A fully isolated partition of the AWS infrastructure
- Each AZ consist of discrete data centers
- They are designed for fault isolation
- Replicate data and resources across Availability Zones for resiliency
- They are interconnected using high-speed private networking

## AWS Data Centers

- Designed for security
- Where data resides and data processing occurs
- Each has redundant power, networking, connectivity and is housed in a separate facility
- Location not disclosed and access is restricted

## Edge Locations

- Used to cache copies of your content for faster delivery to users at any location
- Lower latency

## AWS Infrastructure Features

### Elasticity and Scalability

- Dynamic adaption of capacity
- Adapts to accommodate growth

### Fault Tolerance

- Continues operating properly in event of failure
- Built in redundancy of components

### High Availability

- High level of operational performance
- Minimized downtime
- No human intervention needed

---

# Part 2: AWS Services and Service Category Overview

## Storage

### Amazon Simple Storage Service (S3)

- Object storage that offers scalability, security and performance

### Amazon Elastic Block Storage (EBS)

- High performance block storage for use with EC2

### Amazon Elastic File System (EFS)

- Scalable fully managed elastic network file system

### Amazon Glacier

- Secure, durable and low cost storage for data archiving and long term backup

## Compute

### Amazon EC2

- Resizable compute capacity as virtual machines

### Amazon EC2 Auto Scaling

- Automatically add or remove EC2 instances according to conditions you define

### Amazon Elastic Container Service (ECS)

- Highly scalable and high performance container orchestration service

### Amazon EC2 Container Registry

- Store, manage and deploy docker container images

### AWS Elastic Beanstalk

- Deploy and scale web apps and services like Apache and Microsoft IIS

### AWS Lambda

- Run code without configuring or managing servers
- Only charges when code is running

### Amazon Elastic Kubernetes Services (EKS)

- Deploy and manage and scale containerized application that uses Kubernetes

### AWS Fargate

- Compute engine for Amazon ECS to run containers without having to manage servers or clusters

## AWS Database Service

### Amazon Relational Database Service (RDS)

- Easy to setup, operate and scalable relational database in the cloud
- Automates capacity
- Automates time consuming tasks

### Amazon Aurora

- MySQL and PostgreSQL compatible

### Amazon Redshift

- Run analytic queries against data stored locally in Amazon

### Amazon DynamoDB

- Fully managed key value and document NoSQL database
- Built in security, backup, restore and memory caching

## AWS Networking and Content Delivery Service

### Amazon VPC

- Provision logically isolated sections of the AWS cloud to launch AWS resources in a virtual network you define

### Elastic Load Balancing

- Automatically distributes incoming traffic across multiple targets, like EC2 instances

### Amazon Cloudfront

- Fast CDN that securely delivers data, videos, apps, APIs to customers globally with low latency and high transfer speeds

### AWS Transit Gateway

- Customers can connect their Amazon VPCs and their on-premises networks to a single centrally managed gateway

### Amazon Route 53

- Scalable cloud DNS web service to give you a reliable way to route end users to the internet app

### AWS Direct Connect

- A way to establish a dedicated private network connection from your data center or office to AWS
- Reduces costs and increases bandwidth throughput

### AWS VPN

- Provides a secure private tunnel for your network or device to the AWS global network

## AWS Security, Identity and Compliance Services

### AWS Identity and Access Management (IAM)

- Enables you to manage access to AWS services and resources securely

### AWS Organizations

- Allows you to restrict what services and actions are allowed in your accounts

### Amazon Cognito

- Lets you add user authentication and access control to your web and mobile apps

### AWS Artifact

- Provides on demand access to AWS security and compliance reports and select online agreements

### AWS Key Management Service (KMS)

- Enables you to create and manage encryption keys
- Controls the use of encryption across a wide range of AWS services in your application

### AWS Shield

- A managed DDOS protection service that safeguards applications running on AWS

## AWS Cost Management Services

### AWS Cost and Usage Report

- Contains the most comprehensive set of AWS cost and usage data available
- Includes additional metadata of AWS services, pricing and reservations

### AWS Budgets

- Sets custom budgets and alerts you when usage exceeds the budgeted amount

### AWS Cost Explorer

- Allows you to visualize and understand and manage your AWS cost and usage over time

## AWS Management and Governance Services

### AWS Management Console

- A web-based user interface to access AWS account

### AWS Config

- Helps you track resource inventory and changes

### Amazon CloudWatch

- Allows you to monitor and resources and applications

### AWS Auto Scaling

- Allows you to scale multiple resources to meet demand

### AWS Command Line Interface (CLI)

- Provides a unified tool to manage AWS services

### AWS Trusted Advisor

- Helps you to optimize performance and security using AWS best practices

### AWS Well-Architected Tool

- Provides help in reviewing and improving your workloads

### AWS CloudTrail

- Tracks user activity and API usage across your AWS accounts