from rest_framework import routers
from leads.views import LeadsList
from contacts.views import ContactViewSet
from accounts.views import  UserViewSetGuest,UserViewSetPaid,MyTokenObtainPairView,Logout
from venus.views import VenuViewSet
from django.conf.urls import url
from django.urls import include,path
import accounts.views
# from meetings.views import MeetingViewSet
from rest_framework_simplejwt import views as jwt_views
router=routers.DefaultRouter()
router.register(r'paid_user',UserViewSetPaid,basename="paidUser")
router.register('leads',LeadsList)
router.register('contacts',ContactViewSet)
router.register('venu',VenuViewSet)
router.register(r'account_guest',UserViewSetGuest)
#router.register(r'login',MyTokenObtainPairView,basename="login")
#router.register(r'logout',Logout,basename="logout")
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',
                             namespace='rest_framework')),
    #path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #path('login/' , MyTokenObtainPairView.as_view()),
    #path('logout/' ,Logout.as_view())
    ]

# router.register('user',UserList)

# router.register('meetings',MeetingViewSet)
