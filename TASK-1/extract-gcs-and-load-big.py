from google.cloud import storage
from google.cloud import bigquery
import os
import pandas as pd

def read_from_gcs(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return blob.download_as_text()


bucket_name = os.getenv('BUCKET_NAME')
blob_name = 'tugas.json'
data = read_from_gcs(bucket_name, blob_name)
print(data)

df = pd.DataFrame(eval(data))
print(df)

rows_to_insert = df.to_dict(orient='records')

def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, rows_to_insert)
    if errors:
        print('Encountered errors while inserting rows: {}'.format(errors))
    else:
        print('Successfully insert data')


project_id = os.getenv('PROJECT_ID')
table_id = f'{project_id}.my_dataset.elsa_task1'
write_to_bigquery(table_id, rows_to_insert)
