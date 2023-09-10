import pathlib
import json_log_formatter

from collections import OrderedDict
from contextlib import suppress
from django.conf import settings
from django.utils import timezone

from utils import merge_dict


class ApplicationJSONFormatter(json_log_formatter.JSONFormatter):
    def __init__(self, *args, indent=None, raw_json_fields=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._indent = indent
        self._raw_json_fields = dict.fromkeys(raw_json_fields or ())

    def json_record(self, message, extra, record):
        json_record = super().json_record(message, extra, record)

        filepath = pathlib.Path(record.pathname)
        with suppress(ValueError):
            filepath = filepath.relative_to(settings.BASE_DIR)

        json_record = merge_dict(json_record, OrderedDict(
            level=record.levelname.lower(),
            time=timezone.localtime(timezone=timezone.get_default_timezone()),
            event_source=record.name,
            filename=filepath.as_posix(),
            lineno=record.lineno,
        ))

        return json_record
