import click
import logging
import logging.config
import os

import box
import cerberus
import yaml

from thor.config import main_schema
from thor.source import main as source_main

LOGGER = logging.getLogger(__name__)

TASKS = {
    "source": source_main,
}


def main(cfg: box.Box, task: str):
    """Execute task with specified configuration object."""
    try:
        TASKS[task](cfg)
    except Exception:
        LOGGER.error(f"Task {task} failed")
        raise


@click.command()
@click.option("--config", required=True, help="Name of configuration file",
              type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.option("--task", required=True, help="Name of task to execute",
              type=click.Choice(TASKS.keys()))
def main_cli(config, task):
    """Execution point for command line execution."""

    # Read and validate the YAML file
    with open('./config/main.yml', 'r') as file:
        data = yaml.safe_load(file)
        validator = cerberus.Validator(main_schema)
        if validator.validate(data):
            cfg = box.Box(data, default_box=True, default_box_attr=None)
        else:
            raise KeyError(validator.errors)

    # Initialize the logging from the configuration file
    os.makedirs(cfg.path.logs, exist_ok=True)
    if os.path.exists(cfg.path.log_config):
        with open(cfg.path.log_config, "r") as file:
            logging.config.dictConfig(yaml.safe_load(file))
    else:
        raise FileNotFoundError(f"Log configuration file not found: {cfg.path.log_config}")

    main(cfg, task)
