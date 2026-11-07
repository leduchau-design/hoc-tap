@echo off
chcp 65001 > nul
echo ========================================================
echo       CONG CU DONG BO TAI LIEU HOC TAP LEN GITHUB
echo ========================================================
echo.
echo [1/4] Kiem tra dung luong file an toan (<95MB)...
python check_size.py
echo.
echo [2/4] Kiem tra cac thay doi moi...
git status -s
echo.
echo [3/4] Dang luu thay doi vao Git...
git add .
git commit -m "Cap nhat tai lieu hoc tap va bai tap Python" 2>nul
echo.
echo [4/4] Dang day (push) len GitHub: https://github.com/leduchau-design/hoc-tap...
git push -u origin main
echo.
echo ========================================================
echo [OK] Hoan tat dong bo! Hay kiem tra lai tren GitHub.
echo ========================================================
pause
