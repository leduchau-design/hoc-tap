"""
FILE MẪU TỰ TẠO TEST CHO BÀI TẬP MỚI (DÀNH CHO BẠN)
=====================================================
Mỗi khi có bài tập mới (ví dụ bai2.py, de2.py), bạn chỉ cần làm 3 bước:
1. Copy file này và đổi tên thành: test_bai2.py (hoặc test_de2.py)
2. Sửa tên file import ở BƯỚC 1 thành tên file code của bạn
3. Điền các câu hỏi và đáp án mong muốn ở BƯỚC 2
4. Chạy: python tests/test_bai2.py là nó tự chấm từng câu!
"""

import unittest
import sys
import os

# Đảm bảo tiếng Việt hiển thị đẹp trên Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Cho phép tìm file code ở thư mục gốc
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# =====================================================================
# BƯỚC 1: IMPORT HÀM TỪ FILE CODE CỦA BẠN
# Ví dụ: file bài làm của bạn tên là bai2.py và có các hàm ben duoi:
# from bai2 import tinh_tong, kiem_tra_so_nguyen_to
# =====================================================================
from h import tong_uoc_so, kiem_tra_doi_xung  # <-- Sửa tên file và tên hàm ở đây


# =====================================================================
# BƯỚC 2: VIẾT TEST CHO TỪNG CÂU
# Lưu ý quan trọng: Tên hàm BẮT BUỘC phải bắt đầu bằng chữ "test_"
# =====================================================================
class TestBaiTapMoi(unittest.TestCase):

    def test_cau_1(self):
        """[Câu 1] Kiểm tra hàm tính toán"""
        # Cú pháp: self.assertEqual(hàm_của_bạn(đầu_vào), kết_quả_đúng_kỳ_vọng)
        self.assertEqual(tong_uoc_so(6), 12, "Lỗi: Ước của 6 phải ra 12")
        self.assertEqual(tong_uoc_so(1), 1, "Lỗi: Ước của 1 phải ra 1")

    def test_cau_2(self):
        """[Câu 2] Kiểm tra hàm trả về True / False"""
        # Cú pháp: self.assertTrue(hàm) hoặc self.assertFalse(hàm)
        self.assertTrue(kiem_tra_doi_xung("radar"), "Lỗi: 'radar' phải là đối xứng")
        self.assertFalse(kiem_tra_doi_xung("python"), "Lỗi: 'python' không đối xứng")


# =====================================================================
# BƯỚC 3: TỰ ĐỘNG CHẠY VÀ IN KẾT QUẢ TỪNG CÂU (KHÔNG CẦN CHỈNH SỬA)
# =====================================================================
if __name__ == "__main__":
    unittest.main(verbosity=2)
