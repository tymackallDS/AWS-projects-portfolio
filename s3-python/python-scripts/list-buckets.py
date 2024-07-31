#FOR ME - to execute code from terminal give all the files in the folder permission to be executed
#using chmod u+x folder/sub-folder/* call python file by python then path file

#!usr/bin/env python


#import boto
import boto3

# initialize a session using s3
s3 = boto3.client('s3')

# get list of buckets
response = s3.list_buckets()

##print(type(response))

# extract bucket names and creation date
buckets = response['Buckets']

# Sort buckets by creation date, most recent first
sorted_buckets = sorted(buckets, key=lambda b: b['CreationDate'], reverse=True)

#check and see if there are more than 10 buckets. if so then only display 10
if len(buckets) >= 10:
  sorted_buckets_to_display = sorted_buckets[:5]
  for bucket in sorted_buckets_to_display:
    print(f"Bucket Name: {bucket['Name']}, Creation Date: {bucket['CreationDate']}")
else:
  for bucket in sorted_buckets:
    print(f"Bucket Name: {bucket['Name']}, Creation Date: {bucket['CreationDate']}")