# Copyright 2015 Bradley Rowe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
import decimal


class PositiveDecimalField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    default_error_messages = {
        'positive': _(u'Add only positive numbers.'),
    }

    def to_python(self, value):
        if value is None:
            return value
        try:
            # model validation
            if value < decimal.Decimal(0):
                raise ValidationError(self.error_messages['positive'])

            return value

        except decimal.InvalidOperation:
            raise ValidationError(self.error_messages['invalid'])
