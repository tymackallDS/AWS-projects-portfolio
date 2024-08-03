#### Gotta have pandas and boto3

#secrets library used for generating random numbers, strings,bytes, and uuids (universally uniqued identifiers)
import boto3, pandas as pd, numpy as np, os, secrets

### Set the environment variable (for testing)
### os.environ['BUCKET_NAME'] = 'test-bucket-ty1'

### set up a client to interact with s3 using python
s3 = boto3.client('s3')

bucket_name = os.getenv('BUCKET_NAME')

response = client.create_bucket(
    Bucket= bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region,
    },
)

num_of_files = random.randint(1,6)
print(f'number of files: {num_of_files}')

for i in range(num_of_files):
    print(f'i: {i}')
    filename = f'file_{i}.txt'
    output_path = f'/tmp/{filename}'
    #generate random uuid
    generated_uuid = uuid.uuid4()

#open a file in write mode thus creating it locally
with open(output_path, 'w') as file:
    file.write(str(generated_uuid))

with open(output_path, 'rb') as f:
    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=f
    )