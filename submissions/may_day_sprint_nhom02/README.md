# KTPMUD BKT-1 (Track A) — Dr May Day: Rule Engine Sprint

> **Lưu ý:** educational/synthetic — not for clinical use

Hiện thực Rule Engine phân loại mức độ phản vệ / sốc phản vệ cho bài **Hackathon BKT-1 (Track A)**, môn Kỹ thuật Phần mềm Ứng dụng (KTPMUD).

## Bối cảnh & Ranh giới an toàn

- **Đặc tả chính thức (Data Dictionary + Bảng quyết định V1):** [`docs/decision-table.md`](docs/decision-table.md). Đây là nguồn sự thật duy nhất (Single Source of Truth).
- Không tự suy diễn ngưỡng hay quy tắc lâm sàng mới ngoài `docs/decision-table.md`.
- Chỉ sử dụng dữ liệu giả lập (synthetic), không kết nối dữ liệu bệnh nhân thật và không đưa ra khuyến nghị điều trị.

## Thành phần chính

- `rule_engine/classifier.py`:
  - `classify(patient)`: Phân loại theo 2 tầng (`SOC_PHAN_VE`, `PHAN_VE`, `THEO_DOI`) kèm `rule_id` và `ly_do` truy vết được.
  - `classify_and_audit(patient, user_uuid)`: Gọi `classify()` và ghi audit trail 4 trường `[Timestamp, User_UUID, Action_Type, Status]` vào `audit.log` (không log thông tin lâm sàng hay PII).
- `tests/test_classifier.py`: Bộ unit test (`pytest`) kiểm tra đủ các mức phân loại, ca biên, input thiếu/sai kiểu và kiểm tra audit trail.
- `benchmark.py`: Đo hiệu năng (100 lần warm-up + 1.000 lần chạy chính thức), báo cáo `p50` và `p95` (`p95 < 100 ms`).
- `REQUIREMENTS.md` & `DECISIONS.md`: Phân tích yêu cầu, tiêu chí nghiệm thu (A-01 đến A-11) và các quyết định kiến trúc (ADR).

## Cài đặt, Kiểm thử & Benchmark

```bash
# 1. Cài đặt thư viện
pip install -r requirements.txt

# 2. Chạy toàn bộ unit tests
pytest -q

# 3. Chạy benchmark đo độ trễ (p50/p95)
python benchmark.py
```

## Lưu ý nộp bài

- Bộ test công khai dùng để kiểm chứng các ca cơ bản, biên và lỗi; GV/TA sẽ chấm điểm bổ sung bằng bộ test ẩn riêng.
- Nộp bài qua `ktpmud-project` theo đúng hướng dẫn `nop_bai.md` của môn học.