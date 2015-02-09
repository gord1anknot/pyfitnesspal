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

from django.views import generic

from .models import Food


class IndexView(generic.ListView):
    model = Food


class CreateView(generic.CreateView):
    model = Food


class DetailView(generic.DetailView):
    model = Food


class UpdateView(generic.UpdateView):
    model = Food
