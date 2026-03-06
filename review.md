# Review specs

Goal: review implementations against the project's Constitution and scientific rigor.

### 1. Architecture & Reuse
- **Mixins:** Did the developer use `Cachable`, `Registrable`, or `CachableSettings` where applicable?
- **Utils:** No "reinventing the wheel" if a utility exists in `tanat-utils` or in public standards.
- **Store immutability:** Does any new code write to a physical store outside of a builder or a store mutation method? Reject if yes.
- **Virtual context:** Is `weakref.finalize` used instead of `__del__` for virtual context cleanup? Is `_gc_state` a `list` updated in-place?

### 2. API & Developer Experience (DX)
- **Signatures:** Are type hints strict and accurate? Check `-> Iterator[T]` on all `__iter__` / `keys()` / `values()` / `items()` generators.
- **Docstrings:** Google style. First line is a concise one-liner. Public methods with non-obvious usage patterns must have `Examples::` blocks. No em dashes anywhere.
- **Naming:** Does naming follow TanaT conventions? Check `id_column`, `start_column`, `end_column`, `time_column`, `entity_features`, `static_features`.
- **Import placement:** Reject any PR with imports inside methods or functions. Top of file, PEP 8 order (stdlib > third-party > local).
- **No parenthetical types in Args:** `param (list, optional):` style is banned. Use Python 3.10+ union types in the signature only.

### 3. Builder & Data Registration
- **`features` normalisation:** Every `add_*` method must auto-convert `str` to `[str]`. Verify the pattern `features = [features] if isinstance(features, str) else list(features)` is present.
- **`temporal_columns()` return type:** Must return `list[str]` (ordered), never a `frozenset` or unordered collection.
- **Temporal dtype mismatch warning:** New builder subclasses must set `_TEMPORAL_SCHEMA_MAP` and inherit the warning from `_warn_temporal_dtype_mismatch`. Do not duplicate the warning logic.

### 4. Style Constraints
- **Em dashes banned:** Zero occurrences of `—` in any `.py`, `.md`, or other file. Use ` - ` (space-hyphen-space) or rewrite the sentence.
- **Arrow shorthand:** `None -> all` is acceptable in docstrings (Unicode `→` is also fine). Do not replace these.

### 5. Testing & Validation
- **Functional focus:** Do tests mimic real usage?
- **Snapshots:** Is `syrupy` used for complex outputs?
- **Edge cases:** Check for empty sequences or single-entity trajectories.

## Response Format
For every review, provide:
1. **Approval Status:** [✅ Approved] | [⚠️ Changes Required] | [❌ Rejected].
2. **Critical Flaws:** List anything breaking the Constitution.
3. **Suggestions:** Improvements for performance or DX.
