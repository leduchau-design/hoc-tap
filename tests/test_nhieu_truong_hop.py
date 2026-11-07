# -*- coding: utf-8 -*-
"""
BÀI KIỂM THỬ ĐA TRƯỜNG HỢP (COMPREHENSIVE MULTI-CASE TEST SUITE)
Kiểm tra mở rộng nhiều bộ dữ liệu đầu vào (edge cases, typical cases, stress tests)
cho các hàm trong file h.py.

Hỗ trợ:
1. Tự động kiểm thử toàn bộ các bộ test với unittest (subTests).
2. Xuất bảng thống kê trực quan chi tiết từng trường hợp test.
3. Chế độ tương tác nhập input tùy chọn từ bàn phím (--nhap hoặc -i).
"""

import sys
import os
import unittest

# Đảm bảo hiển thị UTF-8 mượt mà trên console Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ưu tiên import h.py từ thư mục Bai-Tap nếu tồn tại
bai_tap_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Nam-1", "Hoc-Ky-1", "CS101-Nhap-Mon-Lap-Trinh", "Bai-Tap"))
if os.path.exists(bai_tap_dir) and bai_tap_dir not in sys.path:
    sys.path.insert(0, bai_tap_dir)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(1, root_dir)

try:
    from h import (
        tong_uoc_so,
        tinh_tong_luy_thua,
        dem_chu_thuong,
        kiem_tra_doi_xung,
        chuyen_chu_hoa_dau_tu,
        loc_so_duong_chan,
    )
except ImportError as e:
    print(f"❌ Không tìm thấy file h.py để kiểm thử: {e}")
    sys.exit(1)


# =============================================================================
# BỘ DỮ LIỆU KIỂM THỬ ĐA DẠNG (TEST CASES DATASET)
# =============================================================================

TEST_CASES = {
    "tong_uoc_so": [
        # (input_val, expected, mô tả)
        (1, 1, "Trường hợp biên: n = 1 (ước duy nhất là 1)"),
        (2, 3, "Số nguyên tố chẵn: n = 2 (ước 1, 2 -> tổng 3)"),
        (6, 12, "Số hoàn hảo nhỏ: n = 6 (ước 1, 2, 3, 6 -> tổng 12)"),
        (7, 8, "Số nguyên tố lẻ: n = 7 (ước 1, 7 -> tổng 8)"),
        (16, 31, "Lũy thừa của 2: n = 16 (ước 1, 2, 4, 8, 16 -> tổng 31)"),
        (25, 31, "Số chính phương lẻ: n = 25 (ước 1, 5, 25 -> tổng 31)"),
        (28, 56, "Số hoàn hảo: n = 28 (ước 1, 2, 4, 7, 14, 28 -> tổng 56)"),
        (100, 217, "Số hợp số lớn: n = 100 (ước 1, 2, 4, 5, 10, 20, 25, 50, 100)"),
        (0, 0, "Trường hợp biên không hợp lệ: n = 0 -> tổng 0"),
        (-15, 0, "Trường hợp số âm: n = -15 -> tổng 0"),
    ],

    "tinh_tong_luy_thua": [
        (1, 1, "n = 1: 1^1 = 1"),
        (2, 5, "n = 2: 1^1 + 2^2 = 1 + 4 = 5"),
        (3, 32, "n = 3: 1^1 + 2^2 + 3^3 = 1 + 4 + 27 = 32"),
        (4, 288, "n = 4: 32 + 4^4 = 32 + 256 = 288"),
        (5, 3413, "n = 5: 288 + 5^5 = 288 + 3125 = 3413"),
        (0, 0, "Trường hợp n = 0: không có số hạng nào -> trả về 0"),
        (-3, 0, "Trường hợp số âm: n = -3 -> trả về 0"),
    ],

    "dem_chu_thuong": [
        ("python", 6, "Toàn bộ là chữ in thường"),
        ("PYTHON", 0, "Toàn bộ là chữ in hoa"),
        ("Lap Trinh Python", 11, "Chuỗi hỗn hợp hoa và thường (chữ thường: a, p, r, i, n, h, y, t, h, o, n)"),
        ("", 0, "Chuỗi rỗng (không có ký tự nào)"),
        ("123456!@#$%^&*()", 0, "Chuỗi chỉ gồm số và ký tự đặc biệt"),
        ("a", 1, "Chuỗi chỉ có đúng 1 ký tự chữ thường"),
        ("Z", 0, "Chuỗi chỉ có đúng 1 ký tự chữ hoa"),
        ("hello   world   2026", 10, "Chuỗi có nhiều dấu cách và số"),
        ("Học Lập Trình", 8, "Chuỗi có tiếng Việt (các ký tự thường có dấu: ọ, c, ậ, p, r, ì, n, h)"),
    ],

    "kiem_tra_doi_xung": [
        ("radar", True, "Từ đối xứng kinh điển viết thường"),
        ("level", True, "Từ đối xứng độ dài lẻ"),
        ("noon", True, "Từ đối xứng độ dài chẵn"),
        ("Madam", True, "Từ đối xứng có lẫn chữ hoa chữ thường"),
        ("RaceCar", True, "Chữ hoa xen kẽ"),
        ("A nut for a jar of tuna", True, "Câu đối xứng có khoảng trắng"),
        ("Was it a car or a cat I saw", True, "Câu dài đối xứng có nhiều từ"),
        ("a", True, "Chuỗi đơn 1 ký tự luôn đối xứng"),
        ("", True, "Chuỗi rỗng coi như đối xứng"),
        ("python", False, "Chuỗi thông thường không đối xứng"),
        ("hello world", False, "Câu không đối xứng"),
        ("abcca", False, "Gần đối xứng nhưng khác ký tự giữa"),
    ],

    "chuyen_chu_hoa_dau_tu": [
        ("lap trinh python", "Lap Trinh Python", "Chuỗi thường nhiều từ chuẩn"),
        ("dai hoc quoc gia", "Dai Hoc Quoc Gia", "Cụm danh từ tiếng Việt không dấu"),
        ("python", "Python", "Từ đơn lẻ"),
        ("HELLO WORLD", "Hello World", "Chuỗi ban đầu toàn viết hoa"),
        ("Data Science", "Data Science", "Chuỗi đã được viết hoa chuẩn sẵn"),
        ("cau truc du lieu va giai thuat", "Cau Truc Du Lieu Va Giai Thuat", "Chuỗi dài nhiều từ"),
        ("", "", "Chuỗi rỗng giữ nguyên"),
    ],

    "loc_so_duong_chan": [
        ([-4, -2, 0, 1, 2, 4, 5, 8], [2, 4, 8], "Mảng hỗn hợp âm, dương, chẵn, lẻ và số 0"),
        ([-3, -1, 0, 5, 7, 9], [], "Mảng không chứa số dương chẵn nào"),
        ([-2, -4, -6, -8], [], "Mảng chỉ gồm số âm chẵn (không được lấy vì là số âm)"),
        ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], "Mảng toàn bộ là số dương chẵn"),
        ([0, 0, 0], [], "Mảng chỉ toàn số 0 (số 0 không phải số dương)"),
        ([], [], "Mảng rỗng ban đầu"),
        ([100, 101, 102, -100, 0, 50], [100, 102, 50], "Mảng có các số lớn"),
    ],
}


