# MyLibrary (پروژه تمرینی OOP در پایتون)

این پروژه یک نمونه ساده برای تمرین مفاهیم شیءگرایی (OOP) و ساختار پکیج در پایتون است.

---

## ساختار پروژه
```text
ProjectRoot/
├── mylibrary/
│   ├── __init__.py
│   ├── __main__.py
│   └── library.py
├── main.py
├── setup.py
├── README.md
└── .gitignore
"""

راهنمای کامل نصب و اجرا در ویندوز (Windows)
0) رفتن به پوشه پروژه (ProjectRoot) روی Desktop
PowerShell یا Terminal را باز کنید و این دستور را بزنید:

""" cd "$env:USERPROFILE\Desktop\ProjectRoot"  """

1) ساخت محیط مجازی (فقط اگر از قبل ندارید)
اگر پوشه .venv را ندارید، این را اجرا کنید:

""" py -m venv .venv """

2) فعال‌سازی محیط مجازی

"""  .\.venv\Scripts\Activate.ps1  """

بعد از فعال شدن، ابتدای خط ترمینال معمولاً چیزی شبیه (.venv) نمایش داده می‌شود.

3) نصب پروژه به صورت Editable (برای ایمپورت شدن پکیج)
در همان پوشه ProjectRoot اجرا کنید:

""" python -m pip install -e .""""

4) اجرای پروژه
دو روش دارید:

روش 1: اجرای فایل اصلی

""" python main.py """

روش 2: اجرای پکیج

""" python -m mylibrary """

