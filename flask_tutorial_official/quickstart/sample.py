# デコレータの練習
def hello():
    return "こんにちは"
print("normal")
print(hello())

def mydec(f):
    def new_func():
        print("{}が呼び出されました".format(f.__name__))
        return f()
    return new_func

hello = mydec(hello)
print("decotreated")
print(hello())