# =============================================================================
# HỘP BÁO LỖI VÀ CHỈ DẪN SỬA
# =============================================================================

def bao_loi_chi_tiet(ten_cau, vi_tri, input_val, output_val, expected_val, nguyen_nhan, cach_sua):
    border = "=" * 76
    return (
        f"\n{border}\n"
        f" ❌ PHÁT HIỆN LỖI SAI: {ten_cau}\n"
        f" 📍 Vị trí             : {vi_tri}\n"
        f" 📥 Input đầu vào      : {repr(input_val)}\n"
        f" 📤 Code tính ra       : {repr(output_val)}\n"
        f" 🎯 Kỳ vọng chính xác  : {repr(expected_val)}\n"
        f"{'-' * 76}\n"
        f" ⚠️ Nguyên nhân khả dĩ : {nguyen_nhan}\n"
        f" 💡 Gợi ý cách sửa     : {cach_sua}\n"
        f"{border}\n"
    )


# =============================================================================
# UNITTEST CLASS (HỖ TRỢ SUBTEST TỪNG TRƯỜNG HỢP)
# =============================================================================

class TestNhieuTruongHop(unittest.TestCase):
    """Bộ test tự động duyệt qua tất cả các input đa dạng."""

    def test_01_tong_uoc_so(self):
        """[Câu 1] Kiểm tra tong_uoc_so(n) qua nhiều trường hợp số học."""
        for n, expected, mo_ta in TEST_CASES["tong_uoc_so"]:
            with self.subTest(n=n, mo_ta=mo_ta):
                res = tong_uoc_so(n)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 1: tong_uoc_so ({mo_ta})",
                    vi_tri="h.py -> tong_uoc_so(n)",
                    input_val=f"n = {n}",
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Chưa duyệt đến n (cần range(1, n+1)) hoặc chưa xử lý n <= 0.",
                    cach_sua="if n <= 0: return 0; return sum(i for i in range(1, n + 1) if n % i == 0)"
                )
                self.assertEqual(res, expected, msg)

    def test_02_tinh_tong_luy_thua(self):
        """[Câu 2] Kiểm tra tinh_tong_luy_thua(n) với các bậc n khác nhau."""
        for n, expected, mo_ta in TEST_CASES["tinh_tong_luy_thua"]:
            with self.subTest(n=n, mo_ta=mo_ta):
                res = tinh_tong_luy_thua(n)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 2: tinh_tong_luy_thua ({mo_ta})",
                    vi_tri="h.py -> tinh_tong_luy_thua(n)",
                    input_val=f"n = {n}",
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Nhầm lẫn toán tử lũy thừa '**' thành '*' hoặc '^', hoặc chưa chặn n <= 0.",
                    cach_sua="if n <= 0: return 0; return sum(i ** i for i in range(1, n + 1))"
                )
                self.assertEqual(res, expected, msg)

    def test_03_dem_chu_thuong(self):
        """[Câu 3] Kiểm tra dem_chu_thuong(s) với các dạng chuỗi phong phú."""
        for s, expected, mo_ta in TEST_CASES["dem_chu_thuong"]:
            with self.subTest(s=s, mo_ta=mo_ta):
                res = dem_chu_thuong(s)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 3: dem_chu_thuong ({mo_ta})",
                    vi_tri="h.py -> dem_chu_thuong(s)",
                    input_val=s,
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Hàm đếm chưa dùng c.islower() hoặc bị lỗi khi gặp chuỗi rỗng / ký tự lạ.",
                    cach_sua="return sum(1 for c in s if c.islower())"
                )
                self.assertEqual(res, expected, msg)

    def test_04_kiem_tra_doi_xung(self):
        """[Câu 4] Kiểm tra kiem_tra_doi_xung(s) với nhiều loại palindrome."""
        for s, expected, mo_ta in TEST_CASES["kiem_tra_doi_xung"]:
            with self.subTest(s=s, mo_ta=mo_ta):
                res = kiem_tra_doi_xung(s)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 4: kiem_tra_doi_xung ({mo_ta})",
                    vi_tri="h.py -> kiem_tra_doi_xung(s)",
                    input_val=s,
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Chưa loại bỏ khoảng trắng bằng .replace(' ', '') hoặc chưa đưa về chữ thường bằng .lower().",
                    cach_sua="cleaned = s.replace(' ', '').lower(); return cleaned == cleaned[::-1]"
                )
                self.assertEqual(res, expected, msg)

    def test_05_chuyen_chu_hoa_dau_tu(self):
        """[Câu 5] Kiểm tra chuyen_chu_hoa_dau_tu(s) với các loại từ và cụm từ."""
        for s, expected, mo_ta in TEST_CASES["chuyen_chu_hoa_dau_tu"]:
            with self.subTest(s=s, mo_ta=mo_ta):
                res = chuyen_chu_hoa_dau_tu(s)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 5: chuyen_chu_hoa_dau_tu ({mo_ta})",
                    vi_tri="h.py -> chuyen_chu_hoa_dau_tu(s)",
                    input_val=s,
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Dùng hàm capitalize() (chỉ hoa chữ đầu câu) thay vì .title() (hoa mỗi từ).",
                    cach_sua="return s.title()"
                )
                self.assertEqual(res, expected, msg)

    def test_06_loc_so_duong_chan(self):
        """[Câu 6] Kiểm tra loc_so_duong_chan(list) với mọi dạng danh sách."""
        for lst, expected, mo_ta in TEST_CASES["loc_so_duong_chan"]:
            with self.subTest(lst=lst, mo_ta=mo_ta):
                res = loc_so_duong_chan(lst)
                msg = bao_loi_chi_tiet(
                    ten_cau=f"Câu 6: loc_so_duong_chan ({mo_ta})",
                    vi_tri="h.py -> loc_so_duong_chan(danh_sach)",
                    input_val=lst,
                    output_val=res,
                    expected_val=expected,
                    nguyen_nhan="Điều kiện sai: Cần đồng thời x > 0 và x % 2 == 0. (Không nhầm != 0, không nhầm >= 0).",
                    cach_sua="return [x for x in danh_sach if x > 0 and x % 2 == 0]"
                )
                self.assertEqual(res, expected, msg)


