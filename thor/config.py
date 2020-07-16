import logging.config
import os

import yaml
import box

# Global configuration object
with open('./config/main.yml', 'r') as file:
    cfg = box.Box(yaml.safe_load(file), default_box=True, default_box_attr=None)

os.makedirs(cfg.path.logs, exist_ok=True)

if os.path.exists(cfg.path.log_config):
    with open(cfg.path.log_config, "r") as file:
        logging.config.dictConfig(yaml.safe_load(file))
else:
    raise FileNotFoundError(f"Log configuration file not found: {cfg.path.log_config}")
