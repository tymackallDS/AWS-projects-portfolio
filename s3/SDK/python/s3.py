# Import necessary libraries
import boto3  # AWS SDK for Python
import pandas as pd  # Data manipulation and analysis
import numpy as np  # Numerical operations
import os  # Operating system interactions
import secrets  # For generating cryptographically secure random numbers and strings
import random  # For generating random numbers
import uuid  # For generating universally unique identifiers (UUIDs)

# Set the environment variable for the S3 bucket name (for testing)
os.environ['BUCKET_NAME'] = 'test-bucket-ty1'

# Set up a client to interact with Amazon S3 using Python's boto3 library
s3 = boto3.client('s3')

# Retrieve the bucket name from the environment variable
bucket_name = os.getenv('BUCKET_NAME')
# Define the AWS region for the S3 bucket (N. Virginia does not require LocationConstraint)
region = 'us-east-1'

# Create an S3 bucket
# FUN FACT: For the us-east-1 region (N. Virginia), 
# you typically don’t need to specify LocationConstraint. If you do, 
# it can result in an InvalidLocationConstraint error
response = s3.create_bucket(Bucket=bucket_name)

# Print the response from the bucket creation operation

# Generate a random number of files to create (between 1 and 6)
num_of_files = random.randint(1, 6)
print(f'Number of files: {num_of_files}')

# Create a random number of files and upload them to the S3 bucket
for i in range(num_of_files):
    print(f'Processing file index: {i}')
    
    # Define the filename and output path
    filename = f'file_{i}.txt'
    output_path = f'/tmp/{filename}'
    
    # Generate a random UUID
    generated_uuid = uuid.uuid4()  # Call the uuid4 function to generate a UUID

    # Open the file in write mode to create it locally and write the UUID to it
    with open(output_path, 'w') as f:
        f.write(str(generated_uuid))

    # Open the file in read-binary mode and upload it to the S3 bucket
    with open(output_path, 'rb') as f:
        s3.put_object(
            Bucket=bucket_name,
            Key=filename,
            Body=f
        )

    # Optional: Print a message to confirm the file upload
    print(f'Uploaded {filename} to bucket {bucket_name}')