from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import traceback
from datetime import datetime
from .models import UserData

def index(request):
    """顯示表單頁面"""
    return render(request, 'user_profile/index.html')

def get_cities(request):
    """返回城市數據的JSON"""
    city_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'city.json')
    with open(city_path, 'r', encoding='utf-8') as f:
        city_data = json.load(f)
    return JsonResponse(city_data)

def get_towns(request, city_id):
    """返回特定城市的鄉鎮數據的JSON"""
    towns_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'towns.json')
    with open(towns_path, 'r', encoding='utf-8') as f:
        towns_data = json.load(f)
    
    city_towns = towns_data.get(city_id, [])
    return JsonResponse({'towns': city_towns})

@csrf_exempt
def submit_form(request):
    """處理表單提交"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # 檢查必填字段
            required_fields = ['name', 'student_id', 'birthdate_year', 'birthdate_month', 'birthdate_day', 'city', 'town']
            missing = [field for field in required_fields if not data.get(field)]
            
            if missing:
                return JsonResponse({
                    'success': False,
                    'message': f'缺少必填欄位: {", ".join(missing)}',
                    'errors': {field: ['此欄位為必填'] for field in missing}
                }, status=400)
            
            # 檢查學號是否已存在
            student_id = data.get('student_id')
            if UserData.objects.filter(student_id=student_id).exists():
                return JsonResponse({
                    'success': False,
                    'message': '學號重複無法儲存',
                    'errors': {'student_id': ['學號重複無法儲存']}
                }, status=400)
            
            # 驗證並創建日期
            try:
                birthdate = datetime.strptime(
                    f"{data['birthdate_year']}-{data['birthdate_month']}-{data['birthdate_day']}",
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'message': '日期格式錯誤',
                    'errors': {'birthdate_day': ['無效的日期組合']}
                }, status=400)
            
            # 創建記錄
            birth_time = data.get('birth_time') or '00:00'
            user_data = UserData(
                name=data['name'],
                student_id=data['student_id'],
                birthdate=birthdate,
                birth_time=birth_time,
                city=data['city'],
                town=data['town'],
                goal=data.get('goal', '')
            )
            
            user_data.save()
            return JsonResponse({'success': True, 'message': '資料提交成功!'})
            
        except Exception as e:
            print("處理請求時發生錯誤:", str(e))
            print(traceback.format_exc())
            return JsonResponse({
                'success': False,
                'message': f'處理請求時發生錯誤: {str(e)}'
            }, status=400)
            
    return JsonResponse({'success': False, 'message': '請使用POST方法提交資料'})
