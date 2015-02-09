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

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    args = '<username> <password>'
    help = """
    Create a user for pyfitnesspal. If no arguments are passed, read the
    environment variables PYFITNESSPAL_USERNAME and PYFITNESSPAL_PASSWORD,
    and if those are not set, use the default username and password from
    README.md.
    """

    def handle(self, *args, **options):
        if len(args) == 2:
            uname, passwd = args[0], args[1]
        elif 'PYFITNESSPAL_USERNAME' in os.environ and\
                'PYFITNESSPAL_PASSWORD' in os.environ:
            uname, passwd =\
                os.environ['PYFITNESSPAL_USERNAME'],\
                os.environ['PYFITNESSPAL_PASSWORD']
        else:
            uname, passwd = 'demo', 'Passw0rd!'
        try:
            u = User.objects.create_user(
                username=uname,
                password=passwd)
            self.stdout.write(
                'Successfully created user "%s"' % u.username)
        except IntegrityError:
            self.stdout.write(
                'User "%s" already exists.' % u.username)
