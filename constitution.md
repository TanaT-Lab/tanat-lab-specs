# TanaT Constitution

## Core Philosophy
- **Domain:** Temporal Analysis of Trajectories with  a primary focus on patient care pathways.
- **Rigor:** Strict Python typing (`typing` module) and Docstrings (Google format).
- **Docstrings:** Must be clear and concise in english (same for comments).
- **Extensibility:** Use existing architectural patterns to ensure modularity.
- **Imports:** MUST always be at the top of the file. Never inside methods or functions (no lazy imports unless explicitly justified). Follow PEP 8 (Standard lib > Third-party > Local).

## Data Model Concepts (Mandatory)
Agents must respect these three levels of abstraction:
1. **Entity:** Atomic unit (Timestamp or Interval + Features).
2. **Sequence:** Collection of entities for ONE individual (must share the same Type and Features).
3. **Trajectory:** Combines multiple sequences of different types + Static features for ONE individual.
4. **Pool:** Collection of sequences/trajectories from MULTIPLE individuals (primary structure for analysis/clustering).

## Sequence Type Constraints
- **Event:** Single timestamp. No constraints.
- **Interval:** Start/End dates. Can overlap, gaps allowed.
- **State:** Start/End dates. Must be **contiguous** (no gaps, no overlaps).

## TanaT Utils & Mixins (Mandatory Reuse)
When designing new components, check `tanat-utils` and prioritize these Mixins:
- **`Cachable`**: For heavy computations that should be persisted.
- **`CachableSettings`**: To synchronize/invalidate cache based on settings.
- **`Registrable`**: To manage class registries from a base class.

## Execution Workflow: "Signatures First"
1. **Planning:** Create `tasks.md` in the feature directory.
2. **Skeleton (Hold Point):** Create ONLY signatures, types, and docstrings (`pass`).
3. **Validation:** Agent MUST stop and ask: "Does the interface meet your requirements?"
4. **Implementation:** Write logic only after interface approval.

## Store Architecture (Mandatory)

The store layer is the **sole I/O interface** between the domain (Pool, Sequence, Trajectory) and the filesystem. Pools never read Arrow files directly - they always go through a store.

### Physical layout
Each store is a directory on disk with a fixed structure:
```
<store_root>/
  core.json                  ← immutable facts (type, build metadata)
  sequence_index.arrow       ← navigation index (id, offset, length)
  temporal_index.arrow       ← temporal rows (_t_start / _t_end / _t_event)
  entity_features.arrow      ← entity-level feature columns
  static_features.arrow      ← sequence-level static feature columns (optional)
  tmp/
    <virtual_id>/            ← ephemeral context (one per Pool view)
      entity_features.arrow  ← virtual entity columns (added via add_features)
      static_features.arrow  ← virtual static columns (optional)
      temporal_index.arrow   ← virtual temporal override (type conversions only)
```

### Class responsibilities
- **`SequenceStore` / `TrajectoryStore`**: physical read/write for their store type. Inherit `StaticStoreMixin` for shared static-feature I/O.
- **`StaticStoreMixin`**: shared static-feature access (`static()`, `add_static()`, `probe_static_cast()`). Inherited by both store types.
- **`VirtualStore`**: manages `tmp/<virtual_id>/` contexts (create, clear, read, write virtual features and temporal overrides). One `VirtualStore` instance is composed inside each store.

### Virtual context rules
- A **virtual context** is scoped to one Pool instance via `_virtual_id` (a `uuid` string).
- Virtual features are **merged on read** with physical data (hconcat columns).
- A virtual `temporal_index.arrow` **replaces** the physical temporal on read (used for type conversions).
- Cleanup is automatic: `Pool.__del__` / `_cleanup_virtual` calls `store.clear_virtual_context(virtual_id)`.
- Stores are **immutable** outside of their builder and explicit mutation methods. Pools must never write to the physical layer directly.

## Style Constraints (Mandatory)
- **No em dashes:** Never use em dashes (`—`) anywhere in the codebase (docstrings, comments, strings, spec files). Rewrite the sentence.
- **Docstring format:** Google style. First sentence is a concise one-liner. Add `Examples::` blocks on public methods when the usage pattern is not obvious.
- **No inline type hints in Args:** Never write `param (list, optional): …`. Use the Python 3.10+ union style in the signature and leave Args as plain descriptions.
- **Arrow shorthand:** `None -> all` is acceptable shorthand in docstrings.
- **Iterator return types:** All `__iter__`, `keys()`, `values()`, `items()` generators must carry a full return type annotation (`-> Iterator[T]`).

## Builder & Source Registration Conventions (Mandatory)
- **`features` normalisation:** Every `add_*` method on every builder must auto-convert a bare `str` to `[str]` before any other processing. Never rely on the caller to pass a list.
- **`temporal_columns()` ordering:** `StoreSchema.temporal_columns()` returns an **ordered `list[str]`** (not a set/frozenset). The canonical order is `[T_START, T_END, T_EVENT]` with absent columns omitted.
- **Temporal dtype mismatch warning:** When a builder receives a second entity source with temporal columns whose dtype differs from the first registered source, it must emit a `LOGGER.warning` at registration time (not at build time). The warning pattern is implemented in `SequenceStoreBuilder._warn_temporal_dtype_mismatch`.
- **`_prepare_entity` hook:** Builders sort by `SEQ_ID` then temporal column(s), then optionally enrich or validate (e.g. deriving `T_END` for state sequences or running `_check_continuity`).

## GC & Lifecycle Pattern (Mandatory)
- **Virtual context cleanup:** Use `weakref.finalize(self, ClassName._finalize_cleanup, self._gc_state)` instead of `__del__`. The finalizer must be registered at the **very end** of `__init__` to avoid running on a half-constructed object.
- **`_gc_state`:** A `list` of `[store, virtual_id]` passed to the finalizer by reference, so updates to `_virtual_id` are reflected automatically.

## Testing Strategy (Functional Focus)
- **Framework:** Use `pytest` and `syrupy` for snapshot testing.
- **Logic:** Functional/E2E tests only (mimic real-world usage).