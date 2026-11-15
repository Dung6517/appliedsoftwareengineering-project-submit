# REQUIREMENTS — Dr May Day: Rule Engine Sprint (Track A)

## 1. Mục tiêu & Phạm vi (Scope)
- **Mục tiêu:** Hiện thực hàm `classify()` trong `rule_engine/classifier.py` để phân loại mức độ phản vệ/sốc phản vệ dựa trên Data Dictionary và bảng quyết định V1 tại `docs/decision-table.md`.
- **Trong phạm vi:**
  - Phân loại chính xác các mức nguy cơ theo `docs/decision-table.md`.
  - Trả về lý do (`ly_do`) truy vết được rule đã kích hoạt.
  - Ghi nhận audit trail gồm 4 trường: `[Timestamp, User_UUID, Action_Type, Status]`.
  - Đảm bảo độ trễ `p95 < 100 ms` qua benchmark tối thiểu 1.000 lần chạy.
- **Ngoài phạm vi:** Không tự suy diễn quy tắc lâm sàng ngoài `docs/decision-table.md`, không đưa lời khuyên điều trị, không dùng ML/DL, không lưu dữ liệu bệnh nhân thật.

## 2. Tiêu chí nghiệm thu (Acceptance Criteria)
- **A-01 & A-02:** `classify()` chạy đúng contract, không còn `NotImplementedError`, không hard-code theo public fixture.
- **A-03 & A-04:** Bao phủ đủ các mức phân loại; xử lý an toàn khi input thiếu trường, sai kiểu hoặc ngoài miền giá trị.
- **A-05:** Trả về `ly_do` truy vết được rule đã kích hoạt, không đưa lời khuyên điều trị.
- **A-06:** Audit log có đúng 4 trường, tuyệt đối không ghi triệu chứng hay dữ liệu nhạy cảm.
- **A-07 & A-08:** Có unit test cho normal, boundary, invalid, missing cases; `pytest -q` pass từ clean checkout.
- **A-09 & A-10:** CI tự chạy test trên Pull Request; benchmark >= 1.000 lần đạt `p95 < 100 ms`.
- **A-11:** `README.md` ghi rõ *"educational/synthetic — not for clinical use"*.

## 3. Quy tắc làm rõ & Xử lý biên (Theo thông báo #15 và phán quyết #31)
1. **Thứ tự ưu tiên kịch bản Tầng 2 (`PHAN_VE`):**
   - Đánh giá theo thứ tự ưu tiên cứng: **`R01-PV` > `R02-PV` > `R03-PV`**.
   - Nếu bệnh nhân đồng thời thỏa mãn nhiều kịch bản ở Tầng 2, hệ thống chọn kịch bản có độ ưu tiên cao nhất theo thứ tự trên.
   - Sau khi đạt Tầng 2, hệ thống tiếp tục kiểm tra điều kiện tụt huyết áp tâm thu theo tuổi ở Tầng 1: nếu thỏa mãn thì nâng mức phân loại lên `SOC_PHAN_VE` (`rule_id = "R-SOC"`).

2. **Cách chọn `rule_id` đại diện:**
   - Khi `muc_do = "SOC_PHAN_VE"`: `rule_id` luôn là `"R-SOC"`.
   - Khi `muc_do = "PHAN_VE"`: `rule_id` là mã kịch bản đầu tiên khớp theo thứ tự ưu tiên `R01-PV` → `R02-PV` → `R03-PV`.
   - Khi `muc_do = "THEO_DOI"`: `rule_id` luôn là `null` (`None` trong Python).

3. **Quy tắc so sánh "giảm > 30%" ở nhóm tuổi ≥ 18:**
   - Hiểu là **lớn hơn hẳn** (`>`): `(huyet_ap_tam_thu_nen - huyet_ap_tam_thu) / huyet_ap_tam_thu_nen > 0.30`.
   - Trường hợp giảm đúng bằng 30.0% (ví dụ: nền `130`, hiện tại `91`) **không** được tính là tụt huyết áp theo tiêu chí này.

4. **Xử lý cụ thể khi thiếu khóa hoặc giá trị `null` ở từng trường:**
   - **`tuoi` bị thiếu hoặc `null`:** Không ném lỗi; trả về ngay `{"muc_do": "THEO_DOI", "rule_id": null, ...}` do không xác định được ngưỡng huyết áp theo nhóm tuổi (chưa đủ dữ kiện kết luận).
   - **`huyet_ap_tam_thu` bị thiếu hoặc `null`:** Không thỏa điều kiện tụt huyết áp tâm thu ở Tầng 1 (không kích hoạt `R-SOC`), nhưng hệ thống vẫn tiếp tục đánh giá Tầng 2 bình thường để trả về `PHAN_VE` hoặc `THEO_DOI`.
   - **`huyet_ap_tam_thu_nen` bị thiếu hoặc `null`:** Bỏ qua điều kiện "giảm > 30%" ở nhóm ≥ 18 tuổi, chỉ xét ngưỡng `huyet_ap_tam_thu < 90`.
   - **Các khóa kiểu `bool` bị thiếu (`co_di_nguyen_nghi_ngo`, `di_nguyen_qua_duong_hit`, `co_ton_thuong_da_niem_mac`, `co_trieu_chung_ho_hap`, `co_trieu_chung_tuan_hoan`, `co_trieu_chung_tieu_hoa_nang`):** Mặc định hiểu là `false`. Tuyệt đối không gây lỗi `KeyError` và không tự ý hạ mức phân loại sai với bảng quyết định.

