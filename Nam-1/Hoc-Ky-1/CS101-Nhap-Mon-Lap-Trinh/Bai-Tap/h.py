"""
Bài tập Lập trình Python & Ôn tập đề thi
Bao gồm các hàm xử lý số học, chuỗi ký tự và danh sách.
Hỗ trợ cả chạy tự động kiểm thử và chạy tương tác nhập dữ liệu từ bàn phím.
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
    return [x for x in danh_sach if x > 0 and x % 2 == 0]


if __name__ == "__main__":
    print("=" * 68)
    print("       CHƯƠNG TRÌNH ÔN TẬP LẬP TRÌNH PYTHON - NHẬP DỮ LIỆU TỰ DO       ")
    print("=" * 68)

    # 1. Nhập số nguyên n từ bàn phím để kiểm tra câu 1 và câu 2
    try:
        n_str = input("👉 [Câu 1 & 2] Nhập số nguyên n bất kỳ (ví dụ: 6, 28): ").strip()
        if n_str:
            n = int(n_str)
            print(f"   [+] Tổng các ước số của {n} : {tong_uoc_so(n)}")
            if n <= 8:
                print(f"   [+] Tổng lũy thừa S({n})    : {tinh_tong_luy_thua(n)}")
            else:
                print(f"   [+] n = {n} khá lớn, bỏ qua tính lũy thừa để tránh tràn số.")
    except ValueError:
        print("   ⚠️ Giá trị vừa nhập không phải số nguyên hợp lệ!")

    # 2. Nhập chuỗi s để kiểm tra câu 3, câu 4, câu 5
    print()
    s = input("👉 [Câu 3, 4, 5] Nhập một chuỗi ký tự bất kỳ (ví dụ: 'Lap Trinh Python'): ")
    print(f"   [+] Số chữ in thường           : {dem_chu_thuong(s)}")
    print(f"   [+] Chuỗi có đối xứng không?   : {kiem_tra_doi_xung(s)}")
    print(f"   [+] Chuyển hoa đầu mỗi từ      : {chuyen_chu_hoa_dau_tu(s)}")

    # 3. Nhập danh sách số cách nhau bởi khoảng trắng để kiểm tra câu 6
    print()
    raw_list = input("👉 [Câu 6] Nhập các số nguyên cách nhau bằng khoảng trắng (ví dụ: -2 0 1 4 8): ").strip()
    if raw_list:
        try:
            danh_sach = [int(x) for x in raw_list.split()]
            print(f"   [+] Mảng ban đầu               : {danh_sach}")
            print(f"   [+] Các số nguyên dương chẵn   : {loc_so_duong_chan(danh_sach)}")
        except ValueError:
            print("   ⚠️ Có phần tử trong dãy không phải số nguyên hợp lệ!")

    print("=" * 68)
