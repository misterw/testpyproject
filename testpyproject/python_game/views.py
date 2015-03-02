from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from testpyproject.python_game.models import PythonGameResult
from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return redirect('profile_page')
    else:
        form = UserCreationForm()
    return render(request, "registration/registration_form.html", {
        'form': form,
    })


@login_required(login_url='login')
def profile_page(request):
    if not request.user.is_authenticated():
        return redirect(reverse('login')+'?next=%s' % request.path)
    return render(request, "python_game/index.html", {'statistic': _get_user_statistic(request.user)})


def statistic_page(request):
    statistic_list = PythonGameResult.objects.order_by('score').reverse().all()
    paginator = Paginator(statistic_list, 20)

    page_num = request.GET.get('page')
    try:
        statistics = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        statistics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        statistics = paginator.page(paginator.num_pages)

    return render(request, "python_game/statistic.html", {'statistics': statistics})


@csrf_exempt
@login_required(login_url='login')
def save_result(request):
    if request.method == "POST" and request.is_ajax():
        score = request.POST.get('score')
        try:
            PythonGameResult.objects.save_result(score=score, user=request.user)
            result = _get_user_statistic(request.user)
        except Exception as ex:
            result = {'message': ex.message}
        return HttpResponse(json.dumps(result, ensure_ascii=False)
                            , content_type='application/json')
    return Http404


def _get_user_statistic(user):
    if user.results.count():
        return {
            'best_score': user.results.aggregate(Max('score'))['score__max'],
            'last_score': user.results.latest('id').score,
            'count_of_games': user.results.count()
        }
    else:
        return {
            'best_score': 0,
            'last_score': 0,
            'count_of_games': 0
        }