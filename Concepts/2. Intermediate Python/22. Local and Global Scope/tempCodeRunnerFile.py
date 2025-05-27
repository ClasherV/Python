def display():
    a=20
    def show():
        global a
        a=30
        print(a)
    show()
display()