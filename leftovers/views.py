from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from account_user.models import *

import random

WEEKDAYS = {
    "0" : "Sunday",
    "1" : "Monday",
    "2" : "Tuesday",
    "3" : "Wednesday",
    "4" : "Thursday",
    "5" : "Friday",
    "6" : "Saturday"
}

def index(request):
    avaliable_users = Account_User.objects.filter(currently_offering = True)
    logged_in = False
    avaliabilities = None

    if request.user.is_authenticated():
        logged_in = True
        avaliabilities = Schedule.objects.filter(username=request.user.username)

    print avaliable_users
    print len(avaliable_users)
    return render(request, 'index.html', { 'avaliable_users' : avaliable_users, 'users_exist' : len(avaliable_users) !=0, 'logged_in' : logged_in, 'username' : request.user.username, 'avaliabilities' : avaliabilities })

def scheduler(request):
    return render(request, 'scheduler.html')

def add_schedule(request):
    if request.method == 'POST':
        Schedule.objects.filter(username=request.user.username).delete()
        parse_and_add_schedule(request.POST['schedule'], Account_User.objects.filter(username=request.user.username)[0])
        print request.POST
    return render(request, 'scheduler.html')

def parse_and_add_schedule(request, current_user):
    split = request.split(',')
    for index in range(len(split)-1):
        element = split[index]
        day = element[0]
        times = element[2:len(element)-1].split('-')
        start_time = times[0]
        end_time = times[1]
        print WEEKDAYS[day]
        print start_time
        print end_time
        date_time = Schedule(weekday=WEEKDAYS[day], time_start=start_time, time_end=end_time, username=current_user)
        date_time.save()

def post_page(request):
    cleaned = request.path[6:]
    split = cleaned.split('_')
    ngo = split[0].replace('-', ' ')
    p_id = split[1]
    print ngo
    print p_id

    target_post = NGO_Post.objects.filter(post_id=p_id)
    print target_post[0].title

    all_posts = NGO_Post.objects.all()
    return render(request, 'ngo_post.html', { 'post' : target_post[0], })


def random_elements(num, elements):
    eles = elements.values()
    posts = []
    for element in range(num):
        post_index = int(random.random() * len(eles))
        posts += eles[post_index]
    return posts