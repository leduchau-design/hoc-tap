"""
ĐỀ THI KẾT THÚC MÔN HỌC - MÃ ĐỀ: 11301 (ĐỀ 1)
MÔN: LẬP TRÌNH PYTHON (Mã môn: 229152)

CÂU 5 (2.0 điểm):
Tạo lớp có tên DienThoai với các yêu cầu sau:
a. Lớp DienThoai có các thuộc tính và phương thức:
   - Thuộc tính: MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.
   - Phương thức:
     * Khởi tạo __init__(): khởi tạo thông tin cho MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan (1.0 điểm).
     * thongtindienthoai(): dùng để hiển thị thông tin của MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan.
b. Tạo 2 đối tượng:
   - (DT01, iPhone 15 Pro, Apple, 3274, 28990000)
   - (DT02, Galaxy S24 Ultra, Samsung, 5000, 29990000)
   và thực thi phương thức thongtindienthoai(). In kết quả ra màn hình (1.0 điểm).
"""

class DienThoai:
    """Lớp quản lý thông tin điện thoại di động."""

    def __init__(self, MaMay: str, TenMay: str, HangSanXuat: str, DungLuongPin: int, GiaBan: int):
        """Câu 5.a: Hàm khởi tạo các thuộc tính của đối tượng điện thoại."""
        self.MaMay = MaMay
        self.TenMay = TenMay
        self.HangSanXuat = HangSanXuat
        self.DungLuongPin = DungLuongPin
        self.GiaBan = GiaBan

    def thongtindienthoai(self):
        """Câu 5.a: Phương thức hiển thị thông tin chi tiết của điện thoại."""
        print(f"Mã máy        : {self.MaMay}")
        print(f"Tên máy       : {self.TenMay}")
        print(f"Hãng sản xuất : {self.HangSanXuat}")
        print(f"Dung lượng pin: {self.DungLuongPin} mAh")
        print(f"Giá bán       : {self.GiaBan:,} VNĐ" if isinstance(self.GiaBan, (int, float)) else f"Giá bán: {self.GiaBan}")
        print("-" * 35)


if __name__ == "__main__":
    print("=" * 60)
    print("             CÂU 5: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP)             ")
    print("=" * 60)
    
    # 5.b: Tạo 2 đối tượng điện thoại theo đúng yêu cầu đề bài
    DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
    DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)
    
    print("\n📱 THÔNG TIN ĐỐI TƯỢNG ĐIỆN THOẠI 1:")
    DT1.thongtindienthoai()
    
    print("\n📱 THÔNG TIN ĐỐI TƯỢNG ĐIỆN THOẠI 2:")
    DT2.thongtindienthoai()
    print("=" * 60)
