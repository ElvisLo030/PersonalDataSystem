# 個人資料表單系統
# 41211147 網頁設計期中考實作

這是一個使用 Django 框架開發的個人資料表單系統，支援使用者輸入個人基本資料，並提供縣市及鄉鎮市區的連動選單功能。

## 功能特色

- 個人基本資料輸入
  - 姓名
  - 學號 (唯一識別)
  - 生日 (年月日選擇)
  - 出生時間
  - 居住地區 (縣市/鄉鎮市區連動選單)
  - 追求目標

- 表單驗證
  - 必填欄位檢查
  - 學號重複檢查
  - 日期格式驗證

- 響應式設計
  - 使用 Bootstrap 4.5.2 框架
  - 支援各種裝置尺寸

## 技術規格

- 後端框架：Django 4.2.20
- 資料庫：PostgreSQL
- 前端技術：
  - Bootstrap 4.5.2
  - jQuery 3.5.1
  - AJAX 非同步資料傳輸
- 多語系支援：繁體中文（zh-hant）
- 時區設定：Asia/Taipei

## 系統需求

- Python 3.x
- PostgreSQL 資料庫
- 相依套件（請參考 requirements.txt）

## 安裝說明

1. 安裝所需套件：
   ```bash
   pip install -r requirements.txt
   ```

2. 資料庫設定：
   - 建立 PostgreSQL 資料庫 'middb'
   - 設定資料庫連接參數（settings.py）

3. 執行資料庫遷移：
   ```bash
   python manage.py migrate
   ```

4. 收集靜態檔案：
   ```bash
   python manage.py collectstatic --noinput
   ```

## 專案結構

```
1140415-html-test/
├── manage.py           # Django 管理腳本
├── user_profile/       # 主要應用程式
│   ├── models.py      # 資料模型
│   ├── views.py       # 視圖函數
│   ├── forms.py       # 表單類別
│   └── urls.py        # URL 配置
├── templates/         # 模板文件
│   └── user_profile/
│       └── index.html # 主要表單頁面
├── static/           # 靜態文件
│   └── js/
│       └── form.js   # 前端 JavaScript
└── userdata_project/ # 專案設定
    ├── settings.py   # 開發環境設定
    └── settings_prod.py # 生產環境設定
```

## 執行方式

### 開發環境
```bash
python manage.py runserver
```

### 生產環境
```bash
bash run_production.sh
```

## API 端點

- `GET /api/cities/` - 取得縣市資料
- `GET /api/towns/<city_id>/` - 取得特定縣市的鄉鎮市區資料
- `POST /api/submit/` - 提交表單資料
- `POST /api/external/submit/` - 外部 API 提交介面

## 資料庫結構

### UserData 模型
- name (CharField): 姓名
- student_id (CharField): 學號 (主鍵)
- birthdate (DateField): 生日
- birth_time (TimeField): 出生時間
- city (CharField): 縣市
- town (CharField): 鄉鎮市區
- goal (TextField): 追求目標
