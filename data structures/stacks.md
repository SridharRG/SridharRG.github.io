# Stacks

A Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

## Implement Stacks using Arrays

```cpp
class ArrayStack {
private:
    int capacity;
    int* stkArr;
    int topIndex;
public:
    ArrayStack(int size=1000) {
        capacity = size;
        stkArr = new int[capacity];
        topIndex = -1;
    }

    void push(int x) {
      if(topIndex >= capacity-1)return;
        else{
            topIndex += 1;
            stkArr[topIndex] = x;
        }
    }

    int pop() {
        if(topIndex != -1){
            return stkArr[topIndex--];
        }
        return -1;
    }

    int top() {
        if(topIndex != -1){
            return stkArr[topIndex];
        }
        return -1;
    }

    bool isEmpty() {
        if(topIndex == -1) return true;
        else return false;
    }
};

// Time Complexity: O(1) because the individual stack operations take O(1).
// Space Complexity: O(N) for using a stack which is equivalent to the size of the array.
```

## Implement Stacks using Queue

```cpp
class QueueStack {
    queue<int> qStk;
public:
    QueueStack() {
    }

    void push(int x) {
        int s = qStk.size();
        qStk.push(x);
         for(int i=0; i< s; i++){
            qStk.push(qStk.front());
            qStk.pop();
         }
    }

    int pop() {
        int n = qStk.front();
        qStk.pop();
        return n;
    }

    int top() {
        return qStk.front();

    }

    bool isEmpty() {
        if(qStk.size() == 0) return true;
        else return false;
    }
};
// Time Complexity: O(N) where N is the length of the array. We iterate through the input array exactly once and at each element perform constant time operations.
// Space Complexity: O(1) no extra space used.
```

## Implement Stacks using Linked List

```cpp
class LinkedListStack {
private:
    struct ListNode{
    int val;
    ListNode *next;
    ListNode(int data1)
    {
        val = data1;
        next = NULL;
    }
    ListNode(int data1, ListNode *next1)
    {
        val = data1;
        next = next1;
    }
};
    ListNode* topp = NULL;
public:
    LinkedListStack() {

    }

    void push(int x) {
        ListNode* temp = new ListNode(x);
        temp->next = topp;
        topp = temp;
    }

    int pop() {
        if (topp == NULL) return -1;
        else{
       ListNode* temp = topp;
       topp = topp->next;
       int out = temp->val;
       delete temp;
       return out;
        }
    }

    int top() {
        if (topp != NULL) return topp->val;
        else return -1;
    }

    bool isEmpty() {
        if (topp == NULL) return true;
        return false;
    }
};
// Time Complexity: O(1) for push, pop, size,isEmpty, peek operations.
// Space Complexity: O(N) because the stack requires space proportional to the number of elements it stores.
```
