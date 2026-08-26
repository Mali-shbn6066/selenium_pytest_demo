# Selenium + Pytest QA Automation Demo

A small practice project for learning:
- Python
- Selenium
- Pytest
- Page Object Model
- Git/GitHub
- Jenkins

## 1. Install Python
Install Python 3.11+ and make sure `python --version` works.

## 2. Create and activate a virtual environment

Windows PowerShell:
```powershell
cd C:\path\to\selenium_pytest_demo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows CMD:
```cmd
cd C:\path\to\selenium_pytest_demo
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Run the tests
```bash
pytest -v
```

To see the browser:
```bash
pytest -v --headed
```

The project uses Selenium Manager, so a separate ChromeDriver download is normally not required.

## Project structure

```text
selenium_pytest_demo/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
├── Jenkinsfile
└── README.md
```

## Git / GitHub

From the project folder:

```bash
git init
git add .
git commit -m "Initial Selenium Pytest project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Do NOT commit `.venv/`.

## Jenkins

The included `Jenkinsfile` runs:
1. Install Python dependencies
2. Run Pytest
3. Publish the JUnit test report

For a Jenkins Pipeline job, connect the GitHub repository and use:
`Pipeline script from SCM` -> Git -> your repository -> branch `main`.
