# SECURITY & PRIVACY CHECKLIST — Nhóm 02 (Track A: Dr May Day)

## 1. Ranh giới dữ liệu & Môi trường
- [x] **Không dùng dữ liệu thật:** Toàn bộ dữ liệu đầu vào trong unit test, fixture và benchmark đều là dữ liệu tổng hợp/hư cấu (synthetic), không chứa thông tin bệnh nhân thật (PII/PHI).
- [x] **Cô lập môi trường:** Không kết nối starter repo với hệ thống production, Railway hoặc cơ sở dữ liệu thật.
- [x] **Quản lý bí mật (Secrets):** Không commit API key, token, cookie, mật khẩu thật hoặc file `.env` lên repository `Dung6517/bkt-2026-v1` và PR nộp bài.

## 2. An toàn miền nghiệp vụ & Truy vết
- [x] **Khóa quy tắc lâm sàng:** `rule_engine/classifier.py` hiện thực đúng `docs/decision-table.md` và các phán quyết làm rõ (#15, #31), không tự suy diễn ngưỡng lâm sàng mới.
- [x] **Không đưa lời khuyên điều trị (A-05):** Trường `ly_do` chỉ nêu tên kịch bản/quy tắc kích hoạt (`R-SOC`, `R01-PV`, `R02-PV`, `R03-PV`), không chứa chỉ định y khoa hay hướng dẫn điều trị.
- [x] **Audit log tối giản 4 trường (A-06):** Hàm `classify_and_audit()` chỉ ghi đúng 4 trường `[Timestamp, User_UUID, Action_Type, Status]` vào `audit.log`; tuyệt đối không ghi triệu chứng, tuổi hay chỉ số huyết áp thô.
- [x] **Cảnh báo mục đích sử dụng (A-11):** `README.md` đã ghi rõ tuyên bố `"educational/synthetic — not for clinical use"`.

## 3. Rà soát phụ thuộc & AI Boundary
- [x] **Phụ thuộc tối giản:** Lõi `rule_engine/classifier.py` chỉ sử dụng thư viện chuẩn của Python (`datetime`, `json`, `typing`), không dùng thư viện ngoài có license không tương thích và không dùng ML/DL.
- [x] **Kiểm chứng đầu ra AI:** Mọi đoạn mã và tài liệu có sự hỗ trợ của AI đều được thành viên nhóm rà soát thủ công, đối chiếu với `docs/decision-table.md` và kiểm chứng qua `pytest`.