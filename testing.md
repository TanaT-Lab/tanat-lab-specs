# TanaT — Test Strategy

## Philosophy
- **Fixture reuse**: pools are built once per session and shared — never rebuilt per test.
- **Parametrize over pool types**: sequence tests run against all three types via
  class-level `@pytest.mark.parametrize("pool_type", ["interval", "event", "state"])` combined
  with the `pools_dict` session fixture. Trajectory tests use the `traj_pool` parametrized fixture
  (covers both `datetime` and `timestep` variants automatically).
- **Snapshots with syrupy**: complex outputs (DataFrames, nested dicts) are asserted via syrupy
  snapshots rather than manual field checks. Snapshots are committed and updated with `--snapshot-update`.

---

## Snapshot Testing (syrupy)

Syrupy is used for any output where manual field assertions would be brittle or verbose:
DataFrames, column lists, nested dicts, metadata objects.

```python
def test_sequence_data_output(snapshot, interval_pool):
    assert interval_pool.sequence_data(output_format="polars") == snapshot
```

- Snapshots live in `__snapshots__/` next to each test file (auto-created by syrupy).
- Regenerate with `pytest --snapshot-update` after an intentional output change.
- **Scalar assertions** (`len`, `is_dirty`, raised exceptions) never use snapshots.
- **DataFrames and column lists** always use snapshots.

---

## Parametrize Convention

Sequence tests — class-level parametrize over `pool_type` combined with the `pools_dict` fixture:

```python
@pytest.mark.parametrize("pool_type", ["interval", "event", "state"])
class TestSomething:
    def test_foo(self, pools_dict: dict, pool_type: str, snapshot) -> None:
        pool = pools_dict[pool_type]
        ...
```

Trajectory tests — `traj_pool` fixture, already parametrized over both temporal variants:

```python
class TestTrajectoryPool:
    def test_foo(self, traj_pool: TrajectoryPool, snapshot) -> None:
        ...
```

Tests specific to one type or one temporal variant (e.g. `sort_anchor` on `IntervalSequencePool`,
or incompatibility checks between `datetime` and `timestep` pools) are **not** parametrized.

---

## Conventions

- **pytest** only; class grouping only when `parametrize` benefits from shared setup.
- One class per object level in a file: `TestSequencePool` and `TestSequence` coexist in `test_sequence.py`.
- Tests cover the *composed workflow*, not internals \u2014 no `_private` attribute access.
- Markers declared in `pyproject.toml` under `[tool.pytest.ini_options]`.
