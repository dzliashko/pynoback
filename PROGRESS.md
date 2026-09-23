# PROGRESS.md — Python Backend Learning Progress

## Student profile

Language:

`Python`

Primary goal:

`Learn backend development by building a simplified Inoreader-like RSS reader backend`

Target stack:

`Plain Python first -> SQLite/SQL -> HTTP fundamentals -> FastAPI`

Starting level:

`Beginner with working Python basics: independently solved small exercises on assignment, conditions, loops, functions, lists, dictionary access, and reading a simple traceback. Broader mastery is not yet established.`

Approximate study time:

`Not selected yet`

Study start:

`2026-09-17`

---

# Current status

## Current phase

`Phase 1 — Python fundamentals`

## Current topic

`Topic 4 — functions: decomposition and reuse demonstrated`

## Current exercise

Completed `describe_starred(articles)` in `src/pynoback/starred_titles.py`: calls the existing filter, counts its result with `len`, and returns a summary string. All three requested calls and the five earlier calls are present. Four new-function checks passed, with unchanged inputs and no function output. Awaiting the student's decision to continue.

## Current project milestone

`Not started — preparing for Feed Reader Core v1`

## Recommended next action

After the student agrees to continue, introduce updating a dictionary through a function, explicitly explaining mutation and how it differs from the pure functions practiced so far. Use a small article read-state exercise as preparation for the Phase 1 console milestone. Keep IDs, menu design, and persistence for later steps.

---

# Curriculum milestones

## Milestone 1 — Python fundamentals

Status:

`In progress`

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

Phase 1 topic 3 — `for`, `while`, counters, `break`, and `continue` practiced. The first `while` and `break` exercises required feedback; subsequent `while` and `continue` exercises were solved independently. Continue spaced repetition.

Phase 1 topic 2 — conditions: comparisons, boolean operators, grouping, and ordered `if`/`elif`/`else` branches demonstrated across multiple exercises. Continue spaced repetition in later tasks.

Phase 0.2 — initial assessment completed on 2026-09-22. This does not mark all later fundamentals topics as mastered.

Phase 0.1 — practical onboarding sufficient for lessons: script execution, installed-package inspection, and dependency synchronization completed. Used the existing uv workflow in place of standalone pip. No new package installation or independent environment creation demonstrated; revisit when needed.

---

# Topics in progress

Phase 1 topic 4 — reusable search, local result initialization, independent repeated calls, and decomposition practiced. Pure functions explained and used; introduce deliberate state changes before the console milestone.

---

# Exercises

2026-09-17 — three assessment exercises completed independently without hints:

- Predicted assignment/condition program output correctly: `Немного`, `3`, `2`. No follow-up explanation required under the student's updated preference.
- Summed `[3, 0, 5, 2]` using a `for` loop and accumulator without `sum()`; execution returned `10`.
- Implemented `count_nonempty_feeds` with a loop, condition, and `return`; execution produced `3`, `0`, `0` for the three specified cases, including an empty list. Printing is outside the function.

The latest exercise replaces the earlier loop exercise in `src/pynoback/main.py`. These are assessment exercises, not implemented backend features.

2026-09-22 — two additional assessment exercises completed independently without hints:

- Implemented `get_unread_titles(articles)` using dictionary keys, a loop, and `append`, returning titles in input order. Four execution checks passed: mixed, empty, all read, and all unread inputs. Used the meaningful loop variable `article`. Optional style feedback: prefer `not` to comparison with `False`.
- Read a supplied traceback correctly: identified `KeyError`, located the failure on line 2 inside `get_article_title`, and proposed adding `"title": "Космос"` to the input dictionary.

Environment exercise completed without hints: the student supplied `python --version` (Python 3.14.7, activated environment) and `uv run src/pynoback/main.py`, with expected output `3`, `0`, `0`, and the two unread titles. Evidence is the terminal output supplied by the student. No execution errors reported.

Guided package inspection completed: after receiving the exact `uv pip show --python .venv/bin/python pytest` command, the student supplied `Version: 9.1.1` and `Location: /home/dl/w/pynoback/.venv/lib/python3.14/site-packages`. Correctly extracted the requested fields. This verifies completion of the guided inspection, not independent command selection or package installation.

