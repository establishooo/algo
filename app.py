from flask import Flask, render_template
import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية من ملف .env
load_dotenv()

template_dir = os.path.abspath('app/templates')
static_dir = os.path.abspath('app/static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# قراءة المتغيرات البيئية
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    print("تشغيل التطبيق...")
    print(f"مجلد القوالب: {template_dir}")
    print(f"مجلد الملفات الثابتة: {static_dir}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# إضافة هذا السطر في نهاية الملف
application = app