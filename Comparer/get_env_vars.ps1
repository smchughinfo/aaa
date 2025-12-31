# PowerShell script to read environment variables
Write-Host "=== Environment Variables ===" -ForegroundColor Green
Write-Host ""

$vars = @(
    "aaa_neon_db_host",
    "aaa_neon_db_database",
    "aaa_neon_db_username",
    "aaa_neon_db_password",
    "aaa_comparer_openai_api_key",
    "aaa_sb_aaa_connection_string"
)

foreach ($var in $vars) {
    $value = [System.Environment]::GetEnvironmentVariable($var, "User")
    if (-not $value) {
        $value = [System.Environment]::GetEnvironmentVariable($var, "Machine")
    }
    if (-not $value) {
        $value = [System.Environment]::GetEnvironmentVariable($var, "Process")
    }

    if ($value) {
        Write-Host "$var=$value" -ForegroundColor Cyan
    } else {
        Write-Host "$var=NOT_FOUND" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Copy the output above and paste it back to Claude" -ForegroundColor Yellow
