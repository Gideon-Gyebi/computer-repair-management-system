# Setup and Test Guide

This project uses Python and pytest for automated testing.

## 1. Open the project

From the repository root:

```bash
cd "C:/Users/<Name>/Desktop/Local/computer-repair-management-system"
```

## 2. Activate the virtual environment

If you are using PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If you are using Git Bash or a Unix-like shell:

```bash
source venv/bin/activate
```

## 3. Install dependencies

If pytest is missing, install the required packages:

```bash
python -m pip install pytest fastapi uvicorn httpx
```

## 4. Run the tests

Set the project root on PYTHONPATH and run pytest:

```bash
PYTHONPATH=. pytest -q
```

You can also use the Python module form:

```bash
PYTHONPATH=. python -m pytest -q
```

## 5. Run a specific test file

```bash
PYTHONPATH=. pytest ./tests/services/test_customer_service.py -q
```

## 6. Run a specific test

```bash
PYTHONPATH=. pytest tests/services/test_customer_service.py -k customer -q
```

## 7. Useful options

Verbose output:

```bash
PYTHONPATH=. pytest -v
```

Show failing tests only:

```bash
PYTHONPATH=. pytest -q --maxfail=1
```

## Notes

- The project is configured to use pytest.
- The repository is expected to be run from the root so that imports resolve correctly.
- The working validation command for this project is:

```bash
PYTHONPATH=. pytest ./tests/services/test_customer_service.py -q
```
