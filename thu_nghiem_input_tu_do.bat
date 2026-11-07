@echo off
chcp 65001 >nul
title THU NGHIEM NHAP INPUT TU DO - HOC TAP PYTHON

echo ======================================================================
echo           CHET DO THU NGHIEM NHAP INPUT TU DO TU BAN PHIM
echo ======================================================================
echo.

python tests/test_nhieu_truong_hop.py --nhap

echo.
echo Nhan phim bat ky de thoat...
pause >nul
