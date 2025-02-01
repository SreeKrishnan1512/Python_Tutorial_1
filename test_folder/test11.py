import inspect
def getLogger():
    stack = inspect.stack()
    for i, frame in enumerate(stack):
        print(f"Frame {i}: {frame.function},\n File: {frame.filename},\n Line: {frame.lineno}")

getLogger()