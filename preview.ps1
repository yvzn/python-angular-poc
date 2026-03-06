# This script is used to preview the application locally in a production-like environment. 

$currentScriptPath = $PSScriptRoot
Set-Location $currentScriptPath

## Build the Angular application
Set-Location $currentScriptPath/front
npm install
npm run build

## Copy the built Angular application to the static directory of the FastAPI server
Set-Location $currentScriptPath/server
Remove-Item -Path static -Recurse -Force
Copy-Item ../front/dist/front/browser ./static -Recurse -Force

## Build and run the FastAPI server
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
try {
    python -m uvicorn main:app --host 0.0.0.0 --port 8000
} finally {
    Set-Location $currentScriptPath
}
