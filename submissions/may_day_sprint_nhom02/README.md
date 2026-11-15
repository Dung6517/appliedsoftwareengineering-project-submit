# BKT Rule Engine
educational/synthetic — not for clinical use
- Nhóm: n02
- Tóm tắt sản phẩm: Hiện thực Rule Engine phân loại mức độ phản vệ / sốc phản vệ cho bài Hackathon BKT-1 (Track A), môn Kỹ thuật Phần mềm Ứng dụng (KTPMUD).
- Cài đặt, chạy và kiểm thử từ clean checkout:
```bash
# 1. Cài đặt thư viện
pip install -r requirements.txt

# 2. Chạy toàn bộ unit tests
pytest -q

# 3. Chạy benchmark đo độ trễ (p50/p95)
python benchmark.py
```
- Slide/demo: `slides/`
