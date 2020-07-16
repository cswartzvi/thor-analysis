import logging
import pathlib
from typing import Iterable

import boto3

from thor.config import cfg


logger = logging.getLogger(__name__)


def main():
    fetch_s3_data(cfg.source.bucket, cfg.path.data_raw, cfg.source.file_keys)


def fetch_s3_data(bucket: str, destination: str, keys: Iterable[str]):
    """Downloads data from AWS S3 to a destination folder.

    Args:
        bucket: The name of the S3 bucket.
        destination: Path of the destination folder.
        keys: An iterable of S3 bucket keys (relative the bucket).
    """
    logger.info(f"Intializing download from S3 bucket {bucket}")
    folder = pathlib.Path(destination)
    folder.mkdir(parents=True, exist_ok=True)
    logger.debug("Intializing S3 client")
    s3_client = boto3.client('s3')
    for key in keys:
        logger.info(f"Downloading {key} to {folder}")
        s3_client.download_file(bucket, key, str(folder / pathlib.Path(key).name))
