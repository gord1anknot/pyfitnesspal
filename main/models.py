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

from django.core.urlresolvers import reverse
from django.db.models import CharField, DateField, DateTimeField
from django.db.models import ForeignKey, Model

from .fields import PositiveDecimalField


class Food(Model):
    name =\
        CharField(max_length=300,
                  unique=True)
    serving_size =\
        CharField(max_length=300),
    servings_per_container =\
        PositiveDecimalField(max_digits=7,
                             decimal_places=2,
                             default=1)
    calories =\
        PositiveDecimalField(max_digits=7,
                             decimal_places=2,
                             default=0)
    carbs =\
        PositiveDecimalField(max_digits=6,
                             decimal_places=2,
                             null=True,
                             blank=True)
    fat =\
        PositiveDecimalField(max_digits=6,
                             decimal_places=2,
                             null=True,
                             blank=True)
    protein =\
        PositiveDecimalField(max_digits=6,
                             decimal_places=2,
                             null=True,
                             blank=True)
    cholesterol = PositiveDecimalField(max_digits=6,
                                       decimal_places=2,
                                       null=True,
                                       blank=True)
    sodium = PositiveDecimalField(max_digits=7,
                                  decimal_places=2,
                                  null=True,
                                  blank=True)
    sugar = PositiveDecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    fiber =\
        PositiveDecimalField(max_digits=6,
                             decimal_places=2,
                             null=True,
                             blank=True)
    created =\
        DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('pyfitnesspal_food_detail', args=[str(self.id)])


class DiaryEntry(Model):
    date =\
        DateField(
            help_text=u'Please use the following format: <em>YYYY-MM-DD</em>.')
    notes =\
        CharField(max_length=2000,
                  null=True,
                  blank=True)
    food_consumed =\
        ForeignKey(Food,
                   default=0,
                   unique_for_date="date")
    servings_consumed =\
        PositiveDecimalField(max_digits=6,
                             decimal_places=2,
                             default=0)

    def __unicode__(self):
        return u'%s' % self.date

    def get_absolute_url(self):
        return reverse('pyfitnesspal_diary_detail', args=[str(self.id)])
