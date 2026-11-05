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

## 5. Remaining Work — Not Yet Completed

* Complete and verify password analysis and strength classification.
* Verify username-similarity checks, including the Moderate override.
* Implement controlled wordlist and random test-string generation.
* Implement safe text-file export, output-path confirmation, and file-safety checks.
* Add automated tests for normal cases, edge cases, privacy, limits, and file safety.
* Review the design and record actual test results.
* Consider a graphical interface only after the CLI is stable.

## 6. Learning Notes

* The current working directory and the active Python environment are separate concepts.
* Activating `.venv/` changes which Python environment the shell uses; it does not change the working directory.
* Git distinguishes between untracked, staged, and committed files.
* `.gitignore` tells Git what to ignore; it does not delete those files.
* Git commits record snapshots locally. A commit does not automatically upload anything to GitHub.

## 7. Current Checkpoint

Environment setup, Git initialization, the README, project directories, and the initial application files have been created.

The command-line application now contains password-analysis logic, common-password checking, username matching, and strength classification. The custom wordlist generator remains to be implemented.

Manual testing has begun for mandatory username validation. Empty and whitespace-only usernames were rejected, valid usernames were accepted, and a username-match warning was observed in one run. These results are recorded in the test plan.

The syntax check completed successfully after removal of the obsolete partial-assessment route. Full application verification remains incomplete.

## 8. Log Maintenance Rule

Update this log as work progresses. Record actual commands, observed results, decisions, test outcomes, and unresolved issues accurately. Never report planned work as completed or unverified results as successful.

## 9. Work Log — 2026-10-22

### Mandatory Username Validation

**Objective:** Make username input mandatory before password assessment and remove the obsolete route that allowed assessment to continue without username matching.

**Changes made:**
* Removed the option to continue without a username.
* Added validation that rejects empty and whitespace-only usernames and prompts again.
* Removed the obsolete partial-assessment message and its now-unnecessary conditional.
* Simplified username matching because a valid username is now required.

**Commands executed:**

* `python -m py_compile main.py` — initially exposed an indentation error after the obsolete print statement was removed; passed after the associated empty conditional was also removed.
* `grep -n -E "leave blank|Continue without|Assessment status: Partial|username_match" main.py` — confirmed that the old skip/partial-assessment wording was absent and username-matching logic remained.

**Manual observations:**
* An empty username was rejected and the program prompted again.
* A whitespace-only username was rejected and the program prompted again.
* Valid synthetic usernames were accepted, and the program proceeded to password assessment.
* A username-match warning appeared in one run.
* The observed assessment runs returned a score of 1 out of 4 and a Weak classification. Because the password inputs were hidden and the runs did not establish an otherwise-Strong result, the Moderate-override test remains pending.

**Test documentation:** Updated `docs/test-plan.md` to version 1.1, recording partial execution and distinguishing observed results from pending tests.

**Outstanding verification:**
* Test the username-match Moderate override with a synthetic test case that otherwise qualifies as Strong.
* Perform a dedicated attempt to bypass username input.
* Continue testing the remaining password-analysis requirements.
* Implement and test the custom wordlist generator.

No password values were recorded in this log.

## 10. Work Log — 2026-10-23

### Username-Match Moderate Override Verification

**Objective:** Verify that a meaningful username match prevents a password
otherwise eligible for Strong from receiving a Strong classification.

**Test method:** Ran the interactive application with synthetic test data.
The password was entered through the hidden password prompt; its value is
intentionally omitted from this log.

**Observed results:**
* zxcvbn returned a raw strength score of 4 out of 4.
* The application displayed the meaningful-username-match warning.
* The application displayed `Moderate` as the preliminary classification.

**Outcome:** PA-22 — Pass for this test case. The observed result confirms
that the username-match rule overrides an otherwise high-scoring result
to Moderate in this scenario.

**Evidence:** `EL-P04-EV-001_2026-10-23_Username-Match-Moderate-Override.png`
is listed in `docs/evidence-register.md`.

**Verification status:**
* PA-21 — Completed; two blank username submissions were rejected before assessment. See `docs/test-plan.md` and EV-006.
* Continue testing any remaining password-analysis requirements as applicable.
* Custom wordlist generator implemented and tested; see WG-07 through WG-12 in `docs/test-plan.md` and EV-002 through EV-007.

No password values were recorded in this log.
