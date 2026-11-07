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

Tính năng bảo vệ nâng cao:
- Cảnh báo nếu người dùng lỡ nhập n quá lớn (ví dụ n >= 10).
- Cho phép gõ '0' hoặc 'dung' tại mã sách để dừng nhập sớm mà không bị kẹt.
- Bắt phím Ctrl + C (KeyboardInterrupt) để thoát êm ái, không báo lỗi đỏ trên terminal.
"""

from datetime import datetime


def nhap_tu_dien_sach() -> dict:
    """Câu 4.a: Nhập thông tin n cuốn sách và lưu vào từ điển (có cơ chế dừng sớm an toàn)."""
    tudien = {}
    nam_hien_tai = datetime.now().year

    try:
        # Bước 1: Nhập số lượng sách n
        while True:
            try:
                raw_n = input("Nhập số lượng sách cần thêm (n > 0): ").strip()
                if not raw_n:
                    continue
                n = int(raw_n)
                if n <= 0:
                    print("⚠️ Số lượng sách phải lớn hơn 0!")
                    continue
                
                # Cảnh báo thân thiện nếu lỡ gõ số quá lớn
                if n > 10:
                    print(f"⚠️ Bạn vừa nhập {n} cuốn sách (khá nhiều để gõ tay).")
                    xac_nhan = input(f"👉 Bạn có chắc chắn muốn nhập {n} cuốn không? (nhấn Enter để tiếp tục, hoặc gõ 'k' để nhập lại): ").strip().lower()
                    if xac_nhan in ("k", "khong", "no", "lai"):
                        continue
                break
            except ValueError:
                print("⚠️ Vui lòng nhập một số nguyên hợp lệ!")

        # Bước 2: Vòng lặp nhập từng cuốn sách
        print("\n💡 MẸO: Bạn có thể gõ '0' hoặc 'dung' ở Mã số sách để kết thúc sớm bất kỳ lúc nào.")
        
        for i in range(n):
            print(f"\n--- Nhập thông tin cuốn sách thứ {i + 1}/{n} ---")
            
            ma_so = input("Nhập mã số sách (hoặc gõ '0'/'dung' để dừng): ").strip()
            
            # Cho phép dừng sớm nếu lỡ nhập n quá nhiều
            if ma_so in ("0", "dung", "dừng", "exit", "quit", "stop"):
                print(f"⏹️ Đã dừng nhập sớm theo yêu cầu. Hiện đã lưu {len(tudien)} cuốn sách.")
                break
                
            if not ma_so:
                print("⚠️ Mã số sách không được để trống!")
                continue

            ten_sach = input("Nhập tên sách: ").strip()
            tac_gia = input("Nhập tên tác giả: ").strip()
            nxb = input("Nhập nhà xuất bản: ").strip()
            
            while True:
                try:
                    nam_raw = input("Nhập năm xuất bản: ").strip()
                    if not nam_raw:
                        continue
                    nam_xb = int(nam_raw)
                    if nam_xb <= nam_hien_tai:
                        break
                    print(f"⚠️ Năm xuất bản không hợp lệ (phải <= {nam_hien_tai})!")
                except ValueError:
                    print("⚠️ Năm xuất bản phải là số nguyên!")

            # Lưu vào từ điển theo cấu trúc đáp án đề thi:
            # tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan]
            tudien[ma_so] = [ten_sach, tac_gia, nxb, nam_xb]
            print(f"✅ Đã thêm sách '{ma_so}' thành công.")

    except KeyboardInterrupt:
        # Bắt phím Ctrl + C để thoát êm ái, không văng lỗi đỏ
        print("\n\n⏹️ Bạn đã bấm dừng chương trình (Ctrl + C). Đã lưu lại các sách đã nhập trước đó.")

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

    try:
        # 4.a: Nhập thông tin sách
        tudien_sach = nhap_tu_dien_sach()
        print("\n[+] Từ điển sách hiện tại:")
        in_tu_dien_sach(tudien_sach)

        # 4.b: Xóa sách theo mã (nếu từ điển có sách)
        if tudien_sach:
            ma_can_xoa = input("\n👉 Nhập vào một Mã số sách cần xóa: ").strip()
            if xoa_sach(tudien_sach, ma_can_xoa):
                print(f"[+] Cuốn sách có mã số '{ma_can_xoa}' đã được xóa thành công.")
            else:
                print("[-] Không tìm thấy cuốn sách cần xóa.")

            print("\n[+] Từ điển sách sau khi cập nhật:")
            in_tu_dien_sach(tudien_sach)
    except KeyboardInterrupt:
        print("\n\n⏹️ Đã thoát chương trình an toàn.")

    print("=" * 65)
