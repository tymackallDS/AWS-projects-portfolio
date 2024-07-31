# initialize a session using s3
s3 = boto3.client('s3')

# get list of buckets
s3.list_buckets()

# extract bucket names and creation date
buckets = response('Buckets')

# Sort buckets by creation date, most recent first
sorted_buckets = sorted(buckets, key=lambda b: b['CreationDate'], reverse=True)

for bucket in sorted_buckets:
  print(f"Bucket Name: {bucket['Name']}, Creation Date: {bucket['CreationDate']}")