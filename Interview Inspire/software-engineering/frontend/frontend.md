# Frontend Engineering Interview Questions

---

## HTML & Web Fundamentals
1. **[Core Concept]** What are Semantic HTML elements and why should you use them over non-semantic elements (`div`, `span`)?
2. **[Core Concept]** What is `srcset` in HTML and how does it compare to the `<picture>` element?
3. **[Core Concept]** How do you handle responsive image loading in modern web apps?
4. **[Core Concept]** What are Web Components (Custom Elements, Shadow DOM, HTML Templates)?
5. **[Core Concept]** What are Service Workers, Web Workers, and Progressive Web Apps (PWAs)?
6. **[Core Concept]** How do you architect an application for multiple devices (responsive design, media queries, relative units, progressive enhancement)?
7. **[Core Concept]** What is the difference between `keydown`, `keypress`, and `keyup` events, and what is the exact execution sequence when a key is pressed?

---

## CSS & Layouts
1. **[Core Concept]** What is the difference between `display: none` and `visibility: hidden`?
2. **[Core Concept]** Explain CSS Box Model (content, padding, border, margin) and `box-sizing: border-box`.
3. **[Core Concept]** Flexbox vs. CSS Grid: When would you use one over the other?
4. **[Core Concept]** How do CSS specificity and the cascade rule work?
5. **[Core Concept]** How does `position: relative`, `absolute`, `fixed`, and `sticky` behave?
6. **[Technical Deep Dive]** What is the purpose of the CSS `will-change` property, and how does it affect GPU acceleration?

---

## JavaScript (Core & Advanced)
1. **[Core Concept]** Explain Closures: What are their benefits, use cases, and limitations?
2. **[Technical Deep Dive]** When do closures cause memory leaks or unexpected retention in long-lived apps, and how do you avoid them?
3. **[Core Concept]** Explain Hoisting and the Temporal Dead Zone (TDZ).
4. **[Technical Deep Dive]** What is the Event Loop? Explain Call Stack, Task Queue (Macrotasks), and Microtask Queue.
5. **[Core Concept]** Can we bind `this` in an arrow function? What happens if you use the `new` operator with an arrow function?
6. **[Technical Deep Dive]** What does the `new` operator do in JavaScript internally step-by-step?
7. **[Core Concept]** What is the difference between `Map` and `Object` in JavaScript? When should you use which?
8. **[Core Concept]** What is Currying? How does it enable partial application and function composition?
9. **[Core Concept]** What is the difference between Prototypal and Classical Inheritance in JavaScript?
10. **[Core Concept]** How does JavaScript handle asynchronous operations? What mechanisms does it use (callbacks, Promises, async/await, generators)?
11. **[Technical Deep Dive]** Does React use `Promise.allSettled()` for parallel API calls? How does that work internally? What is the difference between `Promise.all()` and `Promise.allSettled()`?
12. **[Technical Deep Dive]** What algorithm does `Array.prototype.sort()` use? What is the output of `[1, null, 5, 2, undefined].sort()`?
13. **[Core Concept]** What are Symbols and Generator functions (`function*` and `yield`)?
14. **[Core Concept]** What is the difference between Event Bubbling, Event Capturing, and Event Delegation?
15. **[Technical Deep Dive]** If a user clicks a button multiple times to fetch data, how do you cancel old API calls (`AbortController`) and use only the latest result?
16. **[Core Concept]** How do we apply Object-Oriented Programming (OOP) and SOLID principles in JavaScript?
17. **[Technical Deep Dive]** How does implicit type coercion work in expressions like `1 + +"2" + 3`, and how does the unary plus operator evaluate strings?
18. **[Technical Deep Dive]** What does `typeof` return on rest parameters `(...args)` in JavaScript functions and why?
19. **[Technical Deep Dive]** What are the 4 standard WebSocket lifecycle events (`open`, `message`, `error`, `close`), and how do you implement heartbeat pings and exponential backoff reconnection?

---

## Typescript
1. **[Core Concept]** What is explicit and implicit type assignment?
2. **[Core Concept]** Difference between `any`, `unknown` and `never` in TypeScript?
3. **[Core Concept]** How do you give the type of Arrays?
4. **[Core Concept]** What is Type Inference in array?
5. **[Core Concept]** What are tuples?
6. **[Core Concept]** What are readonly tuples?
7. **[Core Concept]** How to give the types for Objects?
8. **[Core Concept]** How to have optional properties in Objects?
9. **[Core Concept]** Explain enum/String enum in TypeScript?
10. **[Core Concept]** What are Type Aliases?
11. **[Core Concept]** Interfaces and How to extend interfaces?
12. **[Core Concept]** How to give the return type in function?
13. **[Core Concept]** How to give type of parameters in function?
14. **[Core Concept]** How to give optional, default and rest parameters in function?
15. **[Core Concept]** What is casting in TypeScript?
16. **[Core Concept]** What is public, private and protected in TypeScript classes?
17. **[Technical Deep Dive]** What are Generics in TypeScript? Give examples in functions, classes and type aliases.

---

