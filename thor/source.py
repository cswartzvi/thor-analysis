import logging
import pathlib
from typing import Iterable

import boto3
import box


LOGGER = logging.getLogger(__name__)


def main(cfg: box.Box):
    fetch_s3_data(cfg.source.bucket, cfg.path.data_raw, cfg.source.files)


def fetch_s3_data(bucket: str, destination: str, files: Iterable[str]):
    """Downloads data from AWS S3 to a destination folder.

    Args:
        bucket: The name of the S3 bucket.
        destination: Path of the destination folder.
        keys: An iterable of S3 bucket keys (relative the bucket).
    """
    LOGGER.info(f"Intializing download from S3 bucket {bucket}")
    folder = pathlib.Path(destination)
    folder.mkdir(parents=True, exist_ok=True)
    LOGGER.debug("Intializing S3 client")
    s3_client = boto3.client('s3')
    for file in files:
        LOGGER.info(f"Downloading {file} to {folder}")
        s3_client.download_file(bucket, file, str(folder / pathlib.Path(file).name))
