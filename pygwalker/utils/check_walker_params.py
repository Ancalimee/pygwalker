import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


def check_expired_params(params: Dict[str, Any]):
    expired_params_map = {
        "fieldSpecs": "field_specs",
        "hideDataSourceConfig": "hide_data_source_config",
        "themeKey": "theme_key",
    }

    for old_param, new_param in expired_params_map.items():
        if old_param in params:
            logger.warning(
                f"Parameter `{old_param}` is expired, please use `{new_param}` instead."
            )
