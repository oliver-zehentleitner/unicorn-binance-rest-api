# History

## LUCIT-Systems-and-Development origin

> Superseded — repo now lives under `oliver-zehentleitner`, MIT-licensed.

**Id:** 63a0a620-aa0a-4d61-a9e0-f18ba4b6d101
**Type:** decision
**Status:** superseded
**Evidence:** confirmed
**Source:** git history
**Superseded by:** https://github.com/oliver-zehentleitner/unicorn-binance-suite — 2749fc08-cdca-456b-a8bd-fd4b646ff64c — as of 2026-09-28

The repo moved into the `LUCIT-Systems-and-Development` GitHub org (commit `e8115d3`, 2022-01-02) and was de-branded back out in a batch of commits on 2025-06-22 ("Removing LUCIT"). Residual cleanup continued much later, in April 2026: conda-forge migration and `build_conda.yml` removal (`31004a2`, 2026-04-18), and a hardcoded old-org URL fix in the update-check code (`3e32159`, 2026-04-13 — `get_latest_release_info()` was still querying `LUCIT-Systems-and-Development`'s GitHub API after the org move).

**Reason:** LUCIT is no longer part of how this project is licensed, distributed, or supported.

**Revisit when:** auditing other suite repos for the same class of bug — a hardcoded org/repo URL in an update-check or "latest release" helper doesn't fail loudly when the org moves, it just silently queries the wrong (possibly stale or gone) place.

## The 5-file dependency sync rule caught its own violation

**Id:** b6bccd53-6f7a-46ed-852e-2095378610f6
**Type:** incident
**Status:** active
**Evidence:** confirmed
**Source:** commit `9599c72`

Dependency minimums (in `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, `meta.yaml`) had drifted independently of each other before this commit — different files disagreed on the actual floor versions, and `ujson` was still listed as a dependency in some of them despite no longer being imported anywhere in the code. Fixed by using `setup.py`'s minimums as the source of truth across all five files and dropping `ujson` entirely.

**Reason:** this validates the "all five must be kept in sync manually" rule already in `AGENTS.md` — it's not a hypothetical risk, the files had actually drifted in practice before this cleanup.
