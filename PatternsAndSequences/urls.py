from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.pattern_pruning,name="pattern_pruning")
]