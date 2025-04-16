import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(df, config):
    format = config.get('format', 'parquet')
    table = pa.Table.from_pandas(df)
    filename = f"{uuid.uuid4()}.{format}"
    local_path = f"/tmp/{filename}"

    if format == 'parquet':
        pq.write_table(table, local_path)
    else:
        df.to_csv(local_path, index=False)

    s3 = boto3.client('s3')
    s3.upload_file(local_path, config['s3_bucket'], f"{config['s3_prefix']}{filename}")
    os.remove(local_path)
    print(f"Uploaded {filename} to s3://{config['s3_bucket']}/{config['s3_prefix']}")
