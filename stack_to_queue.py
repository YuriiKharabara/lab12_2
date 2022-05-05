from Queue.arrayqueue import ArrayQueue
from Stack.arraystack import ArrayStack


def stack_to_queue(stack):
    """transrom stack to queue

    Args:
        stack (ArrayStack): stack which is going to be transformed to queue

    Returns:
        ArrayQueue: queue made from stack
    """
    stack_new = ArrayStack(stack)
    new_queue = ArrayQueue()
    # a = new_queue.pop()
    # print(len(new_queue))
    list_of_meanings = []
    for i in range(len(stack_new)):
        if not stack_new.isEmpty():
            list_of_meanings.append(stack_new.pop())
        else:
            break
    # list_of_meanings.reverse()
    for i in list_of_meanings:
        new_queue.add(i)
    return new_queue


if __name__ == '__main__':
    stack = ArrayStack()
    for i in range(10):
        stack.add(i)
    queue = stack_to_queue(stack)
    print(queue)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack.pop())
    # 9
    print(queue.pop())
    # 9
    stack.add(11)
    queue.add(11)
    print(queue)
    # [8, 7, 6, 5, 4, 3, 2, 1, 0, 11]
    print(stack)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]
