def countdown(value):
    call_stack = []
    while value > 0:
        call_stack.append({"input": value})
        print("Call Stack:", call_stack)
        value -= 1
    print("Base Case Reached")
    while len(call_stack) != 0:
        popped = call_stack.pop()
        print("Popping {} from call stack".format(popped))
        new = popped["input"] + 1
        print("Adding 1 to input value for new total: {}".format(new))
        print("Call Stack:", call_stack)


countdown(4)
