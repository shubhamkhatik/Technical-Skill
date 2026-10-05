# Frontend Engineering Interview Questions

---

## HTML & Web Fundamentals
1. What are Semantic HTML elements and why should you use them over non-semantic elements (`div`, `span`)?
2. What is `srcset` in HTML and how does it compare to the `<picture>` element?
3. How do you handle responsive image loading in modern web apps?
4. What are Web Components (Custom Elements, Shadow DOM, HTML Templates)?
5. What are Service Workers, Web Workers, and Progressive Web Apps (PWAs)?
6. How do you architect an application for multiple devices (responsive design, media queries, relative units, progressive enhancement)?

---

## CSS & Layouts
1. What is the difference between `display: none` and `visibility: hidden`?
2. Explain CSS Box Model (content, padding, border, margin) and `box-sizing: border-box`.
3. Flexbox vs. CSS Grid: When would you use one over the other?
4. How do CSS specificity and the cascade rule work?
5. How does `position: relative`, `absolute`, `fixed`, and `sticky` behave?
6. What is the purpose of the CSS `will-change` property, and how does it affect GPU acceleration?

---

## JavaScript (Core & Advanced)
1. Explain Closures: What are their benefits, use cases, and limitations?
2. When do closures cause memory leaks or unexpected retention in long-lived apps, and how do you avoid them?
3. Explain Hoisting and the Temporal Dead Zone (TDZ).
4. What is the Event Loop? Explain Call Stack, Task Queue (Macrotasks), and Microtask Queue.
5. Can we bind `this` in an arrow function? What happens if you use the `new` operator with an arrow function?
6. What does the `new` operator do in JavaScript internally step-by-step?
7. What is the difference between `Map` and `Object` in JavaScript? When should you use which?
8. What is Currying? How does it enable partial application and function composition?
9. What is the difference between Prototypal and Classical Inheritance in JavaScript?
10. How does JavaScript handle asynchronous operations? What mechanisms does it use (callbacks, Promises, async/await, generators)?
11. Does React use `Promise.allSettled()` for parallel API calls? How does that work internally? What is the difference between `Promise.all()` and `Promise.allSettled()`?
12. What algorithm does `Array.prototype.sort()` use? What is the output of `[1, null, 5, 2, undefined].sort()`?
13. What are Symbols and Generator functions (`function*` and `yield`)?
14. What is the difference between Event Bubbling, Event Capturing, and Event Delegation?
15. If a user clicks a button multiple times to fetch data, how do you cancel old API calls (`AbortController`) and use only the latest result?
16. How do we apply Object-Oriented Programming (OOP) and SOLID principles in JavaScript?

---

## Typescript
1. What is explicit and implicit type assignment?
2. Difference between `any`, `unknown` and `never` in TypeScript?
3. How do you give the type of Arrays?
4. What is Type Inference in array?
5. What are tuples?
6. What are readonly tuples?
7. How to give the types for Objects?
8. How to have optional properties in Objects?
9. Explain enum/String enum in TypeScript?
10. What are Type Aliases?
11. Interfaces and How to extend interfaces?
12. How to give the return type in function?
13. How to give type of parameters in function?
14. How to give optional, default and rest parameters in function?
15. What is casting in TypeScript?
16. What is public, private and protected in TypeScript classes?
17. What are Generics in TypeScript? Give examples in functions, classes and type aliases.

---

## React & Next.js
1. Which is better for SEO — React, Next.js, or any other library? Why?
2. Can standalone React improve SEO? If yes, how?
3. What parameters improve SEO (SSR/SSG, meta tags, schema structured data, semantic HTML)?
4. What state management libraries have you used?
5. Which one would you choose between `useContext` and Redux/Zustand, and why?
6. Understanding and optimizing performance in state management (selectors, memoization, preventing unnecessary re-renders).
7. On input change, how do you make API calls for search suggestions and optimize calls using debounce to avoid network spam?
8. Component Lifecycle and Hooks execution order in React.
9. Difference between `useMemo` and `useCallback`. When is memoization an anti-pattern?
10. React Server Components (RSC) vs Client Components in Next.js App Router.

---

## Web Performance & Browser Internals
1. What happens step-by-step when you hit a URL in the browser until pixels are painted?
2. What is the Critical Rendering Path (CRP)? How do you optimize it?
3. What browser events occur when a website is loading (`DOMContentLoaded`, `load`)?
4. What is the difference between Repaint and Reflow (Layout thrashing)? How do you prevent layout thrashing?
5. What are Preload, Preconnect (Reconnect), Prefetch, and Prerender?
6. What are render-blocking resources and how do you eliminate them (`async`, `defer`, inlining critical CSS)?
7. How can you implement caching on a website? Explain `Cache-Control`, `ETag`, `Last-Modified`, and CDN caching.
8. How do you optimize assets? What is image compression and what are the differences between WebP, PNG, and JPG?
9. What is a Memory Leak in frontend applications? What are the common causes (uncleaned listeners, timers, detached DOM nodes) and how do you profile them?
10. What are Core Web Vitals (LCP, FID/INP, CLS)? What are the ideal values and how do you improve each?
11. What is the Webpack build process (Entry, Dependency Graph, Loaders, Plugins, Output)?
12. What is the use of headers in HTTP requests (`Content-Type`, `Authorization`, `Cache-Control`, `User-Agent`)?

---

## Machine Coding & Practical Implementations
1. Write a polyfill for `sum(1)(2)(3)()` to return `6`.
2. Implement a debounce and throttle function from scratch.
3. Build an interactive Star Rating component with hover, click, and half-star support.
4. Build an autocomplete / search suggestion input with debounced API requests and request cancellation.
5. Build a user listing dashboard with live search, dropdown filtering, and TypeScript types.
