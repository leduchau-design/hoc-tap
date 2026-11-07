# 🎓 Kho Lưu Trữ Tài Liệu Học Tập (hoc-tap)

![GitHub repo size](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

Repository này được sử dụng để lưu trữ, quản lý toàn bộ tài liệu học tập, slide bài giảng, bài tập (Lab/Assignment), đồ án môn học và đề thi tham khảo theo từng kỳ học.

---

## 📑 Mục Lục

- [Cấu Trúc Thư Mục](#-cấu-trúc-thư-mục)
- [Bài Tập Python & Kiểm Thử Tự Động (Unit Tests)](#-bài-tập-python--kiểm-thử-tự-động-unit-tests)
- [Bảng Tổng Hợp Môn Học](#-bảng-tổng-hợp-môn-học)
  - [Học Kỳ 1](#học-kỳ-1)
  - [Học Kỳ 2](#học-kỳ-2)
- [Quy Ước Đặt Tên](#-quy-ước-đặt-tên)
- [Hướng Dẫn Sử Dụng Git](#-hướng-dẫn-sử-dụng-git)
  - [Quy trình đẩy bài hàng ngày](#quy-trình-đẩy-bài-hàng-ngày)
  - [Lưu ý về dung lượng file (>100MB)](#lưu-ý-về-dung-lượng-file-100mb)
- [Liên Hệ & Đóng Góp](#-liên-hệ--đóng-góp)

---

## 📂 Cấu Trúc Thư Mục

Cấu trúc gợi ý để sắp xếp tài liệu khoa học, dễ tìm kiếm:

```text
study-repository/
├── README.md                          # Giới thiệu tổng quan và mục lục kho tài liệu
├── .gitignore                         # Loại bỏ file rác, file tạm, file build nặng
├── Tai-Lieu-Chung/                    # Sách giáo trình chung, template báo cáo, biểu mẫu
│   └── README.md
├── Nam-1/
│   ├── Hoc-Ky-1/
│   │   ├── CS101-Nhap-Mon-Lap-Trinh/
│   │   │   ├── Bai-Giang/             # Slide bài giảng tuần 1 -> n (PDF, PPTX)
│   │   │   ├── Bai-Tap/               # Bài tập về nhà, bài thực hành Lab
│   │   │   ├── Do-An/                 # Source code, báo cáo bài tập lớn
│   │   │   ├── De-Thi/                # Đề cương ôn tập, đề thi giữa kỳ, cuối kỳ
│   │   │   └── README.md              # Ghi chú riêng cho môn học này
│   │   └── MATH101-Toan-Cao-Cap-A1/
│   │       ├── Bai-Giang/
│   │       ├── Bai-Tap/
│   │       └── README.md
│   └── Hoc-Ky-2/
│       └── README.md
└── Nam-2/
    └── README.md
```

---

## 🧪 Bài Tập Python & Kiểm Thử Tự Động (Unit Tests)

Kho lưu trữ tích hợp sẵn mã nguồn bài tập ôn tập đề thi Python [`h.py`](h.py) cùng bộ kiểm thử tự động [`tests/test_h.py`](tests/test_h.py).

### Danh mục bài tập trong `h.py`:
1. **`tong_uoc_so(n)`**: Tính tổng tất cả các ước số nguyên dương của `n`.
2. **`tinh_tong_luy_thua(n)`**: Tính tổng $S(n) = 1^1 + 2^2 + 3^3 + \dots + n^n$.
3. **`dem_chu_thuong(s)`**: Đếm số ký tự in thường trong chuỗi `s`.
4. **`kiem_tra_doi_xung(s)`**: Kiểm tra chuỗi đối xứng (Palindrome).
5. **`chuyen_chu_hoa_dau_tu(s)`**: Chuyển ký tự đầu tiên mỗi từ thành chữ hoa (`s.title()`).
6. **`loc_so_duong_chan(list)`**: Lọc danh sách các số nguyên dương chẵn.

### Lệnh chạy kiểm thử (Chạy 1 dòng lệnh là tự chấm):
```bash
python -m unittest tests/test_h.py
```
*Kết quả:* Tất cả 6/6 bài test đều **OK** và pass tuyệt đối.

---

## 📊 Bảng Tổng Hợp Môn Học

### Học Kỳ 1

| Mã môn | Tên môn học | Số tín chỉ | Giảng viên | Thư mục | Trạng thái |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `CS101` | Nhập môn lập trình | 3 | ThS. Nguyễn Văn A | [Xem thư mục](Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/) | 🟢 Hoàn thành |
| `MATH101` | Toán cao cấp A1 | 3 | TS. Trần Thị B | [Xem thư mục](Nam-1/Hoc-Ky-1/MATH101-Toan-Cao-Cap-A1/) | 🟡 Đang học |
| `ENG101` | Tiếng Anh 1 | 2 | Cô Emily | [Xem thư mục](Nam-1/Hoc-Ky-1/ENG101-Tieng-Anh-1/) | ⚪ Chưa học |

> *Gợi ý icon trạng thái: 🟢 Hoàn thành | 🟡 Đang học | ⚪ Chưa học*

### Học Kỳ 2

| Mã môn | Tên môn học | Số tín chỉ | Giảng viên | Thư mục | Trạng thái |
| :--- | :--- | :---: | :--- | :--- | :---: |
| `CS102` | Cấu trúc dữ liệu & Giải thuật | 4 | ThS. Lê Văn C | *Cập nhật sau* | ⚪ Chưa học |
| `PHY101` | Vật lý đại cương | 3 | TS. Phạm Văn D | *Cập nhật sau* | ⚪ Chưa học |

---

## 🏷️ Quy Ước Đặt Tên

Để tránh lỗi font chữ trên GitHub hoặc các hệ điều hành khác nhau:
1. **Tên thư mục & file:** Đặt tên tiếng Việt không dấu, nối bằng dấu gạch ngang `-` hoặc gạch dưới `_`.
   - *Tốt:* `Tuan-01-Gioi-Thieu.pdf`, `Lab-02-Vong-Lap.cpp`
   - *Tránh:* `Tuần 1 Giới thiệu.pdf`, `bài tập mới nhất(1).cpp`
2. **Commit message:** Viết rõ ràng việc vừa làm:
   - `docs: Thêm slide bài giảng tuần 3 môn CS101`
   - `feat: Hoàn thành bài tập Lab 2`
   - `update: Cập nhật đề cương ôn thi giữa kỳ`

---

## 🚀 Hướng Dẫn Sử Dụng Git

### Quy trình đẩy bài hàng ngày

Mỗi khi thêm bài tập mới hoặc slide mới, mở terminal trong thư mục này và chạy:

```bash
# 1. Kiểm tra các file vừa sửa đổi/thêm mới
git status

# 2. Thêm tất cả thay đổi vào vùng chuẩn bị commit
git add .

# 3. Ghi lại nội dung thay đổi
git commit -m "docs: Cập nhật bài tập môn <Tên-Môn>"

# 4. Đẩy lên GitHub
git push
```

### ⚠️ Lưu ý về dung lượng file (>100MB)

- GitHub **từ chối đẩy** các file đơn lẻ có kích thước **lớn hơn 100MB** (như video bài giảng, bộ cài đặt, dataset nặng).
- Đối với các file nặng, bạn nên:
  1. Tải lên **Google Drive / OneDrive**.
  2. Bật chế độ chia sẻ link (Anyone with the link).
  3. Dán link vào file `README.md` của môn học đó.

---

## 📌 Liên Hệ & Đóng Góp

- **Người sở hữu:** [Tên của bạn](https://github.com/)
- **Email:** `your_email@example.com`
- **Ghi chú:** Tài liệu chỉ phục vụ mục đích học tập cá nhân. Vui lòng tuân thủ quy định liêm chính học thuật của nhà trường.
