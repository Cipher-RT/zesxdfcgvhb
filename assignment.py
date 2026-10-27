Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append("")

 
def Push(Word):
    global Stack, TopOfStack
    if TopOfStack == 7:
        return False
    TopOfStack = TopOfStack + 1
    Stack[TopOfStack] = Word
    return True


def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return ""
    Word = Stack[TopOfStack]
    TopOfStack = TopOfStack - 1
    return Word


def GetText():
    Text = ""
    for i in range(TopOfStack + 1):
        if i == 0:
            Text = Stack[i]
        else:
            Text = Text + " " + Stack[i]
    return Text


def DecimalToBinary(Number):
    global Stack, TopOfStack
    TopOfStack = -1
    if Number == 0:
        return "0"
    while Number > 0:
        Push(str(Number % 2))
        Number = Number // 2
    Result = ""
    while TopOfStack != -1:
        Result = Result + Pop()
    return Result
