# STUDY_PLAN.md — Python Backend Roadmap: Inoreader-like Service

## Goal

Build a simplified backend inspired by Inoreader while learning backend development from first principles.

The stack is intentionally introduced in this order:

1. **plain Python** — core programming and backend logic without a web framework;
2. **FastAPI** — HTTP API around already-understood application logic.

The project is a learning vehicle, not a production clone of Inoreader.

The roadmap may be adapted based on actual progress.

Do not mark a topic as mastered merely because it was explained once.

---

# Current learning goal

Language:

`Python`

Main goal:

`Backend development through building a simplified Inoreader-like RSS reader backend`

Current level:

`To be assessed`

Approximate study time:

`To be filled in`

Final target capabilities:

- write Python programs independently;
- structure a multi-module backend project;
- parse and normalize RSS/Atom data;
- persist subscriptions and articles;
- implement read/starred/filtering behavior;
- write tests;
- understand HTTP and REST fundamentals;
- expose the application through FastAPI;
- work with SQLite and basic SQL;
- understand the purpose of repositories/services/models;
- implement basic API authentication concepts;
- debug and extend the project without AI writing most of it.

---

# Phase 0 — Initial assessment and environment

## 0.1 Environment

Learn:

- Python installation and version;
- virtual environments;
- running `.py` files;
- basic terminal usage;
- installing packages with `pip`;
- basic project directory navigation.

Project result:

- repository runs locally;
- virtual environment is understood;
- a simple Python script can be executed.

Status:

`Not started`

## 0.2 Initial assessment

Check practical understanding of:

- variables;
- conditions;
- loops;
- functions;
- lists/dictionaries;
- reading tracebacks.

Use the result to skip or reinforce only what is justified.

Status:

`Not started`

---

# Phase 1 — Python fundamentals

## 1. Variables, values, and expressions

Learn:

- variables;
- assignment;
- `int`, `float`, `str`, `bool`, `None`;
- expressions;
- `print` and basic input;
- type conversion.

Project-oriented practice:

- represent a feed title, URL, unread count, and article state;
- calculate simple statistics.

Status:

`Not started`

## 2. Conditions

Learn:

- booleans;
- comparisons;
- `and`, `or`, `not`;
- `if`, `elif`, `else`.

Project-oriented practice:

- decide whether an article is unread;
- validate simple values;
- choose behavior depending on article state.

Status:

`Not started`

## 3. Loops

Learn:

- `for`;
- `while`;
- counters and accumulators;
- `break` and `continue` when appropriate.

Project-oriented practice:

- count unread articles;
- find articles matching a condition;
- process a list of feed items.

Status:

`Not started`

## 4. Functions

Learn:

- function definition;
- parameters and arguments;
- return values;
- local scope;
- decomposition;
- pure functions at a basic level.

Project-oriented practice:

- functions for filtering, counting, normalizing, and changing article state.

Milestone:

Create a small console program that manages a list of article-like dictionaries using functions.

Status:

`Not started`

---

# Phase 2 — Core Python for backend logic

## 5. Collections

Learn:

- lists;
- dictionaries;
- tuples;
- sets;
- iteration;
- membership;
- searching;
- filtering;
- basic comprehensions after loops are comfortable.

Project-oriented practice:

- subscriptions collection;
- articles by ID;
- unique tags/feeds;
- deduplication using sets.

Status:

`Not started`

## 6. Strings and text processing

Learn:

- indexing/slicing;
- searching;
- normalization;
- formatting;
- splitting/joining;
- parsing small text formats.

Project-oriented practice:

- normalize feed titles;
- clean article text;
- validate URLs at a simple level;
- search article titles.

Status:

`Not started`

## 7. Errors, exceptions, and debugging

Learn:

- syntax errors;
- runtime errors;
- logic errors;
- tracebacks;
- `try` / `except`;
- raising simple exceptions;
- debugging systematically.

Project-oriented practice:

- malformed article data;
- missing fields;
- invalid identifiers;
- failed file reads.

Status:

`Not started`

## 8. Files, JSON, and persistence basics

Learn:

- paths with `pathlib`;
- reading/writing text files;
- context managers;
- JSON serialization/deserialization;
- persistence failure cases.

Project milestone — **Feed Reader Core v1**:

Build a console application that can:

- add a subscription manually;
- store subscriptions in JSON;
- store sample articles;
- mark articles read/unread;
- star/unstar articles;
- list/filter articles;
- persist state between runs.

No FastAPI.

Status:

`Not started`

---

# Phase 3 — Project structure and Python design

## 9. Modules and packages

Learn:

- imports;
- modules;
- packages;
- `__name__ == "__main__"`;
- separating code by responsibility.

Refactor the project into modules such as:

- domain/models;
- application/service logic;
- persistence;
- CLI/interface.

Exact names may differ; understand the reason for separation first.

Status:

`Not started`

## 10. Data modeling

Learn:

- dictionaries vs structured objects;
- `dataclass`;
- object state;
- methods when they improve cohesion;
- identity and IDs.

Model concepts such as:

