import sys
import logging

from mailify.settings.base import *  # noqa
from mailify.settings.modules.accounts import *  # noqa
from mailify.settings.modules.databases import *  # noqa
from mailify.settings.modules.files import *  # noqa
from mailify.settings.modules.languages import *  # noqa
from mailify.settings.modules.rest_framework import *  # noqa
from mailify.settings.modules.security import *  # noqa
from mailify.settings.modules.testing import *  # noqa
from mailify.settings.modules.templates import *  # noqa

try:
    from mailify.settings.local import *   # noqa
except ImportError:
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr)
