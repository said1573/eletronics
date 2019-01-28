from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from app.models import Member, Casend, Bsend


def index(request):
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)

    return render(request, 'app/index.html', {'member': member})

def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        result_dict = {}
        try:
            Member.objects.get(user_id=user_id, user_pw=user_pw)
            result_dict['result'] = 'success'
            request.session['user_id'] = user_id
        except Member.DoesNotExist:
            result_dict['result'] = 'fail'
        return JsonResponse(result_dict)


def register(request):
    if request.method == 'GET':
        return render(request, 'app/register.html', {})
    else:
        result_dict = {}
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_confirm = request.POST['user_pw_confirm']
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']

        if user_id == '' or user_pw == '' or user_pw_confirm == '' or user_name == '' or user_phone == '':
            result_dict['result'] = '공백은 사용할 수 없습니다.'
            return JsonResponse(result_dict)

        elif user_pw != user_pw_confirm:
            result_dict['result'] = '비밀번호 매치 실패'
            return JsonResponse(result_dict)

        else:
            try:
                Member.objects.get(user_id=user_id)
                result_dict['result'] = '이미 가입된 아이디가 있습니다.'
            except Member.DoesNotExist:
                member = Member(user_id=user_id, user_pw=user_pw, user_name=user_name, user_phone=user_phone,
                                )
                member.save()
                result_dict['result'] = 'success'
            return JsonResponse(result_dict)


def change(request):
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    return render(request, 'app/change.html', {'member': member})

def logout(request):
    try:
        del request.session['user_role']
        del request.session['user_id']
        return redirect('login')
    except:
        return render(request, 'app/login.html', {})

def mypage(request):
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)

    return render(request, 'app/mypage.html', {'member': member})

@csrf_exempt
def all_message(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)

        casend = Casend.objects.all()
        context = {
            'casend': casend,
            'member': member,
        }

        return render(request, 'app/all_message.html', context)

    except Exception as e:
        print(e)
        return redirect('all_message')


def send(request):

    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)

    return render(request, 'app/send.html', {'member': member})


def casend(request):
    if request.method == 'GET':
        return render(request, 'app/casend.html', {})
    else:
        result_dict = {}
        address = request.POST['address']
        date = request.POST['date']
        price = request.POST['price']
        ele = request.POST['ele']

        if address == '' or date == '' or price == '' or ele == '':
            result_dict['result'] = '공백은 사용할 수 없습니다.'
            return JsonResponse(result_dict)

        else:
            try:
                user_id = request.session['user_id']
                casend = Casend(address=address, date=date, price=price, ele=ele, user_id_id=user_id
                                )
                casend.save()
                result_dict['result'] = 'success'
            except Exception as e:
                print(e)

            return JsonResponse(result_dict)




def bsend(request):
    if request.method == 'GET':
        return render(request, 'app/bsend.html', {})
    else:
        result_dict = {}
        address2 = request.POST['address2']
        date2 = request.POST['date2']
        price2 = request.POST['price2']
        ele2 = request.POST['ele2']

        if address2 == '' or date2 == '' or price2 == '' or ele2 == '':
            result_dict['result'] = '공백은 사용할 수 없습니다.'
            return JsonResponse(result_dict)

        else:
            try:
                user_id = request.session['user_id']
                bsend = Bsend(address2=address2, date2=date2, price2=price2, ele2=ele2, user_id_id=user_id
                                )
                bsend.save()
                result_dict['result'] = 'success'
            except Exception as e:
                print(e)

            return JsonResponse(result_dict)

def contact(request):
    if request.method == 'GET':
        return render(request, 'app/contact.html', {})

    else:

        return render(request, 'app/contact.html', {})