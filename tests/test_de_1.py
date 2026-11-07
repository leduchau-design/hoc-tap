# -*- coding: utf-8 -*-
"""
BỘ KIỂM THỬ TỰ ĐỘNG CHO ĐỀ THI SỐ 1 (MÃ ĐỀ: 11301)
Kiểm tra tính chính xác của toàn bộ các hàm trong 5 câu hỏi Đề 1.
"""

import sys
import os
import unittest

# Đảm bảo hiển thị UTF-8 trên Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Thêm đường dẫn tới thư mục De-1
de1_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Nam-1", "Hoc-Ky-1", "CS101-Nhap-Mon-Lap-Trinh", "De-Thi", "De-1"))
if de1_dir not in sys.path:
    sys.path.insert(0, de1_dir)

from cau1 import DemChuSoLe, S
from cau2 import dem_chu_hoa, DoiXung, tinh_tong_chu_so
from cau3 import tong_duong_chan, dem_so_lan_xuat_hien
from cau4 import xoa_sach
from cau5 import DienThoai


class TestDeThi1(unittest.TestCase):
    """Kiểm thử tự động các chức năng trong Đề 1."""

    # =========================================================================
    # CÂU 1
    # =========================================================================
    def test_cau1_dem_chu_so_le(self):
        """[Câu 1.b] Đếm chữ số lẻ của số nguyên dương n"""
        self.assertEqual(DemChuSoLe(635), 2, "n=635 có 2 chữ số lẻ (3, 5)")
        self.assertEqual(DemChuSoLe(2468), 0, "n=2468 không có chữ số lẻ nào")
        self.assertEqual(DemChuSoLe(13579), 5, "n=13579 có 5 chữ số lẻ")
        self.assertEqual(DemChuSoLe(100), 1, "n=100 có 1 chữ số lẻ (1)")

    def test_cau1_tinh_tong_s(self):
        """[Câu 1.c] Tính tổng S = 1/2 + 1/4 + ... + 1/(2n)"""
        self.assertAlmostEqual(S(1), 0.5, places=5)
        self.assertAlmostEqual(S(2), 0.75, places=5)
        self.assertAlmostEqual(S(3), 1/2 + 1/4 + 1/6, places=5)

    # =========================================================================
    # CÂU 2
    # =========================================================================
    def test_cau2_dem_chu_hoa(self):
        """[Câu 2.a] Đếm số ký tự in hoa trong chuỗi"""
        self.assertEqual(dem_chu_hoa("Lap Trinh Python"), 3)
        self.assertEqual(dem_chu_hoa("khong co hoa"), 0)
        self.assertEqual(dem_chu_hoa("TOAN HOA"), 7)

    def test_cau2_doi_xung(self):
        """[Câu 2.b] Kiểm tra chuỗi đối xứng"""
        self.assertTrue(DoiXung("radar"))
        self.assertTrue(DoiXung("level"))
        self.assertFalse(DoiXung("python"))
        self.assertTrue(DoiXung("12321"))

    def test_cau2_tong_chu_so(self):
        """[Câu 2.c] Tính tổng các chữ số trong chuỗi"""
        self.assertEqual(tinh_tong_chu_so("abc123xyz45"), 15)  # 1+2+3+4+5
        self.assertEqual(tinh_tong_chu_so("khong co so"), 0)
        self.assertEqual(tinh_tong_chu_so("2026"), 10)  # 2+0+2+6

    # =========================================================================
    # CÂU 3
    # =========================================================================
    def test_cau3_tong_duong_chan(self):
        """[Câu 3.b] Tính tổng các số dương chẵn trong danh sách"""
        lst = [-4, -2, 0, 1, 2, 4, 5, 8]
        self.assertEqual(tong_duong_chan(lst), 14)  # 2 + 4 + 8 = 14
        self.assertEqual(tong_duong_chan([-3, -1, 5, 7]), 0)
        self.assertEqual(tong_duong_chan([]), 0)

    def test_cau3_dem_k(self):
        """[Câu 3.c] Đếm số lần xuất hiện của phần tử k"""
        lst = [1, 2, 5, 2, 8, 2, 9]
        self.assertEqual(dem_so_lan_xuat_hien(lst, 2), 3)
        self.assertEqual(dem_so_lan_xuat_hien(lst, 100), 0)

    # =========================================================================
    # CÂU 4
    # =========================================================================
    def test_cau4_xoa_sach(self):
        """[Câu 4.b] Xóa sách khỏi từ điển theo mã"""
        tudien = {
            "S01": ["Lap Trinh Python", "Nguyen Van A", "Giao Duc", 2023],
            "S02": ["Cau Truc Du Lieu", "Tran Van B", "KHKT", 2022],
        }
        # Xóa sách tồn tại
        kq1 = xoa_sach(tudien, "S01")
        self.assertTrue(kq1)
        self.assertNotIn("S01", tudien)
        # Xóa sách không tồn tại
        kq2 = xoa_sach(tudien, "S99")
        self.assertFalse(kq2)

    # =========================================================================
    # CÂU 5
    # =========================================================================
    def test_cau5_oop_dienthoai(self):
        """[Câu 5] Khởi tạo lớp DienThoai và kiểm tra thuộc tính"""
        dt = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
        self.assertEqual(dt.MaMay, "DT01")
        self.assertEqual(dt.TenMay, "iPhone 15 Pro")
        self.assertEqual(dt.HangSanXuat, "Apple")
        self.assertEqual(dt.DungLuongPin, 3274)
        self.assertEqual(dt.GiaBan, 28990000)
        self.assertTrue(hasattr(dt, "thongtindienthoai"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
