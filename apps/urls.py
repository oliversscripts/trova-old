from apps.trova import *

from apps.forms import *
from apps.functions import *
from apps.models import *
from apps.views import *


urlpatterns = [
    url(r'^$', IndexView, name='index'),
    path('apps/', HomeView, name='home'),
]