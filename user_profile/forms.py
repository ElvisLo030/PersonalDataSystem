from django import forms
from django.core.exceptions import ValidationError
from .models import UserData
from datetime import datetime

class UserDataForm(forms.ModelForm):
    birthdate_year = forms.ChoiceField(label='生日年', required=True)
    birthdate_month = forms.ChoiceField(label='生日月', choices=[(f"{i:02d}", f"{i:02d}") for i in range(1, 13)], required=True)
    birthdate_day = forms.ChoiceField(label='生日日', required=True)
    
    class Meta:
        model = UserData
        fields = ['name', 'student_id', 'birth_time', 'city', 'town', 'goal']
        widgets = {
            'birth_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 設置年份選項
        current_year = 2024
        years = [(str(year), str(year)) for year in range(current_year-30, current_year+1)]
        self.fields['birthdate_year'].choices = [('', '請選擇年份')] + years
        
        # 設置日選項
        days = [(f"{i:02d}", f"{i:02d}") for i in range(1, 32)]
        self.fields['birthdate_day'].choices = [('', '請選擇日期')] + days

    def clean(self):
        cleaned_data = super().clean()
        year = cleaned_data.get('birthdate_year')
        month = cleaned_data.get('birthdate_month')
        day = cleaned_data.get('birthdate_day')
        
        if not all([year, month, day]):
            raise ValidationError('請提供完整的生日日期')
        
        try:
            # 明確地創建日期對象
            date_str = f"{year}-{month}-{day}"
            birthdate = datetime.strptime(date_str, "%Y-%m-%d").date()
            # 直接將birthdate添加到cleaned_data
            cleaned_data['birthdate'] = birthdate
        except ValueError as e:
            raise ValidationError(f'日期格式錯誤: {e}')
        
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # 確保birthdate被設置
        if 'birthdate' in self.cleaned_data:
            instance.birthdate = self.cleaned_data['birthdate']
        
        if commit:
            instance.save()
        return instance 