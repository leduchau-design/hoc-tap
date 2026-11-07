# -*- coding: utf-8 -*-
"""
BỘ KIỂM THỬ TỰ ĐỘNG THÔNG MINH CHO ĐỀ THI SỐ 1 (MÃ ĐỀ: 11301)
Kiểm tra tính chính xác của toàn bộ các hàm trong 5 câu hỏi Đề 1.
TỰ ĐỘNG BÁO LỖI SAI CHI TIẾT: Vị trí lỗi, dữ liệu đầu vào, kết quả tính ra,
đáp án chuẩn, phân tích nguyên nhân và gợi ý cách sửa cụ thể.
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

try:
    from cau1 import DemChuSoLe, S
    from cau2 import dem_chu_hoa, DoiXung, tinh_tong_chu_so
    from cau3 import tong_duong_chan, dem_so_lan_xuat_hien
    from cau4 import xoa_sach
    from cau5 import DienThoai
except ImportError as e:
    print(f"❌ Không thể nạp các file câu hỏi của Đề 1: {e}")
    sys.exit(1)


def bao_loi_chi_tiet(ten_cau, vi_tri, input_val, output_val, expected_val, nguyen_nhan, cach_sua):
    """Tạo hộp thoại chỉ dẫn lỗi sai thông minh và hướng dẫn sửa."""
    border = "=" * 76
    return (
        f"\n{border}\n"
        f" ❌ PHÁT HIỆN LỖI SAI TẠI: {ten_cau}\n"
        f" 📍 Vị trí lỗi        : {vi_tri}\n"
        f" 📥 Dữ liệu thử nghiệm : {input_val}\n"
        f" 📤 Code bạn tính ra   : {output_val}\n"
        f" 🎯 Đáp án chuẩn kỳ vọng: {expected_val}\n"
        f"{'-' * 76}\n"
        f" ⚠️ Phân tích nguyên nhân: {nguyen_nhan}\n"
        f" 💡 HƯỚNG DẪN CÁCH SỬA:\n"
        f"    {cach_sua}\n"
        f"{border}\n"
    )


class TestDeThi1(unittest.TestCase):
    """Kiểm thử tự động các chức năng trong Đề 1."""

    # =========================================================================
    # CÂU 1 (cau1.py)
    # =========================================================================
    def test_cau1_dem_chu_so_le(self):
        """[Câu 1.b] Đếm chữ số lẻ của số nguyên dương n"""
        res = DemChuSoLe(635)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 1.b] Đếm số lượng chữ số lẻ của số nguyên dương n",
            vi_tri="cau1.py -> hàm DemChuSoLe(n)",
            input_val="n = 635",
            output_val=res,
            expected_val="2 (vì số 635 có 2 chữ số lẻ là 3 và 5)",
            nguyen_nhan="Có thể điều kiện chia dư số lẻ bị nhầm thành cs % 2 == 0 hoặc quên bước chia nguyên n //= 10.",
            cach_sua="Duyệt từng chữ số: if (tam % 10) % 2 != 0: dem += 1 sau đó tam //= 10."
        )
        self.assertEqual(res, 2, msg)

        res2 = DemChuSoLe(2468)
        msg2 = bao_loi_chi_tiet(
            ten_cau="[Câu 1.b] Đếm chữ số lẻ khi n toàn số chẵn",
            vi_tri="cau1.py -> hàm DemChuSoLe(n)",
            input_val="n = 2468",
            output_val=res2,
            expected_val="0 (không có chữ số lẻ nào)",
            nguyen_nhan="Hàm đếm nhầm số chẵn thành số lẻ.",
            cach_sua="Kiểm tra điều kiện: cs % 2 != 0 mới tăng biến đếm."
        )
        self.assertEqual(res2, 0, msg2)

    def test_cau1_tinh_tong_s(self):
        """[Câu 1.c] Tính tổng S = 1/2 + 1/4 + ... + 1/(2n)"""
        res = S(2)
        expected = 0.75  # 1/2 + 1/4 = 0.5 + 0.25 = 0.75
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 1.c] Tính tổng S = 1/2 + 1/4 + ... + 1/(2n)",
            vi_tri="cau1.py -> hàm S(n)",
            input_val="n = 2",
            output_val=res,
            expected_val=f"{expected} (1/2 + 1/4 = 0.75)",
            nguyen_nhan="Công thức mẫu số bị nhầm (cần 2*i) hoặc vòng lặp range chưa chạy đến n (cần range(1, n+1)).",
            cach_sua="Dùng vòng lặp: for i in range(1, n + 1): s += 1 / (2 * i)."
        )
        self.assertAlmostEqual(res, expected, places=5, msg=msg)

    # =========================================================================
    # CÂU 2 (cau2.py)
    # =========================================================================
    def test_cau2_dem_chu_hoa(self):
        """[Câu 2.a] Đếm số ký tự in hoa trong chuỗi"""
        s = "Lap Trinh Python"
        res = dem_chu_hoa(s)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 2.a] Đếm số lượng ký tự chữ hoa trong chuỗi",
            vi_tri="cau2.py -> hàm dem_chu_hoa(s)",
            input_val=f"s = '{s}'",
            output_val=res,
            expected_val="3 (các chữ hoa gồm: 'L', 'T', 'P')",
            nguyen_nhan="Chưa dùng c.isupper() hoặc điều kiện đếm chưa chính xác.",
            cach_sua="Duyệt từng ký tự c trong chuỗi s: if c.isupper(): dem += 1."
        )
        self.assertEqual(res, 3, msg)

    def test_cau2_doi_xung(self):
        """[Câu 2.b] Kiểm tra chuỗi đối xứng"""
        res_true = DoiXung("radar")
        msg_true = bao_loi_chi_tiet(
            ten_cau="[Câu 2.b] Kiểm tra chuỗi đối xứng (trường hợp đối xứng)",
            vi_tri="cau2.py -> hàm DoiXung(s)",
            input_val="s = 'radar'",
            output_val=res_true,
            expected_val="True (chuỗi đọc xuôi ngược như nhau)",
            nguyen_nhan="Logic so sánh đảo ngược chuỗi chưa đúng.",
            cach_sua="So sánh trực tiếp: return s == s[::-1]."
        )
        self.assertTrue(res_true, msg_true)

        res_false = DoiXung("python")
        msg_false = bao_loi_chi_tiet(
            ten_cau="[Câu 2.b] Kiểm tra chuỗi đối xứng (trường hợp không đối xứng)",
            vi_tri="cau2.py -> hàm DoiXung(s)",
            input_val="s = 'python'",
            output_val=res_false,
            expected_val="False",
            nguyen_nhan="Hàm trả về True cho chuỗi không đối xứng.",
            cach_sua="return s == s[::-1]."
        )
        self.assertFalse(res_false, msg_false)

    def test_cau2_tong_chu_so(self):
        """[Câu 2.c] Tính tổng các chữ số trong chuỗi"""
        s = "abc123xyz45"
        res = tinh_tong_chu_so(s)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 2.c] Tính tổng các chữ số xuất hiện trong chuỗi",
            vi_tri="cau2.py -> hàm tinh_tong_chu_so(s)",
            input_val=f"s = '{s}'",
            output_val=res,
            expected_val="15 (1 + 2 + 3 + 4 + 5 = 15)",
            nguyen_nhan="Chưa ép kiểu int(c) khi cộng dồn (bị nối chuỗi) hoặc chưa kiểm tra c.isdigit().",
            cach_sua="Duyệt: if c.isdigit(): tong += int(c)."
        )
        self.assertEqual(res, 15, msg)

    # =========================================================================
    # CÂU 3 (cau3.py)
    # =========================================================================
    def test_cau3_tong_duong_chan(self):
        """[Câu 3.b] Tính tổng các số dương chẵn trong danh sách"""
        lst = [-4, -2, 0, 1, 2, 4, 5, 8]
        res = tong_duong_chan(lst)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 3.b] Tính tổng các số dương chẵn trong danh sách",
            vi_tri="cau3.py -> hàm tong_duong_chan(danhsach)",
            input_val=f"danhsach = {lst}",
            output_val=res,
            expected_val="14 (chỉ tính 2 + 4 + 8 = 14; bỏ qua số 0 và các số âm -4, -2)",
            nguyen_nhan="Lấy nhầm số âm chẵn (-4, -2) hoặc lấy nhầm số 0, hoặc kiểm tra sai điều kiện chẵn lẻ.",
            cach_sua="Điều kiện phải thỏa mãn: if i > 0 and i % 2 == 0: tong += i."
        )
        self.assertEqual(res, 14, msg)

    def test_cau3_dem_k(self):
        """[Câu 3.c] Đếm số lần xuất hiện của phần tử k"""
        lst = [1, 2, 5, 2, 8, 2, 9]
        res = dem_so_lan_xuat_hien(lst, 2)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 3.c] Đếm số lần xuất hiện của k trong danh sách",
            vi_tri="cau3.py -> hàm dem_so_lan_xuat_hien(danhsach, k)",
            input_val=f"danhsach = {lst}, k = 2",
            output_val=res,
            expected_val="3 (số 2 xuất hiện 3 lần)",
            nguyen_nhan="Biến đếm chưa tăng khi phần tử bằng k hoặc chưa duyệt hết danh sách.",
            cach_sua="Duyệt: for i in danhsach: if i == k: dem += 1; return dem."
        )
        self.assertEqual(res, 3, msg)

    # =========================================================================
    # CÂU 4 (cau4.py)
    # =========================================================================
    def test_cau4_xoa_sach(self):
        """[Câu 4.b] Xóa sách khỏi từ điển theo mã"""
        tudien = {
            "S01": ["Lap Trinh Python", "Nguyen Van A", "Giao Duc", 2023],
            "S02": ["Cau Truc Du Lieu", "Tran Van B", "KHKT", 2022],
        }
        res = xoa_sach(tudien, "S01")
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 4.b] Xóa sách theo mã khỏi từ điển",
            vi_tri="cau4.py -> hàm xoa_sach(tudien, ma)",
            input_val="tudien có mã 'S01', cần xóa 'S01'",
            output_val=f"Kết quả trả về: {res}, Từ điển còn: {list(tudien.keys())}",
            expected_val="Trả về True và 'S01' phải biến mất khỏi từ điển",
            nguyen_nhan="Chưa dùng 'del tudien[ma]' hoặc chưa kiểm tra 'if ma in tudien:'.",
            cach_sua="if ma in tudien: del tudien[ma]; return True; else: return False."
        )
        self.assertTrue(res and "S01" not in tudien, msg)

    # =========================================================================
    # CÂU 5 (cau5.py)
    # =========================================================================
    def test_cau5_oop_dienthoai(self):
        """[Câu 5] Khởi tạo lớp DienThoai và kiểm tra thuộc tính"""
        try:
            dt = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
            valid = (
                dt.MaMay == "DT01" and
                dt.TenMay == "iPhone 15 Pro" and
                dt.HangSanXuat == "Apple" and
                dt.DungLuongPin == 3274 and
                dt.GiaBan == 28990000 and
                hasattr(dt, "thongtindienthoai")
            )
        except Exception as e:
            valid = False

        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 5] Khởi tạo lớp DienThoai và phương thức thongtindienthoai",
            vi_tri="cau5.py -> class DienThoai",
            input_val="DT01, iPhone 15 Pro, Apple, 3274, 28990000",
            output_val="Thuộc tính hoặc phương thức bị thiếu / sai tên",
            expected_val="Lớp DienThoai có 5 thuộc tính: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan và phương thức thongtindienthoai()",
            nguyen_nhan="Khai báo sai tên thuộc tính (chú ý chữ hoa/thường) hoặc hàm __init__ thiếu tham số self.",
            cach_sua="def __init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan):\n    self.MaMay = MaMay\n    self.TenMay = TenMay\n    self.HangSanXuat = HangSanXuat\n    self.DungLuongPin = DungLuongPin\n    self.GiaBan = GiaBan"
        )
        self.assertTrue(valid, msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
