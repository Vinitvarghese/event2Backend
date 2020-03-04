from rest_framework import routers
from leads.views import LeadsList
from contacts.views import ContactViewSet
from accounts.views import UserViewSetPaid, UserViewSetGuest
from venus.views import VenuViewSet
# from meetings.views import MeetingViewSet

router=routers.DefaultRouter()
router.register('leads',LeadsList)
router.register('contacts',ContactViewSet)
router.register('venu',VenuViewSet)
router.register('account_paid',UserViewSetPaid)
router.register('account_guest',UserViewSetGuest)
# router.register('user',UserList)

# router.register('meetings',MeetingViewSet)
