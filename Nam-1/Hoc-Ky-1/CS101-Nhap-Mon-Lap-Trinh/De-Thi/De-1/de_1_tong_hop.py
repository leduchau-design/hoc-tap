"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN HỌC: LẬP TRÌNH PYTHON - KHOA CNTT TRƯỜNG CĐ CÔNG THƯƠNG TP.HCM
FILE TỔNG HỢP TOÀN BỘ 5 CÂU HỎI & CHẠY THỬ NGHIỆM TƯƠNG TÁC
"""

import sys
import os

# Nạp các câu hỏi từ các file tương ứng
try:
    from cau1 import DemChuSoLe, S, nhap_n
    from cau2 import dem_chu_hoa, DoiXung, tinh_tong_chu_so
    from cau3 import nhap_danh_sach, tong_duong_chan, dem_so_lan_xuat_hien
    from cau4 import nhap_tu_dien_sach, xoa_sach, in_tu_dien_sach
    from cau5 import DienThoai
except ImportError:
    # Nếu chạy từ thư mục khác
    cur_dir = os.path.dirname(__file__)
    if cur_dir not in sys.path:
        sys.path.insert(0, cur_dir)
    from cau1 import DemChuSoLe, S, nhap_n
    from cau2 import dem_chu_hoa, DoiXung, tinh_tong_chu_so
    from cau3 import nhap_danh_sach, tong_duong_chan, dem_so_lan_xuat_hien
    from cau4 import nhap_tu_dien_sach, xoa_sach, in_tu_dien_sach
    from cau5 import DienThoai


def menu():
    print("\n" + "=" * 68)
    print("      🎓 ĐỀ THI KẾT THÚC MÔN: LẬP TRÌNH PYTHON (ĐỀ SỐ 1) 🎓      ")
    print("=" * 68)
    print("  1. Câu 1 (2.0đ): Nhập n in [1; 1500], Đếm chữ số lẻ, Tính tổng S(n)")
    print("  2. Câu 2 (2.0đ): Chuỗi s - Đếm chữ hoa, Đối xứng, Tổng chữ số")
    print("  3. Câu 3 (2.0đ): Danh sách - Nhập dừng số 0, Tổng dương chẵn, Đếm k")
    print("  4. Câu 4 (2.0đ): Từ điển - Quản lý sách thư viện và xóa theo mã")
    print("  5. Câu 5 (2.0đ): Lập trình OOP - Lớp DienThoai và 2 đối tượng mẫu")
    print("  0. Thoát chương trình")
    print("=" * 68)


def main():
    while True:
        menu()
        chon = input("👉 Mời bạn chọn câu hỏi muốn chạy thử (0-5): ").strip()
        
        if chon == "0":
            print("\nCảm ơn bạn đã ôn tập Đề thi số 1. Chúc bạn thi tốt đạt điểm tối đa! 🎉\n")
            break
            
        elif chon == "1":
            print("\n" + "-" * 50)
            print("--- CHẠY CÂU 1 ---")
            n = nhap_n()
            print(f" [+] Số n: {n}")
            print(f" [+] Số lượng chữ số lẻ của {n}: {DemChuSoLe(n)}")
            print(f" [+] Tổng S = 1/2 + 1/4 + ... + 1/(2*{n}) = {S(n):.5f}")
            
        elif chon == "2":
            print("\n" + "-" * 50)
            print("--- CHẠY CÂU 2 ---")
            s = input("Nhập chuỗi s: ")
            print(f" [+] Số ký tự chữ hoa: {dem_chu_hoa(s)}")
            print(f" [+] Chuỗi có đối xứng không? {DoiXung(s)}")
            print(f" [+] Tổng các chữ số trong chuỗi: {tinh_tong_chu_so(s)}")
            
        elif chon == "3":
            print("\n" + "-" * 50)
            print("--- CHẠY CÂU 3 ---")
            ds = nhap_danh_sach()
            print(f" [+] Danh sách vừa nhập: {ds}")
            print(f" [+] Tổng các số dương chẵn: {tong_duong_chan(ds)}")
            try:
                k = int(input("Nhập số k cần đếm: "))
                print(f" [+] Số lần xuất hiện của {k}: {dem_so_lan_xuat_hien(ds, k)}")
            except ValueError:
                print("⚠️ k không phải số nguyên!")
                
        elif chon == "4":
            print("\n" + "-" * 50)
            print("--- CHẠY CÂU 4 ---")
            tudien = nhap_tu_dien_sach()
            in_tu_dien_sach(tudien)
            if tudien:
                ma_xoa = input("\n👉 Nhập mã sách cần xóa: ").strip()
                if xoa_sach(tudien, ma_xoa):
                    print(f"Cuốn sách có mã số {ma_xoa} đã được xóa thành công.")
                else:
                    print("Không tìm thấy cuốn sách cần xóa.")
                in_tu_dien_sach(tudien)
            
        elif chon == "5":
            print("\n" + "-" * 50)
            print("--- CHẠY CÂU 5 ---")
            DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
            DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
            print("\n[+] Đối tượng 1:")
            DT1.thongtindienthoai()
            print("\n[+] Đối tượng 2:")
            DT2.thongtindienthoai()
            
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng chọn từ 0 đến 5!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️ Đã dừng chương trình an toàn.")
