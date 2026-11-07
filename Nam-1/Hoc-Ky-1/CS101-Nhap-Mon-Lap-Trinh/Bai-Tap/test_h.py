import unittest
import sys
import os

# Đảm bảo mã hóa UTF-8 cho Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Thêm đường dẫn thư mục hiện tại để import h.py
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from h import (
    tong_uoc_so,
    tinh_tong_luy_thua,
    dem_chu_thuong,
    kiem_tra_doi_xung,
    chuyen_chu_hoa_dau_tu,
    loc_so_duong_chan,
)


class TestBaiTapPython(unittest.TestCase):
    def test_tong_uoc_so(self):
        """[Câu 1] Kiểm tra hàm tong_uoc_so(n)"""
        self.assertEqual(tong_uoc_so(6), 12, "Lỗi: Ước của 6 là 1+2+3+6=12")
        self.assertEqual(tong_uoc_so(1), 1, "Lỗi: Ước của 1 là 1")
        self.assertEqual(tong_uoc_so(0), 0, "Lỗi: n <= 0 phải trả về 0")

    def test_tinh_tong_luy_thua(self):
        """[Câu 2] Kiểm tra hàm tinh_tong_luy_thua(n)"""
        self.assertEqual(tinh_tong_luy_thua(1), 1, "Lỗi: S(1) = 1^1 = 1")
        self.assertEqual(tinh_tong_luy_thua(2), 5, "Lỗi: S(2) = 1 + 4 = 5")
        self.assertEqual(tinh_tong_luy_thua(3), 32, "Lỗi: S(3) = 1 + 4 + 27 = 32")

    def test_dem_chu_thuong(self):
        """[Câu 3] Kiểm tra hàm dem_chu_thuong(s)"""
        self.assertEqual(dem_chu_thuong("Python"), 5, "Lỗi: 'Python' có 5 chữ thường")
        self.assertEqual(dem_chu_thuong("PYTHON"), 0, "Lỗi: 'PYTHON' không có chữ thường")
        self.assertEqual(dem_chu_thuong("abc 123 !@#"), 3, "Lỗi: 'abc 123 !@#' có 3 chữ thường")

    def test_kiem_tra_doi_xung(self):
        """[Câu 4] Kiểm tra hàm kiem_tra_doi_xung(s)"""
        self.assertTrue(kiem_tra_doi_xung("radar"), "Lỗi: 'radar' là chuỗi đối xứng")
        self.assertTrue(kiem_tra_doi_xung("madam"), "Lỗi: 'madam' là chuỗi đối xứng")
        self.assertTrue(kiem_tra_doi_xung("A nut for a jar of tuna"), "Lỗi: 'A nut for a jar of tuna' là đối xứng")
        self.assertFalse(kiem_tra_doi_xung("python"), "Lỗi: 'python' không đối xứng")

    def test_chuyen_chu_hoa_dau_tu(self):
        """[Câu 5] Kiểm tra hàm chuyen_chu_hoa_dau_tu(s)"""
        self.assertEqual(chuyen_chu_hoa_dau_tu("lap trinh python"), "Lap Trinh Python")
        self.assertEqual(chuyen_chu_hoa_dau_tu("dai hoc"), "Dai Hoc")

    def test_loc_so_duong_chan(self):
        """[Câu 6] Kiểm tra hàm loc_so_duong_chan(list)"""
        self.assertEqual(loc_so_duong_chan([-4, -2, 0, 1, 2, 4, 5, 8]), [2, 4, 8])
        self.assertEqual(loc_so_duong_chan([-1, -3, 0]), [])
        self.assertEqual(loc_so_duong_chan([2, 4, 6]), [2, 4, 6])


if __name__ == "__main__":
    unittest.main(verbosity=2)
