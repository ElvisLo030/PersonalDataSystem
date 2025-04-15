from .settings import *

# 允許調試以便測試靜態文件
DEBUG = True

# 允許指定的域名
ALLOWED_HOSTS = ['41211147.elvislo.tw', 'localhost', '127.0.0.1']

# CSRF設置
CSRF_TRUSTED_ORIGINS = [
    'https://41211147.elvislo.tw',
    'http://41211147.elvislo.tw',
    'https://*.trycloudflare.com'
]

# 安全設置
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 靜態文件配置
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# 添加whitenoise中間件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE

# 啟用靜態文件壓縮和緩存
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
