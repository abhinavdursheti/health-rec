@echo off
cd /d "%~dp0"
echo Starting Health Recommendation System...
echo Current directory: %CD%
echo.

REM Check if manage.py exists
if not exist "manage.py" (
    echo ERROR: manage.py not found!
    echo Please run this script from the project directory.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
echo Checking dependencies...
pip install -r requirements.txt --quiet

REM Create static directory if it doesn't exist
if not exist "static" mkdir static

REM Run migrations
echo Running database migrations...
python manage.py makemigrations
python manage.py migrate

REM Start server
echo.
echo ========================================
echo Starting Django development server...
echo ========================================
echo.
echo Server will be available at:
echo http://127.0.0.1:8000/
echo.
echo Press Ctrl+C to stop the server
echo.
echo Waiting for server to start...
timeout /t 2 /nobreak >nul
start http://127.0.0.1:8000/
echo.
python manage.py runserver

pause

