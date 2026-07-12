class Library():
    def __init__(self):
        self.title_to_id = {}
        self.author_to_id = {}
        self.library_registry = {}
        
        self.book_counter = 1 # برای کتاب (Book)
        self.author_counter = 1 # برای نویسنده (Author)
     
    def add_book(self, title, author):
        # اصلاح کانترها
        if title not in self.title_to_id:
            self.title_to_id[title] = self.book_counter
            self.book_counter += 1
            
        if author not in self.author_to_id:
            self.author_to_id[author] = self.author_counter
            self.author_counter += 1
            
        # ثبت در رجیستری
        key = (self.title_to_id[title], self.author_to_id[author])
        self.library_registry[key] = "موجود"
       
    def remove_book(self, title, author):
        # بررسی وجود کلیدها قبل از دسترسی برای جلوگیری از Crash
        b_id = self.title_to_id.get(title)
        a_id = self.author_to_id.get(author)
        
        if b_id and a_id and (b_id, a_id) in self.library_registry:
            del self.library_registry[(b_id, a_id)]
            print(f"کتاب {title} اثر {author} حذف شد.")
        else:
            print(f"کتاب {title} اثر {author} یافت نشد.")
        
    def search_book(self, title):
        b_id = self.title_to_id.get(title)
        if not b_id:
            print(f"کتاب '{title}' اصلاً در سیستم ثبت نشده است.")
            return

        # پیدا کردن تمام نویسندگانی که این کتاب را نوشته‌اند
        authors_found = []
        for (book_id, author_id), status in self.library_registry.items():
            if book_id == b_id:
                # پیدا کردن نام نویسنده از روی ID (برعکس کردن دیکشنری نویسندگان)
                for name, aid in self.author_to_id.items():
                    if aid == author_id:
                        authors_found.append(name)
        
        if authors_found:
            print(f"نویسندگان کتاب '{title}': {', '.join(authors_found)}")
        else:
            print(f"کتاب '{title}' در کتابخانه موجود نیست.")
