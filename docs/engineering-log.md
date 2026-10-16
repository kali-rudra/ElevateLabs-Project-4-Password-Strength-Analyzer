# Engineering and Learning Log

## Project

**Password Strength Analyzer + Controlled Wordlist Generator**

## 1. Verified Environment

* Operating system: Kali Linux
* Python version: Python 3.13.15
* Git version: 2.53.0
* Project directory: `/home/ameethp/password-strength-analyzer`
* Virtual environment: `.venv/`
* Git branch: `main`

## 2. Verified Setup Work

* Created the project directory.
* Created and activated the Python virtual environment.
* Verified that the `python` executable resolves to `.venv/bin/python`.
* Initialized the local Git repository.
* Renamed the initial branch from `master` to `main`.
* Created `.gitignore` containing `.venv/`.
* Verified that Git does not list `.venv/` as an untracked project item.
* Created and committed `README.md`.
* Created the `data/`, `docs/`, and `tests/` directories.
* Verified the project structure using `ls -la`.

## 3. Git History

* `7c5f405` — Add Git ignore rules
* `cca1413` — Add project README

These commit identifiers were observed in terminal output.

## 4. Design Decisions Agreed

* Build the command-line interface (CLI) before considering a graphical interface.
* Analyze passwords locally; do not save or log actual passwords.
* Include username-similarity checks, avoiding trivial fragment matches.
* A meaningful username match must prevent a Strong rating in version 1.
* Use synthetic test words for controlled wordlist generation.
* Enforce a maximum of 10,000 generated candidates per run.
* Deduplicate candidates and handle output files safely.
* Refuse to overwrite an existing output file by default.
* Prefer the Python standard library unless an additional dependency is justified.

## 5. Planned Work — Not Yet Implemented

* Implement password analysis and strength classification.
* Implement username-similarity checks.
* Implement controlled wordlist and random test-string generation.
* Implement safe text-file export.
* Add automated tests for normal cases, edge cases, privacy, limits, and file safety.
* Review the design and document actual test results.
* Consider a graphical interface only after the CLI is stable.

## 6. Learning Notes

* The current working directory and the active Python environment are separate concepts.
* Activating `.venv/` changes which Python environment the shell uses; it does not change the working directory.
* Git distinguishes between untracked, staged, and committed files.
* `.gitignore` tells Git what to ignore; it does not delete those files.
* Git commits record snapshots locally. A commit does not automatically upload anything to GitHub.

## 7. Current Checkpoint

Environment setup, Git initialization, the README commit, and creation of the project directories have been verified.

Application code has not yet been written.

No application tests have been run.

## 8. Log Maintenance Rule

Update this log as work progresses. Record actual commands, observed results, decisions, test outcomes, and unresolved issues accurately. Never report planned work as completed or unverified results as successful.
