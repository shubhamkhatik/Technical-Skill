# Frontend Engineering Interview Questions

---

## HTML & Web Fundamentals
1. What are Semantic HTML elements and why should you use them over non-semantic elements (`div`, `span`)?
2. What is `srcset` in HTML and how does it compare to the `<picture>` element?
3. How do you handle responsive image loading in modern web apps?
4. What are Web Components (Custom Elements, Shadow DOM, HTML Templates)?
5. What are Service Workers, Web Workers, and Progressive Web Apps (PWAs)?
6. How do you architect an application for multiple devices (responsive design, media queries, relative units, progressive enhancement)?
7. What is the difference between `keydown`, `keypress`, and `keyup` events, and what is the exact execution sequence when a key is pressed?

---

## CSS & Layouts
1. What is the difference between `display: none` and `visibility: hidden`?
2. Explain CSS Box Model (content, padding, border, margin) and `box-sizing: border-box`.
3. Flexbox vs. CSS Grid: When would you use one over the other?
4. How do CSS specificity and the cascade rule work?
5. How does `position: relative`, `absolute`, `fixed`, and `sticky` behave?
6. What is the purpose of the CSS `will-change` property, and how does it affect GPU acceleration?
7. When designing for readability and accessibility in mobile interfaces, what line-height (e.g. 1.5x font size) and typography scale is recommended for body text?

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
17. How does implicit type coercion work in expressions like `1 + +"2" + 3`, and how does the unary plus operator evaluate strings?
18. What does `typeof` return on rest parameters `(...args)` in JavaScript functions and why?
19. What are the 4 standard WebSocket lifecycle events (`open`, `message`, `error`, `close`), and how do you implement heartbeat pings and exponential backoff reconnection?

---

## JavaScript Output-Based & Tricky Snippets
1. What is the output of `[1, null, 5, 2, undefined].sort()` and why does `undefined` always sort to the end regardless of custom comparator logic?
2. What is the output of `eval(1 + +"2" + 3)` and how does the unary plus operator perform type coercion?
3. What does `typeof` return when evaluated on function rest parameters `getAge(...args)` (`typeof args`)?
4. What is the console output of the following hoisting snippet, and why does `let` throw a `ReferenceError` while `var` prints `undefined`?
   ```javascript
   function sayHi() {
     console.log(name);
     console.log(age);
     var name = "Joe";
     let age = 21;
   }
   sayHi();
   ```
5. What is the console output of this classic loop snippet, and how do you fix it using `let` block scoping or an IIFE?
   ```javascript
   for (var i = 0; i < 3; i++) {
     setTimeout(() => console.log(i), 1000);
   }
   ```
6. What are the outputs of `[] == ![]`, `0 == "0"`, and `NaN === NaN`? Explain how the abstract equality comparison algorithm evaluates coercion.
7. What is the exact execution and logging order of the following asynchronous code snippet?
   ```javascript
   console.log('1');
   setTimeout(() => console.log('2'), 0);
   Promise.resolve().then(() => console.log('3'));
   console.log('4');
   ```
8. What is the output of object property assignment with object keys?
   ```javascript
   const a = {};
   const b = { key: 'b' };
   const c = { key: 'c' };
   a[b] = 123;
   a[c] = 456;
   console.log(a[b]);
   ```