Guided dependency synchronization completed: the student supplied successful output from `uv sync --locked` (`Resolved 16 packages`, `Checked 15 packages`) and `.venv/bin/python -m pytest --version` (`pytest 9.1.1`). Existing dependencies required no installation. Demonstrates following the synchronization workflow and launching a package through the selected interpreter; no independent package installation was tested.

Article counts exercise completed independently after the lesson: `src/pynoback/article_counts.py` correctly converts both input strings to integers and sums them. Both requested execution cases passed (12 + 3 = 15; 0 + 0 = 0). Meaningful names and f-string formatting used. Optional usability feedback: `input()` has no prompt, so labels appear only after both values are entered. No code changed by the tutor; no hints required for the arithmetic or conversions.

Refresh duration exercise completed independently after the lesson: `src/pynoback/refresh_time.py` correctly uses `float`, adds durations, and divides the total by two. Execution checks passed: 1.5 and 2.5 produce total 4.0 and average 2.0; 0 and 3 produce total 3.0 and average 1.5. Clear input prompts address earlier usability feedback. Optional naming feedback: use `feed` rather than `thread` for an RSS feed. No tutor code changes or solution hints.

Missing-value exercise completed independently after the lesson: `describe_unread(feed)` in `src/pynoback/feed_status.py` uses `is None`, checks zero separately, and returns a formatted string for positive counts. Five checks passed for `None`, 0, 5, 1, and 27. Early returns correctly separate branches; printing is outside the function. No issues, hints, or tutor code changes.

Refresh rule exercise completed independently after the lesson: `should_refresh(feed)` in `src/pynoback/refresh_rules.py` directly returns `is_enabled and minutes_since_refresh >= 30`. All four requested examples plus disabled-at-30, enabled-at-0, and disabled-at-0 passed, with actual boolean return values verified. The student used a list of cases and a loop to print results outside the function. No issues, hints, or tutor code changes.

Article retention exercise completed independently after the lesson: `should_keep(article)` in `src/pynoback/article_selection.py` correctly returns `is_starred or is_saved`. All four combinations passed, including both flags true; actual boolean return values verified. The student's example list covers every combination and prints results outside the function. No issues, hints, or tutor code changes.

Article visibility exercise completed independently after the lesson: `should_show(article)` in `src/pynoback/article_visibility.py` directly returns `is_starred and not is_read`. All four combinations passed with actual boolean results. The student's list covers all combinations, and printing stays outside the function. No issues, hints, or tutor code changes. Simple boolean exercises have been solved consistently; next exercise should require composing a slightly broader rule.

Reading queue exercise completed: `should_add_to_queue(article)` in `src/pynoback/reading_queue.py` correctly excludes read articles and requires either a star or a saved flag for unread articles. All eight combinations passed with actual boolean return values. The student independently wrote the rule and grouped the `or` expression correctly. Assistance was limited to supplying all eight input dictionaries at the student's explicit request; no solution hints or tutor code edits. Printing remains outside the function.

Unread level exercise completed independently: `describe_unread_level(count)` in `src/pynoback/unread_level.py` uses an ordered `if`/`elif`/`else` chain with thresholds 0, 10, and 50. All six requested boundary cases passed (0, 1, 10, 11, 50, 51). Upper-bound-only checks correctly rely on earlier branches. The student supplied every requested example in a tuple and prints results outside the function. No issues, hints, or tutor code changes; tuple mastery is not inferred from this usage alone.

Reading session exercise completed with a hint: the first version printed the correct output but decremented before the loop and ended at -1. Feedback pointed to the counter's meaning and suggested tracing input 1; no corrected code was supplied. The student moved the decrement inside a `while counter > 0` loop and now ends at zero, skipping the loop for input zero. Exact output and termination verified for 3, 1, and 0. Needs spaced repetition with a different state-update exercise; this is one corrected mistake, not a recurring pattern. No tutor code edits.

Refresh progress exercise completed independently: `src/pynoback/refresh_progress.py` keeps the requested total unchanged, starts a separate counter at zero, updates it inside `while counter < feeds`, and prints progress after incrementing. Exact output and termination checks passed for 3, 1, and 0. This successfully reinforces the state-update issue from the prior exercise. Optional naming feedback: `total_feeds` and `refreshed_count` would express the two quantities more clearly than `feeds` and `counter`. No hints or tutor code changes.