# =============================================================================
# CHẾ ĐỘ CHẠY BÁO CÁO TRỰC QUAN (VISUAL TEST REPORT)
# =============================================================================

def chay_bao_cao_truc_quan():
    """Chạy toàn bộ các test cases và in bảng biểu kết quả đẹp mắt."""
    print("=" * 80)
    print("      🧪 BÁO CÁO KIỂM THỬ ĐA TRƯỜNG HỢP (MULTI-CASE TEST SUITE) 🧪      ")
    print("=" * 80)

    ham_map = {
        "tong_uoc_so": (tong_uoc_so, "Câu 1: tong_uoc_so(n)"),
        "tinh_tong_luy_thua": (tinh_tong_luy_thua, "Câu 2: tinh_tong_luy_thua(n)"),
        "dem_chu_thuong": (dem_chu_thuong, "Câu 3: dem_chu_thuong(s)"),
        "kiem_tra_doi_xung": (kiem_tra_doi_xung, "Câu 4: kiem_tra_doi_xung(s)"),
        "chuyen_chu_hoa_dau_tu": (chuyen_chu_hoa_dau_tu, "Câu 5: chuyen_chu_hoa_dau_tu(s)"),
        "loc_so_duong_chan": (loc_so_duong_chan, "Câu 6: loc_so_duong_chan(list)"),
    }

    tong_so_test = 0
    tong_so_pass = 0

    for key, (func, ten_hien_thi) in ham_map.items():
        cases = TEST_CASES[key]
        so_pass_cau = 0
        so_test_cau = len(cases)
        tong_so_test += so_test_cau

        print(f"\n📌 {ten_hien_thi} [{so_test_cau} trường hợp thử nghiệm]")
        print("-" * 80)

        for idx, (inp, exp, mo_ta) in enumerate(cases, 1):
            try:
                # Nếu input là list, truyền copy để tránh hàm sửa inplace
                if isinstance(inp, list):
                    actual = func(list(inp))
                else:
                    actual = func(inp)

                is_pass = (actual == exp)
                if is_pass:
                    so_pass_cau += 1
                    tong_so_pass += 1
                    icon = "✅ ĐẠT "
                    detail = f"Input: {str(inp):<24} -> Kết quả: {str(actual)}"
                else:
                    icon = "❌ SAI "
                    detail = f"Input: {str(inp):<24} -> Ra: {str(actual)} | Kỳ vọng: {str(exp)}"

                print(f"  [{idx:02d}] {icon} | {detail}")
            except Exception as e:
                print(f"  [{idx:02d}] 💥 LỖI | Input: {str(inp):<24} -> Ngoại lệ: {e}")

        # Tổng kết câu
        tile = (so_pass_cau / so_test_cau) * 100
        print(f"  👉 Kết quả: {so_pass_cau}/{so_test_cau} test case vượt qua ({tile:.0f}%)")

    print("\n" + "=" * 80)
    ty_le_tong = (tong_so_pass / tong_so_test) * 100
    print(f"📊 TỔNG KẾT BÀI THỬ NGHIỆM: {tong_so_pass}/{tong_so_test} ca kiểm thử ĐẠT ({ty_le_tong:.1f}%)")
    if tong_so_pass == tong_so_test:
        print("🎉 TUYỆT VỜI! MÃ NGUỒN ĐÃ VƯỢT QUA TOÀN BỘ CÁC TRƯỜNG HỢP KIỂM THỬ TỪ ĐƠN GIẢN ĐẾN ĐẶC BIỆT!")
    else:
        print(f"⚠️ CÒN {tong_so_test - tong_so_pass} TRƯỜNG HỢP BỊ SAI. HÃY KIỂM TRA LẠI LOG CHI TIẾT PHÍA TRÊN!")
    print("=" * 80)


