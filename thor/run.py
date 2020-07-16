import click
import logging
from thor.source import main as source_main


tasks = {
    "source": source_main,
}

logger = logging.getLogger(__name__)


def main(task):
    try:
        tasks[task]()
    except Exception:
        logger.error(f"Task {task} failed")
        raise


@click.command()
@click.option(
    "--task",
    type=click.Choice(tasks.keys()),
    required=True,
    help="Name of task to execute",
)
def main_cli(task):
    main(task)
