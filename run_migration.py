from app import create_app, db
from flask_migrate import upgrade, migrate

app = create_app()
app.app_context().push()

print("بدء عملية الهجرة...")
migrate(message="Initial migration")
print("اكتمال عملية الهجرة...")

print("بدء عملية الترقية...")
upgrade()
print("اكتمال عملية الترقية...")