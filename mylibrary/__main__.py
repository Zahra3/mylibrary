from .library import Library

def main():
    lib = Library()
    lib.add_book("شاهنامه", "فردوسی")
    lib.add_book("هری پاتر 1", "رولینگ")
    lib.search_book("شاهنامه")

if __name__ == "__main__":
    main()