## React & Next.js
1. **[Core Concept]** Which is better for SEO — React, Next.js, or any other library? Why?
2. **[Core Concept]** Can standalone React improve SEO? If yes, how?
3. **[Core Concept]** What parameters improve SEO (SSR/SSG, meta tags, schema structured data, semantic HTML)?
4. **[Core Concept]** What state management libraries have you used?
5. **[Core Concept]** Which one would you choose between `useContext` and Redux/Zustand, and why?
6. **[Technical Deep Dive]** Understanding and optimizing performance in state management (selectors, memoization, preventing unnecessary re-renders).
7. **[Technical Deep Dive]** On input change, how do you make API calls for search suggestions and optimize calls using debounce to avoid network spam?
8. **[Core Concept]** Component Lifecycle and Hooks execution order in React.
9. **[Technical Deep Dive]** Difference between `useMemo` and `useCallback`. When is memoization an anti-pattern?
10. **[Core Concept]** React Server Components (RSC) vs Client Components in Next.js App Router.
11. **[Technical Deep Dive]** How do stale closures occur in React hooks (`useEffect`, `useCallback`, `useState`), and what design patterns prevent reading outdated state values?
12. **[Technical Deep Dive]** Why do object, array, or inline function dependencies in `useEffect` trigger infinite re-render loops, and how do you stabilize reference equality (`useMemo`, `useCallback`, primitive dependencies, `useRef`)?
13. **[Technical Deep Dive]** If a React component is re-rendering excessively (e.g. 50 times/second), what systematic steps and DevTools Profiler metrics do you use to diagnose the root cause (parent cascades vs context churn vs unstable props) and eliminate the bottleneck?
14. **[Technical Deep Dive]** How do you pass a custom comparison function `(prevProps, nextProps)` to `React.memo` to restrict re-renders strictly to specific prop changes?
15. **[Core Concept]** How do you architect code-splitting for conditional heavy libraries (e.g. image vs audio uploaders) using dynamic `import()` and `React.lazy()`?
16. **[Core Concept]** How do you organize multiple React context providers (`ThemeContext`, `UserContext`, `SettingsContext`) without creating "wrapper hell"?

---

## Web Performance & Browser Internals
1. **[Core Concept]** What happens step-by-step when you hit a URL in the browser until pixels are painted?
2. **[Core Concept]** What is the Critical Rendering Path (CRP)? How do you optimize it?
3. **[Core Concept]** What browser events occur when a website is loading (`DOMContentLoaded`, `load`)?
4. **[Technical Deep Dive]** What is the difference between Repaint and Reflow (Layout thrashing)? How do you prevent layout thrashing?
5. **[Core Concept]** What are Preload, Preconnect (Reconnect), Prefetch, and Prerender?
6. **[Technical Deep Dive]** What are render-blocking resources and how do you eliminate them (`async`, `defer`, inlining critical CSS)?
7. **[Technical Deep Dive]** How can you implement caching on a website? Explain `Cache-Control`, `ETag`, `Last-Modified`, and CDN caching.
8. **[Core Concept]** How do you optimize assets? What is image compression and what are the differences between WebP, PNG, and JPG?
9. **[Technical Deep Dive]** What is a Memory Leak in frontend applications? What are the common causes (uncleaned listeners, timers, detached DOM nodes) and how do you profile them?
10. **[Technical Deep Dive]** What are Core Web Vitals (LCP, FID/INP, CLS)? What are the ideal values and how do you improve each?
11. **[Technical Deep Dive]** What is the Webpack build process (Entry, Dependency Graph, Loaders, Plugins, Output)?
12. **[Core Concept]** What is the use of headers in HTTP requests (`Content-Type`, `Authorization`, `Cache-Control`, `User-Agent`)?

---

## Machine Coding & Practical Implementations
1. **[Machine Coding]** Write a polyfill for `sum(1)(2)(3)()` to return `6`.
2. **[Machine Coding]** Implement a debounce and throttle function from scratch.
3. **[Machine Coding]** Build an interactive Star Rating component with hover, click, and half-star support.
4. **[Machine Coding]** Build an autocomplete / search suggestion input with debounced API requests and request cancellation.
5. **[Machine Coding]** Build a user listing dashboard with live search, dropdown filtering, and TypeScript types.
6. **[Machine Coding]** Build an accessible Modal dialog component in React with keyboard focus trapping, `Escape` key dismissal, backdrop click detection, and describe how to unit test it with Jest and React Testing Library (RTL).
7. **[Machine Coding]** Build an API data-rendering transaction list component handling loading skeleton, error fallback, and empty states, optimizing re-renders with `useMemo` and `React.memo`.

---

## Frontend System Design
1. **[System Design]** **Design a Live Payments Feed / Financial Dashboard Widget (e.g. Razorpay)**:
   - Real-time transport protocols: Polling (Short/Long) vs WebSockets vs Server-Sent Events (SSE) for low-latency live transactions.
   - Large list performance: Virtualization and windowing (`react-window`, `@tanstack/react-virtual`) to render 1,000+ to 10,000+ transaction rows without DOM thrashing.
   - Client state architecture: Server-state caching and deduplication (TanStack Query / SWR) vs Global client store (Redux Toolkit / Zustand).
   - Pagination vs Infinite scrolling: Tradeoffs for financial audit logs, state restoration, and scroll position anchoring.
   - Accessibility (a11y) for dynamic feeds: Utilizing ARIA live regions (`aria-live="polite"` vs `"assertive"`, `aria-atomic`) so assistive technologies announce incoming transactions without disrupting screen reader navigation.
