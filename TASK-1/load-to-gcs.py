from google.cloud import storage
import os


def write_to_gcs(bucket_name, blob_name, data):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data)


bucket_name = os.getenv('BUCKET_NAME')
blob_name = 'tugas.json'
write_to_gcs(bucket_name, blob_name, 
             '{"name": "Elsa", "age":24, "gender":"Female"},{"name": "Farhan", "age":24, "gender":"Male"},{"name": "Brenda", "age":16, "gender":"Female"}'
)
