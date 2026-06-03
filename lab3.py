class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)


class QueueFromTwoStacks:
    OVERFLOW_ERROR = "Ошибка переполнения: очередь достигла максимального размера"
    
    def __init__(self, max_size=None):
        self._stack_input = Stack()
        self._stack_output = Stack()
        self._max_size = max_size
        self._enqueue_count = 0
        self._dequeue_count = 0
    
    def enqueue(self, x):
        if self._max_size is not None and self.size() >= self._max_size:
            raise OverflowError(self.OVERFLOW_ERROR)
        
        self._stack_input.push(x)
        self._enqueue_count += 1
        return True
    
    def _transfer(self):
        while not self._stack_input.is_empty():
            self._stack_output.push(self._stack_input.pop())
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        if self._stack_output.is_empty():
            self._transfer()
        
        self._dequeue_count += 1
        return self._stack_output.pop()
    
    def front(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        if self._stack_output.is_empty():
            self._transfer()
        
        return self._stack_output.peek()
    
    def size(self):
        return self._stack_input.size() + self._stack_output.size()
    
    def is_empty(self):
        return self.size() == 0
    
    def clear(self):
        self._stack_input = Stack()
        self._stack_output = Stack()
    
    def display(self):
        result = []
        current = self._copy()
        
        while not current.is_empty():
            result.append(current.dequeue())
        
        return result
    
    def _copy(self):
        copy_queue = QueueFromTwoStacks(self._max_size)
        
        temp_input_items = []
        while not self._stack_input.is_empty():
            temp_input_items.append(self._stack_input.pop())
        
        for item in reversed(temp_input_items):
            copy_queue._stack_input.push(item)
            self._stack_input.push(item)
        
        temp_output_items = []
        while not self._stack_output.is_empty():
            temp_output_items.append(self._stack_output.pop())
        
        for item in reversed(temp_output_items):
            copy_queue._stack_output.push(item)
            self._stack_output.push(item)
        
        return copy_queue
    
    def contains(self, x):
        current = self._copy()
        
        while not current.is_empty():
            if current.dequeue() == x:
                return True
        
        return False
    
    def get_operation_count(self):
        return (self._enqueue_count, self._dequeue_count)
    
    def get_max_size(self):
        return self._max_size
    
    def __str__(self):
        return str(self.display())


def main():
    print("=" * 50)
    print("Очередь через два стека (вариативная часть №9)")
    print("=" * 50)
    
    queue = QueueFromTwoStacks(max_size=5)
    print(f"\nСоздана очередь с макс. размером: {queue.get_max_size()}")
    
    print("\nДобавление элементов:")
    for i in range(1, 6):
        queue.enqueue(i * 10)
        print(f"  Добавлено: {i * 10}, размер: {queue.size()}")
    
    print(f"\nТекущая очередь: {queue}")
    
    print("\nПроверка переполнения:")
    try:
        print("  Попытка добавить 60...")
        queue.enqueue(60)
    except OverflowError as e:
        print(f"  Ошибка: {e}")
    
    print(f"\nПервый элемент: {queue.front()}")
    
    print("\nУдаление 3 элементов:")
    for i in range(3):
        removed = queue.dequeue()
        print(f"  Удален: {removed}, осталось: {queue.size()}")
    
    print(f"\nОчередь сейчас: {queue}")
    print(f"Содержит 40? {queue.contains(40)}")
    print(f"Содержит 100? {queue.contains(100)}")
    
    enq, deq = queue.get_operation_count()
    print(f"\nСтатистика: enqueue={enq}, dequeue={deq}")
    
    print("\nОчистка очереди...")
    queue.clear()
    print(f"Очередь пуста? {queue.is_empty()}")
    
    print("\n" + "=" * 50)
    print("Доп. тест с разными типами данных")
    print("=" * 50)
    
    queue2 = QueueFromTwoStacks(max_size=3)
    queue2.enqueue("A")
    queue2.enqueue("B")
    queue2.enqueue("C")
    print(f"Очередь: {queue2}")
    
    try:
        queue2.enqueue("D")
    except OverflowError as e:
        print(f"Ошибка: {e}")
    
    print("Извлечение всех элементов:")
    while not queue2.is_empty():
        print(f"  {queue2.dequeue()}")


if __name__ == "__main__":
    main()
