# Password Strength Analyzer + Controlled Wordlist Generator

## Project Overview

An educational Python command-line application that assesses password strength and generates controlled wordlists from synthetic inputs.

## Features

- Password-strength assessment using zxcvbn and additional validation rules.
- Mandatory username input and similarity checks.
- Weakness identification and improvement suggestions.
- Custom wordlist generation using contextual words, case variations, limited leetspeak and selected suffixes.
- Duplicate removal and a maximum generation limit of 10,000 candidates.
- Text-file export with output-path validation and overwrite protection.
- Separate analysis and wordlist-generation functions.

## Technology

- **Language:** Python 3
- **Platform:** Kali Linux
- **Interface:** Command-line interface (CLI)
- **Dependency:** zxcvbn
- **Version control:** Git

## Setup

Clone the repository and enter the project directory:

```bash
git clone https://github.com/kali-rudra/ElevateLabs-Project-4-Password-Strength-Analyzer.git
cd ElevateLabs-Project-4-Password-Strength-Analyzer
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependency:

```bash
python -m pip install zxcvbn
```

## Usage

Analyze a password:

```bash
python main.py analyze
```

Generate a custom wordlist:

```bash
python main.py generate
```

View available commands:

```bash
python main.py --help
```

Use synthetic test data for wordlist generation. Only use generated wordlists in authorized educational environments.

## Security and Privacy

- Password analysis is performed locally.
- Password and username inputs are not intentionally saved or logged.
- Password input uses hidden terminal entry.
- No password transmission is intended.
- Generated wordlists contain user-provided contextual candidates, not analysed passwords.
- Existing output files require confirmation before overwrite.

## Testing and Project Status

Core password-analysis and wordlist-generation functionality has been implemented and tested.

Testing includes input validation, username checks, candidate deduplication, generation limits, text export, overwrite protection and output-path error handling.

Privacy handling has also undergone source-code review.

## Disclaimer

Password-strength results are educational estimates, not guarantees of security. This tool does not replace unique passwords, password managers or multi-factor authentication.

## License

No open-source licence has been assigned.
