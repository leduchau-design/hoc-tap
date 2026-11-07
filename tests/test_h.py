import unittest
import sys
import os

# Đảm bảo tiếng Việt hiển thị đẹp trên Windows Console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Thêm đường dẫn thư mục gốc để nạp file h.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from h import (
    tong_uoc_so,
    tinh_tong_luy_thua,
    dem_chu_thuong,
    kiem_tra_doi_xung,
    chuyen_chu_hoa_dau_tu,
    loc_so_duong_chan,
)


def bao_loi_chi_tiet(ten_cau, vi_tri, input_val, output_val, expected_val, nguyen_nhan, cach_sua, code_mau=""):
    """Tạo hộp thoại chỉ dẫn lỗi sai và hướng dẫn cách sửa chi tiết."""
    border = "=" * 76
    msg = [
        "",
        border,
        f" ❌ PHÁT HIỆN LỖI SAI TẠI: {ten_cau}",
        "-" * 76,
        f" 📍 Vị trí lỗi        : {vi_tri}",
        f" 📥 Dữ liệu thử nghiệm : {input_val}",
        f" 📤 Code bạn tính ra   : {output_val}",
        f" 🎯 Đáp án chuẩn kỳ vọng: {expected_val}",
        "-" * 76,
        f" ⚠️ Phân tích nguyên nhân: {nguyen_nhan}",
        f" 💡 HƯỚNG DẪN CÁCH SỬA:",
        f"    {cach_sua}",
    ]
    if code_mau:
        msg.append(" 📝 Code mẫu gợi ý:")
        for line in code_mau.strip().split("\n"):
            msg.append(f"    {line}")
    msg.append(border)
    return "\n".join(msg)


