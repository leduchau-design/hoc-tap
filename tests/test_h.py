import unittest
import sys
import os

# Thêm đường dẫn thư mục gốc để import h.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
        # Ước của 6 là 1, 2, 3, 6 -> tổng = 12
        self.assertEqual(tong_uoc_so(6), 12)
        # Ước của 1 là 1 -> tổng = 1
        self.assertEqual(tong_uoc_so(1), 1)
        # Số <= 0
        self.assertEqual(tong_uoc_so(0), 0)

    def test_tinh_tong_luy_thua(self):
        # S(1) = 1^1 = 1
        self.assertEqual(tinh_tong_luy_thua(1), 1)
        # S(2) = 1^1 + 2^2 = 1 + 4 = 5
        self.assertEqual(tinh_tong_luy_thua(2), 5)
        # S(3) = 1 + 4 + 27 = 32
        self.assertEqual(tinh_tong_luy_thua(3), 32)

    def test_dem_chu_thuong(self):
        self.assertEqual(dem_chu_thuong("Python"), 5)
        self.assertEqual(dem_chu_thuong("PYTHON"), 0)
        self.assertEqual(dem_chu_thuong("abc 123 !@#"), 3)

    def test_kiem_tra_doi_xung(self):
        self.assertTrue(kiem_tra_doi_xung("radar"))
        self.assertTrue(kiem_tra_doi_xung("madam"))
        self.assertTrue(kiem_tra_doi_xung("A nut for a jar of tuna"))
        self.assertFalse(kiem_tra_doi_xung("python"))

    def test_chuyen_chu_hoa_dau_tu(self):
        self.assertEqual(chuyen_chu_hoa_dau_tu("lap trinh python"), "Lap Trinh Python")
        self.assertEqual(chuyen_chu_hoa_dau_tu("dai hoc"), "Dai Hoc")

    def test_loc_so_duong_chan(self):
        self.assertEqual(loc_so_duong_chan([-4, -2, 0, 1, 2, 4, 5, 8]), [2, 4, 8])
        self.assertEqual(loc_so_duong_chan([-1, -3, 0]), [])
        self.assertEqual(loc_so_duong_chan([2, 4, 6]), [2, 4, 6])


if __name__ == "__main__":
    unittest.main()
