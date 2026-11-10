# REQUIREMENTS — Dr May Day: Rule Engine Sprint (Track A)

## 1. Mục tiêu & Phạm vi (Scope)
* **Mục tiêu:** Hiện thực hàm `classify()` trong `rule_engine/classifier.py` để phân loại mức độ phản vệ/sốc phản vệ dựa trên Data Dictionary và bảng quyết định V1 tại `docs/decision-table.md`.
* **Trong phạm vi:**
  * Phân loại chính xác các mức nguy cơ theo `docs/decision-table.md`.
  * Trả về lý do (`ly_do`) truy vết được rule đã kích hoạt.
  * Ghi nhận audit trail gồm 4 trường: `[Timestamp, User_UUID, Action_Type, Status]`.
  * Đảm bảo độ trễ `p95 < 100 ms` qua benchmark tối thiểu 1.000 lần chạy.
* **Ngoài phạm vi:** Không tự suy diễn quy tắc lâm sàng ngoài `docs/decision-table.md`, không đưa lời khuyên điều trị, không dùng ML/DL, không lưu dữ liệu bệnh nhân thật.

## 2. Tiêu chí nghiệm thu (Acceptance Criteria)
* **A-01 & A-02:** `classify()` chạy đúng contract, không còn `NotImplementedError`, không hard-code theo public fixture.
* **A-03 & A-04:** Bao phủ đủ các mức phân loại; xử lý an toàn khi input thiếu trường, sai kiểu hoặc ngoài miền giá trị.
* **A-05:** Trả về `ly_do` truy vết được rule đã kích hoạt, không đưa lời khuyên điều trị.
* **A-06:** Audit log có đúng 4 trường, tuyệt đối không ghi triệu chứng hay dữ liệu nhạy cảm.
* **A-07 & A-08:** Có unit test cho normal, boundary, invalid, missing cases; `pytest -q` pass từ clean checkout.
* **A-09 & A-10:** CI tự chạy test trên Pull Request; benchmark >= 1.000 lần đạt `p95 < 100 ms`.
* **A-11:** `README.md` ghi rõ *"educational/synthetic — not for clinical use"*.

## 3. Kế hoạch kiểm thử (Test Plan)
1. **Normal cases:** Tối thiểu 1 test case cho mỗi mức nguy cơ trong bảng quyết định.
2. **Boundary cases:** Các giá trị nằm sát ngưỡng chuyển mức (ngưỡng tuổi, huyết áp tâm thu).
3. **Invalid & Missing cases:** Input rỗng, thiếu trường `tuoi`, sai kiểu dữ liệu, giá trị âm/ngoài miền.
4. **Audit & Explainability:** Kiểm tra log chỉ chứa đúng 4 trường quy định và `ly_do` không chứa lời khuyên điều trị.