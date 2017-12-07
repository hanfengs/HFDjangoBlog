from django.conf.urls import url
from article.views import *

# import views

urlpatterns = [

    url(r'^$', hello), #不能这样会报错

    url(r'^test/$', test),

    # url(r'test/(\d)+s', detail)
    url('^test/(\d+)/$', 'article.views.detail'),
]
