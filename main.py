from core.config_loader import load_config
from core.etl_engine import run_migration
import sys
import logging

logging.basicConfig(filename='logs/migration.log', level=logging.INFO)

def main():
    config = load_config("config/sources.yaml")
    for job in config['jobs']:
        run_migration(job)

if __name__ == "__main__":
    main()
