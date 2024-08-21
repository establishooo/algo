import sys
import subprocess
from app import create_app, db
from flask_migrate import Migrate

print("بدء تنفيذ السكريبت", file=sys.stderr)

try:
    app = create_app()
    print("تم إنشاء التطبيق بنجاح", file=sys.stderr)
except Exception as e:
    print(f"حدث خطأ أثناء إنشاء التطبيق: {str(e)}", file=sys.stderr)
    sys.exit(1)

migrate = Migrate(app, db)
print("تم تهيئة Migrate", file=sys.stderr)

def run_migration():
    print("داخل سياق التطبيق", file=sys.stderr)
    
    print("بدء عملية الهجرة...", file=sys.stderr)
    try:
        result = subprocess.run(["flask", "db", "revision", "--autogenerate", "-m", "Initial migration"], capture_output=True, text=True)
        print(f"مخرجات عملية الهجرة:\n{result.stdout}", file=sys.stderr)
        print(f"أخطاء عملية الهجرة (إن وجدت):\n{result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"حدث خطأ أثناء عملية الهجرة: {str(e)}", file=sys.stderr)
    
    print("بدء عملية الترقية...", file=sys.stderr)
    try:
        result = subprocess.run(["flask", "db", "upgrade"], capture_output=True, text=True)
        print(f"مخرجات عملية الترقية:\n{result.stdout}", file=sys.stderr)
        print(f"أخطاء عملية الترقية (إن وجدت):\n{result.stderr}", file=sys.stderr)
    except Exception as e:
        print(f"حدث خطأ أثناء عملية الترقية: {str(e)}", file=sys.stderr)

if __name__ == '__main__':
    with app.app_context():
        run_migration()

print("انتهاء تنفيذ السكريبت", file=sys.stderr)