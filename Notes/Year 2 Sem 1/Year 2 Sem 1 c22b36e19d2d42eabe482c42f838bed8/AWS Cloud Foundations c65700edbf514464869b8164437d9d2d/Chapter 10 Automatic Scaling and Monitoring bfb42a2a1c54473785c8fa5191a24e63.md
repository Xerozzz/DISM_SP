# Chapter 10: Automatic Scaling and Monitoring

# Part 1: Elastic Load Balancing

## Elastic Load Balancing

- Distributes incoming application or network traffic across multiple targets in a single AZ or multiple AZs
- Scales your load balancer as traffic to your application changes over time

## Types of Load Balancers

### Application Load Balancer

- Load balancing of HTTP and HTTPS traffic
- Routes traffic to targets based on content of request
- Provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers
- Operates at the application layer (Layer 7)

### Network Load Balancer

- Load balancing of TCP, UDP and TLS traffic where extreme performance is required
- Routes traffic to targets based on IP protocol data
- Can handle millions of requests per second while maintaining low-latencies
- Is optimized to handle sudden and volatile traffic patterns
- Operates at transport layer (Layer 4)

### Classic Load Balancer

- Load balancing of HTTP, HTTPS, TCP and SSL traffic
- Load balancing across multiple EC2 instances
- Operates at both the application and transport layers (Layer 7 and 4)

## How ELB Works

- With Application and Network Load Balancers, you register targets in target groups, and route traffic to the target groups
- With Classic Load Balancers, you register instances with the load balancer

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_142402.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_142402.png)

## ELB Use Cases

- Highly available and fault-tolerant applications
- Containerized applications
- Elasticity and scalability
- Virtual private cloud (VPC)
- Hybrid environments
- Invoke Lambda function over HTTPS

### Application Load Balancer

- You must support traffic to a containerized application
- You must support HTTPS requests

### Network Load Balancer

- You have extremely spiky and unpredictable TCP traffic
- You need to support a static or Elastic IP address, or an IP target outside a VPC
- You need a load balancer that can handle millions of requests per second while maintaining low latencies

### Classic Load Balancer

- You need simple load balancing with multiple protocols

## Load Balancer Monitoring

- Use CloudWatch metrics to verify that the system is performing as expected and creates an alarm to initiate an action if a metric goes outside an acceptable range
- Access logs to capture detailed information about requests sent to your load balancers
- CloudTrail logs to capture the who, what, when and where of API interactions in AWS services

# Part 2: Amazon CloudWatch

## Monitoring AWS Resources

- To use AWS efficiently, you need insight into your AWS resources
- How do you know when you should launch more EC2 instances
- Is your application's performance or availability being affected by a lack of sufficient capacity
- How much of your infrastructure is actually being used?

## Amazon CloudWatch

- Monitors AWS resources and applications that run on AWS
- Collects and tracks standard and custom metrics
- Alarms to send notifications to an SNS topic and perform EC2 Auto Scaling or other actions
- Uses events to define rules to match changes in AWS environment and route these events to one of more target functions or streams for processing

## CloudWatch Alarms

- Create alarms based on static threshold, anomaly detection, metric math expression
- Specify namespace, metrics, statistics, period, conditions, additional configuration and actions

### Examples of Right and Wrong Alarms Setup

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_144244.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_144244.png)

# Part 3: Amazon EC2 Auto Scaling

## Amazon EC2 Auto Scaling

- Helps you maintain application availability
- Enables you to automatically add or remove EC2 instances according to conditions you define
- Detects impaired EC2 instances and unhealthy applications, and replaces the instances without your intervention
- Provides several scaling options such as Manual, Scheduled, Dynamic, On-Demand and Predictive

## Auto Scaling Groups

- A collection of instances that are treated as a logical grouping for the purposes of automatic scaling and management

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_144931.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_144931.png)

## Scaling Out vs Scaling In

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145001.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145001.png)

## How EC2 Auto Scaling Works

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145030.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145030.png)

## Implementing Dynamic Scaling

![Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145414.png](Chapter%2010%20Automatic%20Scaling%20and%20Monitoring%20bfb42a2a1c54473785c8fa5191a24e63/Annotation_2020-07-13_145414.png)

## AWS Auto Scaling

- Monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost
- Provides a simple, powerful user interface that enables you to build scaling plans for resources like EC2 instances and Spot Fleets, Amazon ECS, DynamoDB tables and indexes as well as Aurora Replicas