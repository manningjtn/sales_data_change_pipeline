import boto3
import requests
from datetime import datetime

S3_BUCKET = "sales-data-update-with-scdtype1"
S3_FOLDER = "change-data/"

GITHUB_URL = "https://raw.githubusercontent.com/manningjtn/sales_data_change_pipeline/dev/customer_change_data%20%283%29.csv"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

s3 = boto3.client("s3")

def main():
    response = requests.get(GITHUB_URL, timeout=60)
    response.raise_for_status()

    s3_key = f"{S3_FOLDER}customer_change_data_{timestamp}.csv"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=s3_key,
        Body=response.content
    )

    print(f"Uploaded to s3://{S3_BUCKET}/{s3_key}")

if __name__ == "__main__":
    main()