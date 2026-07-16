# PDF生成スクリプト
# 使い方: powershell -ExecutionPolicy Bypass -File tools/build-pdf.ps1
# tools/pdf/*.html を Chrome ヘッドレスで downloads/*.pdf へ変換する
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
if (-not (Test-Path $chrome)) { $chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" }
if (-not (Test-Path $chrome)) { Write-Error "Chrome が見つかりません"; exit 1 }

$outDir = Join-Path $root "downloads"
if (-not (Test-Path $outDir)) { New-Item -ItemType Directory $outDir | Out-Null }

Get-ChildItem (Join-Path $root "tools\pdf\*.html") | ForEach-Object {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
    $out = Join-Path $outDir ($name + ".pdf")
    $src = "file:///" + ($_.FullName -replace "\\", "/")
    Write-Host "generating $name.pdf ..."
    # Chromeはstderrへ進捗を出すため、Start-Processでエラー扱いを回避する
    $args = @("--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=$out", $src)
    Start-Process -FilePath $chrome -ArgumentList $args -Wait -WindowStyle Hidden
    if (Test-Path $out) {
        $kb = [math]::Round((Get-Item $out).Length / 1KB)
        Write-Host "  -> OK ($kb KB)"
    } else {
        Write-Error "  -> FAILED: $out"
    }
}
Write-Host "done."
