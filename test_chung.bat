@echo off
chcp 65001 > nul
title KIEM THU TOAN BO BAI TAP (TEST CHUNG)
echo ========================================================
echo       KIEM THU TOAN BO BAI TAP (TEST CHUNG)
echo ========================================================
echo.
python -m unittest discover -s tests -p "test_*.py" -v
echo.
echo ========================================================
echo [OK] Da hoan thanh kiem thu tat ca cac bai tap!
echo ========================================================
pause
