from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from app.models import Member


def calendar(request):
    return render(request, 'app/calendar.html', {})

def chartjs(request):
    return render(request, 'app/chartjs.html', {})

def chartjs2(request):
    return render(request, 'app/chartjs2.html', {})

def contacts(request):
    return render(request, 'app/contacts.html', {})

def e_commerce(request):
    return render(request, 'app/e_commerce.html', {})

def echarts(request):
    return render(request, 'app/echarts.html', {})

def fixed_footer(request):
    return render(request, 'app/fixed_footer.html', {})

def fixed_sidebar(request):
    return render(request, 'app/fixed_sidebar.html', {})

def form(request):
    return render(request, 'app/form.html', {})

def form_advanced(request):
    return render(request, 'app/form_advanced.html', {})





def form_buttons(request):
    return render(request, 'app/form_buttons.html', {})

def form_upload(request):
    return render(request, 'app/form_upload.html', {})

def form_validation(request):
    return render(request, 'app/form_validation.html', {})

def form_wizards(request):
    return render(request, 'app/form_wizards.html', {})

def general_elements(request):
    return render(request, 'app/general_elements.html', {})

def glyphicons(request):
    return render(request, 'app/glyphicons.html', {})

def icons(request):
    return render(request, 'app/icons.html', {})

def inbox(request):
    return render(request, 'app/inbox.html', {})

def index(request):
    return render(request, 'app/index.html', {})

def invoice(request):
    return render(request, 'app/invoice.html', {})

def level2(request):
    return render(request, 'app/level2.html', {})

def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        result_dict = {}
        print(user_id)
        try:
            Member.objects.get(user_id=user_id, user_pw=user_pw)
            result_dict['result'] = 'success'
            request.session['user_id'] = user_id
        except Member.DoesNotExist:
            result_dict['result'] = 'fail'
        return JsonResponse(result_dict)

def media_gallery(request):
    return render(request, 'app/media_gallery.html', {})

def morisjs(request):
    return render(request, 'app/morisjs.html', {})

def other_charts(request):
    return render(request, 'app/other_charts.html', {})

def page_403(request):
    return render(request, 'app/page_403.html', {})

def page_404(request):
    return render(request, 'app/page_404.html', {})





def page_500(request):
    return render(request, 'app/page_500.html', {})

def plain_page(request):
    return render(request, 'app/plain_page.html', {})

def pricing_tables(request):
    return render(request, 'app/pricing_tables.html', {})

def profile(request):
    return render(request, 'app/profile.html', {})

def project_detail(request):
    return render(request, 'app/project_detail.html', {})

def projects(request):
    return render(request, 'app/projects.html', {})

def tables(request):
    return render(request, 'app/tables.html', {})

def tables_dynamic(request):
    return render(request, 'app/tables_dynamic.html', {})

def typography(request):
    return render(request, 'app/typography.html', {})

def widgets(request):
    return render(request, 'app/widgets.html', {})





def xx(request):
    return render(request, 'app/xx.html', {})

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


def mypage(request):
    return render(request, 'app/mypage.html', {})

def logout(request):
    try:
        del request.session['user_role']
        del request.session['user_id']
        return redirect('login')
    except:
        return render(request, 'app/login.html', {})
