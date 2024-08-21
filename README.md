# AlgoBot Project

## هيكلية المشروع

```
algobot_project/
│
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── crypto.py
│   │   ├── user.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── crypto.py
│   │   ├── main.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── crypto.py
│   │   ├── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── coingecko_service.py
│   │   ├── market_service.py
│   │   ├── news_service.py
│   │   ├── notification_service.py
│   │   ├── prediction_service.py
│   │   ├── sentiment_service.py
│   │   ├── twitter_service.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── analysis_tasks.py
│   │   ├── crypto_tasks.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── helpers.py
│   │   ├── ml_models.py
│
├── static/
│   ├── css/
│   │   ├── main.css
│   ├── js/
│   │   ├── main.js
│   │   ├── predictions.js
│   ├── images/  (فارغ)
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── index.html
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_models.py
│   ├── test_routes.py
│   ├── test_services.py
│   ├── test_tasks.py
│
├── .env
├── .flake8
├── .gitignore
├── celery_worker.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
└── run.py
```

## شرح المجلدات والملفات

### 1. app/
المجلد الرئيسي الذي يحتوي على جميع ملفات الكود الخاص بالتطبيق.

- `__init__.py`: ملف تهيئة لتحديد مجلد app كموديول بايثون.
- `api/`: المجلد الذي يحتوي على مسارات الـ API.
- `models/`: يحتوي على نماذج قاعدة البيانات.
- `routes/`: يحتوي على مسارات الويب الخاصة بالتطبيق.
- `schemas/`: مخططات التحقق من البيانات قبل إدخالها إلى قاعدة البيانات.
- `services/`: يحتوي على الخدمات التي تتعامل مع البيانات ومعالجة المنطق الخلفي.
- `tasks/`: المهام الخلفية المجدولة باستخدام Celery.
- `utils/`: أدوات مساعدة مثل إرسال البريد الإلكتروني والنماذج الرياضية.

### 2. static/
مجلد يحتوي على الملفات الثابتة مثل CSS و JavaScript والصور.

### 3. templates/
مجلد يحتوي على قوالب HTML.

### 4. tests/
مجلد يحتوي على اختبارات الوحدة.

### 5. الملفات الرئيسية
- `.env`: ملف يحتوي على المتغيرات البيئية مثل مفاتيح API، إعدادات قاعدة البيانات، إلخ.
- `.flake8`: إعدادات Flake8 لتحليل الكود وتحسينه.
- `.gitignore`: ملف يحتوي على الملفات التي يجب تجاهلها من قبل Git.
- `celery_worker.py`: ملف لتشغيل عامل Celery.
- `config.py`: ملف يحتوي على إعدادات التطبيق العامة مثل إعدادات قاعدة البيانات.
- `docker-compose.yml`: ملف إعدادات Docker Compose لتشغيل الخدمات المختلفة.
- `Dockerfile`: ملف يحتوي على تعليمات لإنشاء صورة Docker للتطبيق.
- `poetry.lock` & `pyproject.toml`: ملفات إدارة التبعيات باستخدام Poetry.
- `pytest.ini`: ملف إعدادات pytest لاختبارات الوحدة.
- `README.md`: هذا الملف، يحتوي على إرشادات حول كيفية إعداد وتشغيل المشروع.
- `run.py`: الملف الرئيسي لتشغيل التطبيق.

## التكامل مع APIs الخارجية

1. CoinGecko API
   - يستخدم لجلب بيانات العملات المشفرة وتحديثها باستمرار.
   - يتم تنفيذ التخزين المؤقت باستخدام Redis لتقليل الطلبات الخارجية.

2. GeckoTerminal API
   - يستخدم لجلب بيانات السوق المالي وتقديمها في لوحة التحكم.

3. Alpha Vantage API
   - يستخدم لجلب بيانات الأسهم والاتجاهات السوقية.
   - يتم تنفيذ نماذج تعلم الآلة لتحليل البيانات المتقدمة.

## كيفية تشغيل المشروع

1. قم بتثبيت Poetry إذا لم يكن مثبتاً بالفعل:
    ```
    pip install poetry
    ```

2. قم بتثبيت التبعيات:
    ```
    poetry install
    ```

3. قم بإنشاء ملف `.env` وإضافة المتغيرات البيئية اللازمة (انظر `.env.example`).

4. قم بتشغيل التطبيق:
    ```
    poetry run python run.py
    ```

5. لتشغيل اختبارات الوحدة:
    ```
    poetry run pytest
    ```

6. لتشغيل Celery worker:
    ```
    poetry run celery -A celery_worker.celery worker --loglevel=info
    ```

## ملاحظات إضافية

- تأكد من تثبيت وتشغيل Redis و PostgreSQL قبل تشغيل التطبيق.
- راجع ملف `docker-compose.yml` لمعرفة كيفية تشغيل جميع الخدمات المطلوبة باستخدام Docker.
