# 큐의 크기 및 초기화
MAX_SIZE = 8
queue = [None] * MAX_SIZE
front = -1
rear = -1

# enqueue(인큐) 함수
def enqueue(item):
    global rear
    if rear == MAX_SIZE - 1:
        print("오버플로(Overflow) 발생!")
        return
    rear += 1
    queue[rear] = item

# dequeue(디큐) 함수
def dequeue():
    global front
    if front == rear:
        print("언더플로(Underflow) 발생!")
        return None
    front += 1
    item = queue[front]
    queue[front] = None
    return item

# 주어진 상태를 만들기 위한 실행 과정
# A, B, C, D, E를 차례대로 삽입한 뒤, 3번(A, B, C)을 삭제하면 결과 이미지와 동일해집니다!
enqueue('A')
enqueue('B')
enqueue('C')
enqueue('D')
enqueue('E')

dequeue() # 'A' 삭제 -> front: 0
dequeue() # 'B' 삭제 -> front: 1
dequeue() # 'C' 삭제 -> front: 2

# 최종 결과 확인
print("큐 상태:", queue)
print("front 위치:", front)
print("rear 위치:", rear)