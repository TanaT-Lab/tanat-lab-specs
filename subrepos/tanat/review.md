# General Code Review Specification

**Goal:** Verify that the code strictly meets the requirements and the project's Constitution. If it doesn't, reject it. Reviews must ensure scientific rigor, absolute code simplicity, and high maintainability.

## 1. Core Philosophy

- **Strict Adherence:** Does it do exactly what the specifications ask? If NO, return to sender.
- **Simplicity over Cleverness:** Code must be simple, readable, and easy to maintain. Reject any "clever" or overly complex code.
- **No Noise:** Delete any useless internal comments, redundant documentation, or dead code.
- **Do Not Reinvent the Wheel:** Always use standard Python libraries or existing project utilities (e.g., `tanat-utils`).

## 2. General Review Criteria

### Architecture & Code Quality
- **Consistency & Patterns:** Maintain strict homogeneity across the library (matching argument names, method signatures, return structures, etc.).
- **Reuse:** Leverage existing architectural patterns and mixins (e.g., `Cachable`, `Registrable`, and utilities from `tanat-utils`).

### Documentation & Developer Experience (DX)
- **User Doc vs. Dev Doc:** Clear separation is required. 
  - *User Doc:* Explain how to use it (always include `Examples::` blocks for non-obvious public methods).
  - *Dev Doc:* Explain how it works internally.
- **Standardization:** Use Google style docstrings. The first line must be a concise one-liner.
- **Type Hints:** Must be strict, accurate, and use modern Python syntax in the signature. Do not use parenthetical types in docstrings.

### Testing & Validation
- **Functional Focus:** Tests must mimic real-world usage and validate exact specification requirements.
- **Edge Cases:** Always check for edge cases (e.g., empty sequences, missing data).
- **Snapshots:** Use tools like `syrupy` for validating complex data outputs.

## 3. TanaT-Specific Strict Constraints
*Any violation of these rules warrants an immediate request for changes.*
- **Formatting:** Em dashes (`—`) are strictly banned everywhere. Use `:`,`-`, `;`, ....
- **Imports:** Must be at the top of the file, following PEP 8 order. No imports inside methods or functions.
- **Naming:** Follow project conventions strictly (e.g., `id_column`, `start_column`, `entity_features`).
- **Builders:** 
  - `features` inputs must gracefully handle single strings by auto-converting them to lists.
  - Generative or temporal methods (e.g., `temporal_columns()`) must return ordered collections (`list[str]`), not sets.

## 4. Required Review Output Format

Every code review response must strictly follow this format:

- **Status:** [✅ PASS / Approved] | [⚠️ Changes Required] | [❌ FAIL / Rejected]
- **Missing Specs / Adherence:** List anything that deviates from or misses the original specifications.
- **Code Cleanliness:** Provide suggestions to simplify the code, remove "clever" code, or improve readability.
- **Doc & Test Check:** Note any missing user/dev docs, bloated/noisy comments, and missing test edge cases.
