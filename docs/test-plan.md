# Password Strength Analyzer — Test Plan

## 1. Purpose

This test plan defines the expected behaviour of the Password Strength Analyzer before implementation. It covers strength classification, username similarity, input validation, and predictable password patterns.

All examples are synthetic test data. The analyzer is educational and does not guarantee that a password is secure.

## 2. Planned Test Cases

| Test ID | Test Input / Condition                                          | Expected Result                     | Reason                                                                                       |
| ------- | --------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------- |
| PA-01   | Password: `password`                                            | Weak                                | Exact match in the local common-password list                                                |
| PA-02   | Password: `1234567`                                             | Weak                                | Fewer than 8 characters                                                                      |
| PA-03   | Password: `vQ7!mZ2@`                                            | Moderate                            | 8 characters; does not qualify as Strong under the initial rules                             |
| PA-04   | Password: `BlueRiver2026`                                       | Moderate                            | 13 characters; familiar words and a year make it predictable                                 |
| PA-05   | Password: `vQ7!mZ2@pL9#tR`                                      | Strong candidate                    | 14 characters, varied character types, and no obvious pattern detected by the planned checks |
| PA-06   | Password: `aaaaaaaB9!`                                          | Weak                                | Excessive repetition                                                                         |
| PA-07   | Password: `Riverstone!482`; username: `riverstone`              | Not Strong                          | Meaningful username match, compared without case sensitivity                                 |
| PA-08   | Password: `rT8#pL4!zQ2@`                                        | Moderate                            | 12 characters; below the initial 14-character Strong threshold                               |
| PA-09   | Empty password input                                            | Clear validation error              | An empty password must not be analysed as a normal password                                  |
| PA-10   | Password contains only a single common letter from the username | No automatic username-match penalty | Avoid false positives from insignificant matches                                             |

## 3. Initial Classification Rules

The following rules are proposed for version 1 and must be implemented and tested.

1. An exact match in the local common-password list is Weak.
2. Passwords shorter than 8 characters are Weak.
3. Clearly severe repetition or predictable sequences may result in Weak.
4. A meaningful username match prevents a Strong classification but does not automatically make the password Weak.
5. Strong requires at least 14 characters, at least 3 character categories (lowercase, uppercase, digits, symbols), and no disqualifying weakness detected by the implemented checks.
6. Valid inputs that are neither Weak nor Strong are Moderate.
7. Character variety alone must never be treated as proof of security.
8. The result must explain the detected weaknesses and offer useful improvement suggestions.

These are educational heuristics, not a scientifically validated password-strength estimate. The limitations must be documented.

## 4. Privacy and Safety Tests

* Passwords must not be written to logs, diagnostic output, or files.
* Passwords must not be transmitted over a network.
* Username and password values must not be saved by the analyzer.
* Interactive password entry should hide typed characters.
* Invalid input must be handled without exposing sensitive data.

## 5. Wordlist Generator Tests

* Generate candidates only from synthetic test words and explicitly selected transformations.
* Remove duplicate candidates.
* Enforce the maximum of 10,000 candidates during generation.
* Reject invalid settings with a clear error.
* Export candidates to a user-confirmed `.txt` path.
* Refuse to overwrite an existing file unless the user explicitly confirms replacement.
* Do not log or save actual account passwords.

## 6. Test Status

**Status: Planned — not yet executed.**

Test results will be recorded only after the relevant application code exists and the tests have actually been run.

## 7. Known Limitations

* The initial rules may misclassify some passwords.
* A password that receives Strong is not guaranteed to be secure.
* The analyzer is not a substitute for a mature password-strength estimation library.
* The common-password list must remain small, local, documented, and suitable for the project's licensing requirements.
