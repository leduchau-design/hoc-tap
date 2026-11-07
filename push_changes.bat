@echo off
chcp 65001 > nul
echo ========================================================
echo       CÔNG CỤ ĐỒNG BỘ TÀI LIỆU HỌC TẬP LÊN GITHUB
echo ========================================================
echo.
echo [1/3] Kiểm tra trạng thái file...
git status -s
echo.
echo [2/3] Đang lưu thay đổi vào Git...
git add .
git commit -m "Cap nhat tai lieu hoc tap va bai tap Python" 2>nul
echo.
echo [3/3] Đang đẩy (push) lên GitHub: https://github.com/leduchau-design/hoc-tap...
git push -u origin main
echo.
echo ========================================================
echo [OK] Hoàn tất đồng bộ! Hãy kiểm tra lại trên GitHub.
echo ========================================================
pause
