# 📚 ĐỀ THI KẾT THÚC MÔN HỌC - ĐỀ SỐ 1

* **Trường:** Trường Cao Đẳng Công Thương TP.HCM
* **Khoa:** Công Nghệ Thông Tin - **Bộ Môn:** Công Nghệ Phần Mềm
* **Môn thi:** Lập trình Python (Mã môn: `229152`)
* **Mã đề thi:** `11301`
* **Hình thức thi:** Thực hành trên máy (Được sử dụng tài liệu)
* **Thời gian làm bài:** 90 phút

---

## 📂 Cấu Trúc File Bài Làm (Theo Đúng Yêu Cầu Đề Thi)

Đề bài yêu cầu: *"Cách tổ chức bài thi: Folder HOTEN_MSSV chứa 5 file .py"*. Thư mục này bao gồm:

| File bài làm | Điểm | Nội dung chính |
| :--- | :---: | :--- |
| [`cau1.py`](cau1.py) | **2.0đ** | Kiểm tra $n \in [1; 1500]$; Hàm `DemChuSoLe(n)`; Hàm tính tổng $S = \frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2n}$. |
| [`cau2.py`](cau2.py) | **2.0đ** | Chuỗi ký tự $s$: Đếm ký tự in hoa; Hàm `DoiXung(s)`; Tính tổng các chữ số trong chuỗi. |
| [`cau3.py`](cau3.py) | **2.0đ** | Danh sách (List): Nhập dừng khi gõ số 0; Tính tổng các số dương chẵn; Đếm số lần xuất hiện của $k$. |
| [`cau4.py`](cau4.py) | **2.0đ** | Từ điển (Dictionary): Quản lý sách thư viện (Mã, Tên, Tác giả, NXB, Năm XB); Tìm và xóa sách theo mã. |
| [`cau5.py`](cau5.py) | **2.0đ** | Hướng đối tượng (OOP): Định nghĩa lớp `DienThoai` và khởi tạo 2 đối tượng mẫu (iPhone 15 Pro, Galaxy S24 Ultra). |
| [`de_1_tong_hop.py`](de_1_tong_hop.py) | - | File menu tích hợp giúp bạn dễ dàng chạy và ôn tập cả 5 câu cùng lúc. |
| [`De_Thi_1_Lập_trình_Python_229152.pdf`](De_Thi_1_Lập_trình_Python_229152.pdf) | - | Bản scan PDF gốc của đề thi & barem đáp án chấm điểm chính thức. |

---

## 🚀 Hướng Dẫn Chạy & Thử Nghiệm

### 1. Chạy từng câu đơn lẻ
```bash
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/cau1.py
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/cau2.py
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/cau3.py
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/cau4.py
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/cau5.py
```

### 2. Chạy file tổng hợp có Menu chọn câu
```bash
python Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/de_1_tong_hop.py
```

### 3. Chạy bài kiểm thử tự động (Unit Test Đề 1)
```bash
python -m unittest tests/test_de_1.py -v
```

---

## 📝 Chi Tiết Barem & Lời Giải Chuẩn

### Câu 1 (2.0 điểm)
* **1.a (0.5đ):** Dùng vòng lặp `while n < 1 or n > 1500:` để bắt người dùng nhập lại nếu vượt ngoài đoạn $[1; 1500]$.
* **1.b (0.75đ):** Tách từng chữ số bằng phép chia dư `tam % 10`, kiểm tra lẻ bằng `cs % 2 != 0`, sau đó dịch số bằng phép chia nguyên `tam //= 10`.
* **1.c (0.75đ):** Vòng lặp `for i in range(1, n + 1):` cộng dồn `s += 1 / (2 * i)`.

### Câu 2 (2.0 điểm)
* **2.a (0.75đ):** Dùng phương thức chuẩn `c.isupper()` để nhận diện ký tự in hoa.
* **2.b (0.5đ):** Kiểm tra đối xứng cực nhanh với kỹ thuật cắt chuỗi đảo ngược: `s == s[::-1]`.
* **2.c (0.75đ):** Dùng `c.isdigit()` để lọc ký tự số và ép kiểu `int(c)` cộng dồn vào tổng.

### Câu 3 (2.0 điểm)
* **3.a (0.75đ):** Vòng lặp `while True:` đọc số, nếu `x == 0` thì `break`, ngược lại `danhsach.append(x)`.
* **3.b (0.75đ):** Điều kiện số dương chẵn: `if i > 0 and i % 2 == 0: tong += i`.
* **3.c (0.5đ):** Đếm phần tử: duyệt mảng so sánh `if i == k: dem += 1` (hoặc dùng `danhsach.count(k)`).

### Câu 4 (2.0 điểm)
* **4.a (1.5đ):** Cấu trúc lưu trữ từ điển: `tudien[MaSoSach] = [TenSach, TenTacGia, NhaXuatBan, NamXuatBan]`. Có kiểm tra năm xuất bản $\le$ năm hiện tại bằng `datetime.now().year`.
* **4.b (0.5đ):** Kiểm tra tồn tại bằng toán tử `in`, nếu có dùng lệnh `del tudien[ma_so]` để xóa.

### Câu 5 (2.0 điểm)
* **5.a (1.0đ):** Khai báo lớp `class DienThoai`, viết hàm khởi tạo `__init__(self, MaMay, TenMay, HangSanXuat, DungLuongPin, GiaBan)` và phương thức `thongtindienthoai(self)`.
* **5.b (1.0đ):** Khởi tạo 2 đối tượng:
  * `DT1 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)`
  * `DT2 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)`
  * Gọi `DT1.thongtindienthoai()` và `DT2.thongtindienthoai()`.
