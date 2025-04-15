from .settings import *

# 啟用調試以便直接提供靜態文件
DEBUG = True

# 允許所有主機 - 在生產環境中應更嚴格
ALLOWED_HOSTS = ['*']

# CSRF設置
CSRF_TRUSTED_ORIGINS = [
    'https://41211147.elvislo.tw',
    'http://41211147.elvislo.tw'
]

# 靜態文件配置
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 確保STATICFILES_DIRS包含您的靜態文件目錄
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