- `Feed`;
- `Article`;
- `Subscription`;
- optional `Folder`.

Avoid unnecessary inheritance.

Status:

`Not started`

## 11. Problem decomposition and application services

Learn:

- requirements -> use cases;
- inputs and outputs;
- separating domain rules from I/O;
- designing functions before implementation;
- basic service-layer thinking without framework jargon overload.

Implement use cases such as:

- subscribe to a feed;
- unsubscribe;
- list subscriptions;
- add/refresh articles;
- mark article read;
- star article;
- filter unread/starred items.

Status:

`Not started`

---

# Phase 4 — RSS/Atom domain

## 12. RSS and Atom concepts

Learn conceptually:

- what RSS/Atom feeds are;
- feed metadata;
- feed items/entries;
- GUID/ID/link concepts;
- published/updated timestamps;
- optional/missing fields.

First inspect small example feeds.

Then use a suitable parsing library rather than writing a complete XML parser.

Status:

`Not started`

## 13. Feed parsing and normalization

Learn:

- converting external feed data into internal models;
- defensive handling of missing fields;
- normalization;
- stable identifiers;
- date parsing at a practical level.

Project milestone — **Feed Reader Core v2**:

Given a real feed URL or feed document:

- parse feed metadata;
- convert entries to internal `Article` objects;
- store new articles;
- avoid duplicate entries.

Status:

`Not started`

## 14. Refresh and deduplication logic

Learn:

- idempotent operations conceptually;
- deduplication strategies;
- update-vs-insert decisions;
- handling repeated refreshes;
- basic failure isolation.

Implement a synchronous refresh flow in plain Python.

Do not introduce background queues yet.

Status:

`Not started`

---

# Phase 5 — Testing and reliability

## 15. Testing fundamentals

Learn:

- why tests exist;
- assertions;
- test cases;
- edge cases;
- Arrange/Act/Assert;
- `pytest` basics.

Write tests for existing functions and services.

Status:

`Not started`

## 16. Testing the feed domain

Test cases should include:

- duplicate article IDs;
- missing optional fields;
- empty feed;
- malformed data;
- read/starred state transitions;
- persistence round trips;
- refresh called multiple times.

Milestone:

Core domain behavior has automated tests before adding FastAPI.

Status:

`Not started`

## 17. Refactoring

Learn:

- duplication;
- naming;
- extracting functions;
- simplifying control flow;
- separating responsibilities;
- changing structure without changing behavior.

Refactor using tests as protection.

Status:

`Not started`

---

# Phase 6 — Databases before frameworks

## 18. Relational database fundamentals

Learn:

- table;
- row;
- column;
- primary key;
- foreign key;
- constraints;
- one-to-many relationships;
- basic normalization intuition.

Map project concepts to tables.

Status:

`Not started`

## 19. SQLite and SQL

Learn basic SQL:

- `CREATE TABLE`;
- `INSERT`;
- `SELECT`;
- `UPDATE`;
- `DELETE`;
- `WHERE`;
- `ORDER BY`;
- joins at a basic level.

Use Python's SQLite support before introducing an ORM.

Project milestone — **Feed Reader Core v3**:

Replace or supplement JSON persistence with SQLite.

Status:

`Not started`

## 20. Repository abstraction

Learn why persistence should not dominate business logic.

Create repository interfaces/protocols only when the need is understood.

Possible repositories:

- feed repository;
- article repository;
- subscription repository.

Keep abstractions small.

Status:

`Not started`

---

# Phase 7 — HTTP fundamentals

## 21. Client/server and HTTP

Learn:

- client and server;
- request/response;
- methods: GET, POST, PUT/PATCH, DELETE;
- URL/path/query parameters;
- request body;
- headers at a basic level;
- status codes;
- JSON over HTTP;
- stateless request concept.

Relate HTTP operations to existing use cases.

Status:

`Not started`

## 22. REST-style resource design

Design endpoints on paper before FastAPI.

Possible resources:

- `/feeds`;
- `/subscriptions`;
- `/articles`;
- `/articles/{id}`;
- `/folders` later if needed.

Discuss tradeoffs instead of pretending there is one perfect REST design.

Status:

`Not started`

---

# Phase 8 — FastAPI fundamentals

## 23. First FastAPI application

Learn:

- creating the app;
- development server;
- route decorators;
- request/response cycle;
- automatic docs.

First API should call existing plain-Python application logic.

Do not rewrite the domain around FastAPI.

Status:

`Not started`

## 24. Parameters and Pydantic models

Learn:

- path parameters;
- query parameters;
- request bodies;
- Pydantic models;
- validation;
- serialization.

Map API schemas to internal application inputs/outputs deliberately.

Status:

`Not started`

## 25. Status codes and errors

Learn:

- appropriate success codes;
- 400/404/409-style error cases;
- FastAPI exceptions;
- translating domain/application errors into HTTP responses.

Do not make domain logic depend on `HTTPException`.

Status:

`Not started`

## 26. Dependency injection

Learn FastAPI dependency injection only after ordinary function dependencies are understood.

Use it for things such as:

- repositories;
- database connection/session;
- current user later.

