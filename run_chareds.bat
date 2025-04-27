@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
python -m streamlit run chareds_app.py
