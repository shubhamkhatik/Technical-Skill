

# On input change, make API calls for search suggestions.

To make API calls for search suggestions on input change, use an event listener (preferably 'input') and debounce the requests to avoid excessive calls. Here’s a breakdown:

## What

Trigger **API calls** to fetch search suggestions whenever the search input value changes.[^2_1]

## Why

This provides a dynamic, responsive user experience by offering real-time suggestions and reduces input errors for users.[^2_1]

## How

1. Add an event listener for the `input` event on the search field.
2. Use a debounce function to delay API requests until the user pauses typing.[^2_2][^2_1]
3. Make the API call and display suggestions.

Example (Vanilla JS):

```html
<input type="search" id="search" placeholder="Type to search...">
<div id="suggestions"></div>
<script>
let timer;
document.getElementById('search').addEventListener('input', function() {
  clearTimeout(timer);
  const query = this.value;
  timer = setTimeout(() => {
    if (query.length > 0) {
      fetch(`/api/suggestions?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
          // Update suggestions
          const suggestions = document.getElementById('suggestions');
          suggestions.innerHTML = '';
          data.forEach(item => {
            const div = document.createElement('div');
            div.textContent = item;
            suggestions.appendChild(div);
          });
        });
    } else {
      document.getElementById('suggestions').innerHTML = '';
    }
  }, 300); // 300ms debounce
});
</script>
```


## When

Use this for autocomplete or search suggestion UIs, especially when querying remote APIs or databases on user input.[^2_1]

## Where

Implement in search bars, filter fields, or any user input-driven dynamic search UI within web applications.[^2_1]
<span style="display:none">[^2_3][^2_4][^2_5][^2_6][^2_7][^2_8]</span>

<div style="text-align: center">⁂</div>

[^2_1]: https://www.educative.io/answers/javascript-autocomplete-with-api-for-input-fields

[^2_2]: https://stackoverflow.com/questions/70729992/making-api-calls-based-on-user-input-on-a-search-field

[^2_3]: https://www.w3schools.com/jsref/event_onchange.asp

[^2_4]: https://forum.freecodecamp.org/t/autocomplete-with-an-api-call/79121

[^2_5]: https://dev.to/rajnishkatharotiya/best-practice-to-handle-input-change-requests-with-google-custom-search-1eh0

[^2_6]: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search

[^2_7]: https://www.youtube.com/watch?v=nwJQBDPfGEk

[^2_8]: https://developers.google.com/maps/documentation/places/web-service/place-autocomplete


---

# On input change, make API calls for search suggestions and optimize calls using debounce to avoid network spam.

To make API calls for search suggestions on input change without spamming the network, use **debounce**—a method that delays the API request until the user pauses typing. This greatly reduces unnecessary network requests and enhances performance.[^3_1][^3_2]

## What

A debounced API call means triggering the search suggestion API after a specified delay (e.g., 300ms) when the input value changes and no new input occurs during that interval.[^3_2][^3_1]

## Why

This avoids network spam, reduces server load, and ensures efficient use of resources without sacrificing user experience.[^3_1][^3_2]

## How

1. Write a debounce function that wraps the API call.
2. Attach an input event listener to the search field.
3. Call the debounced function inside the listener.

### Example (Plain JavaScript)

```html
<input type="search" id="search" placeholder="Search..." />
<div id="suggestions"></div>
<script>
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

function fetchSuggestions(query) {
  if (!query) {
    document.getElementById('suggestions').innerHTML = '';
    return;
  }
  fetch('/api/suggestions?q=' + encodeURIComponent(query))
    .then(res => res.json())
    .then(data => {
      const suggestions = document.getElementById('suggestions');
      suggestions.innerHTML = '';
      data.forEach(item => {
        const div = document.createElement('div');
        div.textContent = item;
        suggestions.appendChild(div);
      });
    });
}

const debouncedFetch = debounce(fetchSuggestions, 300);