Status:

`Not started`

Project milestone — **Feed Reader API v1**:

Expose endpoints for:

- create/list/delete subscriptions;
- list articles;
- filter unread/starred;
- mark read/unread;
- star/unstar;
- trigger synchronous feed refresh.

Status:

`Not started`

---

# Phase 9 — API testing and database integration

## 27. FastAPI testing

Learn:

- API test client;
- endpoint tests;
- request validation tests;
- integration tests;
- test database isolation at a simple level.

Status:

`Not started`

## 28. ORM introduction

Only now introduce an ORM if useful.

Learn what the ORM abstracts compared with SQL already practiced.

Possible choice:

- SQLAlchemy / SQLModel depending on project direction.

Topics:

- mapped models;
- sessions;
- queries;
- relationships;
- transactions at a basic level.

Do not hide SQL understanding.

Status:

`Not started`

## 29. Migrations

Learn why schemas change over time.

Introduce migrations only after the database model changes enough to justify them.

Status:

`Not started`

---

# Phase 10 — Users and authentication

## 30. Multi-user model

Learn:

- ownership;
- user-specific subscriptions;
- user-specific article state;
- separating global feed/article data from per-user state where appropriate.

Discuss data-model alternatives.

Status:

`Not started`

## 31. Authentication basics

Learn conceptually:

- authentication vs authorization;
- password hashing;
- tokens;
- current-user dependency;
- protected endpoints.

Implement only after the concepts are understood.

Status:

`Not started`

Project milestone — **Feed Reader API v2**:

Multiple users can maintain independent subscriptions and article states.

Status:

`Not started`

---

# Phase 11 — Background work and production concepts

## 32. Background refresh concepts

First understand why feed refresh should eventually not block normal API traffic.

Learn conceptually:

- synchronous vs asynchronous work;
- background jobs;
- scheduler;
- retry;
- idempotency;
- failure handling.

Start with the simplest mechanism appropriate to the learning stage.

Do not jump directly to Celery/Redis.

Status:

`Not started`

## 33. Async Python and FastAPI

Introduce `async`/`await` only after synchronous Python and HTTP code are comfortable.

Learn:

- what async solves;
- I/O-bound work;
- coroutine basics;
- when `async` does not help.

Refactor only where justified.

Status:

`Not started`

## 34. Configuration and logging

Learn:

- environment-based configuration;
- secrets conceptually;
- structured logging basics;
- useful application logs;
- not logging secrets.

Status:

`Not started`

---

# Phase 12 — Search, filtering, and final project quality

## 35. Filtering and pagination

Add practical API behavior:

- pagination;
- date ordering;
- unread/starred filters;
- feed/folder filters;
- simple search.

Discuss database implications.

Status:

`Not started`

## 36. Project architecture review

Review the final codebase:

- domain models;
- application/service layer;
- repositories;
- persistence;
- FastAPI layer;
- tests;
- configuration.

Identify unnecessary abstractions as well as missing separation.

Status:

`Not started`

## 37. Final independent feature

Choose and implement one feature with minimal Codex help.

Possible examples:

- folders/tags;
- bulk mark-as-read;
- saved searches;
- per-feed refresh settings;
- OPML import/export;
- simple pagination cursor;
- article cleanup policy.

Before implementation:

1. define requirements;
2. design data changes;
3. design application flow;
4. design API changes if applicable;
5. write test plan;
6. implement independently.

Status:

`Not started`

---

# Git track — used throughout the project

Git should not be postponed until the end.

Learn progressively:

- `status`;
- `diff`;
- `add`;
- `commit`;
- `log`;
- `.gitignore`;
- branches;
- merge basics.

Use commits at meaningful milestones.

Status:

`Not started`

---

# Review checkpoints

After each major phase:

- give a short knowledge assessment;
- give practical exercises without naming every tested topic;
- identify weak areas;
- update `PROGRESS.md`;
- revisit prerequisites when needed;
- decide whether the next project milestone is appropriate.

Important checkpoints:

1. after Python fundamentals;
2. after JSON/file-based core;
3. after RSS parsing/refresh;
4. after testing;
5. after SQLite/SQL;
6. before FastAPI;
7. after first FastAPI API;
8. after authentication/multi-user work;
9. final project review.

---

# Graduation criteria

Do not consider the curriculum complete until I can independently:

- read and write normal Python backend code;
- decompose requirements into functions/modules;
- model feeds, articles, subscriptions, and user state;
- parse external feed data and handle missing fields;
- implement deduplication and refresh logic;
- persist data in SQLite;
- write and understand basic SQL;
- write unit and API tests;
- debug Python and FastAPI errors;
- explain HTTP methods and status codes;
- build and extend FastAPI endpoints without putting all logic in routes;
- understand what Pydantic, dependency injection, and an ORM are abstracting;
- use Git for normal work;
- research library documentation;
- design and implement a new project feature without AI generating most of the solution;
- explain important architecture decisions in my own code.

The final goal is not to memorize Python or FastAPI syntax.

The final goal is to be able to build and reason about a backend independently.
