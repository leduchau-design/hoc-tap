"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN: LẬP TRÌNH PYTHON (Mã môn: 229152)

CÂU 1 (2.0 điểm):
a. Kiểm tra giá trị n nếu ngoài đoạn [1; 1500] thì yêu cầu nhập lại (0.5 điểm).
b. Viết hàm con đếm số lượng chữ số lẻ của số nguyên dương n (0.75 điểm).
   Ví dụ: n = 635, số lượng chữ số lẻ của n là 2.
c. Viết hàm con tính S = 1/2 + 1/4 + 1/6 + ... + 1/(2n) (0.75 điểm).
"""

def nhap_n() -> int:
    """Câu 1.a: Nhập số nguyên dương n trong đoạn [1; 1500]."""
    while True:
        try:
            n = int(input("Nhập giá trị n (1 <= n <= 1500): "))
            if 1 <= n <= 1500:
                return n
            print("⚠️ Giá trị n phải nằm trong đoạn [1; 1500]. Vui lòng nhập lại!")
        except ValueError:
            print("⚠️ Vui lòng nhập số nguyên hợp lệ!")


def DemChuSoLe(n: int) -> int:
    """Câu 1.b: Hàm con đếm số lượng chữ số lẻ của số nguyên dương n."""
    dem = 0
    tam = abs(n)
    while tam != 0:
        cs = tam % 10
        if cs % 2 != 0:
            dem += 1
        tam //= 10
    return dem


def S(n: int) -> float:
    """Câu 1.c: Hàm con tính tổng S = 1/2 + 1/4 + 1/6 + ... + 1/(2n)."""
    if n <= 0:
        return 0.0
    tong = 0.0
    for i in range(1, n + 1):
        tong += 1.0 / (2 * i)
    return tong


if __name__ == "__main__":
    print("=" * 60)
    print("             CÂU 1: XỬ LÝ SỐ NGUYÊN DƯƠNG N             ")
    print("=" * 60)
    
    # 1.a: Nhập và kiểm tra n
    n = nhap_n()
    print(f"\n[+] Số nguyên n hợp lệ vừa nhập: {n}")
    
    # 1.b: Đếm chữ số lẻ
    so_chu_so_le = DemChuSoLe(n)
    print(f"[+] Số lượng chữ số lẻ của {n} là: {so_chu_so_le}")
    
    # 1.c: Tính tổng S(n)
    tong_s = S(n)
    print(f"[+] Tổng S = 1/2 + 1/4 + ... + 1/(2*{n}) là: {tong_s:.5f}")
    print("=" * 60)
