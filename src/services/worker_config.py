import os

def get_worker_config():
    return {
        'max_ram_mb': int(os.getenv('WORKER_MAX_RAM_MB', 1024)),
        'concurrency': int(os.getenv('WORKER_CONCURRENCY', 2)),
    }
