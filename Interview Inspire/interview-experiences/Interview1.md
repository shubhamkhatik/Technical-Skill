## Quiz 1:

1. **When designing for readability in mobile interfaces, which line height (or line spacing) is typically recommended for body text?**

   - A) 2.0x the font size
   - B) 1.5x the font size
   - C) 1.0x the font size
   - D) 0.8x the font size  
     **Answer:** Option B

2. **You are given a string representing a mathematical expression containing parentheses, addition, subtraction, multiplication, and division operations. You need to evaluate the expression and return the result. What is the most efficient algorithm to solve this problem?**

   - A) Breadth-First Search (BFS)
   - B) Binary search
   - C) Depth-First Search (DFS)
   - D) Linear scan with stack  
     **Answer:** Option D

3. **What's the output of the following code?**

```javascript
function getAge(...args) {
  console.log(typeof args);
}
getAge(21);
```

- A) object
- B) Error
- C) array
- D) undefined  
  **Answer:** Option A

4. **How many WebSocket events are there?**

- A) 3
- B) 2
- C) 4
- D) 5  
  **Answer:** Option C

5. **What is the output of the following code?**

```javascript
function sayHi() {
  console.log(name);
  console.log(age);
  var name = "Joe";
  let age = 21;
}
sayHi();
```

- A) Joe and ReferenceError
- B) undefined and undefined
- C) undefined and ReferenceError
- D) Joe and 21  
  **Answer:** Option C

6. **Which of the array methods always returns an array as an output?**

- A) map
- B) filter
- C) slice
- D) concat  
  **Answer:** Option A

7. **What is the output of the following code?**

```javascript
eval(1 + +"2" + 3);
```

- A) 123
- B) 6
- C) 15
- D) 24  
  **Answer:** Option B

8. **What is the following a Quantitative method of gathering user feedback in UI testing?**

- A) Userability Tests
- B) Card Sorting
- C) Heatmaps
- D) Surveys  
  **Answer:** Option D

9. **You are given a list of employee records containing their names and salaries. You need to find the highest-paid employee(s) in the list. However, there can be multiple employees with the same highest salary. What is the most efficient algorithm to solve this problem?**

- A) Iterate through the list and keep track of the highest salary and the employee(s) with that salary
- B) Implement a binary search algorithm to find the highest salary and the corresponding employee(s)
- C) Sort the list in descending order of salaries and select the employee(s) at the top
- D) Use a hash table to track the highest salary and the employees with that salary  
  **Answer:** Option A

10. **How can you ensure that a child component only re-renders when its specific props value changes? Not when any other prop of the parent component changes?**

```
import React from 'react';

interface MyComponentProps {
  importantProp: string;
  otherProp: string;
}

const MyComponent = React.memo((props: MyComponentProps) => {
  console.log("Rendering MyComponent");
  return <div>{props.importantProp}</div>;
}, (prevProps, nextProps) => {
  return prevProps.importantProp === nextProps.importantProp;
});

export default MyComponent;
```

**Answer:** The above core code snippet is correct.

11. **Imagine a user is pressing a key on the keyboard. Which of the following events always occurs, and is the first to occur?**

- A) onkeydown
- B) None of the options
- C) onkeypress
- D) onkeyup  
  **Answer:** Option A

12. **Which of the following is a recommended practice for reducing the bundle size in a React application?**

- A) Applying aggressive code splitting at the component level
- B) Utilizing React's Concurrent Mode to optimize rendering
- C) Storing all component state in a centralized global store
- D) Including all library dependencies in a single, minified file  
  **Answer:** Option A

13. **Your component has a dropdown where an Image or Audio can be uploaded. ImageUpload and AudioUpload are the two different libraries we are using for this. The Image option is selected by default in the dropdown. On page render, how would you ensure that the ImageUpload library gets downloaded and executed, but AudioUpload is downloaded only when the Audio option is selected? Multiple options may be correct**

- A) Create a function that imports libraries using `import("libraryName").then` and call this function based on the media type
- B) None of the options
- C) Create separate components for these libraries, which will be imported using `const OtherComponent = React.lazy(() => import('./someLibraryComponent'))` Then, render that particular component based on the media type
- D) Use the react-loadable library that imports libraries dynamically  
  **Answer:** Option A, Option C, Option D

14. **Consider a React application where multiple components require access to several different contexts (e.g., ThemeContext, UserContext, SettingsContext). Which of the following approaches aligns best with React's composition model and promotes better component reusability?**

- A) Using context bridging to avoid prop drilling and re-rendering issues by creating an intermediary component that subscribes to contexts and passes them down
- B) Creating a compound component that provides all contexts and using React.cloneElement to inject the contexts into each consumer
- C) Wrapping the entire application in a single higher-order component that provides all contexts
- D) Nesting individual context providers at the top-level of the application and using the useContext hook in nested components  
  **Answer:** Option D

### Problem Statement

You are given an array `arr` of integers containing `n` elements and an integer `k`. Rotate the array to the right by `k` steps, where `k` can be any positive integer (less than or equal to 1000). Rotation means each element of the array is shifted right by one position, and the last element moves to the beginning.

---

### Input Format

- First line contains an integer `n`, the size of the array `arr`.
- Second line contains `n` space-separated integers, representing the elements of the array `arr`.
- Third line contains an integer `k`.

---

### Input Constraints

- \(1 \leq n \leq 100\)
- \(-10^4 \leq arr[i] \leq 10^4\)
- \(1 \leq k \leq 10^4\)

---

### Output Format

Output the rotated array as a space-separated string.

---

### Examples

**Example 1**

Input:
5
1 2 3 4 5
2

Output:
4 5 1 2 3

Explanation: Rotating `[1, 2, 3, 4, 5]` two steps to the right results in `[4, 5, 1, 2, 3]`.

**Example 2**

Input:
6
10 20 30 40 50 60
4

Output:
40 50 60 10 20 30

Explanation: Rotating `[10, 20, 30, 40, 50, 60]` four steps to the right results in `[40, 50, 60, 10, 20, 30]`.

### Solution

```javascript
function solution(n, arr, k) {
  // Since rotating by n steps brings the array to original state,
  // we only need to rotate by k % n steps
  const steps = k % n;

  // Slice the last 'steps' elements and concatenate
  // with the rest at front
  const rotated = arr.slice(-steps).concat(arr.slice(0, n - steps));

  // Print the rotated array as space-separated string
  console.log(rotated.join(" "));
}
```

---

### Explanation:

- `k % n` handles the case where `k` might be greater than `n`.
- `arr.slice(-steps)` extracts the last `steps` elements.
- `arr.slice(0, n - steps)` extracts the first part of the array before the rotation.
- Concatenating these gives the rotated array.
- Finally, output the rotated array as requested.

---