9. Which array methods mutate the original array in-place (`splice`, `sort`, `reverse`, `push`, `pop`, `shift`, `unshift`) versus returning a new copy (`map`, `filter`, `slice`, `concat`, `toSorted`)?
10. What is the output of the following arrow function context snippet?
    ```javascript
    const user = {
      name: "Alex",
      greet: () => console.log(this.name),
      sayName() { console.log(this.name); }
    };
    user.greet();
    user.sayName();
    const fn = user.sayName;
    fn();
    ```

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
11. How do stale closures occur in React hooks (`useEffect`, `useCallback`, `useState`), and what design patterns prevent reading outdated state values?
12. Why do object, array, or inline function dependencies in `useEffect` trigger infinite re-render loops, and how do you stabilize reference equality (`useMemo`, `useCallback`, primitive dependencies, `useRef`)?
13. If a React component is re-rendering excessively (e.g. 50 times/second), what systematic steps and DevTools Profiler metrics do you use to diagnose the root cause (parent cascades vs context churn vs unstable props) and eliminate the bottleneck?
14. How do you pass a custom comparison function `(prevProps, nextProps)` to `React.memo` to restrict re-renders strictly to specific prop changes?
15. How do you architect code-splitting for conditional heavy libraries (e.g. image vs audio uploaders) using dynamic `import()` and `React.lazy()`?
16. How do you organize multiple React context providers (`ThemeContext`, `UserContext`, `SettingsContext`) without creating "wrapper hell"?

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
13. What is the difference between quantitative methods (surveys, heatmaps, analytics metrics) versus qualitative methods (usability testing, user interviews) when gathering user feedback in UI performance and usability evaluations?

---

## Machine Coding & Practical Implementations
1. Write a polyfill for `sum(1)(2)(3)()` to return `6`.
2. Implement a debounce and throttle function from scratch.
3. Build an interactive Star Rating component with hover, click, and half-star support.
4. Build an autocomplete / search suggestion input with debounced API requests and request cancellation.
5. Build a user listing dashboard with live search, dropdown filtering, and TypeScript types.
6. Build an accessible Modal dialog component in React with keyboard focus trapping, `Escape` key dismissal, backdrop click detection, and describe how to unit test it with Jest and React Testing Library (RTL).
7. Build an API data-rendering transaction list component handling loading skeleton, error fallback, and empty states, optimizing re-renders with `useMemo` and `React.memo`.

---

## Frontend System Design
1. **Design a Live Payments Feed / Financial Dashboard Widget (e.g. Razorpay)**:
   - Real-time transport protocols: Polling (Short/Long) vs WebSockets vs Server-Sent Events (SSE) for low-latency live transactions.
   - Large list performance: Virtualization and windowing (`react-window`, `@tanstack/react-virtual`) to render 1,000+ to 10,000+ transaction rows without DOM thrashing.
   - Client state architecture: Server-state caching and deduplication (TanStack Query / SWR) vs Global client store (Redux Toolkit / Zustand).
   - Pagination vs Infinite scrolling: Tradeoffs for financial audit logs, state restoration, and scroll position anchoring.
   - Accessibility (a11y) for dynamic feeds: Utilizing ARIA live regions (`aria-live="polite"` vs `"assertive"`, `aria-atomic`) so assistive technologies announce incoming transactions without disrupting screen reader navigation.
2. **Design an Enterprise Microfrontend Architecture (Independent Team Deployments)**:
   - Architecture & integration approaches: Webpack 5 `Module Federation` vs `iframes` vs `Web Components` (Custom Elements / Shadow DOM) vs Build-time package composition.
   - Shared dependencies: Singleton management for `React` and `ReactDOM`, handling version mismatches, and peer dependency federation.
   - Inter-microfrontend communication: Custom Events (`window.dispatchEvent`), shared event emitters, URL/query params, and centralized routing.
   - Isolation & resilience: CSS namespace scoping, independent CI/CD deployment pipelines, and error boundaries protecting the host container from remote runtime crashes.

---

## Web Security (Client & Full-Stack)
1. How do you protect React applications against Cross-Site Scripting (XSS) when using `dangerouslySetInnerHTML`, and how does JSX automatically sanitize interpolated variables?
2. In a React + Node.js application, where should authentication tokens (JWT access & refresh tokens) be stored, and why are `HttpOnly`, `Secure`, `SameSite=Strict` cookies superior to `localStorage` or `sessionStorage`?
3. How do you protect against Cross-Site Request Forgery (CSRF) in Single Page Applications (SPA) communicating with Node.js APIs (Double-Submit Cookie pattern vs anti-CSRF tokens vs `SameSite` attribute)?
4. What HTTP security headers should a Node.js/Express backend enforce using `helmet` (`Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`)?
