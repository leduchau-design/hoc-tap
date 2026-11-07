"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN: LẬP TRÌNH PYTHON (Mã môn: 229152)

CÂU 2 (2.0 điểm):
Viết chương trình nhập một chuỗi s từ bàn phím và thực hiện các công việc sau:
a. Đếm số ký tự chữ hoa có trong chuỗi (0.75 điểm).
b. Kiểm tra xem chuỗi s có đối xứng hay không (0.5 điểm).
c. Tính tổng các chữ số trong chuỗi (0.75 điểm).
"""

def dem_chu_hoa(s: str) -> int:
    """Câu 2.a: Đếm số lượng ký tự in hoa trong chuỗi."""
    dem = 0
    for c in s:
        if c.isupper():
            dem += 1
    return dem


def DoiXung(s: str) -> bool:
    """Câu 2.b: Hàm kiểm tra xem chuỗi s có đối xứng (palindrome) hay không."""
    return s == s[::-1]


def tinh_tong_chu_so(s: str) -> int:
    """Câu 2.c: Tính tổng tất cả các ký tự chữ số xuất hiện trong chuỗi."""
    tong = 0
    for c in s:
        if c.isdigit():
            tong += int(c)
    return tong


if __name__ == "__main__":
    print("=" * 60)
    print("                 CÂU 2: XỬ LÝ CHUỖI KÝ TỰ                ")
    print("=" * 60)
    
    # Nhập chuỗi s từ bàn phím
    s = input("Nhập chuỗi s: ")
    
    # 2.a: Đếm chữ hoa
    so_chu_hoa = dem_chu_hoa(s)
    if so_chu_hoa == 0:
        print("[+] Chuỗi không có ký tự chữ hoa.")
    else:
        print(f"[+] Số ký tự chữ hoa: {so_chu_hoa}")
        
    # 2.b: Kiểm tra đối xứng
    if DoiXung(s):
        print("[+] Chuỗi đối xứng.")
    else:
        print("[+] Chuỗi không đối xứng.")
        
    # 2.c: Tính tổng các chữ số
    tong_so = tinh_tong_chu_so(s)
    print(f"[+] Tổng các chữ số trong chuỗi: {tong_so}")
    print("=" * 60)
