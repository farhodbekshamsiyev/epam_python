import re


class Pagination(object):
    _pages = []
    _whole_text = ''
    _symbols_per_page = 0
    pages_count = 0

    def __init__(self, text: str, symbols_per_page: int = 100):
        self._whole_text = text
        self._symbols_per_page = symbols_per_page

        for i in range(0, len(text), symbols_per_page):
            self._pages.append(text[i:i + symbols_per_page])
        self.pages_count = len(self._pages)
        self.item_count = len(text)

    def count_items_on_page(self, page: int = 0):
        try:
            return len(self._pages[page])
        except IndexError:
            return 'Exception: Invalid index. Page is missing.'

    def find_page(self, text: str):
        if text not in self._whole_text:
            return f"Exception: '{text}' is missing on the pages"
        ans = []
        if len(text) > self._symbols_per_page:
            for i in range(0, len(text), self._symbols_per_page):
                x = text[i:i + self._symbols_per_page]
                for m in re.finditer(x, self._whole_text):
                    ans.append(m.start() // self._symbols_per_page)
        else:
            return [m.start() // self._symbols_per_page for m in re.finditer(text, self._whole_text)]
        return sorted(ans)

    def display_page(self, page: int = 0):
        try:
            return self._pages[page]
        except IndexError:
            return 'Exception: Invalid index. Page is missing.'


pages = Pagination('Your beautiful text', 5)
print(pages.pages_count)
print(pages.item_count)
# print(pages.count_items_on_page(0))
# print(pages.count_items_on_page(3))
# print(pages.count_items_on_page(4))
# print(pages.find_page('Your'))
# print(pages.find_page('e'))
# print(pages.find_page('beautiful'))
# print(pages.find_page('great'))
# print(pages.display_page(0))
