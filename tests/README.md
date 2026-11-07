# 🧪 Thư Mục Kiểm Thử Tự Động (Unit Tests)

Thư mục này chứa toàn bộ các bài kiểm thử tự động (Unit Tests) cho mã nguồn bài tập trong kho lưu trữ học tập, sử dụng thư viện chuẩn `unittest` của Python (và tương thích hoàn toàn với `pytest`).

---

## 📋 Danh Sách File Kiểm Thử

| File kiểm thử | Đối tượng kiểm tra | Mục đích |
| :--- | :--- | :--- |
| [`test_h.py`](test_h.py) | [`h.py`](../h.py) | Kiểm thử chuẩn 6 bài toán lập trình Python cơ bản có kèm hộp thoại chỉ dẫn sửa lỗi sai. |
| [`test_nhieu_truong_hop.py`](test_nhieu_truong_hop.py) | [`h.py`](../h.py) | Kiểm thử mở rộng với **52 trường hợp đa dạng** (số nguyên tố, lũy thừa, chuỗi phức tạp, palindrome, mảng âm/dương) + chế độ tự nhập input từ bàn phím. |
| [`test_de_1.py`](test_de_1.py) | [`De-Thi/De-1/`](../Nam-1/Hoc-Ky-1/CS101-Nhap-Mon-Lap-Trinh/De-Thi/De-1/) | Kiểm thử tự động toàn bộ 5 câu hỏi của Đề thi số 1 (Mã đề: 11301). |

---

## 🚀 Hướng Dẫn Chạy Test

Bạn có thể chạy kiểm thử trực tiếp từ thư mục gốc của dự án bằng một trong các lệnh sau trong Terminal / PowerShell:

### 1. Chạy bài test cụ thể cho file `h.py` (Khuyên dùng)
```bash
python -m unittest tests/test_h.py
```

### 2. Chạy với thông tin chi tiết từng bài test (Verbose mode)
Lệnh này sẽ hiển thị tên từng hàm test và trạng thái `ok`:
```bash
python -m unittest tests/test_h.py -v
```

**Kết quả mẫu:**
```text
test_chuyen_chu_hoa_dau_tu (tests.test_h.TestBaiTapPython.test_chuyen_chu_hoa_dau_tu) ... ok
test_dem_chu_thuong (tests.test_h.TestBaiTapPython.test_dem_chu_thuong) ... ok
test_kiem_tra_doi_xung (tests.test_h.TestBaiTapPython.test_kiem_tra_doi_xung) ... ok
test_loc_so_duong_chan (tests.test_h.TestBaiTapPython.test_loc_so_duong_chan) ... ok
test_tinh_tong_luy_thua (tests.test_h.TestBaiTapPython.test_tinh_tong_luy_thua) ... ok
test_tong_uoc_so (tests.test_h.TestBaiTapPython.test_tong_uoc_so) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### 3. Tự động tìm và chạy tất cả các file test trong thư mục
```bash
python -m unittest discover -s tests -p "test_*.py"
```

### 4. Nếu máy đã cài đặt `pytest`
```bash
pytest tests/ -v
```

---

## 🛠️ Chi Tiết Các Trường Hợp Kiểm Thử trong `test_h.py`

1. **`test_tong_uoc_so`:**
   - Kiểm tra tính tổng ước số của số dương chuẩn (ví dụ `n = 6` có ước `1, 2, 3, 6` -> tổng `12`).
   - Kiểm tra trường hợp biên (`n = 1` -> tổng `1`).
   - Kiểm tra trường hợp giá trị không hợp lệ (`n <= 0` -> trả về `0`).

2. **`test_tinh_tong_luy_thua`:**
   - Kiểm tra $S(1) = 1^1 = 1$.
   - Kiểm tra $S(2) = 1^1 + 2^2 = 5$.
   - Kiểm tra $S(3) = 1^1 + 2^2 + 3^3 = 32$.

3. **`test_dem_chu_thuong`:**
   - Kiểm tra chuỗi có cả hoa lẫn thường (`"Python"` -> `5`).
   - Kiểm tra chuỗi toàn hoa (`"PYTHON"` -> `0`).
   - Kiểm tra chuỗi có số và ký tự đặc biệt (`"abc 123 !@#"` -> `3`).

4. **`test_kiem_tra_doi_xung`:**
   - Kiểm tra chuỗi đối xứng đơn (`"radar"`, `"madam"` -> `True`).
   - Kiểm tra câu đối xứng có khoảng trắng (`"A nut for a jar of tuna"` -> `True`).
   - Kiểm tra chuỗi không đối xứng (`"python"` -> `False`).

5. **`test_chuyen_chu_hoa_dau_tu`:**
   - Kiểm tra viết hoa đầu mỗi từ (`"lap trinh python"` -> `"Lap Trinh Python"`).

6. **`test_loc_so_duong_chan`:**
   - Kiểm tra lọc mảng hỗn hợp âm, dương, số 0 (`[-4, -2, 0, 1, 2, 4, 5, 8]` -> `[2, 4, 8]`).
   - Kiểm tra mảng không có số dương chẵn (`[-1, -3, 0]` -> `[]`).

---

## ✍️ Hướng Dẫn Viết Thêm Bài Test Mới
Khi bạn bổ sung bài tập mới (ví dụ `bai2.py`), bạn chỉ cần tạo file `tests/test_bai2.py` theo mẫu:

```python
import unittest
import sys
import os

# Cho phép import mã nguồn từ thư mục gốc
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bai2 import ham_can_test

class TestBai2(unittest.TestCase):
    def test_chuc_nang_1(self):
        self.assertEqual(ham_can_test(dau_vao), ket_qua_mong_muon)

if __name__ == "__main__":
    unittest.main()
```
