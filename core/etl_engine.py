from connectors import oracle, sql_server, mongodb, datfile
from core.file_writer import upload_to_s3
import logging

def run_migration(job):
    source_type = job['source']['type']
    reader = {
        'oracle': oracle,
        'sql_server': sql_server,
        'mongodb': mongodb,
        'dat': datfile
    }.get(source_type)

    if not reader:
        logging.error(f"Unsupported source type: {source_type}")
        return

    df = reader.read(job['source'])
    upload_to_s3(df, job['target'])
