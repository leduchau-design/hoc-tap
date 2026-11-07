# 📝 Ghi Chú Mẫu: Nhập Môn Lập Trình Python

*File mẫu này giúp bạn trải nghiệm việc ghi chép bài học bằng Markdown thay vì Word. Bạn có thể mở và sửa file này trực tiếp trên điện thoại, web GitHub hoặc VS Code bất cứ lúc nào.*

---

## 📌 1. Các Kiểu Dữ Liệu Cơ Bản Trong Python

| Kiểu dữ liệu | Tên gọi | Ví dụ | Ý nghĩa |
| :--- | :--- | :--- | :--- |
| `int` | Số nguyên | `x = 10`, `y = -5` | Lưu các số nguyên |
| `float` | Số thực | `pi = 3.14159` | Lưu các số thập phân |
| `str` | Chuỗi ký tự | `name = "Lê Đức Hậu"` | Lưu văn bản, ký tự |
| `bool` | Đúng / Sai | `is_passed = True` | Chỉ nhận giá trị `True` hoặc `False` |
| `list` | Danh sách | `scores = [8.5, 9.0, 10.0]` | Mảng có thể thay đổi giá trị |

---

## 🧮 2. Công Thức Toán Học Trong Lập Trình ($\LaTeX$)

Markdown hỗ trợ viết các công thức toán học cực đẹp mà không cần dùng MathType như Word:

- Công thức tính phương trình bậc 2:
  $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

- Công thức tính tổng lũy thừa bài tập Câu 2:
  $$S(n) = \sum_{i=1}^{n} i^i = 1^1 + 2^2 + 3^3 + \dots + n^n$$

---

## 💻 3. Đoạn Code Mẫu (Syntax Highlighting)

```python
def kiem_tra_so_nguyen_to(n: int) -> bool:
    """Hàm kiểm tra số nguyên tố tối ưu O(sqrt(n))"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chạy thử
for so in [2, 3, 4, 7, 10, 13]:
    print(f"{so} là số nguyên tố? {kiem_tra_so_nguyen_to(so)}")
```

---

## 💡 4. Mẹo Khi Dùng Markdown
- Nhấn phím dấu chấm **`.`** khi xem repo trên web GitHub để mở trình soạn thảo online trực tiếp.
- Mọi ghi chú viết bằng Markdown đều nhẹ dưới 5 KB và tự động đồng bộ lên GitHub ngay khi chạy `push_changes.bat`.
