# استخدام صورة Python الرسمية كصورة أساسية
FROM python:3.9-slim-buster

# تعيين دليل العمل في الحاوية
WORKDIR /app

# نسخ ملفات المتطلبات أولاً لتحسين التخزين المؤقت للطبقات
COPY requirements.txt requirements.txt

# تثبيت المتطلبات
RUN pip install -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تعريف متغير بيئي للتطبيق
ENV FLASK_APP=run.py

# تعريض المنفذ الذي سيعمل عليه التطبيق
EXPOSE 5000

# تشغيل التطبيق
CMD ["flask", "run", "--host=0.0.0.0"]