# Project 4 — Evidence Register

**Programme:** ElevateLabs CyberSecurity Internship
**Project:** Password Strength Analyzer with Custom Wordlist Generator

## Evidence Log

### EL-P04-EV-001 — Username-Match Moderate Override

- **Capture date:** 2026-10-23
- **Repository file:** `evidence/EL-P04-EV-001_2026-10-23_Username-Match-Moderate-Override.png`
- **Evidence type:** Interactive CLI test
- **Objective:** Verify that a meaningful username match prevents a Strong classification.
- **Observed result:** zxcvbn returned 4/4; the application displayed the username-match warning and classified the result as Moderate.
- **Status:** Pass for this test case
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Portfolio use:** Project summary and potential LinkedIn progress update.
- **Security note:** Do not publish screenshots containing real credentials, passwords, or other sensitive information.

### EL-P04-EV-002 — Wordlist Generator Export

- **Capture date:** 2026-10-29
- **Repository file:** `evidence/EL-P04-EV-002_2026-10-29_Wordlist-Generator-Export.jpg`
- **Evidence type:** Interactive CLI test
- **Objective:** Record successful generation and export of a custom wordlist.
- **Observed result:** The shared terminal output reported 6 unique candidates generated and saved to `generator_export_evidence.txt`.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** Successful generation and export observed in terminal output.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Synthetic test input used.

### EL-P04-EV-003 — Suffix Input Validation

- **Capture date:** 2026-10-29
- **Repository file:** `evidence/EL-P04-EV-003_2026-10-29_Suffix-Input-Validation.png`
- **Evidence type:** Interactive CLI validation test
- **Objective:** Verify that invalid suffix selections are rejected and valid options are displayed again.
- **Observed result:** The earlier shared terminal output showed invalid input `#` rejected, the menu redisplayed, and valid selections `1,3,4` accepted.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** Validation behaviour observed in terminal output.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Synthetic test input used.

### EL-P04-EV-004 — Suffix Export Verification

- **Capture date:** 2026-10-29
- **Repository file:** `evidence/EL-P04-EV-004_2026-10-29_Suffix-Export-Verification.png`
- **Evidence type:** Exported-file content check
- **Objective:** Record verification of generated candidates and selected suffix combinations in the exported text file.
- **Observed result:** The earlier shared terminal output from `cat suffix_validation_test.txt` displayed 12 candidates, including `river!`, `river#`, and `river123` in the expected case variants.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** Exported-file contents observed in terminal output.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Synthetic test input used.

### EL-P04-EV-005 — Candidate Limit Verification

- **Capture date:** 2026-11-05
- **Repository file:** `evidence/EL-P04-EV-005_2026-11-05_Candidate-Limit-Verification.png`
- **Evidence type:** Programmatic candidate-limit test
- **Objective:** Verify that wordlist generation stops at the configured maximum of 10,000 candidates.
- **Observed result:** 10,000 candidates generated; `truncated` returned `True`; the candidate count did not exceed 10,000.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** Pass for the candidate-limit test.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Synthetic test data used.


### EL-P04-EV-006 — Mandatory Username Check

- **Capture date:** 2026-11-05
- **Repository file:** `evidence/EL-P04-EV-006_2026-11-05_Mandatory-Username-Check.png`
- **Evidence type:** Interactive CLI validation test
- **Objective:** Verify that password assessment cannot proceed without a valid username.
- **Observed result:** Two blank username submissions were rejected. Assessment proceeded only after `testuser` was entered.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** PA-21 passed.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Synthetic test data used.

### EL-P04-EV-007 — Overwrite Protection

- **Capture date:** 2026-11-05
- **Repository file:** `evidence/EL-P04-EV-007_2026-11-05_Overwrite-Protection.png`
- **Evidence type:** Interactive CLI export-safety test
- **Objective:** Verify that an existing file is not overwritten when the user declines confirmation.
- **Observed result:** Export was cancelled after entering `n`; the original file content `DO NOT OVERWRITE` remained unchanged.
- **Screenshot status:** Saved locally, confirmed by the user; image not independently inspected.
- **Test status:** Pass for overwrite protection.
- **Related documentation:** `docs/test-plan.md`, `docs/engineering-log.md`
- **Security note:** Disposable test file and synthetic input used.
