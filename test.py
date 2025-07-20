import boto3

s3 = boto3.client('s3')

try:
    s3.put_object(
        Bucket='artun-crime-data',
        Key='test-permissions/test.txt',
        Body='Hello, world!',
        ContentType='text/plain'
    )
    print("✅ Success: You have s3:PutObject permission.")
except Exception as e:
    print("❌ Error:", e)