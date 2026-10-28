@echo off
chcp 65001 >nul
title Podglad strony - Buduj z Kaszubami
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0podglad.ps1"
if errorlevel 1 pause
