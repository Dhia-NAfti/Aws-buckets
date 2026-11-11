import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def list_s3_buckets():
    # Initialize the S3 client. Boto3 automatically detects the
    # credentials you just set up via 'aws configure'.
    s3_client = boto3.client("s3")

    try:
        print("Connecting to AWS S3 from Google Cloud Shell...")
        response = s3_client.list_buckets()

        buckets = response.get("Buckets", [])

        if not buckets:
            print(
                "Connection successful! However, "
                "no S3 buckets were found in this account."
            )
        else:
            print(f"Connection successful! Found {len(buckets)} bucket(s):")
            for bucket in buckets:
                print(f"  - {bucket['Name']}")

    except NoCredentialsError:
        print("Error: AWS credentials not found. Please run 'aws configure' first.")
    except ClientError as e:
        print(f"AWS Permission or Client Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    list_s3_buckets()
