from queue import Queue

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    print("Dequeued:", queue.dequeue())
    print("Is empty?", queue.is_empty())
