@echo off
chcp 65001 > nul
title HỆ THỐNG KIỂM THỬ TOÀN BỘ BÀI TẬP (TEST CHUNG)
echo ========================================================
echo       ĐANG CHẠY KIỂM THỬ TOÀN BỘ BÀI TẬP (TEST CHUNG)
echo ========================================================
echo.
python -m unittest discover -s tests -p "test_*.py" -v
echo.
echo ========================================================
echo [OK] Đã hoàn thành kiểm thử tất cả các bài tập!
echo ========================================================
pause
