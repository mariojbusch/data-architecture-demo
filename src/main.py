from ingestion.ingest_api import run_ingestion
from transformation.transform import run_transformation
from load.load import upload_to_gcs

def main():
    print("ETL started")

    # 1. Ingestão via API
    data_path = run_ingestion()

    # 2. Transformação
    transformed_path = run_transformation(data_path)

    # 3. Upload para GCS
    bucket = "data-architecture-demo-raw"
    destination = transformed_path.split("/")[-1]
    upload_to_gcs(transformed_path, bucket, f"raw/{destination}")

    print("ETL finished")

if __name__ == "__main__":
    main()
