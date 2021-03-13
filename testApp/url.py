from .views import *
from .views_web import *
from django.urls import path,include 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/test', TestViewSet, basename='user')


urlpatterns = [
    
    path('report/', report, name='report'),
    path('report/create/', createReport, name='create-report'),
    path('report/test/<int:id>/', createTest, name='create-test'),
    path('report/complete/<int:id>/', completeTestResults, name='complete-test-results'),

    # testResultsList
    path('report/list/', testResultsList, name='complete-test-results'),

]  + router.urls