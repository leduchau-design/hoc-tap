import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

big = []
for r, d, fs in os.walk("."):
    if ".git" in r:
        continue
    for f in fs:
        fp = os.path.join(r, f)
        try:
            sz = os.path.getsize(fp)
            if sz > 95 * 1024 * 1024:
                big.append((f, sz / (1024 * 1024)))
        except OSError:
            pass

if big:
    print("\n[⚠️ CẢNH BÁO DUNG LƯỢNG] Phát hiện file vượt quá 95MB:")
    for f, mb in big:
        print(f"  - {f} ({mb:.1f} MB)")
    print("GitHub giới hạn 100MB/file. Vui lòng tải lên Google Drive hoặc dùng Git LFS!\n")
else:
    print("  [OK] Tất cả các file đều an toàn dưới 95MB.")
