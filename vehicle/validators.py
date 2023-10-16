import re

from rest_framework.exceptions import ValidationError


class NameValidator:

    reg = r"^[a-zA-Z0-9\.\- ]+$"

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)

        if not bool(re.match(self.reg, tmp_value)):
            raise ValidationError("FORBIDDEN SYMBOLS")
