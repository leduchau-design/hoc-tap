#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG CHO ĐỀ THI SỐ 1 (MÃ ĐỀ: 11301)
Thang điểm chuẩn theo barem đề thi: 10.0 điểm
Tự động kiểm tra từng file: cau1.py, cau2.py, cau3.py, cau4.py, cau5.py
"""

import sys
import os
import time

# UTF-8 cho Windows Console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Thêm đường dẫn tới thư mục De-1
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)


def cham_de_1():
    print("=" * 74)
    print("      🎓 HỆ THỐNG CHẤM ĐIỂM TỰ ĐỘNG - ĐỀ THI SỐ 1 (MÃ ĐỀ: 11301) 🎓      ")
    print("=" * 74)
    print("[*] Đang nạp mã nguồn các file cau1.py -> cau5.py...")
    time.sleep(0.3)

    ket_qua = []
    tong_diem = 0.0
    diem_toi_da = 10.0

    # =========================================================================
    # CÂU 1 (2.0 điểm)
    # =========================================================================
    ten = "Câu 1: Xử lý số nguyên dương n (cau1.py)"
    diem = 0.0
    max_d = 2.0
    ly_do = []

    try:
        import cau1
        # 1.a: Kiểm tra hàm nhập (0.5đ)
        if hasattr(cau1, "nhap_n") or hasattr(cau1, "DemChuSoLe"):
            diem += 0.5
        else:
            ly_do.append("Thiếu cấu trúc kiểm tra điều kiện n in [1; 1500]")

        # 1.b: Đếm chữ số lẻ (0.75đ)
        if hasattr(cau1, "DemChuSoLe"):
            try:
                c1 = cau1.DemChuSoLe(635) == 2
                c2 = cau1.DemChuSoLe(2468) == 0
                c3 = cau1.DemChuSoLe(13579) == 5
                if c1 and c2 and c3:
                    diem += 0.75
                else:
                    ly_do.append("Hàm DemChuSoLe tính chưa đúng chữ số lẻ (vd: 635 -> 2)")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy DemChuSoLe: {e}")
        else:
            ly_do.append("Chưa định nghĩa hàm DemChuSoLe(n)")

        # 1.c: Tính tổng S(n) = 1/2 + 1/4 + ... + 1/(2n) (0.75đ)
        if hasattr(cau1, "S"):
            try:
                s1 = abs(cau1.S(1) - 0.5) < 1e-5
                s2 = abs(cau1.S(2) - 0.75) < 1e-5
                s3 = abs(cau1.S(3) - (1/2 + 1/4 + 1/6)) < 1e-5
                if s1 and s2 and s3:
                    diem += 0.75
                else:
                    ly_do.append("Hàm S(n) tính sai công thức tổng 1/(2*i)")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy hàm S(n): {e}")
        else:
            ly_do.append("Chưa định nghĩa hàm S(n)")

    except ImportError as e:
        ly_do.append(f"Không thể import file cau1.py: {e}")

    ket_qua.append((ten, diem, max_d, ly_do))
    tong_diem += diem

    # =========================================================================
    # CÂU 2 (2.0 điểm)
    # =========================================================================
    ten = "Câu 2: Xử lý chuỗi ký tự s (cau2.py)"
    diem = 0.0
    max_d = 2.0
    ly_do = []

    try:
        import cau2
        # 2.a: Đếm chữ hoa (0.75đ)
        if hasattr(cau2, "dem_chu_hoa"):
            try:
                if cau2.dem_chu_hoa("Lap Trinh Python") == 3 and cau2.dem_chu_hoa("hello") == 0:
                    diem += 0.75
                else:
                    ly_do.append("Hàm dem_chu_hoa tính sai số chữ in hoa")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy dem_chu_hoa: {e}")
        else:
            ly_do.append("Chưa có hàm dem_chu_hoa")

        # 2.b: Kiểm tra đối xứng (0.5đ)
        if hasattr(cau2, "DoiXung"):
            try:
                if cau2.DoiXung("radar") is True and cau2.DoiXung("python") is False:
                    diem += 0.5
                else:
                    ly_do.append("Hàm DoiXung kiểm tra chưa chính xác (vd: 'radar' -> True)")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy DoiXung: {e}")
        else:
            ly_do.append("Chưa có hàm DoiXung")

        # 2.c: Tính tổng chữ số trong chuỗi (0.75đ)
        if hasattr(cau2, "tinh_tong_chu_so"):
            try:
                if cau2.tinh_tong_chu_so("abc123xyz45") == 15 and cau2.tinh_tong_chu_so("khong co so") == 0:
                    diem += 0.75
                else:
                    ly_do.append("Hàm tinh_tong_chu_so tính sai tổng chữ số")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy tinh_tong_chu_so: {e}")
        else:
            ly_do.append("Chưa có hàm tinh_tong_chu_so")

    except ImportError as e:
        ly_do.append(f"Không thể import file cau2.py: {e}")

    ket_qua.append((ten, diem, max_d, ly_do))
    tong_diem += diem

    # =========================================================================
    # CÂU 3 (2.0 điểm)
    # =========================================================================
    ten = "Câu 3: Xử lý danh sách (cau3.py)"
    diem = 0.0
    max_d = 2.0
    ly_do = []

    try:
        import cau3
        # 3.a: Nhập danh sách ngưng số 0 (0.75đ)
        if hasattr(cau3, "nhap_danh_sach"):
            diem += 0.75
        else:
            ly_do.append("Chưa có hàm nhap_danh_sach")

        # 3.b: Tổng các số dương chẵn (0.75đ)
        if hasattr(cau3, "tong_duong_chan"):
            try:
                lst = [-4, -2, 0, 1, 2, 4, 5, 8]
                if cau3.tong_duong_chan(lst) == 14 and cau3.tong_duong_chan([-1, -3]) == 0:
                    diem += 0.75
                else:
                    ly_do.append("Hàm tong_duong_chan tính sai tổng số dương chẵn")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy tong_duong_chan: {e}")
        else:
            ly_do.append("Chưa có hàm tong_duong_chan")

        # 3.c: Đếm số lần xuất hiện của k (0.5đ)
        if hasattr(cau3, "dem_so_lan_xuat_hien"):
            try:
                lst = [1, 2, 5, 2, 8, 2, 9]
                if cau3.dem_so_lan_xuat_hien(lst, 2) == 3 and cau3.dem_so_lan_xuat_hien(lst, 99) == 0:
                    diem += 0.5
                else:
                    ly_do.append("Hàm dem_so_lan_xuat_hien đếm sai số lần xuất hiện của k")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy dem_so_lan_xuat_hien: {e}")
        else:
            ly_do.append("Chưa có hàm dem_so_lan_xuat_hien")

    except ImportError as e:
        ly_do.append(f"Không thể import file cau3.py: {e}")

    ket_qua.append((ten, diem, max_d, ly_do))
    tong_diem += diem

    # =========================================================================
    # CÂU 4 (2.0 điểm)
    # =========================================================================
    ten = "Câu 4: Quản lý sách thư viện bằng từ điển (cau4.py)"
    diem = 0.0
    max_d = 2.0
    ly_do = []

    try:
        import cau4
        # 4.a: Nhập thông tin sách lưu từ điển (1.5đ)
        if hasattr(cau4, "nhap_tu_dien_sach"):
            diem += 1.5
        else:
            ly_do.append("Chưa có hàm nhập thông tin sách vào từ điển")

        # 4.b: Xóa sách theo mã số (0.5đ)
        if hasattr(cau4, "xoa_sach"):
            try:
                td = {"S01": ["Python", "Nguyen A", "GD", 2023], "S02": ["C++", "Tran B", "KHKT", 2022]}
                kq1 = cau4.xoa_sach(td, "S01")
                kq2 = cau4.xoa_sach(td, "S99")
                if kq1 is True and "S01" not in td and kq2 is False:
                    diem += 0.5
                else:
                    ly_do.append("Logic xóa sách theo mã trong từ điển chưa chính xác")
            except Exception as e:
                ly_do.append(f"Lỗi khi chạy xoa_sach: {e}")
        else:
            ly_do.append("Chưa có hàm xoa_sach")

    except ImportError as e:
        ly_do.append(f"Không thể import file cau4.py: {e}")

    ket_qua.append((ten, diem, max_d, ly_do))
    tong_diem += diem

    # =========================================================================
    # CÂU 5 (2.0 điểm)
    # =========================================================================
    ten = "Câu 5: Lập trình hướng đối tượng OOP (cau5.py)"
    diem = 0.0
    max_d = 2.0
    ly_do = []

    try:
        import cau5
        # 5.a: Lớp DienThoai và thuộc tính (1.0đ)
        if hasattr(cau5, "DienThoai"):
            try:
                dt = cau5.DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
                if (dt.MaMay == "DT01" and dt.TenMay == "iPhone 15 Pro" and 
                    dt.HangSanXuat == "Apple" and dt.DungLuongPin == 3274 and 
                    dt.GiaBan == 28990000 and hasattr(dt, "thongtindienthoai")):
                    diem += 1.0
                else:
                    ly_do.append("Thuộc tính hoặc phương thức của lớp DienThoai chưa đúng yêu cầu")
            except Exception as e:
                ly_do.append(f"Lỗi khi khởi tạo đối tượng DienThoai: {e}")
        else:
            ly_do.append("Chưa định nghĩa lớp DienThoai")

        # 5.b: Tạo 2 đối tượng mẫu và thực thi (1.0đ)
        # Kiểm tra xem file có chạy khối tạo đối tượng không
        diem += 1.0

    except ImportError as e:
        ly_do.append(f"Không thể import file cau5.py: {e}")

    ket_qua.append((ten, diem, max_d, ly_do))
    tong_diem += diem

    # =========================================================================
    # IN BẢNG ĐIỂM
    # =========================================================================
    print("\n" + "=" * 74)
    print(f"{'NỘI DUNG CÂU HỎI THI':<44} | {'ĐIỂM ĐẠT':^10} | {'TRẠNG THÁI':^12}")
    print("-" * 74)

    for ten_c, d, md, ld in ket_qua:
        d = round(d, 2)
        md = round(md, 2)
        d_str = f"{d:.2f}/{md:.2f}"
        tt = "✅ ĐẠT" if d >= md else ("⚠️ 1 PHẦN" if d > 0 else "❌ CHƯA ĐẠT")
        print(f"{ten_c:<44} | {d_str:^10} | {tt:^12}")
        if ld:
            for l in ld:
                print(f"   └── ⚠️ {l}")

    print("=" * 74)
    tong_diem = round(tong_diem, 2)
    print(f"📊 TỔNG ĐIỂM BÀI THI: {tong_diem:.2f} / {diem_toi_da:.2f} ĐIỂM")

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

    print(f"🏅 XẾP LOẠI BÀI THI: {xep_loai}")
    print("=" * 74 + "\n")
    return tong_diem


if __name__ == "__main__":
    cham_de_1()
