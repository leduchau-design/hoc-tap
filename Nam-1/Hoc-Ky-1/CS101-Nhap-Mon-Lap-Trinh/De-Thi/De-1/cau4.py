"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN: LẬP TRÌNH PYTHON (Mã môn: 229152)

CÂU 4 (2.0 điểm):
Viết chương trình nhập thông tin của các cuốn sách trong thư viện:
a. Nhập thông tin gồm: Mã số sách, Tên sách, Tên tác giả, Nhà xuất bản, Năm xuất bản. 
   Lưu các thông tin này trong một từ điển (1.5 điểm).
b. Nhập vào một Mã số sách từ bàn phím. Nếu tồn tại cuốn sách có mã số cần tìm 
   thì tiến hành xóa cuốn sách này khỏi từ điển, ngược lại thông báo 
   "Không tìm thấy cuốn sách cần xóa" (0.5 điểm).
"""

from datetime import datetime


def nhap_tu_dien_sach() -> dict:
    """Câu 4.a: Nhập thông tin n cuốn sách và lưu vào từ điển."""
    while True:
        try:
            n = int(input("Nhập số lượng sách (n > 0): "))
            if n > 0:
                break
            print("⚠️ Số lượng sách phải lớn hơn 0!")
        except ValueError:
            print("⚠️ Vui lòng nhập số nguyên hợp lệ!")

    tudien = {}
    nam_hien_tai = datetime.now().year

    for i in range(n):
        print(f"\n--- Nhập thông tin cuốn sách thứ {i + 1} ---")
        ma_so = input("Nhập mã số sách: ").strip()
        ten_sach = input("Nhập tên sách: ").strip()
        tac_gia = input("Nhập tên tác giả: ").strip()
        nxb = input("Nhập nhà xuất bản: ").strip()
        
        while True:
            try:
                nam_xb = int(input("Nhập năm xuất bản: "))
                if nam_xb <= nam_hien_tai:
                    break
                print(f"⚠️ Năm xuất bản không hợp lệ (phải <= {nam_hien_tai})!")
            except ValueError:
                print("⚠️ Năm xuất bản phải là số nguyên!")

        # Lưu vào từ điển theo đáp án đề thi: tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan]
        tudien[ma_so] = [ten_sach, tac_gia, nxb, nam_xb]

    return tudien


def xoa_sach(tudien: dict, ma_so_can_xoa: str) -> bool:
    """Câu 4.b: Xóa sách khỏi từ điển theo mã số."""
    if ma_so_can_xoa in tudien:
        del tudien[ma_so_can_xoa]
        return True
    return False


def in_tu_dien_sach(tudien: dict):
    """In danh sách sách trong từ điển ra bảng đẹp mắt."""
    if not tudien:
        print("[!] Từ điển sách hiện đang rỗng.")
        return
    print("-" * 75)
    print(f"{'MÃ SÁCH':<10} | {'TÊN SÁCH':<25} | {'TÁC GIẢ':<15} | {'NXB':<10} | {'NĂM XB':^6}")
    print("-" * 75)
    for ma, info in tudien.items():
        print(f"{ma:<10} | {info[0]:<25} | {info[1]:<15} | {info[2]:<10} | {info[3]:^6}")
    print("-" * 75)


if __name__ == "__main__":
    print("=" * 65)
    print("             CÂU 4: QUẢN LÝ SÁCH THƯ VIỆN BẰNG TỪ ĐIỂN          ")
    print("=" * 65)

    # 4.a: Nhập thông tin sách
    tudien_sach = nhap_tu_dien_sach()
    print("\n[+] Từ điển sách vừa nhập:")
    in_tu_dien_sach(tudien_sach)

    # 4.b: Xóa sách theo mã
    ma_can_xoa = input("\n👉 Nhập vào một Mã số sách cần xóa: ").strip()
    if xoa_sach(tudien_sach, ma_can_xoa):
        print(f"[+] Cuốn sách có mã số '{ma_can_xoa}' đã được xóa thành công.")
    else:
        print("[-] Không tìm thấy cuốn sách cần xóa.")

    print("\n[+] Từ điển sách sau khi cập nhật:")
    in_tu_dien_sach(tudien_sach)
    print("=" * 65)
