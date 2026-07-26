"""
Upload Raw CSV Files to Google Cloud Storage
Author : Manjit Kumar Sharma
Project: Customer 360 Analytics Platform
"""

from pathlib import Path
from google.cloud import storage

from config import BUCKET_NAME, RAW_DATA_DIR, RAW_GCS


def upload_folder(local_folder=RAW_DATA_DIR, gcs_folder=RAW_GCS):
    """
    Upload all CSV files from the local raw data folder
    to Google Cloud Storage.
    """

    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    uploaded_files = 0

    for file_path in Path(local_folder).glob("*.csv"):

        blob = bucket.blob(f"{gcs_folder}{file_path.name}")

        try:

            blob.upload_from_filename(file_path)

            print(f"✅ Uploaded : {file_path.name}")

            uploaded_files += 1

        except Exception as e:

            print(f"❌ Failed : {file_path.name}")
            print(f"Reason   : {e}")

    print("=" * 60)
    print("Upload Process Completed")
    print("=" * 60)
    print(f"Files Uploaded : {uploaded_files}")
    print(f"Bucket         : {BUCKET_NAME}")
    print(f"GCS Folder     : {gcs_folder}")
    print("=" * 60)


def main():
    upload_folder()


if __name__ == "__main__":
    main()