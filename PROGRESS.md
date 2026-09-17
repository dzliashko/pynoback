# PROGRESS.md — Python Backend Learning Progress

## Student profile

Language:

`Python`

Primary goal:

`Learn backend development by building a simplified Inoreader-like RSS reader backend`

Target stack:

`Plain Python first -> SQLite/SQL -> HTTP fundamentals -> FastAPI`

Starting level:

`Assessment in progress: basic conditions, list iteration, accumulation, and function return demonstrated independently; dictionaries and traceback reading still to assess.`

Approximate study time:

`Not selected yet`

Study start:

`2026-09-17`

---

# Current status

## Current phase

`Phase 0 — Initial assessment and environment`

## Current topic

`Initial level assessment — dictionaries next, then traceback reading`

## Current exercise

Completed `count_nonempty_feeds(unread_counts)` in `src/pynoback/main.py`. Session paused at the student's request; no new exercise assigned.

## Current project milestone

`Not started — preparing for Feed Reader Core v1`

## Recommended next action

Resume with a small dictionary exercise, then assess traceback reading. Finish Phase 0 assessment before selecting the first appropriate study topic. Environment execution was verified (system Python 3.14.4, local `.venv` Python 3.14.7, uv available); the student's understanding of virtual environments and script execution is not yet assessed.

---

# Curriculum milestones

## Milestone 1 — Python fundamentals

Status:

`Not started`

Expected outcome:

Can use variables, conditions, loops, functions, collections, and basic debugging independently.

## Milestone 2 — Feed Reader Core v1

Status:

`Not started`

Expected outcome:

Plain-Python console application with JSON/file persistence, article state, filtering, and subscriptions represented locally.

## Milestone 3 — Feed Reader Core v2

Status:

`Not started`

Expected outcome:

RSS/Atom parsing, normalization, real feed entries, and deduplication.

## Milestone 4 — Tested Core

Status:

`Not started`

Expected outcome:

Core business behavior covered by meaningful automated tests.

## Milestone 5 — Feed Reader Core v3

Status:

`Not started`

Expected outcome:

SQLite persistence using understood SQL and a clean persistence boundary.

## Milestone 6 — HTTP-ready architecture

Status:

`Not started`

Expected outcome:

Core application logic can be called independently of CLI, files, or web framework.

## Milestone 7 — Feed Reader API v1

Status:

`Not started`

Expected outcome:

FastAPI exposes subscriptions, articles, state changes, filters, and synchronous refresh.

## Milestone 8 — Feed Reader API v2

Status:

`Not started`

Expected outcome:

Multi-user ownership and basic authentication/authorization concepts are implemented.

## Milestone 9 — Independent backend feature

Status:

`Not started`

Expected outcome:

A meaningful feature is designed, tested, and implemented mostly independently.

---

# Completed topics

None yet.

---

# Topics in progress

Phase 0 — initial Python assessment.

---

# Exercises

2026-09-17 — three assessment exercises completed independently without hints:

- Predicted assignment/condition program output correctly: `Немного`, `3`, `2`. No follow-up explanation required under the student's updated preference.
- Summed `[3, 0, 5, 2]` using a `for` loop and accumulator without `sum()`; execution returned `10`.
- Implemented `count_nonempty_feeds` with a loop, condition, and `return`; execution produced `3`, `0`, `0` for the three specified cases, including an empty list. Printing is outside the function.

The latest exercise replaces the earlier loop exercise in `src/pynoback/main.py`. These are assessment exercises, not implemented backend features.

For completed exercises, use this format:

## Exercise XXX — Exercise name

**Phase:**  
Phase number/name

**Topic:**  
Topic name

**Project relevance:**  
What backend capability this exercise supports.

**Result:**  
Completed / Completed with help / Needs revision

**What I understood:**  
Short note.

**Problems encountered:**  
Short note.

**Hints required:**  
None / Small / Significant / Full solution

**Important mistake:**  
Short note if relevant.

**Needs repetition:**  
Yes / No

---

# Project features

Track actual backend capabilities separately from theory.

For each feature use:

## Feature — Name

**Milestone:**  
Milestone name

**Status:**  
Not started / In progress / Working / Needs revision

**Implemented independently:**  
Yes / Mostly / With significant help / No

**Concepts practiced:**

- item;

**Tests:**  
None / Manual / Automated

**Known limitations:**  
Short note.

**Next improvement:**  
Short note.

---

# Projects

## Main project — Inoreader-like backend

**Goal:**  
Build a simplified RSS reader backend while learning Python backend development from fundamentals to FastAPI.

**Start date:**  
Not started.

**Current version:**  
Not started.

**Current interface:**  
None / CLI / FastAPI

**Current persistence:**  
None / Memory / JSON / SQLite / ORM-backed database

**Current test level:**  
None / Basic unit / Core unit / Integration / API

**Major difficulties:**  
None recorded yet.

**Important lessons:**  
None recorded yet.

---

# Concepts understood well

Demonstrated in small assessment exercises: conditions, iteration over lists, accumulators, counting matching elements, basic function parameters and return values, and separating printing from a function's result.

