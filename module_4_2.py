# ДЗ модуль 4_2 Пространство имен.
# ===================================
def test_function(txt_):
    def inner_function(txt_):
        txt_ = "Я в области видимости функции test_function"
        return txt_
    result = inner_function("test")
    print(result)
test_function("test")
# result = inner_function("test")
# print(result)
