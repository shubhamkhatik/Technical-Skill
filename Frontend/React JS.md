# React JS

# React.js

---

## Core Concepts

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Functional Components | The modern standard. Pure functions that take props and return JSX. React re-renders when state or props change. No `this` keyword. | React 18+, React DevTools | Destructuring props, default props, children composition, named exports | [react.dev – Your First Component](https://react.dev/learn/your-first-component) |
| Class Components *(Legacy)* | Older lifecycle-based model (`componentDidMount`, `componentDidUpdate`). Still exists in many codebases — know how to read, not write | React (any version) | Reading `this.state`, `this.setState`, lifecycle methods, migrating to hooks | [react.dev – Class Components](https://react.dev/reference/react/Component) |
| JSX | Syntactic sugar over `React.createElement`. Not HTML — class→`className`, for→`htmlFor`, self-closing tags required, only one root element | Babel / esbuild (transpiles JSX) | Conditional rendering (`&&`, ternary), list rendering with `.map()` + `key`, fragments (`<>`) | [react.dev – JSX](https://react.dev/learn/writing-markup-with-jsx) |
| Component Composition | Building UIs by combining small, focused components. Prefer composition over inheritance in React | — | Props + children pattern, slot pattern via named props, compound components, render delegation | [react.dev – Passing JSX as children](https://react.dev/learn/passing-props-to-a-component#passing-jsx-as-children) |
| Props & Data Flow | Unidirectional data flow — data flows down via props, events bubble up via callbacks. Enforces predictability | PropTypes *(runtime)*, TypeScript *(compile-time)* | Props destructuring, callback props for child→parent communication, prop drilling (and when it becomes a problem) | [react.dev – Passing Props](https://react.dev/learn/passing-props-to-a-component) |
| Event Handling | React uses synthetic events (cross-browser normalized wrapper over native events). All events are camelCase | — | `onClick`, `onChange`, `onSubmit`, `e.preventDefault()`, `e.stopPropagation()`, event delegation | [react.dev – Responding to Events](https://react.dev/learn/responding-to-events) |

---

## React Hooks

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| `useState` | Declares state in a functional component. Re-renders the component on each state change. State updates are asynchronous (batched in React 18+) | — | Functional updater form `setState(prev => ...)`, avoid mutating state directly, initializer function for expensive default | [react.dev – useState](https://react.dev/reference/react/useState) |
| `useEffect` | Synchronize component with an external system (fetch, DOM, subscriptions). Runs after render. Cleanup function prevents memory leaks | — | Dependency array, cleanup via return function, empty `[]` = run once on mount, avoid missing dependencies | [react.dev – useEffect](https://react.dev/reference/react/useEffect) |
| `useRef` | Mutable ref that doesn't trigger re-renders. Two uses: (1) access DOM nodes, (2) persist values across renders without re-rendering | — | DOM refs (`ref.current` for focus/scroll), storing previous values, `forwardRef` to expose refs to parent components | [react.dev – useRef](https://react.dev/reference/react/useRef) |
| `useContext` | Consume values from a Context without prop drilling. Re-renders every consumer when context value changes | — | `createContext`, `Provider` wrapping, context splitting to avoid over-renders, combine with `useMemo` for stable values | [react.dev – useContext](https://react.dev/reference/react/useContext) |
| `useMemo` | Cache an expensive computed value between renders. Only recomputes when dependencies change | — | Wrap CPU-intensive calculations, stabilize object/array references passed as props to memoized children | [react.dev – useMemo](https://react.dev/reference/react/useMemo) |
| `useCallback` | Cache a function definition between renders. Needed when passing callbacks to `React.memo` children or as effect dependencies | — | Wrap event handlers passed to memoized children, stabilize callbacks used in `useEffect` dependency arrays | [react.dev – useCallback](https://react.dev/reference/react/useCallback) |
| `useReducer` | Alternative to `useState` for complex state logic with multiple sub-values or when next state depends on previous state. Follows Redux-like pattern | — | Action dispatch pattern, reducer purity, combining with `useContext` for lightweight global state | [react.dev – useReducer](https://react.dev/reference/react/useReducer) |
| `useLayoutEffect` | Like `useEffect` but fires synchronously after DOM mutations and before the browser paints. Use only when you need to read/write DOM layout | — | Measuring DOM size/position, preventing visual flicker, tooltip/popover positioning | [react.dev – useLayoutEffect](https://react.dev/reference/react/useLayoutEffect) |
| `useId` *(React 18)* | Generates stable unique IDs that are consistent across server and client. Solves hydration mismatch for accessibility IDs | — | Label–input association (`htmlFor` + `id`), ARIA attribute IDs | [react.dev – useId](https://react.dev/reference/react/useId) |
| `useTransition` *(React 18)* | Mark a state update as non-urgent so React can interrupt it for higher-priority updates (e.g., typing). Core to Concurrent React | — | Wrap slow state updates, `isPending` flag for loading UI, tab switching, search filtering on large lists | [react.dev – useTransition](https://react.dev/reference/react/useTransition) |
| `useDeferredValue` *(React 18)* | Defer re-rendering a part of the UI to keep the interface responsive. Similar to debounce but React-aware | — | Defer expensive child re-renders, show stale content while new content loads, combine with `React.memo` | [react.dev – useDeferredValue](https://react.dev/reference/react/useDeferredValue) |
| Custom Hooks | Extract and reuse stateful logic between components. The most important abstraction pattern in React | — | `use` prefix convention, composing built-in hooks, returning values + setters, hook libraries (ahooks, react-use) | [react.dev – Custom Hooks](https://react.dev/learn/reusing-logic-with-custom-hooks) |

---

## Routing & Navigation

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Client-Side Routing | SPA navigation without full page reload. History API manipulation. Routes defined as a component tree | React Router v6+ *(Reach Router is merged and deprecated — do not use)* | `<BrowserRouter>`, `<Routes>`, `<Route>`, `<Link>`, `<NavLink>` (active state styling) | [React Router docs](https://reactrouter.com/en/main) |
| Dynamic Routes & Params | URL segments as data. Nested routes with shared layout via `<Outlet>` | React Router v6+ | `useParams`, `useSearchParams`, route loaders (data fetching at route level), `<Outlet>` for nested layouts | [React Router – Dynamic Segments](https://reactrouter.com/en/main/route/route#dynamic-segments) |
| Programmatic Navigation | Navigate from code (after form submit, auth check, etc.) | React Router v6+ | `useNavigate` *(replaces deprecated `useHistory` from v5)*, `navigate(-1)` for back, `replace: true` to avoid history stack entries | [React Router – useNavigate](https://reactrouter.com/en/main/hooks/use-navigate) |
| Protected Routes | Guard routes behind authentication or authorization checks | React Router v6+, React context | Redirect unauthenticated users, role-based access, loader-based auth checks | [React Router – Auth example](https://reactrouter.com/en/main/start/examples) |
| Route-level Code Splitting | Load component code only when the route is visited — reduces initial bundle | `React.lazy`, `Suspense`, React Router v6 | Wrap lazy-imported components in `<Suspense fallback={...}>`, combine with route loaders | [react.dev – lazy](https://react.dev/reference/react/lazy) |

---

## Forms & Input Handling

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Controlled Components | React state is the single source of truth for input values. Verbose but predictable and testable | `useState` | `value` + `onChange` on every input, controlled select/checkbox/radio, forms as state snapshots | [react.dev – Forms](https://react.dev/learn/sharing-state-between-components) |
| Uncontrolled Components | DOM is the source of truth. Use when integrating with non-React libraries or for simple forms where controlled is overkill | `useRef` | `ref` on input, `defaultValue`, `ref.current.value` on submit — avoid for complex validation | [react.dev – Uncontrolled](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable) |
| Form Libraries | Manage form state, validation, error messages, and submission declaratively — reduces boilerplate significantly | **React Hook Form** *(performant, minimal re-renders)*, Formik *(older, more re-renders)* | `register`, `handleSubmit`, `formState.errors`, field arrays, `watch`, `setValue` | [React Hook Form docs](https://react-hook-form.com/) |
| Schema Validation | Declare validation rules as a schema separate from UI logic. Works with both RHF and Formik | **Zod** *(TypeScript-first, preferred)*, Yup | `zodResolver` / `yupResolver` with RHF, type inference from schema (`z.infer<typeof schema>`), nested object validation | [Zod docs](https://zod.dev/), [RHF + Zod](https://react-hook-form.com/get-started#SchemaValidation) |

---

## Data Fetching & API Integration

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Native Fetch / Axios | Understand the base layer before reaching for libraries. Axios adds interceptors, automatic JSON parsing, request cancellation | `fetch` (built-in), Axios | `async/await`, `AbortController` for cancellation, Axios request/response interceptors, error status handling | [MDN Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), [Axios docs](https://axios-http.com/) |
| Server State Management | Distinguish client state (UI) from server state (remote data). Server state needs caching, background refetching, staleness management — this is not what Redux is for | TanStack Query, SWR | Query keys strategy, `staleTime` vs `cacheTime`, mutations + `invalidateQueries`, optimistic updates, prefetching | [TanStack Query docs](https://tanstack.com/query/latest) |
| Error Boundaries | React mechanism to catch render errors in a subtree and display a fallback UI. Essential for graceful degradation | `react-error-boundary` library | `<ErrorBoundary fallback={...}>`, `useErrorBoundary` hook for imperative throws, per-route boundaries | [react-error-boundary](https://github.com/bvaughn/react-error-boundary) |
| Suspense for Data | Declarative loading states. Component "suspends" while data loads; React shows the nearest `<Suspense>` fallback | TanStack Query (experimental), Next.js (stable) | `<Suspense fallback={<Skeleton />}>`, streaming in Next.js App Router, `use()` hook in React 19 | [react.dev – Suspense](https://react.dev/reference/react/Suspense) |

---

## Performance Optimization

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Preventing Re-renders | A component re-renders when its state/props change OR when its parent re-renders. Understand this before optimizing | React DevTools Profiler | `React.memo` (memoize component), `useMemo` (memoize values), `useCallback` (memoize functions) — **only add when profiler confirms a problem** | [react.dev – Render Performance](https://react.dev/learn/render-and-commit) |
| Code Splitting | Load JavaScript only when needed. Route-level splitting is the highest-ROI optimization in most apps | `React.lazy`, `Suspense`, dynamic `import()` | Lazy-load routes, lazy-load heavy modals/drawers, named chunk comments `/* webpackChunkName */` | [react.dev – lazy](https://react.dev/reference/react/lazy) |
| Virtualized Lists | Rendering thousands of DOM nodes destroys performance. Virtualization only renders visible items | react-window, TanStack Virtual | `FixedSizeList`, `VariableSizeList`, `WindowScroller` for page-level scroll, infinite scroll with virtualization | [react-window docs](https://react-window.vercel.app/) |
| Concurrent Features | React 18's scheduler can interrupt, pause, and resume renders. Use `useTransition` + `useDeferredValue` to mark non-urgent work | React 18+ | `startTransition` for non-urgent state updates, `useDeferredValue` for derived expensive renders | [react.dev – Concurrent React](https://react.dev/blog/2022/03/29/react-v18) |
| Profiling | Measure before optimizing. Guessing is wasteful; the Profiler shows exactly which components are slow and why | React DevTools Profiler, Chrome Performance tab | Record → identify slow commits → find the component → apply targeted fix | [react.dev – Profiler](https://react.dev/reference/react/Profiler) |

---

## State Management (Advanced)

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Redux Toolkit | Centralized store for complex, highly shared state. Overkill for most apps — use when state is shared across many unrelated components | Redux Toolkit, Redux DevTools | `createSlice`, `createAsyncThunk`, `createSelector`, time-travel debugging, state normalization | [Redux Toolkit docs](https://redux-toolkit.js.org/) |
| RTK Query | Data fetching + caching built into Redux Toolkit. Competes with TanStack Query but keeps everything in Redux | Redux Toolkit | `createApi`, endpoints, cache tag invalidation, auto-generated hooks | [RTK Query docs](https://redux-toolkit.js.org/rtk-query/overview) |
| Zustand | Minimal global state. No boilerplate, no providers. Best for small-to-medium apps | Zustand | `create` store with actions, slice pattern for large stores, persist middleware, devtools middleware | [Zustand docs](https://docs.pmnd.rs/zustand) |
| Jotai | Atomic state model — state is split into small atoms. Bottom-up approach, avoids unnecessary re-renders | Jotai | Primitive atoms, derived atoms, async atoms, atom families, Jotai DevTools | [Jotai docs](https://jotai.org/) |
| Context API | Built-in React mechanism for sharing state. Fine for low-frequency updates (theme, auth user). **Not a performance-optimized global state solution** | React built-in | `createContext`, `useContext`, context splitting, combine with `useReducer` for a Redux-lite pattern | [react.dev – Context](https://react.dev/learn/passing-data-deeply-with-context) |

---

## Styling in React

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| CSS Modules | Scoped CSS — class names are locally scoped by default, preventing collisions. **Not CSS-in-JS** — still plain CSS files, processed at build time | Vite (built-in), webpack `css-loader` | `styles.className` import syntax, `:global()` for unscoped selectors, `composes` for shared styles | [Vite CSS Modules](https://vitejs.dev/guide/features.html#css-modules) |
| CSS-in-JS | Write CSS as JavaScript. Runtime (styled-components, emotion) or zero-runtime (vanilla-extract). Tradeoff: flexibility vs runtime cost | styled-components, emotion *(runtime)*; vanilla-extract *(zero-runtime)* | Tagged template literals, dynamic styles via props, theme provider, `css` helper, global styles | [styled-components docs](https://styled-components.com/) |
| Tailwind CSS in React | Utility-first — compose design directly in JSX. Works extremely well with component-based architecture | Tailwind CSS, `clsx`, `cva` (class-variance-authority) | Conditional classes with `clsx`, variant system with `cva`, `@apply` for extracted components | [Tailwind + React guide](https://tailwindcss.com/docs/guides/create-react-app) |
| Headless UI | Fully accessible, unstyled component primitives. You own the styling, they own the accessibility logic | Radix UI, Headless UI (Tailwind Labs) | Compound component API, controlled/uncontrolled modes, ARIA attributes auto-managed, pair with Tailwind | [Radix UI docs](https://www.radix-ui.com/) |
| Animation | CSS transitions for simple, Framer Motion for complex gesture/physics-based animations | Framer Motion, React Spring, CSS | `motion.div`, `AnimatePresence` for exit animations, layout animations, drag gestures, `useSpring` | [Framer Motion docs](https://www.framer.com/motion) |

---

## Testing

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Unit Testing (Logic) | Test pure functions, hooks, utilities in isolation from the DOM | Jest, Vitest | Arrange-Act-Assert, `jest.mock`, module mocking, test coverage | [Jest docs](https://jestjs.io/) |
| Component Testing | Test component behavior from the user's perspective — what they see and interact with, not implementation details | React Testing Library | `getByRole`, `getByText`, `userEvent.type/click`, async `findBy`, `waitFor`, render with custom providers | [testing-library.com](https://testing-library.com/docs/react-testing-library/intro) |
| Hook Testing | Test custom hooks in isolation. **`@testing-library/react-hooks` is deprecated** — use `renderHook` from `@testing-library/react` instead | `@testing-library/react` (v13+) | `renderHook`, `act`, asserting hook return values and state changes | [RTL – renderHook](https://testing-library.com/docs/react-testing-library/api/#renderhook) |
| API Mocking | Intercept network requests at the service worker level — same mocks work in browser, unit tests, and E2E | MSW (Mock Service Worker) | `http.get/post` handlers, `server.use` for per-test overrides, error scenario mocking | [mswjs.io](https://mswjs.io/) |
| E2E Testing | Full browser automation testing real user flows through the actual UI | Playwright *(preferred)*, Cypress | Page Object Model, `data-testid` attributes, network intercepts, parallel runs, visual comparisons | [Playwright docs](https://playwright.dev/) |
| Snapshot Testing | Catches unintended UI changes by comparing rendered output to a saved snapshot. **Brittle if overused** — prefer behavior tests | Jest | `toMatchSnapshot`, inline snapshots, when to update vs investigate a snapshot diff | [Jest – Snapshot Testing](https://jestjs.io/docs/snapshot-testing) |

---

## Architecture & Patterns

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Component Design Principles | Single responsibility, separation of concerns, container vs presentational (now often done via hooks), smart vs dumb components | — | Extract logic into custom hooks, keep UI components "dumb", colocate related files | [react.dev – Thinking in React](https://react.dev/learn/thinking-in-react) |
| Compound Components | Components that work together and share implicit state (e.g., `<Select>` + `<Select.Option>`). Cleaner API than deeply nested props | — | `React.Children`, `cloneElement`, or Context-based sharing between parent and child components | [Kent C. Dodds – Compound Components](https://kentcdodds.com/blog/compound-components-with-react-hooks) |
| Higher-Order Components *(Legacy)* | Wrap a component to inject props or behavior. Mostly replaced by hooks — but still found in older codebases | — | Reading HOC-wrapped code, understanding prop injection, migrating to custom hooks | — |
| Render Props *(Legacy)* | Pass a function as a prop that returns JSX — shares stateful logic. Mostly replaced by hooks | — | Reading render prop pattern, understanding the inversion of control, migrating to hooks | — |
| Error Boundaries | Catch JavaScript errors during rendering in a subtree, display a fallback instead of crashing the whole app. **Only class components can be error boundaries natively** | `react-error-boundary` (hooks-friendly wrapper) | Per-section boundaries, `onError` for logging, `resetKeys` to auto-recover on prop change | [react-error-boundary](https://github.com/bvaughn/react-error-boundary) |
| Feature-based Folder Structure | Organize by feature/domain, not by file type. Scales better than `components/`, `hooks/`, `utils/` flat structure | — | `features/auth/`, `features/dashboard/` with co-located component, hook, test, and type files | [Bulletproof React](https://github.com/alan2207/bulletproof-react) |

---

## Accessibility (a11y)

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Semantic HTML & ARIA | Screen readers rely on semantic meaning. Use native elements when possible (`<button>`, `<nav>`, `<main>`). ARIA supplements when native semantics aren't enough | axe-core, Storybook a11y addon | ARIA roles, `aria-label` vs `aria-labelledby`, `aria-live` for dynamic content, avoid ARIA anti-patterns | [MDN ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA), [web.dev/accessibility](https://web.dev/accessibility) |
| Keyboard Navigation | All interactive elements must be keyboard accessible. Focus management is critical in SPAs | — | `tabIndex`, `onKeyDown` for custom components, `focus()` after modal open/close, focus trap in modals, skip-nav links | [WCAG 2.1 Guidelines](https://www.w3.org/TR/WCAG21) |
| Accessible Forms | Labels, error messages, and descriptions must be programmatically associated with inputs | React Hook Form + Zod | `htmlFor` + `id` association, `aria-describedby` for error messages, `aria-invalid`, `role="alert"` for errors | [WebAIM Forms](https://webaim.org/techniques/forms) |
| Auditing | Automated tools catch ~30% of issues. Manual testing with keyboard + screen reader required for real confidence | axe-core, Lighthouse, NVDA/VoiceOver | Run axe in tests (`jest-axe`), Lighthouse a11y audit, keyboard-only walkthrough | [jest-axe](https://github.com/nickcolley/jest-axe) |

---

## Development Tools & Workflow

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Project Setup | **CRA (Create React App) is deprecated and unmaintained** — do not use for new projects | **Vite** *(recommended for SPA)*, Next.js *(full-stack/SSR)*, Remix | Vite's `create vite` template, HMR, fast dev server, minimal config | [Vite docs](https://vitejs.dev/) |
| React DevTools | Inspect component tree, props, state, and context at runtime. Profiler tab shows render performance | React Developer Tools (browser extension) | Component tree inspection, props/state editing, Profiler flamechart, highlight re-renders | [React DevTools](https://react.dev/learn/react-developer-tools) |
| Code Quality | Enforce consistent code style and catch errors before runtime | ESLint (`eslint-plugin-react`, `eslint-plugin-react-hooks`), Prettier, Husky, lint-staged | `react-hooks/rules-of-hooks`, `react-hooks/exhaustive-deps` rules, pre-commit hooks to block bad code | [eslint-plugin-react-hooks](https://www.npmjs.com/package/eslint-plugin-react-hooks) |
| TypeScript in React | Type-safe props, events, refs, hooks. Prefer explicit prop interfaces over `React.FC` (which has subtle issues with generics and `children`) | TypeScript, `@types/react` | `interface Props {}`, typed `useState<Type>`, typed event handlers (`React.ChangeEvent<HTMLInputElement>`), generic components | [react.dev – TypeScript](https://react.dev/learn/typescript) |