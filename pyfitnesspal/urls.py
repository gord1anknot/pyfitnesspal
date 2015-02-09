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

from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import diary_views, food_views
import main

admin.autodiscover()
urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns(
    'main.views',

    url(r'^$', 'home',
        name='pyfitnesspal_home'),
)

urlpatterns += patterns(
    'main.food_views',

    url(r'^foods/$', food_views.IndexView.as_view(),
        name='pyfitnesspal_food_list_all'),
    url(r'^foods/(?P<pk>\d+)/$', food_views.DetailView.as_view(),
        name='pyfitnesspal_food_detail'),
    url(r'^foods/create$', food_views.CreateView.as_view(),
        name='pyfitnesspal_food_create'),
    url(r'^foods/(?P<pk>\d+)/edit$', food_views.UpdateView.as_view(),
        name='pyfitnesspal_food_update'),
)

urlpatterns += patterns(
    'main.diary_views',

    url(r'^diary/$', diary_views.IndexView.as_view(),
        name='pyfitnesspal_diary_list_all'),
    url(r'^diary/(?P<pk>\d+)/$', diary_views.DetailView.as_view(),
        name='pyfitnesspal_diary_detail'),
    url(r'^diary/create$', diary_views.CreateView.as_view(),
        name='pyfitnesspal_diary_create'),
    url(r'^diary/(?P<pk>\d+)/edit$', diary_views.UpdateView.as_view(),
        name='pyfitnesspal_diary_update'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='pyfitnesspal_login'),
    url(r'^logout/$', 'logout',
        {'next_page': 'pyfitnesspal_home'},
        name='pyfitnesspal_logout'),
)
