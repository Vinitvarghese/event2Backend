from rest_framework import routers
from leads.views import LeadsList
from contacts.views import ContactViewSet
from accounts.views import  UserViewSetGuest
from accounts_register.views import UserViewSetPaid
from venus.views import VenuViewSet
from django.conf.urls import url
from django.urls import include,path
# from meetings.views import MeetingViewSet

router=routers.DefaultRouter()
router.register(r'paid_user',UserViewSetPaid,basename="paudUser")
router.register('leads',LeadsList)
router.register('contacts',ContactViewSet)
router.register('venu',VenuViewSet)
router.register(r'account_guest',UserViewSetGuest)
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',
                             namespace='rest_framework'))]

# router.register('user',UserList)

# router.register('meetings',MeetingViewSet)
