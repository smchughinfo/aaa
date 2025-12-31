#!/bin/bash
# Kill all Python processes from the Comparer folder
powershell.exe -Command "Get-Process python -ErrorAction SilentlyContinue | Where-Object {\$_.Path -like '*Comparer*'} | Stop-Process -Force"
echo "Killed all Comparer Python processes"
