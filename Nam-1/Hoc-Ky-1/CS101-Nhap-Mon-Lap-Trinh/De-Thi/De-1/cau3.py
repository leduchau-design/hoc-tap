"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN: LẬP TRÌNH PYTHON (Mã môn: 229152)

CÂU 3 (2.0 điểm):
Tạo một danh sách rỗng, viết chương trình xử lý danh sách với các chức năng sau:
a. Nhập các phần tử số nguyên vào danh sách, ngưng khi người dùng nhập số 0. In danh sách vừa nhập (0.75 điểm).
b. Tính tổng các số dương chẵn có trong danh sách (0.75 điểm).
c. Đếm số lần xuất hiện của phần tử k có trong danh sách (với k nhập từ bàn phím) (0.5 điểm).
"""

def nhap_danh_sach() -> list[int]:
    """Câu 3.a: Nhập danh sách số nguyên, dừng khi nhập số 0."""
    danhsach = []
    print("Nhập các số nguyên (nhập 0 để dừng lại):")
    while True:
        try:
            x = int(input("Nhập phần tử: "))
            if x == 0:
                break
            danhsach.append(x)
        except ValueError:
            print("⚠️ Vui lòng nhập số nguyên hợp lệ!")
    return danhsach


def tong_duong_chan(danhsach: list[int]) -> int:
    """Câu 3.b: Tính tổng các số dương chẵn có trong danh sách."""
    tong = 0
    for i in danhsach:
        if i > 0 and i % 2 == 0:
            tong += i
    return tong


def dem_so_lan_xuat_hien(danhsach: list[int], k: int) -> int:
    """Câu 3.c: Đếm số lần xuất hiện của phần tử k trong danh sách."""
    dem = 0
    for i in danhsach:
        if i == k:
            dem += 1
    return dem


if __name__ == "__main__":
    print("=" * 60)
    print("                CÂU 3: XỬ LÝ DANH SÁCH (LIST)            ")
    print("=" * 60)
    
    # 3.a: Nhập danh sách và in ra
    danhsach = nhap_danh_sach()
    print(f"\n[+] Danh sách vừa nhập: {danhsach}")
    
    # 3.b: Tính tổng số dương chẵn
    tong = tong_duong_chan(danhsach)
    if tong != 0:
        print(f"[+] Tổng các số dương chẵn trong danh sách: {tong}")
    else:
        print("[+] Không có số dương chẵn trong danh sách.")
        
    # 3.c: Đếm số lần xuất hiện của k
    try:
        k = int(input("\n👉 Nhập giá trị k cần tìm: "))
        so_lan = dem_so_lan_xuat_hien(danhsach, k)
        if so_lan == 0:
            print(f"[+] Không có phần tử {k} trong danh sách.")
        else:
            print(f"[+] Số lần xuất hiện của {k} là: {so_lan}")
    except ValueError:
        print("⚠️ Giá trị k không phải số nguyên hợp lệ!")
        
    print("=" * 60)
