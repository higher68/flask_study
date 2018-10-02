def mydec(func):
    def new_func():
        print("{}\tこれはいいものだ".format(func.__name__))  # 入力したメソッドにprintを付け加える。
        return func()
    return new_func  # hello+付け加えのメソッドを返す。
@mydec
def hello():
    return "こんにちは。いい天気ですね"
print(hello())
