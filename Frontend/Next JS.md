# Next JS

[UI System Design in Next JS](Next%20JS/UI%20System%20Design%20in%20Next%20JS%20325bc1534cbb8016b26cc2bad7df7f61.md)

# Next.js

> **Mental Model First:** Next.js is a React framework that moves work to the server — rendering, data fetching, caching, routing — so the client receives less JavaScript and more ready-to-use HTML. Every decision in Next.js is about *where* and *when* code runs: build time, server request time, or client.
> 

---

## Routing — App Router vs Pages Router

> These are two completely different routing paradigms. **App Router (Next.js 13+) is the current standard.** Pages Router still works and is in millions of production apps — you must understand both.
> 

| Skill | Core Concepts | App Router (`/app`) | Pages Router (`/pages`) | Resources |
| --- | --- | --- | --- | --- |
| File-based Routing | Folder/file structure defines URL structure — no router config needed | `app/dashboard/page.tsx` → `/dashboard`. Special files: `page`, `layout`, `loading`, `error`, `not-found` | `pages/dashboard.tsx` → `/dashboard`. `_app.tsx` (global wrapper), `_document.tsx` (HTML shell) | [Next.js – App Router](https://nextjs.org/docs/app/building-your-application/routing) |
| Layouts | Persistent UI that wraps child routes. Layouts do **not** re-render on navigation — state is preserved | `layout.tsx` files nest automatically. Root layout required. Layouts can fetch their own data | `_app.tsx` for global layout; custom layout pattern using per-page `getLayout` function | [Next.js – Layouts](https://nextjs.org/docs/app/building-your-application/routing/layouts-and-templates) |
| Dynamic Routes | URL segments as parameters | `app/blog/[slug]/page.tsx` → `params.slug`; `[...slug]` for catch-all; `[[...slug]]` for optional | `pages/blog/[slug].tsx` → `useRouter().query.slug` or `getStaticProps({ params })` | [Next.js – Dynamic Routes](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes) |
| Nested Routes & Parallel Routes | Render multiple independent route segments in the same layout | Parallel Routes via `@slot` folders — render sibling pages (e.g., modal + page simultaneously). Intercepting Routes via `(.)` convention | Not available | [Next.js – Parallel Routes](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) |
| Route Groups | Organize routes without affecting URL structure. Share layouts among a subset of routes | `(marketing)/about/page.tsx` → `/about` (parens excluded from URL) | Not available | [Next.js – Route Groups](https://nextjs.org/docs/app/building-your-application/routing/route-groups) |
| Navigation | Client-side navigation without full page reload | `<Link>` component (prefetches on hover), `useRouter()` for programmatic nav, `redirect()` for server-side redirects | `<Link>` component, `useRouter().push()`, `router.replace()` | [Next.js – Linking](https://nextjs.org/docs/app/building-your-application/routing/linking-and-navigating) |

---

## Rendering Strategies

> The core question: *when* is the HTML generated? Each strategy has different performance, freshness, and infrastructure tradeoffs.
> 

| Strategy | When HTML is Generated | App Router Approach | Pages Router Approach | Best For |
| --- | --- | --- | --- | --- |
| **SSG** – Static Site Generation | Once at **build time** | `fetch(url, { cache: 'force-cache' })` inside async Server Component; `generateStaticParams` for dynamic paths | `getStaticProps` + `getStaticPaths` | Marketing pages, blogs, docs — content that rarely changes |
| **SSR** – Server-Side Rendering | On **every request** | `fetch(url, { cache: 'no-store' })` or `const data = await fetchData()` with no caching in a Server Component | `getServerSideProps` — runs on every request | Dashboards with real-time data, personalized pages, auth-protected content |
| **ISR** – Incremental Static Regeneration | At build time, **revalidated** after N seconds or on-demand | `fetch(url, { next: { revalidate: 60 } })` or `export const revalidate = 60` at segment level | `getStaticProps` with `revalidate: 60` return value | E-commerce product pages, news sites — mostly static but needs freshness |
| **CSR** – Client-Side Rendering | In the **browser** after JS loads | Add `'use client'` + TanStack Query / SWR for data fetching — opt out of server rendering | `useEffect` + fetch, or SWR/React Query on page component | Highly interactive sections, real-time data (dashboards, charts, user feeds) |
| **Streaming** | Progressively from the **server** as components resolve | Wrap slow components in `<Suspense fallback={...}>`. `loading.tsx` auto-wraps the entire segment | Not available natively | Pages with mixed fast/slow data sources — avoid blocking the whole page on one slow query |

---

## Server Components vs Client Components

> The most important mental model in the App Router. **All components are Server Components by default.**
> 

| Aspect | Server Components | Client Components |
| --- | --- | --- |
| **Where they run** | Node.js server — never shipped to browser | Browser (+ server for initial HTML via SSR) |
| **How to declare** | Default — no directive needed | Add `'use client'` at the top of the file |
| **Can use** | `async/await`, direct DB access, secrets/env vars, server-only APIs | Hooks (`useState`, `useEffect`), browser APIs, event listeners |
| **Cannot use** | Hooks, browser APIs, `window`, event handlers | Direct DB access, server-only modules |
| **Bundle impact** | Zero JS added to client bundle | JavaScript is shipped to and executed by the browser |
| **When to use** | Layout, data fetching, non-interactive UI | Interactive UI, forms, animations, anything that responds to user input |
| **Composition rule** | Server Components **can** import Client Components | Client Components **cannot** import Server Components (but can receive them as `children` props) |

---

## Data Fetching

> App Router fundamentally changed data fetching. The extended `fetch` API and React's cache system replace `getStaticProps` / `getServerSideProps` entirely.
> 

| Skill | Core Concepts | Tools & Techniques | Key Details | Resources |
| --- | --- | --- | --- | --- |
| Server Component Fetching | `async/await` directly in the component body — no `useEffect`, no loading state needed. React deduplicates identical `fetch` calls automatically | Extended `fetch` with cache options | `cache: 'force-cache'` (SSG), `cache: 'no-store'` (SSR), `next: { revalidate: N }` (ISR). Fetch at the component level, not the page level — only fetch what each component needs | [Next.js – Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching) |
| Server Actions | **Next.js 14+ feature.** Async server functions called directly from forms or client components — no API route needed for mutations. Replace most POST endpoints | `'use server'` directive (inline or in a separate file) | Form `action={serverAction}`, `useFormState` / `useActionState` for progressive enhancement, automatic revalidation with `revalidatePath` / `revalidateTag` | [Next.js – Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations) |
| Route Handlers | API endpoints inside the App Router. Replace `pages/api/` routes. Used for webhooks, OAuth callbacks, or when you need a real HTTP endpoint | `app/api/route/route.ts` with exported `GET`, `POST`, `PATCH`, `DELETE` functions | Request/Response Web API, no Express needed, streaming responses supported, `NextRequest` / `NextResponse` helpers | [Next.js – Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) |
| ORM / Database Access | Query the database directly from Server Components or Server Actions — no intermediary API layer needed | Prisma *(type-safe, popular)*, Drizzle *(lightweight, SQL-first)*, Mongoose *(MongoDB)* | Keep DB logic in a `lib/db.ts` or `server/` folder; never import server-only modules into Client Components; use `server-only` package to guard | [Prisma + Next.js](https://www.prisma.io/nextjs) |
| Caching & Revalidation | Next.js has a multi-layer cache. Understanding it prevents stale data bugs | `revalidatePath`, `revalidateTag`, `unstable_cache` | Tag fetches with `next: { tags: ['products'] }` → call `revalidateTag('products')` on mutation for surgical cache invalidation | [Next.js – Caching](https://nextjs.org/docs/app/building-your-application/caching) |

---

## Middleware

| Skill | Core Concepts | Tools & Techniques | Key Details | Resources |
| --- | --- | --- | --- | --- |
| Middleware | Runs at the **Edge** before a request reaches your page or API route. Used for auth checks, redirects, locale detection, A/B testing, request/response header manipulation | `middleware.ts` at project root, `NextRequest`, `NextResponse`, `matcher` config | Does **not** have access to Node.js APIs (no `fs`, no Prisma) — runs in Edge Runtime. Use `matcher` to limit which routes trigger it. Avoid heavy logic — it adds latency to every matched request | [Next.js – Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware) |

---

## Performance Optimization

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| `next/image` | Automatic WebP/AVIF conversion, responsive `srcset`, lazy loading, prevents CLS by requiring `width`/`height` or `fill`. CDN delivery via Vercel or custom loader | `<Image>` component | `priority` prop for LCP image (above the fold), `fill` + `object-fit` for cover images, `sizes` prop for responsive, custom `loader` for external CDN | [Next.js – Image](https://nextjs.org/docs/app/api-reference/components/image) |
| `next/font` | Downloads fonts at build time, self-hosts them — zero layout shift, no external network request to Google Fonts at runtime | `next/font/google`, `next/font/local` | `Inter({ subsets: ['latin'], display: 'swap' })`, apply via CSS variable to Tailwind, font subsetting to reduce size | [Next.js – Font](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) |
| `next/dynamic` | Client-side lazy loading for heavy components. App Router equivalent is `React.lazy` + `Suspense`, but `next/dynamic` adds `ssr: false` option | `dynamic(() => import(...), { ssr: false })` | `ssr: false` for browser-only libraries (charts, maps, rich text editors), `loading` prop for fallback UI | [Next.js – Dynamic Imports](https://nextjs.org/docs/app/building-your-application/optimizing/lazy-loading) |
| `next/script` | Control when third-party scripts load — avoid blocking rendering | `<Script>` component | `strategy: 'lazyOnload'` (after everything), `'afterInteractive'` (after hydration), `'beforeInteractive'` (before hydration — rare) | [Next.js – Script](https://nextjs.org/docs/app/api-reference/components/script) |
| Bundle Analysis | Identify which dependencies are bloating your JavaScript bundle | `@next/bundle-analyzer` | Wrap `next.config.js` with analyzer, look for large vendor chunks, check for duplicate packages | [Bundle Analyzer](https://www.npmjs.com/package/@next/bundle-analyzer) |
| Partial Prerendering *(PPR, experimental)* | Next.js 14+ experimental feature. Combines static shell with dynamic streaming holes in a single request — best of SSG + SSR | `experimental: { ppr: true }` in `next.config.js` | Static outer shell serves instantly from CDN, dynamic `<Suspense>` holes stream in — reduces TTFB without sacrificing freshness | [Next.js – PPR](https://nextjs.org/docs/app/building-your-application/rendering/partial-prerendering) |

---

## SEO & Metadata

| Skill | Core Concepts | Tools & Techniques | Key Details | Resources |
| --- | --- | --- | --- | --- |
| Metadata API | App Router's built-in way to set `<head>` tags — replaces `next/head`. Supports both static and dynamic metadata | `export const metadata` (static), `export async function generateMetadata()` (dynamic) | Dynamic metadata can fetch data (e.g., blog post title from DB), colocated per `page.tsx`, type-safe `Metadata` object from Next.js | [Next.js – Metadata](https://nextjs.org/docs/app/building-your-application/optimizing/metadata) |
| Open Graph & Twitter Cards | Rich previews when links are shared on social media | `metadata.openGraph`, `metadata.twitter`, `opengraph-image.tsx` | Dynamic OG images via `opengraph-image.tsx` (renders JSX to image at request time using Satori) | [Next.js – OG Image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) |
| Sitemap & Robots | Help search engines discover and crawl your pages | `sitemap.ts` (dynamic generation), `robots.ts` | `sitemap.ts` exports an array of URLs with `lastModified` — auto-generates `/sitemap.xml`; `robots.ts` replaces manual `robots.txt` | [Next.js – Sitemap](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap) |
| Structured Data | Machine-readable context for search engines — enables rich results | JSON-LD via `<script type="application/ld+json">` in Server Component | Inject in `layout.tsx` or `page.tsx` using a Server Component — no third-party library needed | [Schema.org](https://schema.org/), [Google Rich Results](https://search.google.com/test/rich-results) |

---

## Authentication & Authorization

| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |
| --- | --- | --- | --- | --- |
| Authentication Solutions | Managed vs self-hosted auth. Clerk handles UI + sessions; Auth.js gives you full control; Lucia is lightweight DIY | **Clerk** *(managed, easiest UX)*, **Auth.js v5 / NextAuth** *(self-hosted, flexible)*, Lucia *(DIY, full control)* | Session cookie vs JWT strategy, OAuth provider setup, database adapter for persisting sessions | [Auth.js docs](https://authjs.dev/), [Clerk docs](https://clerk.com/docs) |
| Authorization & Route Protection | Protect pages and API routes based on auth state or user roles | Middleware (`middleware.ts`) + session check | Check session in `middleware.ts` for route-level protection — redirect unauthenticated users before the page renders; check roles inside Server Components or Server Actions for data-level authorization | [Auth.js – Middleware](https://authjs.dev/getting-started/session-management/protecting) |
| Security Headers | Protect against XSS, clickjacking, MIME sniffing, and other header-based attacks | `next.config.js` `headers()` function | Set `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Referrer-Policy` | [Next.js – Security Headers](https://nextjs.org/docs/app/building-your-application/configuring/content-security-policy) |

---

## Deployment & Infrastructure

| Skill | Core Concepts | Tools & Platforms | Key Details | Resources |
| --- | --- | --- | --- | --- |
| Vercel *(first-party)* | Built by the Next.js team — zero-config deployment, automatic preview deployments per PR, Edge Network, analytics | Vercel CLI, GitHub integration | Automatic static/serverless/edge routing per Next.js output type, environment variables via dashboard, `vercel.json` for config | [Vercel docs](https://vercel.com/docs) |
| Self-hosted (Node.js) | Run `next start` after `next build`. Standard Node.js server — full feature support | Node.js, PM2, Nginx (reverse proxy) | `output: 'standalone'` in `next.config.js` for minimal deployment package (Docker-friendly) | [Next.js – Self-hosting](https://nextjs.org/docs/app/building-your-application/deploying) |
| Docker | Containerize the Next.js app for consistent environments across dev, staging, production | Docker, Docker Compose, multi-stage Dockerfile | Multi-stage build (dependencies → builder → runner), `output: 'standalone'` to reduce image size significantly | [Next.js – Docker example](https://github.com/vercel/next.js/tree/canary/examples/with-docker) |
| Static Export | Export as pure static HTML/CSS/JS — no Node.js server needed. **`next export` is removed in Next.js 13+** | `output: 'export'` in `next.config.js` | Limitations: no Server Components with dynamic data, no middleware, no ISR, no image optimization without custom loader | [Next.js – Static Export](https://nextjs.org/docs/app/building-your-application/deploying/static-exports) |
| Edge Deployment | Run route handlers and middleware at the CDN edge — lower latency globally, but limited runtime (no Node.js APIs) | Vercel Edge, Cloudflare Workers, `runtime: 'edge'` | `export const runtime = 'edge'` on a route handler/page; use only Web APIs; best for geolocation, auth redirects, personalization | [Next.js – Edge Runtime](https://nextjs.org/docs/app/building-your-application/rendering/edge-and-nodejs-runtimes) |
| CI/CD | Automate build, test, and deploy pipeline | GitHub Actions, Vercel (built-in preview deploys) | Run `next build` in CI to catch build errors early; add `next lint` and type-check step; use Vercel preview deployments for PRs | [GitHub Actions + Vercel](https://vercel.com/guides/how-can-i-use-github-actions-with-vercel) |

---

## Advanced Features

| Skill | Core Concepts | Tools & Techniques | Key Details | Resources |
| --- | --- | --- | --- | --- |
| Middleware (Advanced) | Beyond auth: A/B testing, feature flags, bot detection, locale/country-based routing | `NextRequest.geo`, `NextRequest.ip`, `next-ab-test` | Read `request.geo.country` for geo-routing; set cookies in middleware to persist A/B variant; combine with edge config for real-time flag changes without redeploy | [Next.js – Middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware) |
| Internationalization (i18n) | Multi-language support. App Router handles i18n via folder structure + middleware — no plugin needed | `[locale]` route segment + middleware for locale detection, `next-intl` for translations | `app/[locale]/page.tsx`, middleware detects browser locale and redirects, `next-intl` for message dictionaries and pluralization | [next-intl docs](https://next-intl-docs.vercel.app/) |
| Custom Server *(avoid unless necessary)* | Replace Next.js's built-in server with Express/Fastify. **Disables most Next.js optimizations** — avoid unless you need very specific server behavior | Express, Fastify | Loses automatic static optimization, ISR, edge features. Use Route Handlers + Middleware instead — they cover 95% of custom server use cases | [Next.js – Custom Server](https://nextjs.org/docs/pages/building-your-application/configuring/custom-server) |
| Monorepo Setup | Share code (UI components, types, utils) across multiple Next.js apps | Turborepo *(recommended)*, Nx | `packages/ui` shared component library, workspace-aware builds, remote caching with Turborepo Cloud | [Turborepo docs](https://turbo.build/repo) |
| Environment Variables | Manage secrets and config per environment. Next.js has a specific loading order | `.env.local`, `.env.production`, `.env` | `NEXT_PUBLIC_` prefix exposes to browser — never put secrets here. Server-only vars stay private. `process.env` access in Server Components is safe | [Next.js – Env Vars](https://nextjs.org/docs/app/building-your-application/configuring/environment-variables) |