#### Gotta have pandas and boto3

#secrets library used for generating random numbers, strings,bytes, and uuids (universally uniqued identifiers)
import boto3, pandas as pd, numpy as np, os, secrets

### set up a client to interact with s3 using python
s3 = boto3.client('s3')

bucket_name = os.getenv('BUCKET_NAME')
print(bucket_name)