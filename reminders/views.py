from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Reminder
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from datetime import date
from .forms import ReminderCreationForm

@login_required
def upcoming_view(request):
    rem = Reminder.objects.filter(user=request.user, date__gte = date.today())
    rem = rem.order_by('date')
    context = {
        'my_reminders': rem,
    }
    return render(request, 'reminders/rem_list_upcoming.html' ,context)

@login_required
def all_view(request):
    rem = Reminder.objects.filter(user=request.user)
    rem = rem.order_by('date')
    context = {
        'my_reminders': rem,
    }
    return render(request, 'reminders/rem_list_all.html' ,context)

@login_required
def detail_view(request,rem_id):
    try:
        rem = Reminder.objects.get(user = request.user, pk = rem_id)
    except Reminder.DoesNotExist:
        raise Http404()
    context = {
        'rem' : rem,
    }
    return render(request, 'reminders/rem_detail.html', context)

@login_required
def remove_view(request,rem_id):
    try:
        rem = Reminder.objects.get(user = request.user, pk=rem_id)
    except Reminder.DoesNotExist:
        raise Http404()
    rem.delete()
    return HttpResponseRedirect(reverse('reminders:upcoming'))

@login_required
def add_reminder_view(request):
    if request.method == 'POST':
        form = ReminderCreationForm(request.POST)
        if form.is_valid():
            rem = form.save(commit=False)
            rem.user = request.user
            rem.save()
            return HttpResponseRedirect(reverse('reminders:upcoming'))
        else:
            return render(request,'reminders/add_reminder.html',{'form':form,
                                                                })

    return render(request,'reminders/add_reminder.html',{'form':ReminderCreationForm()})

@login_required
def update_reminder_view(request,rem_id):
    try:
        rem = Reminder.objects.get(user = request.user, pk=rem_id)
    except Reminder.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        form = ReminderCreationForm(request.POST,instance=rem)
        if form.is_valid():
            rem = form.save(commit=False)
            rem.user = request.user
            rem.save()
            return HttpResponseRedirect(reverse('reminders:upcoming'))
        else:
            return render(request,'reminders/update_reminder.html',{'form':form,
                                                                    'rem_id':rem_id,
                                                                   })
    data = {
        'title':rem.title,
        'detail':rem.detail,
        'date':rem.date,
    }
    return render(request,'reminders/update_reminder.html',{'form':ReminderCreationForm(initial=data),
                                                            'rem_id':rem_id,
                                                           })
    

