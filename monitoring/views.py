from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.utils import timezone

from users_control.models import CustomUser
# Create your views here.


def dashboard(request):
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_ids = [s.get_decoded().get('_auth_user_id') for s in active_sessions if "_auth_user_id" in s.get_decoded()]
    online_users = CustomUser.objects.filter(id__in=user_ids)

    total_users = CustomUser.objects.count()

    return render(request, 'for_admin/monitoring_dash.html', {
        'online_users_count': online_users,
        'total_users': total_users,
    })

