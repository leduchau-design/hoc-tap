"""
FILE MẪU TỰ TẠO TEST THÔNG MINH CHO BÀI TẬP MỚI
=====================================================
Khi làm bài tập mới (ví dụ bai2.py, de2.py), bạn chỉ cần làm 3 bước:
1. Copy file này thành: test_bai2.py (nằm trong thư mục tests)
2. Sửa dòng import ở BƯỚC 1 thành tên file code của bạn
3. Viết các câu hỏi và hướng dẫn sửa lỗi ở BƯỚC 2
4. Chạy: python tests/test_bai2.py
"""

import unittest
import sys
import os

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# =====================================================================
# HÀM BÁO LỖI THÔNG MINH (TỰ ĐỘNG CHỈ VỊ TRÍ VÀ HƯỚNG DẪN SỬA)
# =====================================================================
def bao_loi(cau, dau_vao, ket_qua_ban, ket_qua_dung, nguyen_nhan, cach_sua):
    border = "=" * 70
    return (
        f"\n{border}\n"
        f" ❌ PHÁT HIỆN LỖI SAI TẠI: {cau}\n"
        f" 📥 Dữ liệu thử nghiệm : {dau_vao}\n"
        f" 📤 Code của bạn ra    : {ket_qua_ban}\n"
        f" 🎯 Đáp án chuẩn kỳ vọng: {ket_qua_dung}\n"
        f" ⚠️ Nguyên nhân lỗi   : {nguyen_nhan}\n"
        f" 💡 HƯỚNG DẪN CÁCH SỬA : {cach_sua}\n"
        f"{border}"
    )


# =====================================================================
# BƯỚC 1: IMPORT HÀM TỪ FILE BÀI TẬP CỦA BẠN
# Ví dụ: from bai2 import binh_phuong
# =====================================================================
from h import tong_uoc_so


# =====================================================================
# BƯỚC 2: VIẾT TEST KÈM HƯỚNG DẪN SỬA LỖI
# =====================================================================
class TestBaiTapMoi(unittest.TestCase):

    def test_cau_1(self):
        """[Câu 1] Kiểm tra hàm"""
        res = tong_uoc_so(6)
        msg = bao_loi(
            cau="[Câu 1] Hàm tong_uoc_so(n)",
            dau_vao="n = 6",
            ket_qua_ban=res,
            ket_qua_dung="12 (vì 1 + 2 + 3 + 6 = 12)",
            nguyen_nhan="Vòng lặp chạy thiếu số n (ước lớn nhất).",
            cach_sua="Đổi range(1, n) thành range(1, n + 1) để duyệt hết số n."
        )
        self.assertEqual(res, 12, msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
