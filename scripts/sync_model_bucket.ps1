# Sync DeepSeek-R1-Distill-Qwen-32B weights from Hugging Face Bucket
# Bucket: keshavrao887/DeepSeek-R1-Distill-Qwen-32B-bucket

param (
    [string]$DestinationDir = "./models/DeepSeek-R1-Distill-Qwen-32B",
    [string]$BucketUri = "hf://buckets/keshavrao887/DeepSeek-R1-Distill-Qwen-32B-bucket"
)

Write-Host "=== DeepSeek-R1-Distill-Qwen-32B Bucket Sync ===" -ForegroundColor Cyan
Write-Host "Target Bucket: $BucketUri"
Write-Host "Destination:   $DestinationDir"

# 1. Check if HF CLI is installed
if (-not (Get-Command hf -ErrorAction SilentlyContinue)) {
    Write-Host "Hugging Face CLI ('hf') is not detected on PATH. Installing..." -ForegroundColor Yellow
    powershell -ExecutionPolicy ByPass -c "irm https://hf.co/cli/install.ps1 | iex"
}

# 2. Ensure destination folder exists
if (-not (Test-Path $DestinationDir)) {
    New-Item -ItemType Directory -Force -Path $DestinationDir | Out-Null
    Write-Host "Created destination directory: $DestinationDir" -ForegroundColor Green
}

# 3. Run sync command
Write-Host "Starting hf sync..." -ForegroundColor Cyan
hf sync $BucketUri $DestinationDir

if ($LASTEXITCODE -eq 0) {
    Write-Host "`nSuccessfully synced model weights to: $DestinationDir" -ForegroundColor Green
    Write-Host "You can now point Ollama or vLLM to this model path." -ForegroundColor Green
} else {
    Write-Host "`nhf sync encountered an error (exit code: $LASTEXITCODE)." -ForegroundColor Red
}
