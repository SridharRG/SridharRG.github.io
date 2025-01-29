# Queues

A Queue Data Structure is a fundamental concept in computer science used for storing and managing data in a specific order. It follows the principle of "First in, First out" (FIFO), where the first element added to the queue is the first one to be removed. Queues are commonly used in various algorithms and applications for their simplicity and efficiency in managing data flow.

## Implement Queues using Arrays

```cpp
class ArrayQueue {
private:
    int capacity = 1000;
    int currentSize;
    int start;
    int end;
    int *queueArr;
public:
    ArrayQueue(int size=1000) {
        capacity = size;
        queueArr = new int[capacity];
        currentSize = 0;
        start = -1;
        end = -1;
    }
    ~ArrayQueue(){
        delete[] queueArr;
    }
    void push(int x) {
        if(currentSize == capacity) return;
        else if(currentSize == 0){
            start = 0;
            end = 0;
        }else{
            end = (end + 1)% capacity;
        }
        queueArr[end] = x;
        currentSize += 1;
    }

    int pop() {
        if(currentSize == 0) return -1;
        int element = queueArr[start];
        if(currentSize == 1) {
            start = -1;
            end = -1;
        } else{
            start = (start + 1) % capacity;
        }
        currentSize -= 1;
        return element;
    }

    int peek() {
        if(currentSize > 0) return queueArr[start];
        return -1;
    }

    bool isEmpty() {
        if (currentSize == 0)return true;
        return false;
    }
};

// Time Complexity: O(1) because the individual stack operations take O(1).
// Space Complexity: O(N) for using a stack which is equivalent to the size of the array.

```

## Implement Queues using Stacks

```cpp
class StackQueue {
private:
    stack<int> s1;
    stack<int> s2;
public:
    StackQueue() {
    }
    // s1 -> s2
    // x -> s1
    // s2 -> s1
    void push(int x) {
            while(s1.size() != 0){
                int n = s1.top();
                s2.push(n);
                s1.pop();
            }
            s1.push(x);
            while(s2.size() != 0){
                int n = s2.top();
                s1.push(n);
                s2.pop();
            }
    }

    int pop() {
        if(s1.size() != 0){
            int n = s1.top();
            s1.pop();
            return n;
        } else return -1;
    }

    int peek() {
        if(s1.size() != 0) {
            return s1.top();
        }
        return -1;
    }

    bool isEmpty() {
        if (s1.size() == 0) return true;
        return false;
    }
};
// Time Complehxity: O(N) where N is the number of elements.
// Space Complexity: O(2N) because, in the worst case, both the input and output stacks can each hold up to N elements, totalling 2N elements. Here N is the size of the stack.
```

## Implement Queues using Linked List

```cpp
class StackQueue {
private:
    stack<int> s1;
    stack<int> s2;
public:
    StackQueue() {
    }
    // s1 -> s2
    // x -> s1
    // s2 -> s1
    void push(int x) {
            while(s1.size() != 0){
                int n = s1.top();
                s2.push(n);
                s1.pop();
            }
            s1.push(x);
            while(s2.size() != 0){
                int n = s2.top();
                s1.push(n);
                s2.pop();
            }
    }

    int pop() {
        if(s1.size() != 0){
            int n = s1.top();
            s1.pop();
            return n;
        } else return -1;
    }

    int peek() {
        if(s1.size() != 0) {
            return s1.top();
        }
        return -1;
    }

    bool isEmpty() {
        if (s1.size() == 0) return true;
        return false;
    }
};
// Time Complehxity: O(N) where N is the number of elements.
// Space Complexity: O(2N) because, in the worst case, both the input and output stacks can each hold up to N elements, totalling 2N elements. Here N is the size of the stack.
```