Only add a concept here after I have successfully used it more than once or demonstrated it in an assessment.

---

# Concepts needing practice

Meaningful loop variable names: both written exercises use `i` for an unread count. Suggested practice: choose names describing the value. This does not block further assessment. Dictionaries and traceback reading remain unassessed, not confirmed weaknesses.

For each concept, include:

- concept;
- evidence of difficulty;
- suggested practice;
- prerequisite impact.

---

# Recurring mistakes

None recorded yet.

Only add a recurring mistake after a pattern appears more than once.

Possible examples:

- forgetting to return values;
- mixing data access with business logic;
- mutating shared data unintentionally;
- weak input validation;
- difficulty decomposing a feature;
- putting all logic in one function;
- putting business rules directly in FastAPI routes;
- misunderstanding IDs or deduplication;
- writing tests that only cover happy paths.

---

# Debugging skills

## Current level

`Not assessed`

Track progress in:

- reading Python error messages;
- reading tracebacks;
- locating source of errors;
- inspecting variable values;
- testing hypotheses;
- distinguishing syntax/runtime/logic errors;
- debugging file/JSON state;
- debugging SQLite/SQL issues;
- debugging HTTP request/response issues;
- debugging FastAPI validation errors.

---

# Problem-solving skills

## Current level

`Not assessed`

Track:

- understanding requirements;
- identifying inputs and outputs;
- breaking a feature into steps;
- choosing data structures;
- writing pseudocode;
- separating business logic from I/O;
- identifying edge cases;
- designing tests before implementation when appropriate;
- solving without AI assistance.

---

# Backend design skills

## Current level

`Not assessed`

Track understanding of:

- domain models;
- application/service functions;
- repositories;
- persistence boundaries;
- HTTP/API layer;
- validation boundaries;
- database relationships;
- dependency direction;
- avoiding premature abstraction.

---

# Python skills

Track confidence in:

- variables and types;
- conditions;
- loops;
- functions;
- lists/dicts/sets/tuples;
- strings;
- exceptions;
- files;
- JSON;
- modules/packages;
- dataclasses/classes;
- typing basics;
- testing;
- SQLite integration;
- async basics later.

Current summary:

`Not assessed`

---

# RSS/feed domain skills

Track understanding of:

- RSS/Atom structure;
- feed metadata;
- entries/items;
- GUID/ID/link;
- timestamps;
- normalization;
- missing fields;
- deduplication;
- refresh behavior.

Current summary:

`Not started`

---

# HTTP/FastAPI skills

Track understanding of:

- client/server;
- requests/responses;
- HTTP methods;
- status codes;
- path/query/body data;
- JSON API design;
- FastAPI routing;
- Pydantic validation;
- dependencies;
- exception mapping;
- API testing;
- authentication basics.

Current summary:

`Not started`

---

# Database skills

Track understanding of:

- relational model;
- tables/rows/columns;
- primary/foreign keys;
- basic SQL;
- joins;
- SQLite;
- transactions at a basic level;
- repository abstraction;
- ORM concepts later;
- migrations later.

Current summary:

`Not started`

---

# Testing skills

## Current level

`Not assessed`

Track:

- choosing useful test cases;
- assertions;
- edge cases;
- `pytest`;
- unit tests;
- persistence tests;
- integration tests;
- FastAPI endpoint tests;
- test isolation.

---

# Independence

Track how much assistance I require.

### Level 1 — Heavy assistance

Needs detailed instructions and substantial hints.

### Level 2 — Guided

Can solve problems with several hints.

### Level 3 — Mostly independent

Usually solves problems alone but occasionally needs conceptual hints.

### Level 4 — Independent

Can design, implement, debug, and test normal tasks independently.

### Level 5 — Strong independence

Can approach unfamiliar backend problems, research documentation, design solutions, evaluate tradeoffs, and implement features independently.

Current independence level:

`Not assessed`

---

# Topics to repeat

None yet.

For each topic record:

- topic;
- why it needs repetition;
- when it was last practiced;
- suggested future exercise;
- whether it blocks the next project phase.

---

# Assessments

Phase 0 assessment started on 2026-09-17 and remains incomplete. Three small exercises passed independently; dictionaries, traceback reading, and practical environment understanding remain to assess. No final starting-level classification yet.

Use assessments at phase checkpoints rather than after every lesson.

Record:

- topics tested;
- project capabilities tested;
- strengths;
- weaknesses;
- exercises solved independently;
- exercises requiring hints;
- architecture misunderstandings;
- recommended next steps.

---

# Learning observations

Ask understanding follow-ups only after incorrect answers. After each completed exercise, ask whether to continue and wait before assigning the next task. The student requested a pause until tomorrow after the function exercise.

Keep this section concise.

Record only observations useful for future teaching.

---

# Architecture observations

None yet.

Use this section only when the project is large enough for architecture decisions to matter.

Record things such as:

- responsibilities that are mixed together;
- abstractions introduced too early;
- useful separation that should be preserved;
- recurring dependency problems.

---

# Next milestone

Complete the initial Python assessment and begin the first appropriate topic in `STUDY_PLAN.md`.
