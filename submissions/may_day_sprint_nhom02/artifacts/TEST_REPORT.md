# TEST REPORT — Nhóm 02 (Track A: Dr May Day)

## 1. Môi trường kiểm thử & Cấu hình máy đo (Tiêu chí A-10)
- **Hệ điều hành:** `Windows-11-10.0.26200-SP0`
- **Vi xử lý (CPU):** `Intel64 Family 6 Model 154 Stepping 3, GenuineIntel`
- **Phiên bản Python:** `Python 3.13.16` (môi trường ảo `.venv`)
- **Framework kiểm thử:** `pytest 9.2.0`
- **Mã nguồn kiểm thử:** `Dung6517/bkt-2026-v1` (`rule_engine/classifier.py`, `tests/test_classifier.py`, `benchmark.py`)

## 2. Kết quả kiểm thử tự động (Unit & Integration Tests — Tiêu chí A-07, A-08)
- **Lệnh thực thi:** `pytest -v`
- **Kết quả tổng quan:** **22/22 test cases PASSED (100%)** trong `0.14s`.

| Nhóm kiểm thử | Mã ca kiểm thử | Số lượng | Trạng thái | Nội dung xác minh |
| :--- | :--- | :---: | :---: | :--- |
| **Normal** | `TC-N01` → `TC-N06` | 6 | PASSED | Phân loại đúng `R01-PV`, `R02-PV`, `R03-PV`, `R-SOC`, `THEO_DOI` và thứ tự ưu tiên `R01-PV > R02-PV > R03-PV`. |
| **Boundary** | `TC-B01` → `TC-B06` | 6 | PASSED | Đúng ngưỡng HATT theo 4 nhóm tuổi (`0–<1`, `1–<11`, `11–<18`, `≥18`) và ranh giới giảm đúng `30.0%` vs `> 30%`. |
| **Missing** | `TC-M01` → `TC-M04` | 4 | PASSED | Thiếu/null `tuoi` trả về `THEO_DOI`; thiếu `huyet_ap_tam_thu` vẫn xét Tầng 2; thiếu khóa `bool` mặc định `False`. |
| **Invalid** | `TC-I01` → `TC-I04` + Non-dict | 5 | PASSED | Input rỗng `{}`, `None`, tuổi âm, sai kiểu dữ liệu trả về `THEO_DOI` an toàn; HATT âm bỏ qua Tầng 1. |
| **Audit & Explainability** | `test_audit_trail_...` | 1 | PASSED | `classify_and_audit()` ghi đúng 4 trường `[Timestamp, User_UUID, Action_Type, Status]`, không chứa PII hay lời khuyên điều trị. |

## 3. Kết quả đo hiệu năng (Benchmark — Tiêu chí A-10)
- **Lệnh thực thi:** `python benchmark.py`
- **Phương pháp đo:** Chạy làm nóng (warm-up) **100 lần**, sau đó đo thời gian thực thi bằng `time.perf_counter()` qua **1.000 lần chạy** liên tiếp trên dữ liệu synthetic chuẩn.
- **Số liệu thực tế:**
  - **p50 (trung vị):** `0.0007 ms`
  - **p95 (phân vị 95):** `0.0007 ms`
  - **Đánh giá ngưỡng (`p95 < 100 ms`):** **PASSED**

## 4. Giới hạn hiện tại (Limitations)
- Kết quả benchmark được đo trực tiếp ở mức gọi hàm Python trong bộ nhớ (in-process) trên môi trường cục bộ, chưa bao gồm độ trễ mạng hay lớp giao thức HTTP/REST API.
- Bộ dữ liệu kiểm thử hiện tại sử dụng các kịch bản synthetic bao phủ toàn bộ 20 ca trong `REQUIREMENTS.md` và `docs/decision-table.md` V1; chưa mở rộng cho các quy tắc ngoài phạm vi V1.