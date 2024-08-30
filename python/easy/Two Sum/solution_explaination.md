
# Solution

In order to solve this prolbem, we have to use a hash map in order to keep track of the values as we go through the array. When we iterate through the array, we check the following:
- If the value is in the hashmap, which means that we have found a pairing of 2 numbers that adds to target. This then allows us to return the value of the hashmap (which is the index of the other number) and the current index. 
- If the value is not in the hashmap, to which when then store(target - value) into the hashmap as the "key", and the index of the value as "value" of the hashmap.
![image](https://github.com/user-attachments/assets/e6dcb551-68aa-484f-8770-95c6cee61690)
![image](https://github.com/user-attachments/assets/36b5a6b0-4a25-48e9-a2cd-0337c0d51e12)
