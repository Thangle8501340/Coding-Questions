
# Solution

In order to solve this problem we will use the fast and slow two pointer method where the slow will go to the next node, and the fast will go to the next next node. In this solution, if the fast and slow were to ever meet, then we know that there is a cycle as it created a loop
Complexity:
- Splace Complexity: O(1) -> Did not created a new linked list, thus it is constant space
- Time Complexity: O(N) -> Worse case we iterate through the whole list and there are no cycle, thus it is O(N)
