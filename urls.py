from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.index,name='index'),
             url(r'dhaba/form/$',views.form,name='form'),


             url(r'form1/$',views.form1,name='form1'),
             url(r'form2/$',views.form2,name='form2'),
             ]
