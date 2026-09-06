# JavaScript Basics Roadmap → Node.js

Goal: Build solid JavaScript fundamentals as a stepping stone to learning **Node.js**.

Since Node.js is the target, this roadmap weights async, modules, and core language features heavier, and treats browser DOM work as optional (useful but not essential for Node).

---

## Phase 1 — Foundations (Week 1–2)
- Variables: `let`, `const`, `var` (and why `const` is the default)
- Data types: string, number, boolean, `null` vs `undefined`, object, array
- Operators: arithmetic, comparison, logical (`&&`, `||`, `??`)
- Conditionals: `if/else`, `switch`, ternary `? :`
- Loops: `for`, `while`, `for...of`, `for...in`

**Mini-project:** Counter / number-guessing game in the console.

---

## Phase 2 — Functions (Week 3)
- Function declarations vs expressions
- Arrow functions `=>`
- Parameters, default values, `return`
- Scope (global, function, block)
- **Closures** — learn this well; it unlocks everything later

**Mini-project:** A small library of utility functions (math, string helpers).

---

## Phase 3 — Data Structures (Week 4)
- Array methods: `map`, `filter`, `reduce`, `forEach`, `find`, `some`, `every`
- Objects (keys, methods, nested)
- Destructuring (arrays & objects)
- Spread / rest `...`

**Mini-project:** A command-line todo list stored in an array.

---

## Phase 4 — The DOM (Week 5) [optional for Node]
- `querySelector`, `getElementById`
- Modify text, HTML, attributes, styles
- Event listeners (`click`, `input`, `submit`)
- Form handling

> Skip this if you want to jump to Node.js sooner. Come back if you ever do frontend work.

**Mini-project:** Browser-based todo list or calculator.

---

## Phase 5 — Async JavaScript (Week 6–7) [CRITICAL for Node]
- Callbacks → why they cause "callback hell"
- Promises (`.then`, `.catch`, `Promise.all`)
- `async` / `await`
- `fetch` API (browser) — and note Node has its own ways to fetch

> Node.js is heavily async (file I/O, network, DB). Master this phase before touching Node.

**Mini-project:** Fetch data from a public API (e.g. jsonplaceholder, openweather) and display it.

---

## Phase 6 — Modern JS & Patterns (Week 8) [CRITICAL for Node]
- **ES Modules** (`import`/`export`) AND **CommonJS** (`require`/`module.exports`) — Node uses both, know the difference
- Template literals, optional chaining `?.`
- Classes (basic)
- Error handling (`try/catch`)
- `this` binding rules (important in Node callbacks and class methods)

**Mini-project:** Split your utility library into multiple files using ES modules.

---

## After This → Node.js
You're ready when you can:
- Read async code with `async/await` without confusion
- Use `map`/`filter`/`reduce` comfortably
- Understand what a module is and how to import/export
- Explain closures and `this` at a basic level

Start Node.js with:
1. `fs` module (read/write files)
2. `http` module (build a raw server)
3. `npm` and packages
4. `express` framework
5. Build a REST API

---

# Tips to Learn Faster

1. **Build, don't watch.** Tutorial hell is real. After every concept, build something tiny.
2. **Code every day**, even 20 min. Consistency beats marathons.
3. **Type code by hand** — never copy-paste. Muscle memory matters.
4. **Use the browser console** (F12) for instant feedback. No setup needed.
5. **Solve problems on Codewars / Edabit / LeetCode (easy)** — reinforces syntax through repetition.
6. **Read other people's code** on GitHub, even if you don't get it all.

# Tips to Learn Properly

1. **Understand *why*, don't memorize.** Know why `===` differs from `==`. Reasoning sticks; memorizing doesn't.
2. **MDN is your bible** — `developer.mozilla.org`. Bookmark it, read it when unsure.
3. **Learn debugging early**: `console.log`, `debugger` statement, DevTools Sources tab.
4. **Don't skip fundamentals** for frameworks. Everything builds on core JS.
5. **Expect confusion** — closures, `this`, and promises are hard for everyone. Revisit after a week; they click.
6. **Explain it out loud** (rubber-duck style). If you can't explain it, you don't understand it yet.

---

# Mini-Project Progression (in order)
1. Counter button
2. To-do list (array only)
3. Calculator
4. Weather app (fetch API) — async practice
5. Notes app with `localStorage` (browser) OR file-based (Node later)

---

# Resources
- **MDN Web Docs** — https://developer.mozilla.org
- **javascript.info** — https://javascript.info (free, comprehensive)
- **Eloquent JavaScript** (free book) — https://eloquentjavascript.net
- **Node.js official docs** (when you reach Node) — https://nodejs.org/docs

---

Last updated: 2026-08-06
