def sta():
    stack = ['a', 'b', 'c']
    print('Initial stack')
    print(stack)

    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    sta()


def que():
    queue = ['a', 'b', 'c']
    queue.append("hari")
    print(queue)

