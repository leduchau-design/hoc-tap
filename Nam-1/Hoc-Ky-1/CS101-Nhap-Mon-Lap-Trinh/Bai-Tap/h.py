"""
Bài tập Lập trình Python & Ôn tập đề thi
Bao gồm các hàm xử lý số học, chuỗi ký tự và danh sách.
"""

def tong_uoc_so(n: int) -> int:
    """Tính tổng tất cả các ước số nguyên dương của n."""
    if n <= 0:
        return 0
    return sum(i for i in range(1, n + 1) if n % i == 0)


def tinh_tong_luy_thua(n: int) -> int:
    """Tính S(n) = 1 + 2^2 + 3^3 + ... + n^n."""
    if n <= 0:
        return 0
    return sum(i ** i for i in range(1, n + 1))


def dem_chu_thuong(s: str) -> int:
    """Đếm số lượng ký tự chữ thường có trong chuỗi s."""
    return sum(1 for c in s if c.islower())


def kiem_tra_doi_xung(s: str) -> bool:
    """Kiểm tra xem chuỗi s có phải là chuỗi đối xứng (palindrome) hay không."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def chuyen_chu_hoa_dau_tu(s: str) -> str:
    """Đổi tất cả các ký tự đầu tiên của mỗi từ thành chữ hoa."""
    return s.title()


def loc_so_duong_chan(danh_sach: list[int]) -> list[int]:
    """Lọc và trả về các số nguyên dương chẵn có trong danh sách."""
    return [x for x in danh_sach if x > 0 and x % 2 != 0]


if __name__ == "__main__":
    print("--- CHƯƠNG TRÌNH ÔN TẬP LẬP TRÌNH PYTHON ---")
    n = 6
    print(f"Tổng ước số của {n}: {tong_uoc_so(n)}")
    print(f"Tổng lũy thừa S({n}): {tinh_tong_luy_thua(3)}")
    
    chuoi = "Lap Trinh Python"
    print(f"Số chữ thường trong '{chuoi}': {dem_chu_thuong(chuoi)}")
    print(f"Chuỗi 'radar' đối xứng? {kiem_tra_doi_xung('radar')}")
    
    lst = [-2, 0, 1, 4, 7, 8, 10, -6]
    print(f"Số dương chẵn trong {lst}: {loc_so_duong_chan(lst)}")
