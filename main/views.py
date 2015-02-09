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

from django.shortcuts import get_object_or_404, redirect, render

from .models import Food, DiaryEntry
from .forms import FoodForm, DiaryEntryForm


def home(request):
    return render(request, "main/home.html", {'message': "Hi there!"})


def new_diary_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pyfitnesspal_diary_list_all')
    else:
        form = DiaryEntryForm()
    return render(request, "main/create_diary_entry.html", {'form': form})


def list_all_diary_entries(request):
    entries = DiaryEntry.objects.all()
    return render(request, "main/diary.html", {'diary_entries': entries})
