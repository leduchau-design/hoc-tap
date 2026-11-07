#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG CHẤM ĐIỂM BÀI TẬP PYTHON TỰ ĐỘNG (AUTO-GRADER)
Thang điểm: 10.0 điểm
Tự động kiểm tra các hàm trong h.py và xuất bảng điểm chi tiết.
"""

import sys
import os
import time

# Đảm bảo mã hóa UTF-8 cho console Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def cham_bai():
    print("=" * 72)
    print("       🎓 HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG BÀI TẬP PYTHON - HỌC TẬP 🎓       ")
    print("=" * 72)
    print(f"[*] Đang nạp mã nguồn từ file 'h.py'...")
    time.sleep(0.3)

    try:
        import h
    except ImportError as e:
        print(f"\n[❌ LỖI NGHIÊM TRỌNG] Không thể import file 'h.py': {e}")
        print("Vui lòng đảm bảo file 'h.py' nằm cùng thư mục với file chấm điểm.")
        return 0.0

    tong_diem = 0.0
    diem_toi_da = 10.0
    ket_qua_chi_tiet = []

    # =========================================================================
    # CÂU 1: Tính tổng ước số (2.0 điểm)
    # =========================================================================
    ten_cau = "Câu 1: Hàm tong_uoc_so(n)"
    diem_cau = 0.0
    max_cau = 2.0
    ly_do = []

    if hasattr(h, "tong_uoc_so"):
        try:
            # Test 1.1: n = 6 -> ước: 1, 2, 3, 6 -> 12 (0.7đ)
            if h.tong_uoc_so(6) == 12:
                diem_cau += 0.7
            else:
                ly_do.append("Sai với n=6 (kỳ vọng 12)")

            # Test 1.2: n = 28 -> ước: 1, 2, 4, 7, 14, 28 -> 56 (0.7đ)
            if h.tong_uoc_so(28) == 56:
                diem_cau += 0.7
            else:
                ly_do.append("Sai với n=28 (kỳ vọng 56)")

            # Test 1.3: n = 0 hoặc n < 0 (0.6đ)
            if h.tong_uoc_so(0) == 0 and h.tong_uoc_so(-5) == 0:
                diem_cau += 0.6
            else:
                ly_do.append("Sai với n<=0 (kỳ vọng 0)")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm tong_uoc_so(n)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # CÂU 2: Tính tổng lũy thừa S(n) = 1^1 + 2^2 + ... + n^n (2.0 điểm)
    # =========================================================================
    ten_cau = "Câu 2: Hàm tinh_tong_luy_thua(n)"
    diem_cau = 0.0
    max_cau = 2.0
    ly_do = []

    if hasattr(h, "tinh_tong_luy_thua"):
        try:
            # Test 2.1: n = 1 -> 1 (0.6đ)
            if h.tinh_tong_luy_thua(1) == 1:
                diem_cau += 0.6
            else:
                ly_do.append("Sai với n=1 (kỳ vọng 1)")

            # Test 2.2: n = 3 -> 1 + 4 + 27 = 32 (0.7đ)
            if h.tinh_tong_luy_thua(3) == 32:
                diem_cau += 0.7
            else:
                ly_do.append("Sai với n=3 (kỳ vọng 32)")

            # Test 2.3: n = 4 -> 32 + 256 = 288 (0.7đ)
            if h.tinh_tong_luy_thua(4) == 288:
                diem_cau += 0.7
            else:
                ly_do.append("Sai với n=4 (kỳ vọng 288)")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm tinh_tong_luy_thua(n)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # CÂU 3: Đếm số ký tự in thường (1.5 điểm)
    # =========================================================================
    ten_cau = "Câu 3: Hàm dem_chu_thuong(s)"
    diem_cau = 0.0
    max_cau = 1.5
    ly_do = []

    if hasattr(h, "dem_chu_thuong"):
        try:
            # Test 3.1: "Python" -> 5 (0.5đ)
            if h.dem_chu_thuong("Python") == 5:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với chuỗi 'Python'")

            # Test 3.2: "PYTHON 123" -> 0 (0.5đ)
            if h.dem_chu_thuong("PYTHON 123") == 0:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với chuỗi toàn in hoa 'PYTHON 123'")

            # Test 3.3: "abc XYZ @#$" -> 3 (0.5đ)
            if h.dem_chu_thuong("abc XYZ @#$") == 3:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với chuỗi hỗn hợp 'abc XYZ @#$'")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm dem_chu_thuong(s)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # CÂU 4: Kiểm tra chuỗi đối xứng (1.5 điểm)
    # =========================================================================
    ten_cau = "Câu 4: Hàm kiem_tra_doi_xung(s)"
    diem_cau = 0.0
    max_cau = 1.5
    ly_do = []

    if hasattr(h, "kiem_tra_doi_xung"):
        try:
            # Test 4.1: "radar" -> True (0.5đ)
            if h.kiem_tra_doi_xung("radar") is True:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với chuỗi 'radar' (kỳ vọng True)")

            # Test 4.2: "A nut for a jar of tuna" -> True (0.5đ)
            if h.kiem_tra_doi_xung("A nut for a jar of tuna") is True:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với câu đối xứng có khoảng trắng")

            # Test 4.3: "python" -> False (0.5đ)
            if h.kiem_tra_doi_xung("python") is False:
                diem_cau += 0.5
            else:
                ly_do.append("Sai với chuỗi không đối xứng 'python' (kỳ vọng False)")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm kiem_tra_doi_xung(s)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # CÂU 5: Chuyển ký tự đầu tiên mỗi từ thành chữ hoa (1.5 điểm)
    # =========================================================================
    ten_cau = "Câu 5: Hàm chuyen_chu_hoa_dau_tu(s)"
    diem_cau = 0.0
    max_cau = 1.5
    ly_do = []

    if hasattr(h, "chuyen_chu_hoa_dau_tu"):
        try:
            # Test 5.1 (0.8đ)
            if h.chuyen_chu_hoa_dau_tu("lap trinh python") == "Lap Trinh Python":
                diem_cau += 0.8
            else:
                ly_do.append("Sai với 'lap trinh python'")

            # Test 5.2 (0.7đ)
            if h.chuyen_chu_hoa_dau_tu("dai hoc quoc gia") == "Dai Hoc Quoc Gia":
                diem_cau += 0.7
            else:
                ly_do.append("Sai với 'dai hoc quoc gia'")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm chuyen_chu_hoa_dau_tu(s)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # CÂU 6: Lọc các số nguyên dương chẵn (1.5 điểm)
    # =========================================================================
    ten_cau = "Câu 6: Hàm loc_so_duong_chan(list)"
    diem_cau = 0.0
    max_cau = 1.5
    ly_do = []

    if hasattr(h, "loc_so_duong_chan"):
        try:
            # Test 6.1 (0.8đ)
            input_list = [-4, -2, 0, 1, 2, 4, 5, 8]
            if h.loc_so_duong_chan(input_list) == [2, 4, 8]:
                diem_cau += 0.8
            else:
                ly_do.append("Sai khi lọc danh sách hỗn hợp [-4, -2, 0, 1, 2, 4, 5, 8]")

            # Test 6.2 (0.7đ)
            if h.loc_so_duong_chan([-3, -1, 0, 5, 7]) == []:
                diem_cau += 0.7
            else:
                ly_do.append("Sai khi không có số dương chẵn nào (kỳ vọng [])")
        except Exception as e:
            ly_do.append(f"Gặp lỗi ngoại lệ khi chạy: {e}")
    else:
        ly_do.append("Chưa định nghĩa hàm loc_so_duong_chan(list)")

    ket_qua_chi_tiet.append((ten_cau, diem_cau, max_cau, ly_do))
    tong_diem += diem_cau

    # =========================================================================
    # IN BẢNG KẾT QUẢ CHẤM ĐIỂM
    # =========================================================================
    print("\n" + "=" * 72)
    print(f"{'NỘI DUNG KIỂM TRA':<42} | {'ĐIỂM ĐẠT':^10} | {'TRẠNG THÁI':^12}")
    print("-" * 72)

    for ten, diem, max_d, ly_do in ket_qua_chi_tiet:
        diem = round(diem, 2)
        max_d = round(max_d, 2)
        diem_str = f"{diem:.1f}/{max_d:.1f}"
        trang_thai = "✅ ĐẠT" if diem >= max_d else ("⚠️ 1 PHẦN" if diem > 0 else "❌ KHÔNG ĐẠT")
        print(f"{ten:<42} | {diem_str:^10} | {trang_thai:^12}")
        if ly_do:
            for ld in ly_do:
                print(f"   └── Chi tiết: {ld}")

    print("=" * 72)
    tong_diem = round(tong_diem, 1)
    print(f"📊 TỔNG ĐIỂM BÀI THI: {tong_diem:.1f} / {diem_toi_da:.1f} ĐIỂM")

    # Xếp loại
    if tong_diem >= 9.0:
        xep_loai = "🏆 XUẤT SẮC (A+)"
    elif tong_diem >= 8.0:
        xep_loai = "🌟 GIỎI (A)"
    elif tong_diem >= 7.0:
        xep_loai = "👍 KHÁ (B)"
    elif tong_diem >= 5.0:
        xep_loai = "👌 TRUNG BÌNH (C)"
    else:
        xep_loai = "⚠️ CẦN CỐ GẮNG THÊM (F)"

    print(f"🏅 XẾP LOẠI HỌC TẬP : {xep_loai}")
    print("=" * 72 + "\n")

    return tong_diem


if __name__ == "__main__":
    cham_bai()
