# MyLibrary (Python OOP Practice Project)

<div dir="rtl">

## معرفی

این پروژه یک نمونه ساده برای تمرین مفاهیم شیءگرایی (OOP) و ساختار پکیج در پایتون است.

هدف اصلی پروژه، تمرین طراحی کلاس‌ها، ماژول‌ها و ساختاردهی پروژه به صورت یک پکیج قابل نصب است.

---
## ساختار پروژه

' ' ' text
ProjectRoot/
│
├── mylibrary/
│   ├── __init__.py
│   ├── __main__.py
│   └── library.py
│
├── main.py
├── setup.py
├── README.md
└── .gitignore

' ' '
---
##توضیح فایل‌ها

- mylibrary/
  - __init__.py معرفی پوشه به عنوان پکیج پایتون
  - __main__.py امکان اجرای پکیج با دستور python -m mylibrary
  - library.py شامل کلاس‌ها و توابع اصلی پروژه

- main.py
  - فایل اصلی برای اجرای نمونه و تست پروژه

- setup.py
  - تنظیمات نصب و بسته‌بندی پکیج

- .gitignore
  - جلوگیری از اضافه شدن فایل‌های موقت، محیط مجازی و فایل‌های Build به Git

---

## پیش‌نیازها

- Python 3
- آشنایی مقدماتی با PowerShell یا Command Prompt

---

## راه‌اندازی پروژه (Windows)

### 1) ورود به پوشه پروژه

</div>

powershell
cd "$env:USERPROFILE\Desktop\ProjectRoot"


<div dir="rtl">

### 2) ایجاد محیط مجازی (اختیاری ولی توصیه می‌شود)

</div>

powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1


<div dir="rtl">

پس از فعال شدن، ابتدای خط فرمان معمولاً عبارت (.venv) نمایش داده می‌شود.

### 3) نصب پروژه به صورت Editable

</div>

powershell
python -m pip install -e .


<div dir="rtl">

---

## اجرای پروژه

### روش اول

</div>

powershell
python main.py


<div dir="rtl">

### روش دوم

</div>

powershell
python -m mylibrary


<div dir="rtl">

---

## اهداف آموزشی

در این پروژه با مفاهیم زیر آشنا می‌شوید:

- برنامه‌نویسی شیءگرا (OOP)
- طراحی کلاس‌ها و اشیاء
- ساخت پکیج در Python
- استفاده از __init__.py
- استفاده از __main__.py
- نصب پروژه با setup.py
- نصب Editable Package
- استفاده صحیح از .gitignore

---

## توسعه‌های آینده

این پروژه فعلاً آموزشی است اما می‌تواند به پروژه‌های بزرگ‌تر توسعه داده شود، مانند:

- ساخت کتابخانه‌های شخصی Python
- پروژه‌های آموزشی OOP
- انتشار پکیج در PyPI

در آینده می‌توان بخش‌های Features، Examples و Documentation را نیز به این README اضافه کرد.

---

## License

This project is intended for educational purposes.

</div>
