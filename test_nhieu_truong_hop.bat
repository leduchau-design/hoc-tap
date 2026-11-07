@echo off
chcp 65001 >nul
title TEST NHIEU TRUONG HOP - HOC TAP PYTHON

echo ======================================================================
echo         KIEM THU DA TRUONG HOP (MULTI-CASE TEST) BAI TAP PYTHON
echo ======================================================================
echo.
echo [*] Dang chay kiem tra 52 truong hop dau vao khac nhau...
echo.

python tests/test_nhieu_truong_hop.py

echo.
echo ======================================================================
echo [*] Meo: Muon tu go input tu ban phim, chay: thu_nghiem_input_tu_do.bat
echo ======================================================================
echo.
echo Nhan phim bat ky de dong cua so...
pause >nul
