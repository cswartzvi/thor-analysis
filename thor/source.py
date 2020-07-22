"""Contains functionality to retrive data sources."""

import logging
import pathlib
from typing import Iterable

import boto3
import box


LOGGER = logging.getLogger(__name__)


def main(cfg: box.Box):
    for source in cfg.sources:
        fetch_s3_data(source.bucket, source.folder, source.files, cfg.path.data_raw)


def fetch_s3_data(bucket: str, folder: str, files: Iterable[str], destination: str):
    """Downloads data from AWS S3 to a destination folder.

    Args:
        bucket: The name of the S3 bucket.
        destination: Path of the destination folder.
        keys: An iterable of S3 bucket keys (relative the bucket).
    """
    LOGGER.info(f"Intializing download from S3 bucket {bucket}")
    parent = pathlib.Path(destination)
    parent.mkdir(parents=True, exist_ok=True)
    LOGGER.debug("Intializing S3 client")
    s3_client = boto3.client('s3')
    for file in files:
        url = f"{folder}/{file}"
        LOGGER.info(f"Downloading {url} to {parent}")
        s3_client.download_file(bucket, url, str(parent / file))
