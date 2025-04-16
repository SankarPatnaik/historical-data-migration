# Historical Data Migration Framework

A low-code, configuration-based data migration framework to pull data from 100+ source systems and upload to Amazon S3.

## 🧩 Features
- Supports Oracle, SQL Server, MongoDB, File Server, and more
- Uses config-driven job definitions
- Low-code: developers only touch YAML files
- Pandas for transformation, Arrow/Parquet for efficient writes
- Uploads to S3 in chosen format

## 🚀 Running a Migration
```bash
python main.py
```

## ✍️ Job Config Example
See `config/sources.yaml` for job structure.

## 🔐 Secrets
Use `.env` or environment variables for AWS credentials.