## 4. Kế hoạch kiểm thử (Test Plan)

| Mã ca | Nhóm | Đầu vào JSON tối thiểu | Kết quả mong đợi (`muc_do`, `rule_id`) |
| :--- | :--- | :--- | :--- |
| **TC-N01** | Normal | `{"tuoi": 25, "huyet_ap_tam_thu": 115, "co_di_nguyen_nghi_ngo": false, "co_ton_thuong_da_niem_mac": true, "co_trieu_chung_ho_hap": true}` | `("PHAN_VE", "R01-PV")` |
| **TC-N02** | Normal | `{"tuoi": 30, "huyet_ap_tam_thu": 110, "co_di_nguyen_nghi_ngo": true, "co_ton_thuong_da_niem_mac": true, "co_trieu_chung_tieu_hoa_nang": true}` | `("PHAN_VE", "R02-PV")` |
| **TC-N03** | Normal | `{"tuoi": 10, "huyet_ap_tam_thu": 95, "co_di_nguyen_nghi_ngo": true, "di_nguyen_qua_duong_hit": false, "co_trieu_chung_ho_hap": true}` | `("PHAN_VE", "R03-PV")` |
| **TC-N04** | Normal | `{"tuoi": 35, "huyet_ap_tam_thu": 80, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` | `("SOC_PHAN_VE", "R-SOC")` |
| **TC-N05** | Normal | `{"tuoi": 22, "huyet_ap_tam_thu": 120, "co_di_nguyen_nghi_ngo": true, "co_ton_thuong_da_niem_mac": true}` | `("THEO_DOI", null)` |
| **TC-N06** | Normal | `{"tuoi": 28, "huyet_ap_tam_thu": 110, "co_di_nguyen_nghi_ngo": true, "di_nguyen_qua_duong_hit": false, "co_ton_thuong_da_niem_mac": true, "co_trieu_chung_ho_hap": true}` (Khớp cả R02 & R03 → ưu tiên R02) | `("PHAN_VE", "R02-PV")` |
| **TC-B01** | Boundary | `{"tuoi": 0.5, "huyet_ap_tam_thu": 69, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Nhóm 0–<1t, HATT < 70) | `("SOC_PHAN_VE", "R-SOC")` |
| **TC-B02** | Boundary | `{"tuoi": 0.5, "huyet_ap_tam_thu": 70, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Nhóm 0–<1t, HATT = 70) | `("PHAN_VE", "R03-PV")` |
| **TC-B03** | Boundary | `{"tuoi": 5, "huyet_ap_tam_thu": 79, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Nhóm 1–<11t, ngưỡng 70+2×5=80) | `("SOC_PHAN_VE", "R-SOC")` |
| **TC-B04** | Boundary | `{"tuoi": 11, "huyet_ap_tam_thu": 89, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Nhóm 11–<18t, HATT < 90) | `("SOC_PHAN_VE", "R-SOC")` |
| **TC-B05** | Boundary | `{"tuoi": 18, "huyet_ap_tam_thu": 91, "huyet_ap_tam_thu_nen": 130, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Giảm đúng 30.0%) | `("PHAN_VE", "R03-PV")` |
| **TC-B06** | Boundary | `{"tuoi": 18, "huyet_ap_tam_thu": 90, "huyet_ap_tam_thu_nen": 130, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Giảm 30.77% > 30%) | `("SOC_PHAN_VE", "R-SOC")` |
| **TC-M01** | Missing | `{"co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Thiếu `tuoi`) | `("THEO_DOI", null)` |
| **TC-M02** | Missing | `{"tuoi": null, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (`tuoi` là `null`) | `("THEO_DOI", null)` |
| **TC-M03** | Missing | `{"tuoi": 25, "huyet_ap_tam_thu": null, "co_di_nguyen_nghi_ngo": false, "co_ton_thuong_da_niem_mac": true, "co_trieu_chung_ho_hap": true}` (Thiếu HATT) | `("PHAN_VE", "R01-PV")` |
| **TC-M04** | Missing | `{"tuoi": 25, "co_ton_thuong_da_niem_mac": true, "co_trieu_chung_ho_hap": true}` (Thiếu toàn bộ các khóa `bool` khác → mặc định `false`) | `("PHAN_VE", "R01-PV")` |
| **TC-I01** | Invalid | `{}` (Input rỗng, không có trường nào) | `("THEO_DOI", null)` |
| **TC-I02** | Invalid | `{"tuoi": -1, "huyet_ap_tam_thu": 100, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Tuổi âm) | `("THEO_DOI", null)` |
| **TC-I03** | Invalid | `{"tuoi": 25, "huyet_ap_tam_thu": -50, "co_di_nguyen_nghi_ngo": true, "co_trieu_chung_tuan_hoan": true}` (Huyết áp âm) | `("PHAN_VE", "R03-PV")` |
| **TC-I04** | Invalid | `{"tuoi": "hai mươi", "huyet_ap_tam_thu": 100}` (Sai kiểu dữ liệu) | `("THEO_DOI", null)` |

*(Ghi chú kiểm thử bổ sung: Ngoài bảng trên, bộ test tự động còn kiểm tra tính chất Audit & Explainability: log chỉ gồm 4 trường `[Timestamp, User_UUID, Action