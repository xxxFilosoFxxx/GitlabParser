python -m venv venv
Write-Host "Created virtual environment..."
.\venv\Scripts\activate
pip install -r packages.txt
pyinstaller --onefile GitlabParser.py
Write-Host "Successfully build .\dist\GitlabParser.exe"