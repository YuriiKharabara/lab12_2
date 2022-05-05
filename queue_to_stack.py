from Queue.arrayqueue import ArrayQueue
from Stack.arraystack import ArrayStack


def queue_to_stack(queue):
    """transrom queue to stack

    Args:
        queue (ArrayQueue): queue which is going to be transformed to stack

    Returns:
        ArrayStack: stack made from queue
    """
    stack_new = ArrayStack()
    new_queue = ArrayQueue(queue)
    # a = new_queue.pop()
    # print(len(new_queue))
    list_of_meanings = []
    for i in range(len(new_queue)):
        if not new_queue.isEmpty():
            list_of_meanings.append(new_queue.pop())
        else:
            break
    list_of_meanings.reverse()
    for i in list_of_meanings:
        stack_new.push(i)
    return stack_new


if __name__ == '__main__':
    queue = ArrayQueue()
    for i in range(10):
        queue.add(i)
    stack = queue_to_stack(queue)
    print(queue)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(stack.pop())
    # 0
    print(queue.pop())
    # 0
    stack.add(11)
    queue.add(11)
    print(queue)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    print(stack)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 11]
