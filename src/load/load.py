from google.cloud import storage

def upload_to_gcs(local_path, bucket_name, destination_path):
    print(f"Uploading {local_path} to gs://{bucket_name}/{destination_path}")

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_path)

    blob.upload_from_filename(local_path)

    print("Upload completed.")