document.getElementById('search').addEventListener('input', (e) => {
  debouncedFetch(e.target.value);
});
</script>
```


## When

Use this for real-time search, autocomplete, or suggestion features where frequent input could cause excessive requests.[^3_1]

## Where

Apply this pattern in any frontend (HTML/JS, React, Vue, etc.) as part of user-facing search, filter, or data query UIs.[^3_2]
<span style="display:none">[^3_10][^3_3][^3_4][^3_5][^3_6][^3_7][^3_8][^3_9]</span>

<div style="text-align: center">⁂</div>

[^3_1]: https://www.geeksforgeeks.org/html/implement-search-box-with-debounce-in-javascript/

[^3_2]: https://www.telerik.com/blogs/debouncing-and-throttling-in-javascript

[^3_3]: https://stackoverflow.com/questions/74143346/how-to-add-debouncing-to-my-simple-search-query

[^3_4]: https://www.freecodecamp.org/news/deboucing-in-react-autocomplete-example/

[^3_5]: https://www.youtube.com/watch?v=MHm-2YmWEek

[^3_6]: https://apidog.com/blog/understanding-and-implementing-debouncing-for-api-calls-in-react/

[^3_7]: https://dev.to/ohdylan/create-a-debounce-hook-for-search-box-auto-completion-11n1

[^3_8]: https://dev.to/manishkc104/debounce-input-in-react-3726

[^3_9]: https://blog.devgenius.io/asynchronous-autocomplete-search-with-react-axios-and-lodash-debounce-b59e57be5b3b

[^3_10]: https://blog.openreplay.com/optimizing-api-calls-react-debounce-strategies/


---

# Explain Closures. What are its benefits, use cases, and limitations?

A **closure** is a JavaScript feature where an inner function retains access to its outer (enclosing) function’s variables and parameters, even after the outer function has completed execution.[^4_2][^4_3][^4_5]

## What

A closure is formed when a function is defined inside another function and the inner function references variables from the outer function’s scope. The inner function “remembers” its environment (the lexical scope) even after the outer function is no longer active.[^4_3][^4_5][^4_2]

## Why

Closures allow for data privacy, state maintenance, and modular coding. They enable inner functions to maintain and manipulate variables privately, shielding them from the global scope and external interference.[^4_1][^4_6]

## How

Closures are created every time a function is defined inside another function and the inner function accesses outer function variables. For example:

```javascript
function makeCounter() {
  let count = 0;
  return function() {
    return count++;
  }
}
const counter = makeCounter();
console.log(counter()); // 0
console.log(counter()); // 1
```

Here, the returned function forms a closure over the `count` variable, preserving its state across calls.[^4_6][^4_7]

## Benefits

- **Data privacy:** Variables in the outer function are private to the closure, inaccessible from outside.[^4_7]
- **Persistent state:** Functions can “remember” and update their environment between invocations.[^4_6]
- **Encapsulation:** Useful for defining APIs or modules with hidden, internal logic.[^4_5][^4_6]
- **Functional patterns:** Enables patterns like function factories, once-only initializations, and more.[^4_7]


## Use Cases

- **Data hiding \& encapsulation:** Private variables in modules or object constructors.[^4_1]
- **Event handlers:** Functions that retain data relevant to a particular UI event.[^4_5]
- **Callbacks:** Delayed or deferred execution with access to originating variables.
- **Partial application/currying:** Functions retaining preset arguments for later use.[^4_7]


## Limitations

- **Memory leaks:** Unintentional references may prevent garbage collection.
- **Debugging difficulty:** Captured state can introduce unexpected results if mutated poorly.[^4_5][^4_7]
- **Overuse:** Excessive closures in large applications can lead to maintainability or performance concerns.

Closures are a cornerstone of JavaScript’s flexibility, used for creating robust, modular, and safe code, but should be applied with understanding to avoid misuse.[^4_6][^4_5][^4_7]
<span style="display:none">[^4_4][^4_8][^4_9]</span>

<div style="text-align: center">⁂</div>

[^4_1]: https://www.w3schools.com/js/js_function_closures.asp

[^4_2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures

[^4_3]: https://www.geeksforgeeks.org/javascript/closure-in-javascript/

[^4_4]: https://www.freecodecamp.org/news/lets-learn-javascript-closures-66feb44f6a44/

[^4_5]: https://builtin.com/articles/javascript-closures

[^4_6]: https://www.linkedin.com/pulse/javascript-closure-examples-laurence-svekis-

[^4_7]: https://www.humankode.com/javascript/javascript-closures-made-easy/

[^4_8]: https://www.youtube.com/watch?v=beZfCfiuIkA

[^4_9]: https://joelolawanle.com/blog/javascript-closures


---

# When do closures cause memory leaks or unexpected retention in long‑lived apps

Closures cause **memory leaks or unexpected retention** in long‑lived applications when they unintentionally keep references to variables or large objects in their outer scope that are no longer needed, preventing the garbage collector from freeing that memory.[^5_1][^5_6]

## Why It Happens

- A closure captures and retains all variables from its outer function scope it references, including large data structures or objects.[^5_6][^5_1]
- If these closures persist (e.g., stored in long-lived objects, event handlers, or callbacks), they keep those variables alive in memory.[^5_1]
- Even if the outer function finishes execution, the closure’s reference keeps the entire outer scope from being cleaned up.[^5_6][^5_1]


## Common Scenarios

- Returning closures that capture large objects or arrays, causing those objects to stay in memory indefinitely.[^5_1]
- Closures used in event listeners or timers that are not properly cleaned up, holding onto variables longer than needed.[^5_5]
- In frameworks like React, closures capturing outdated state or large data inside hooks (like useCallback, useEffect) without proper dependencies can cause leaks.[^5_4]


## Example

```javascript
function createLeak() {
  const largeObject = new Array(1000000).fill('data');
  return function leakyFunction() {
    console.log(largeObject);
  };
}
const leak = createLeak();
// `largeObject` is retained in memory because `leakyFunction` closure holds a reference
```

Here, `largeObject` stays in memory as long as `leakyFunction` exists, even though `createLeak` has finished.[^5_1]

## How to Avoid

- Minimize the data captured by closures; avoid referencing large objects entirely.[^5_1]
- Clean up event listeners, timers, or callbacks to release closures no longer needed.[^5_5]
- In React, manage hook dependencies carefully to avoid stale closures retaining unnecessary references.[^5_4]
- Use tools like heap profilers and memory snapshots to detect unexpected retained memory.[^5_1]

Closures are powerful but require careful management in long-lived apps to prevent memory retention issues that degrade performance over time.[^5_4][^5_6][^5_1]
<span style="display:none">[^5_2][^5_3][^5_7][^5_8]</span>

<div style="text-align: center">⁂</div>

[^5_1]: https://dev.to/mshidlov/how-closures-can-cause-memory-leaks-and-what-you-can-do-about-it-fjd

[^5_2]: https://forums.swift.org/t/unexpected-memory-leak-when-using-task-in-a-closure-causes/66272

[^5_3]: https://stackoverflow.com/questions/72876350/why-does-closure-cause-memory-leak-in-javascript-in-this-case

[^5_4]: https://www.linkedin.com/pulse/understanding-react-closures-preventing-memory-leaks-functional-r-u9d2c

[^5_5]: https://blogs.halodoc.io/diagnosing-and-resolving-ios-memory-leaks-with-different-approaches/

[^5_6]: https://www.netdata.cloud/academy/nodejs-memory-leak/

[^5_7]: https://www.guvi.in/blog/memory-leaks-in-javascript-application/

[^5_8]: https://blog.meteor.com/an-interesting-kind-of-javascript-memory-leak-8b47d2e7f156


---

# Write a Polyfill for sum(1)(2)(3)() to return 6

To create a polyfill for a function that supports chained calls like `sum(1)(2)(3)()` and returns the cumulative sum (6 in this case), use a function that returns another function capturing the ongoing total. When called without arguments, it returns the total.

Here's a step-by-step explanation and implementation:

## What

A function `sum` that supports **currying** with chained calls and returns the sum when called with no arguments.

## How

- Initialize a total accumulator.
- Return a function that accepts a number and adds it to the accumulator.
- When called with no arguments, return the accumulator.


## Polyfill Code

```
function sum(x) {
  let total = x;

  function inner(y) {
    total += y;
    return inner;
  }

  inner.valueOf = () => total;
  inner.toString = () => String(total);

  return inner;
}

const result = sum(1)(2)(3);

console.log(result);       // function inner {...}
console.log(result + 0);   // 6   <-- valueOf called
console.log(`${result}`);  // "6" <-- toString called


```


## Explanation

- The outer `sum` initializes `total` with the first argument or zero.
- The inner function `inner` accumulates values or returns total if called without arguments.
- Each call returns itself (except the last, which returns the sum), enabling chaining.[^6_1]

This approach works efficiently with any number of chained calls ending with an empty call to get the total.

<div style="text-align: center">⁂</div>

[^6_1]: https://stackoverflow.com/questions/70729992/making-api-calls-based-on-user-input-on-a-search-field

