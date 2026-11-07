@echo off
chcp 65001 > nul
echo ========================================================
echo       CÔNG CỤ ĐỒNG BỘ TÀI LIỆU HỌC TẬP LÊN GITHUB
echo ========================================================
echo.
echo [1/3] Kiểm tra trạng thái file...
git status -s
echo.
set /p commit_msg="Nhập nội dung cập nhật (Nhấn Enter để dùng mặc định: 'Cập nhật tài liệu'): "
if "%commit_msg%"=="" set commit_msg=Cập nhật tài liệu môn học
echo.
echo [2/3] Đang lưu thay đổi vào Git...
git add .
git commit -m "%commit_msg%"
echo.
echo [3/3] Đang đẩy (push) lên GitHub...
git push origin main
echo.
echo ========================================================
echo [OK] Đã hoàn tất đồng bộ lên GitHub!
echo ========================================================
pause
