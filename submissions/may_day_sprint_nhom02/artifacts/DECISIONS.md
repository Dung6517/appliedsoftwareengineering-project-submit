# DECISIONS (Architecture Decision Records)

## ADR-001: Thiết kế Rule Engine tất định (Deterministic)
* **Trạng thái:** Đã chốt
* **Bối cảnh:** Cần phân loại chính xác 100% theo `docs/decision-table.md`, dễ giải thích và đạt hiệu năng cao (`p95 < 100 ms`).
* **Quyết định:** Sử dụng cấu trúc điều kiện rẽ nhánh tuần tự (kiểm tra input $\rightarrow$ Tầng 2: Phản vệ $\rightarrow$ Tầng 1: Sốc phản vệ).
* **Lý do:** Tốc độ thực thi cực nhanh (micro-seconds), không phụ thuộc thư viện nặng, dễ truy vết chính xác `rule_id` nào vừa kích hoạt để điền vào `ly_do`.

## ADR-002: Cô lập dữ liệu nhạy cảm trong Audit Trail
* **Trạng thái:** Đã chốt
* **Bối cảnh:** Đề bài yêu cầu ghi audit nhưng cấm lộ triệu chứng, điểm số sức khỏe hoặc PII.
* **Quyết định:** Tách riêng lớp ghi nhận audit, chỉ truyền vào đúng 4 tham số `[Timestamp, User_UUID, Action_Type, Status]` sau khi `classify()` chạy xong; tuyệt đối không truyền raw input dict vào logger.