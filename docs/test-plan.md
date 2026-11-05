# Password Strength Analyzer with Custom Wordlist Generator
## Test Plan

**Document status:** Approved baseline — partial test execution recorded; remaining tests pending
**Project:** ElevateLabs Project 4
**Version:** 1.1

## 1. Purpose

This test plan defines how the Password Strength Analyzer with Custom Wordlist Generator will be verified against its approved requirements.

Testing will cover:

- Password-strength classification and explanations.
- Common-password detection and predictable patterns.
- Username-related password warnings.
- Input validation and privacy protections.
- Custom wordlist generation and transformations.
- Candidate limits, deduplication and text-file export.

Test results must record actual observations. A test must not be marked as passed until its behaviour has been verified.

## 2. Test Environment

The planned environment is:

- Operating system: Kali Linux.
- Programming language: Python.
- Primary password estimator: zxcvbn.
- Command-line interface: argparse.
- Wordlist export format: plain-text `.txt`.
- Testing approach: controlled examples and repeatable checks.

Exact dependency versions and the final test commands will be recorded when implementation begins.

## 3. Password Classification Rules

The initial classification policy is:

1. An exact match in the configured local common-password list is **Weak**, regardless of letter case.
2. Passwords shorter than 8 characters are **Weak**.
3. Clearly severe repetition or predictable sequences may result in **Weak**, according to defined and tested rules.
4. Username input is mandatory. The analyzer must not begin password assessment until a username containing at least one non-whitespace character has been supplied.
5. A meaningful match with the supplied username prevents a **Strong** classification but does not automatically make the password Weak.
6. **Strong** requires at least 14 characters as a project baseline and an appropriate assessment by zxcvbn, supplemented by the application's rules.
7. The initial zxcvbn score mapping is:
   - Scores 0–1: Weak.
   - Score 2: Moderate.
   - Scores 3–4: Strong candidate before project-specific overrides.
8. Any mandatory project rule that makes a password Weak takes precedence over a more favourable estimator score.
9. A password that is not Weak and does not qualify as Strong is classified as Moderate.
10. Character variety alone must never be treated as proof of security.
11. The result must explain detected weaknesses and offer useful improvement suggestions.

The implementation must apply these rules consistently. The 14-character baseline is a project policy, not a universal security guarantee.

## 4. Password Analyzer Test Cases

All cases below are planned tests. Expected outcomes are not observed results.

| Test ID | Scenario | Test input or condition | Expected result |
|---|---|---|---|
| PA-01 | Common password | `password` | Weak; explain the common-password match. |
| PA-02 | Short password | `1234567` | Weak because it is shorter than 8 characters. |
| PA-03 | Case-insensitive match | `Password` | Weak if `password` is in the local common-password list. |
| PA-04 | Uppercase common password | `PASSWORD` | Weak if the equivalent lowercase entry is in the list. |
| PA-05 | Word with year | `BlueRiver2026` | Must not be classified Strong merely because it contains mixed character types; assess predictability and apply project rules. |
| PA-06 | Strong candidate | `vQ7!mZ2@pL9#tR` | Determine the result from the actual zxcvbn score and project rules; do not assume Strong in advance. |
| PA-07 | Repetition | `aaaaaaaB9!` | Assess repetition and predictability; apply the agreed rules consistently. |
| PA-08 | Meaningful username match | Password `Riverstone!482`; username `riverstone` | Must not be Strong; explain the meaningful username match. |
| PA-09 | Trivial username fragment | A password shares only a trivial fragment with the username | No automatic username penalty solely for that fragment. |
| PA-10 | Empty password | Empty input | Clear validation message; no misleading strength result. |
| PA-11 | URL-looking string | `https://example.com` | Treat as a password candidate string; do not visit or validate the URL. Assess its predictability. |
| PA-12 | Username override | A password otherwise eligible for Strong contains a meaningful username component | Final classification cannot be Strong; explain why. |
| PA-13 | Long but predictable password | A long password containing obvious sequences or familiar patterns | Length alone must not make it Strong. |
| PA-14 | Less-predictable passphrase | A sufficiently long passphrase with no disqualifying project rule | May qualify as Strong if the actual estimator result and all project rules support it. |
| PA-15 | Score mapping | Controlled tests producing zxcvbn scores 0, 1, 2, 3 and 4 | Each score maps to the documented initial category before overrides. |
| PA-16 | Privacy during analysis | Analyze a test password and inspect application behaviour | Password and username are not written to logs, files or network destinations. |
| PA-17 | Invalid output path | Supply an invalid or unusable wordlist output path | Clear error; no silent fallback to a different path. |
| PA-18 | Blank username | Submit an empty username | Reject it; do not begin password assessment; prompt again. |
| PA-19 | Whitespace-only username | Enter spaces or tabs as the username | Reject it; do not begin password assessment; prompt again. |
| PA-20 | Valid username after invalid input | Enter a blank or whitespace-only username, then a valid username | Continue only after valid username input; perform the username check. |
| PA-21 | Username check cannot be skipped | Follow the interactive prompts and attempt to bypass the username field | No bypass or partial-assessment route; password assessment requires a valid username. |
| PA-22 | Username-match Moderate override | Use a synthetic password that scores 4/4 and contains a meaningful part of the supplied username | Display the username-match warning and classify as Moderate, not Strong. |

## 5. Custom Wordlist Generator Test Cases

