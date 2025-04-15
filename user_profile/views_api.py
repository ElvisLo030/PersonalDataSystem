from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .forms import UserDataForm

@csrf_exempt
def api_submit_form(request):
    """處理API表單提交"""
    if request.method == 'POST':
        try:
            # 嘗試從JSON解析數據
            try:
                data = json.loads(request.body)
            except json.JSONDecodeError:
                # 如果不是JSON，嘗試從POST數據獲取
                data = request.POST.dict()
            
            # 創建表單實例並填充數據
            form_data = {
                'name': data.get('name'),
                'student_id': data.get('student_id'),
                'birthdate_year': data.get('birthdate_year'),
                'birthdate_month': data.get('birthdate_month'),
                'birthdate_day': data.get('birthdate_day'),
                'birth_time': data.get('birth_time') or '00:00',
                'city': data.get('city'),
                'town': data.get('town'),
                'goal': data.get('goal') or '',
            }
            
            form = UserDataForm(form_data)
            
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True, 'message': '資料提交成功!'})
            else:
                return JsonResponse({'success': False, 'errors': form.errors})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
            
    return JsonResponse({'success': False, 'message': '請使用POST方法提交資料'})