class TestBaiTapPython(unittest.TestCase):

    def test_tong_uoc_so(self):
        """[Câu 1] Kiểm tra hàm tong_uoc_so(n)"""
        # Test 1.1: n = 6
        res = tong_uoc_so(6)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 1] Tính tổng ước số của n",
            vi_tri="File h.py -> hàm tong_uoc_so(n)",
            input_val="n = 6",
            output_val=res,
            expected_val="12 (vì các ước của 6 là 1, 2, 3, 6 -> 1 + 2 + 3 + 6 = 12)",
            nguyen_nhan="Có thể vòng lặp chỉ chạy range(1, n) nên bỏ sót chính số n (ước lớn nhất).",
            cach_sua="Sửa vòng lặp thành range(1, n + 1) để duyệt tính luôn cả số n.",
            code_mau="def tong_uoc_so(n):\n    if n <= 0: return 0\n    return sum(i for i in range(1, n + 1) if n % i == 0)"
        )
        self.assertEqual(res, 12, msg)

        # Test 1.2: n <= 0
        res_0 = tong_uoc_so(0)
        msg_0 = bao_loi_chi_tiet(
            ten_cau="[Câu 1] Tính tổng ước số khi n <= 0",
            vi_tri="File h.py -> hàm tong_uoc_so(n)",
            input_val="n = 0 hoặc n < 0",
            output_val=res_0,
            expected_val="0 (số không hoặc số âm không có ước nguyên dương)",
            nguyen_nhan="Hàm chưa có điều kiện chặn trường hợp n <= 0.",
            cach_sua="Thêm dòng 'if n <= 0: return 0' vào đầu hàm.",
            code_mau="if n <= 0:\n    return 0"
        )
        self.assertEqual(res_0, 0, msg_0)

    def test_tinh_tong_luy_thua(self):
        """[Câu 2] Kiểm tra hàm tinh_tong_luy_thua(n)"""
        res = tinh_tong_luy_thua(3)
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 2] Tính S(n) = 1^1 + 2^2 + 3^3 + ... + n^n",
            vi_tri="File h.py -> hàm tinh_tong_luy_thua(n)",
            input_val="n = 3",
            output_val=res,
            expected_val="32 (vì 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32)",
            nguyen_nhan="Bạn có thể đã dùng nhầm toán tử nhân 'i * i' hoặc mũ '^' thay vì lũy thừa '**'.",
            cach_sua="Trong Python, phép tính lũy thừa là dấu '**' (ví dụ i ** i).",
            code_mau="def tinh_tong_luy_thua(n):\n    return sum(i ** i for i in range(1, n + 1))"
        )
        self.assertEqual(res, 32, msg)

    def test_dem_chu_thuong(self):
        """[Câu 3] Kiểm tra hàm dem_chu_thuong(s)"""
        res = dem_chu_thuong("Python")
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 3] Đếm số ký tự chữ in thường trong chuỗi",
            vi_tri="File h.py -> hàm dem_chu_thuong(s)",
            input_val="s = 'Python'",
            output_val=res,
            expected_val="5 (chuỗi 'Python' có 5 chữ thường: y, t, h, o, n)",
            nguyen_nhan="Hàm đếm nhầm cả chữ hoa hoặc logic đếm chưa chính xác.",
            cach_sua="Duyệt từng ký tự c trong s và kiểm tra bằng c.islower().",
            code_mau="def dem_chu_thuong(s):\n    return sum(1 for c in s if c.islower())"
        )
        self.assertEqual(res, 5, msg)

    def test_kiem_tra_doi_xung(self):
        """[Câu 4] Kiểm tra hàm kiem_tra_doi_xung(s)"""
        # Test đối xứng có khoảng trắng
        res = kiem_tra_doi_xung("A nut for a jar of tuna")
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 4] Kiểm tra chuỗi đối xứng (Palindrome)",
            vi_tri="File h.py -> hàm kiem_tra_doi_xung(s)",
            input_val="s = 'A nut for a jar of tuna'",
            output_val=res,
            expected_val="True (đọc xuôi hay ngược đều giống nhau nếu bỏ khoảng trắng)",
            nguyen_nhan="Bạn chưa loại bỏ khoảng trắng hoặc chưa chuyển về chữ thường trước khi so sánh ngược.",
            cach_sua="Làm sạch chuỗi bằng s.replace(' ', '').lower() rồi so sánh với chuỗi đảo ngược [::-1].",
            code_mau="def kiem_tra_doi_xung(s):\n    cleaned = s.replace(' ', '').lower()\n    return cleaned == cleaned[::-1]"
        )
        self.assertTrue(res, msg)

    def test_chuyen_chu_hoa_dau_tu(self):
        """[Câu 5] Kiểm tra hàm chuyen_chu_hoa_dau_tu(s)"""
        res = chuyen_chu_hoa_dau_tu("lap trinh python")
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 5] Đổi ký tự đầu tiên của MỖI TỪ thành chữ hoa",
            vi_tri="File h.py -> hàm chuyen_chu_hoa_dau_tu(s)",
            input_val="s = 'lap trinh python'",
            output_val=res,
            expected_val="'Lap Trinh Python'",
            nguyen_nhan="Bạn có thể đã dùng s.capitalize() (chỉ viết hoa chữ đầu câu) thay vì viết hoa mỗi từ.",
            cach_sua="Sử dụng hàm s.title() trong Python để viết hoa đầu TẤT CẢ các từ.",
            code_mau="def chuyen_chu_hoa_dau_tu(s):\n    return s.title()"
        )
        self.assertEqual(res, "Lap Trinh Python", msg)

    def test_loc_so_duong_chan(self):
        """[Câu 6] Kiểm tra hàm loc_so_duong_chan(list)"""
        res = loc_so_duong_chan([-4, -2, 0, 1, 2, 4, 5, 8])
        msg = bao_loi_chi_tiet(
            ten_cau="[Câu 6] Lọc các số nguyên dương chẵn",
            vi_tri="File h.py -> hàm loc_so_duong_chan(danh_sach)",
            input_val="[-4, -2, 0, 1, 2, 4, 5, 8]",
            output_val=res,
            expected_val="[2, 4, 8]",
            nguyen_nhan="Có thể bạn lấy nhầm số 0 (số 0 không phải số dương) hoặc lấy nhầm số âm chẵn (-4, -2).",
            cach_sua="Điều kiện lọc phải thỏa mãn cả 2 ý: x > 0 và x % 2 == 0.",
            code_mau="def loc_so_duong_chan(danh_sach):\n    return [x for x in danh_sach if x > 0 and x % 2 == 0]"
        )
        self.assertEqual(res, [2, 4, 8], msg)


if __name__ == "__main__":
    unittest.main(verbosity=2)
