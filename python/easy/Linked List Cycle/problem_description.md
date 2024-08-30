# 141. Linked List Cycle

**Difficulty:** Easy  
**Topics:** Hash Table, Linked List, Two Pointers  
**Companies:** [Multiple Companies]

---

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that the tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Example 1:
![image](https://github.com/user-attachments/assets/a21be6fa-521c-49f0-a7cc-7d501ef923b6)
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2:
![image](https://github.com/user-attachments/assets/107b90ba-f118-48f7-84a3-2b29c421d290)

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

### Example 3:
![image](https://github.com/user-attachments/assets/e9aaa8ff-9637-432f-b6fd-4f066dd0443f)

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