2026-09-23 — first unread search completed with a hint: initial `find_unread.py` correctly used `break` and `for ... else`, but printed the found title inside the loop contrary to the exercise requirement. Tutor suggested storing a result without supplying code. The student initialized a default message, assigned the found title, retained `break`, moved printing after the loop, and used `not` instead of `== False`. Checks passed for the supplied mixed list, an empty list, all-read input, and an unread first article. Test inputs were substituted in memory; the student's file was not modified. No correctness issues remain. Revisit separation of processing and output; this is not a recurring error pattern.

2026-09-23 — unread report completed independently: `src/pynoback/unread_report.py` skips read articles with `continue`, appends unread titles in order, increments a counter, and prints both results after the loop. Four checks passed: supplied mixed list, empty list, all read, and all unread. Optional style feedback: use a direct boolean check instead of `== True`, name the title list `unread_titles`, and consider `len` instead of a separate counter. The counter is correct and was not prohibited. No solution hints or tutor code edits.

2026-09-23 — reusable first-unread search completed with feedback: `src/pynoback/article_search.py` initially selected read articles; a hint directed attention to the meaning of `is_read`, and the student corrected the condition. Required example calls were added over subsequent reviews after reminders about missing cases. Final script covers mixed input, all-read input, a single unread article, and an empty list, printing `Космос`, `None`, `Python`, `None`. Earlier execution checks verified independent calls, no input mutation, and no printing inside the function; the function remained unchanged afterward. Uses its parameter rather than external data and returns `None` after the loop. Optional style feedback: prefer `not` to `!= True` and descriptive example names. No tutor code edits. Needs practice checking the full exercise requirements before review; do not infer broad scope mastery from this exercise alone.

2026-09-23 — starred titles exercise completed independently after the lesson: `get_starred_titles(articles)` in `src/pynoback/starred_titles.py` initializes its list inside the function, directly checks the boolean flag, collects titles in order, and returns after the loop. All five requested example calls are present in the requested order, including a repeated mixed-list call. Execution checks verified expected values, distinct result lists for each call, unchanged input data, and no function output. Earlier omissions of required examples did not recur. Optional naming feedback: `starred_titles` describes the local list more precisely than `starred_articles`. No hints or tutor code edits.

2026-09-23 — starred summary exercise completed independently: `describe_starred(articles)` calls `get_starred_titles`, uses `len`, and returns the required empty/nonempty summary without duplicating filtering. All three requested new calls and five previous calls are retained. Four new-function cases passed (mixed, empty, single starred, all unstarred), with unchanged inputs and no function printing. The student also improved the filter's local result name to `starred_titles`. No issues, hints, or tutor code edits.

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

Demonstrated in small assessment exercises: conditions, iteration over lists, accumulators, counting matching elements, basic function parameters and return values, separating printing from a function's result, dictionary key access, building a filtered list, and locating a missing-key failure from a traceback.

Only add a concept here after I have successfully used it more than once or demonstrated it in an assessment.

---

# Concepts needing practice

Meaningful loop variable names: the first two written exercises used `i` for an unread count; the latest exercise improved this with `article`. Continue reinforcing descriptive names. Optional boolean style practice: use `not` instead of `== False`. No correctness weaknesses found in the assessment; untested topics are not confirmed weaknesses.

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

`Can read a simple KeyError traceback, locate the failing line, and identify a missing dictionary key. Other debugging skills remain unassessed.`

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

Phase 0.2 assessment completed on 2026-09-22: five small exercises passed independently without hints, covering all six requested areas (variables, conditions, loops, functions, lists/dictionaries, traceback reading). Starting level: beginner with working basics. Strengths: correct iteration, filtering, return placement, and interpreting a simple traceback. Improvements: naming and boolean style. Phase 0.1 practical environment skills remain to assess; larger problem decomposition and backend design were not tested.

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

Ask understanding follow-ups only after incorrect answers. After each completed exercise, ask whether to continue and wait before assigning the next task. Study resumed on 2026-09-22 after the earlier pause.

The student authorizes recording progress, committing relevant changes, and pushing after every completed exercise without repeated permission requests.

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

Continue Phase 1 topic 4 with deliberate dictionary state changes through functions, after the student agrees to continue.