# =============================================================================
# CHẾ ĐỘ TƯƠNG TÁC (CHO PHÉP BẠN TỰ NHẬP INPUT BẤT KỲ ĐỂ TEST TRỰC TIẾP)
# =============================================================================

def che_do_nhap_tu_do():
    """Cho phép người dùng tự tay nhập input từ bàn phím để kiểm tra hàm."""
    print("\n" + "=" * 70)
    print("🎮 CHẾ ĐỘ THỬ NGHIỆM INPUT TỰ DO TỪ BÀN PHÍM")
    print("Nhập giá trị bất kỳ để xem hàm trong h.py xử lý ra kết quả gì!")
    print("=" * 70)

    menu = (
        "1. Test câu 1: tong_uoc_so(n)        (Nhập một số nguyên n)\n"
        "2. Test câu 2: tinh_tong_luy_thua(n) (Nhập một số nguyên n)\n"
        "3. Test câu 3: dem_chu_thuong(s)     (Nhập chuỗi ký tự)\n"
        "4. Test câu 4: kiem_tra_doi_xung(s)  (Nhập chuỗi cần kiểm tra)\n"
        "5. Test câu 5: chuyen_chu_hoa_dau_tu (Nhập chuỗi cần viết hoa)\n"
        "6. Test câu 6: loc_so_duong_chan     (Nhập các số cách nhau bởi dấu cách)\n"
        "0. Thoát chế độ tương tác\n"
    )

    while True:
        print("\n" + menu)
        chon = input("👉 Chọn chức năng bạn muốn test (0-6): ").strip()
        if chon == "0":
            print("Tạm biệt!")
            break

        if chon == "1":
            raw = input("Nhập số nguyên n: ").strip()
            try:
                val = int(raw)
                kq = tong_uoc_so(val)
                # Tính chuẩn để đối chiếu
                uoc = [i for i in range(1, val + 1) if val % i == 0] if val > 0 else []
                chuan = sum(uoc)
                print(f"  📤 Hàm của bạn trả về : {kq}")
                print(f"  🎯 Đáp án chuẩn        : {chuan} (các ước: {uoc})")
                print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")
            except ValueError:
                print("⚠️ Giá trị nhập không phải số nguyên hợp lệ!")

        elif chon == "2":
            raw = input("Nhập số nguyên n (khuyên chọn n <= 8): ").strip()
            try:
                val = int(raw)
                kq = tinh_tong_luy_thua(val)
                chuan = sum(i ** i for i in range(1, val + 1)) if val > 0 else 0
                print(f"  📤 Hàm của bạn trả về : {kq}")
                print(f"  🎯 Đáp án chuẩn        : {chuan}")
                print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")
            except ValueError:
                print("⚠️ Giá trị nhập không phải số nguyên!")

        elif chon == "3":
            raw = input("Nhập chuỗi bất kỳ: ")
            kq = dem_chu_thuong(raw)
            chuan = sum(1 for c in raw if c.islower())
            chu_thuong_tim_thay = [c for c in raw if c.islower()]
            print(f"  📤 Hàm của bạn trả về : {kq}")
            print(f"  🎯 Đáp án chuẩn        : {chuan} (Ký tự: {chu_thuong_tim_thay})")
            print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")

        elif chon == "4":
            raw = input("Nhập chuỗi cần kiểm tra đối xứng: ")
            kq = kiem_tra_doi_xung(raw)
            clean = raw.replace(" ", "").lower()
            chuan = (clean == clean[::-1])
            print(f"  📤 Chuỗi sau chuẩn hóa : '{clean}' (đảo ngược: '{clean[::-1]}')")
            print(f"  📤 Hàm của bạn trả về : {kq}")
            print(f"  🎯 Đáp án chuẩn        : {chuan}")
            print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")

        elif chon == "5":
            raw = input("Nhập chuỗi cần chuyển chữ hoa đầu từ: ")
            kq = chuyen_chu_hoa_dau_tu(raw)
            chuan = raw.title()
            print(f"  📤 Hàm của bạn trả về : '{kq}'")
            print(f"  🎯 Đáp án chuẩn        : '{chuan}'")
            print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")

        elif chon == "6":
            raw = input("Nhập dãy số cách nhau bởi khoảng trắng (vd: -2 0 1 4 8 9): ")
            try:
                lst = [int(x) for x in raw.split()]
                kq = loc_so_duong_chan(lst)
                chuan = [x for x in lst if x > 0 and x % 2 == 0]
                print(f"  📥 Mảng đầu vào        : {lst}")
                print(f"  📤 Hàm của bạn trả về : {kq}")
                print(f"  🎯 Đáp án chuẩn        : {chuan}")
                print(f"  Trạng thái: {'✅ CHÍNH XÁC' if kq == chuan else '❌ SAI RỒI'}")
            except ValueError:
                print("⚠️ Dãy nhập có chứa phần tử không phải số nguyên!")


if __name__ == "__main__":
    # Nếu chạy với cờ -i hoặc --nhap -> mở menu nhập liệu tự do
    if len(sys.argv) > 1 and sys.argv[1] in ("-i", "--interactive", "--nhap", "nhap"):
        che_do_nhap_tu_do()
    elif len(sys.argv) > 1 and sys.argv[1] in ("-u", "--unittest"):
        # Chạy chuẩn unittest runner
        unittest.main(argv=[sys.argv[0]] + sys.argv[2:])
    else:
        # Mặc định chạy bảng báo cáo trực quan
        chay_bao_cao_truc_quan()
