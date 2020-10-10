# Chapter 7: Storage

# Section 1: Amazon Elastic Block Store

## Storage Options Difference

- What if changing or updating data?

### Block Storage

- Only change the block that contains the character
- Fast and cost less bandwidth but cost more money

### Object Storage

- Entire file must be updated

## Amazon EBS

- Amazon EBS enables you to create individual storage volumes and attach them to an EC2 instance
- Amazon EBS offers block-level storage
- Volumes can be automatically replicated within its Availability Zone
- Can be backed up automatically to Amazon S3 through snapshots
    - Uses differential backup. The first backup is called baseline snapshot

### Uses of Amazon EBS

- Boot volumes and storage for Amazon EC2 instances
- Data storage with a file system
- Database hosts
- Enterprise application

### Snapshots

- Point in time snapshots
- Recreate a new volume at any time
- Added cost of EBS snapshots to Amazon S3 is per GB month of data stored

### Encryption

- Encrypted Amazon EBS volumes
- No additional cost

### Elasticity

- Increase capacity
- Change to different types

### Volumes

- Amazon EBS volumes persist independently from the instance
- All volume types are charged by the amount that is provided per month

### IOPS

- General purpose SSDs are charged by the amount you provision in GB per month until storage is released
- Magnetic is charged by the number of requests to the volume
- Provisioned IOPS SSD is charged by the amount that you provision in IOPS

### Data Transfer

- Inbound data transfer is free
- Outbound data transfer across Regions incurs charges

# Section 2: Amazon Simple Storage Service (S3)

## Overview

- Data is stored as objects in buckets
- Virtually unlimited storage, single object is limited to 5 TB, scales seamlessly as your bucket grows
- Designed for 11 9s of durability (Just read)
- Granular access to bucket and objects
- Data is stored in 3 availability zone by default

## Storage Classes

- Amazon S3 Standard
- Amazon S3 Intelligent-Tiering
- Amazon S3 Standard-Infrequent Access
- Amazon S3 One Zone-Infrequent Access
- Amazon S3 Glacier
- Amazon Glacier Deep Archive

## Lifecycle Policies

![Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175311.png](Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175311.png)

## Uploading Amazon S3 Bucket Data

1. Create a bucket in an AWS Region
2. Upload almost any number of objects to the bucket
3. When data is stored in bucket, it is replicated across 3 availability zones in the region

### Bucket Path-Style URL Endpoint

- [https://s3.<region-code>.amazonaws.com/](https://s3.ap-northeast-1.amazonaws.com/bucket-name)<bucket-name>

### Bucket Virtual-Hosted Style URL Endpoint

- https://<bucket-name>.s3-<region-code>.amazonaws.com

## Access

- AWS Management Console
- AWS CLI
- SDK

## Common Scenarios

- Backup and storage
- Application hosting
- Media hosting
- Software delivery

## Pricing

- Pay only for what you use
    - GBs per month
    - Transfer OUT to other Regions
    - PUT, COPY, POST, LIST and GET requests
- You do not pay for
    - Transfers IN to Amazon S3
    - Transfer OUT from Amazon S3 to Amazon CloudFront or Amazon EC2 in the same Region

## Estimating Costs

### Types of Storage Classes

- Standard storage is designed for high durability and high availability
- S3 Standard Infrequent Access is designed for high durability and lesser availability than standard

### Amount of Storage

- The number and size of objects

### Requests

- The number of requests (GET, PUT, COPY)
- Different rates for GET requests than others

### Data Transfer

- Pricing is based on amount of data being transferred out of S3 Region

## Lifecycle Policies

- Enables you to delete or move objects based on age

    ![Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175311%201.png](Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175311%201.png)

# Section 3: Amazon Elastic File System (EFS)

## Features

- File storage in AWS Cloud with petabyte-scale, low-latency file system
- Works well for big data and analytics, media processing workflows, content management, web serving and home directories
- Shared storage with elastic capacity
- Supports Network File System (NFS) v4.0 and v4.1
- Compatible with all Linux-based AMIs for EC2

## Architecture

![Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_174544.png](Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_174544.png)

## Implementation

1. Create EC2 resources and launch the instance
2. Create Amazon EFS file system
3. Create your mount targets in the appropriate subnets
4. Connect your EC2 instances to the mount targets
5. Verify the resources and protection of your AWS account

## Resources

### File System Mount Target

- Subnet ID
- Security Groups
- Create in a VPC subnet
- One per AZ
- Must be in the same VPC

### File System Tages

- Key-value pairs

# Section 4: Amazon S3 Glacier

## Review

- A data archiving service designed for security, durability and very low cost
- Supports the encryption of data in transit and at rest through SSL or TLS
- The Vault Lock feature enforces compliance through a policy
- Extremely low cost design works well for long-term archiving
- Storage service for low-cost data archiving and long-term backup
- Can configure lifecycle archiving of Amazon S3 content to Amazon S3 glacier

### Three options for access to archives

- Expedited
- Standard
- Bulk

## Common Use Cases

- Media asset archiving
- Healthcare information archiving
- Regulatory and compliance archiving
- Scientific data archiving
- Digital preservation
- Magnetic tape replacement

## Using Amazon S3 Glacier

- AWS Management Console (Limited Operations)
- RESTful Web Services
- Java or .NET SDKs
- Amazon S3 with lifecycle policies

## S3 vs Glacier

![Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175629.png](Chapter%207%20Storage%20fa6fda40a59e495eb7cc5e6b8ec37591/Annotation_2020-06-23_175629.png)

## Security with Glacier

- Control access with IAM
- Glacier encrypts data with AES-256
- Glacier manages your keys for you