| Test ID | Scenario | Test condition | Expected result |
|---|---|---|---|
| WG-01 | Contextual inputs | Supply synthetic words and optional numbers or years | Generator uses valid inputs to produce candidates. |
| WG-02 | Case variations | Enable the predefined case transformations | Only the configured variations are generated. |
| WG-03 | Selected suffixes | Supply a word and configure supported suffixes | Expected configured suffix combinations are generated. |
| WG-04 | Year combinations | Supply a word and selected years | Candidates follow the approved year-combination rules. |
| WG-05 | Limited leetspeak | Supply a word such as `security` | Only the predefined substitutions are applied; transformations are predictable and testable. |
| WG-06 | Candidate limit | Configure inputs that could generate more than 10,000 candidates | Generation never exceeds 10,000 candidates in one run. |
| WG-07 | Deduplication | Use inputs and transformations that produce duplicate candidates | Duplicate candidates are removed. |
| WG-08 | Invalid settings | Provide missing or invalid required settings | Clear validation error; invalid settings are not silently accepted. |
| WG-09 | Text export | Generate a small known set of candidates | Exported `.txt` file contains the generated candidates in the documented format. |
| WG-10 | Overwrite protection | Choose an output path that already contains a file | Existing file is not overwritten without explicit confirmation. |
| WG-11 | Output-path confirmation | Start a generation run | User is prompted to confirm the output path for that run. |
| WG-12 | Privacy | Generate a wordlist from synthetic contextual inputs | Passwords and usernames used for analysis are not saved or logged by the application. |
| WG-13 | Separation of functions | Generate a wordlist without analyzing a password | Wordlist generation operates independently of password analysis. |

## 6. Privacy and Safety Requirements

The implementation must:

- Perform password analysis locally using the installed estimator.
- Avoid transmitting passwords or usernames over the network.
- Avoid saving or logging passwords and usernames.
- Hide password characters during interactive entry.
- Treat URL-looking strings as ordinary candidate strings, without visiting them.
- Keep wordlist generation separate from attempts to authenticate to a service.
- Use synthetic examples and controlled, authorized environments for testing.

These requirements must be verified against the implementation; they are not considered satisfied merely because they are written here.

## 7. Wordlist Generator Requirements

The generator must:

- Accept synthetic, user-provided contextual words and supported optional numeric inputs.
- Apply only the approved transformations and combination rules.
- Enforce a maximum of 10,000 generated candidates per run.
- Remove duplicate candidates.
- Validate inputs and report clear errors.
- Prompt the user to confirm the output path each run.
- Export candidates in plain-text `.txt` format.
- Refuse to overwrite an existing file unless the user explicitly confirms.
- Operate as a controlled educational utility for authorized security learning.

The generator is not required to perform password cracking or submit login attempts.

## 8. Recording Test Results

For each executed test, record:

- Test ID.
- Date executed.
- Exact test input or test condition, using safe synthetic examples.
- Expected result.
- Actual observed result.
- Pass, Fail or Blocked status.
- Relevant notes or corrective action.

Do not record real passwords or usernames in the test report or engineering log.

**Current status:** Partial execution recorded. Only the results listed below have been observed; all other tests remain pending until executed.

### Executed Test Results

| Test ID | Observed condition | Actual observed result | Status |
|---|---|---|---|
| PA-18 | Empty username submitted | Rejected; program prompted for a username again. | Pass |
| PA-19 | Whitespace-only username submitted | Rejected; program prompted for a username again. | Pass |
| PA-20 | Invalid username input followed by a valid username | Program accepted the valid username and continued to password assessment. | Pass |
| PA-21 | Attempt to bypass the mandatory username check | Two blank username submissions were rejected; assessment proceeded only after `testuser` was entered. | Pass |
| PA-22 | Synthetic username-matching test; zxcvbn score 4/4 | Warning displayed; preliminary classification was Moderate. | Pass |
| Username-match warning | A test run produced a meaningful-username-match warning. | Warning observed in an earlier run; the dedicated Moderate-override behaviour was subsequently verified by PA-22. | Pass for warning observation; see PA-22 for override |

**Verification note:** `python -m py_compile main.py` completed without a syntax error after the obsolete partial-assessment route was removed. A search confirmed that the old skip/partial-assessment wording was absent. These checks do not establish that every application requirement has passed.

## 9. Known Limitations

- zxcvbn estimates guessability; it cannot guarantee that a password is secure.
- Its dictionaries and pattern recognition may not identify every predictable construction.
- The local common-password list detects only entries it contains.
- Username matching can produce false positives or miss meaningful relationships; matching rules must be defined and tested.
- The 14-character threshold is a project classification policy, not a universal security standard.
- Test outcomes may depend on the installed dependency version and configured dictionaries.

These limitations must be considered when interpreting test results.

### Generator Test Execution Results - 2026-11-05

| Test ID | Observed result | Status |
|---|---|---|
| WG-07 | Duplicate input `river` produced six unique candidates; no duplicate entries were returned. | Pass |
| WG-08 | Invalid suffix `#` was rejected during the earlier validation test; valid selections were accepted. | Pass |
| WG-09 | Earlier successful generator runs exported candidate lists and their contents were inspected. The later custom-path rerun encountered an existing file and was cancelled at the overwrite prompt. | Pass - earlier export evidence; custom-path rerun not reconfirmed |
| WG-10 | Existing file was preserved after overwrite confirmation was declined. | Pass |
| WG-11 | Custom output directory and filename were accepted. Invalid absolute path produced a handled `OSError` message without crashing. | Pass |
| WG-12 | Source review found no password or username persistence, logging, database writes or credential export. Password input uses `getpass`; generated wordlist export is separate. | Pass - source-code review |
