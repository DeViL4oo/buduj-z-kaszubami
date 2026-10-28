# Podglad strony na lokalnym serwerze (bez instalowania czegokolwiek).
# Uruchamiany przez PODGLAD.cmd
$ErrorActionPreference = "Stop"

$root = Join-Path $PSScriptRoot "site"
if (-not (Test-Path $root)) {
    Write-Host "Nie znaleziono katalogu 'site' obok tego pliku." -ForegroundColor Red
    Read-Host "Enter, aby zamknac"
    exit 1
}
$root = (Resolve-Path $root).Path

$port = 8080
$listener = $null
while ($port -lt 8100) {
    try {
        $listener = New-Object System.Net.Sockets.TcpListener([System.Net.IPAddress]::Loopback, $port)
        $listener.Start()
        break
    } catch {
        $listener = $null
        $port++
    }
}
if (-not $listener) {
    Write-Host "Brak wolnego portu w zakresie 8080-8099." -ForegroundColor Red
    Read-Host "Enter, aby zamknac"
    exit 1
}

$url = "http://localhost:$port/"
Write-Host ""
Write-Host "  Podglad strony:  $url" -ForegroundColor Green
Write-Host "  Katalog:         $root"
Write-Host "  Zatrzymanie:     Ctrl + C  (albo zamknij to okno)"
Write-Host ""
Start-Process $url

$mime = @{
    ".html" = "text/html; charset=utf-8"
    ".css"  = "text/css; charset=utf-8"
    ".js"   = "text/javascript; charset=utf-8"
    ".json" = "application/json; charset=utf-8"
    ".svg"  = "image/svg+xml"
    ".jpg"  = "image/jpeg"
    ".jpeg" = "image/jpeg"
    ".png"  = "image/png"
    ".webp" = "image/webp"
    ".avif" = "image/avif"
    ".ico"  = "image/x-icon"
    ".woff2" = "font/woff2"
    ".xml"  = "application/xml; charset=utf-8"
    ".txt"  = "text/plain; charset=utf-8"
}

function Send-Response($stream, [int]$code, [string]$status, [string]$ctype, [byte[]]$body) {
    $head = "HTTP/1.1 $code $status`r`n"
    $head += "Content-Type: $ctype`r`n"
    $head += "Content-Length: $($body.Length)`r`n"
    $head += "Cache-Control: no-store`r`n"
    $head += "Connection: close`r`n`r`n"
    $bytes = [System.Text.Encoding]::ASCII.GetBytes($head)
    $stream.Write($bytes, 0, $bytes.Length)
    if ($body.Length -gt 0) { $stream.Write($body, 0, $body.Length) }
    $stream.Flush()
}

while ($true) {
    $client = $listener.AcceptTcpClient()
    try {
        $stream = $client.GetStream()
        $stream.ReadTimeout = 5000

        $buffer = New-Object byte[] 8192
        $read = $stream.Read($buffer, 0, $buffer.Length)
        if ($read -le 0) { $client.Close(); continue }
        $request = [System.Text.Encoding]::ASCII.GetString($buffer, 0, $read)
        $firstLine = ($request -split "`r`n")[0]
        $parts = $firstLine -split " "
        $method = $parts[0]
        $rawPath = "/"
        if ($parts.Length -ge 2) { $rawPath = $parts[1] }

        $rawPath = $rawPath.Split("?")[0]
        $decoded = [System.Uri]::UnescapeDataString($rawPath)
        $relative = $decoded.TrimStart("/")
        $target = Join-Path $root ($relative -replace "/", "\")

        $full = [System.IO.Path]::GetFullPath($target)
        if (-not $full.StartsWith($root, [System.StringComparison]::OrdinalIgnoreCase)) {
            Send-Response $stream 403 "Forbidden" "text/plain; charset=utf-8" ([System.Text.Encoding]::UTF8.GetBytes("403"))
            $client.Close(); continue
        }

        if ((Test-Path $full) -and (Test-Path $full -PathType Container)) {
            $full = Join-Path $full "index.html"
        } elseif (-not (Test-Path $full) -and (Test-Path "$full\index.html")) {
            $full = Join-Path $full "index.html"
        }

        if (-not (Test-Path $full)) {
            $notFound = Join-Path $root "404.html"
            if (Test-Path $notFound) {
                Send-Response $stream 404 "Not Found" "text/html; charset=utf-8" ([System.IO.File]::ReadAllBytes($notFound))
            } else {
                Send-Response $stream 404 "Not Found" "text/plain; charset=utf-8" ([System.Text.Encoding]::UTF8.GetBytes("404"))
            }
            $client.Close(); continue
        }

        $ext = [System.IO.Path]::GetExtension($full).ToLower()
        $ctype = "application/octet-stream"
        if ($mime.ContainsKey($ext)) { $ctype = $mime[$ext] }
        $bytes = [System.IO.File]::ReadAllBytes($full)
        Send-Response $stream 200 "OK" $ctype $bytes
    } catch {
        # pojedyncze bledne zadanie nie zatrzymuje serwera
    } finally {
        $client.Close()
    }
}
