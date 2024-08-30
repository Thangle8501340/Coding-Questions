
# Solution

In order to solve this problem we will use the fast and slow two pointer method where the slow will go to the next node, and the fast will go to the next next node. In this solution, if the fast and slow were to ever meet, then we know that there is a cycle as it created a loop
Complexity:
- Splace Complexity: O(1) -> Did not created a new linked list, thus it is constant space
- Time Complexity: O(N) -> Worse case we iterate through the whole list and there are no cycle, thus it is O(N)
![image](https://github.com/user-attachments/assets/d256a945-5d6c-4f31-ab11-7698bb75adbd)
![image](https://github.com/user-attachments/assets/2b7677f1-2962-4a95-8eb6-7f0b7540c70c)
![image](https://github.com/user-attachments/assets/f4722e0d-7c7c-4a14-befa-57d5124f2e58)
