# Iniciar o backend
Write-Host "Iniciando o backend..."
Start-Process -NoNewWindow -FilePath "python3" -ArgumentList "-m backend.app"

# Mudar para o diretório do frontend
Set-Location -Path "./frontend"

# Iniciar o frontend
Write-Host "Iniciando o frontend..."
Start-Process -NoNewWindow -FilePath "npm" -ArgumentList "run dev"

# Para rodar no PowerShell: ./start.ps1