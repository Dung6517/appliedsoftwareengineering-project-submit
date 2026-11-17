# AI USAGE REPORT — Nhóm 02 (Track A: Dr May Day)

## 1. Tuyên bố sử dụng AI
Nhóm 02 xác nhận có sử dụng các công cụ Trí tuệ Nhân tạo (AI) trong quá trình nghiên cứu, thiết kế, lập trình và kiểm thử cho bài tập lớn KTPMUD Track A. Mọi kết quả do AI sinh ra đều được thành viên trong nhóm trực tiếp kiểm chứng, rà soát logic y khoa theo `docs/decision-table.md` và chạy kiểm thử tự động qua `pytest`.

## 2. Danh mục công cụ AI & Phạm vi ứng dụng
| STT | Công cụ AI | Nhà cung cấp | Phạm vi ứng dụng / Nhiệm vụ hỗ trợ | Mức độ kiểm soát của con người |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Gemini** | Google | Hỗ trợ phân tích đề bài, quy chế KTPMUD V1, thiết kế cấu trúc rule engine, viết code Python (`classifier.py`, `benchmark.py`) và soạn thảo tài liệu báo cáo kỹ thuật. | **Chủ đạo (100%)**: Thành viên nhóm trực tiếp đọc hiểu, review toàn bộ code, chạy và nghiệm thu kết quả qua unit test. |
| **2** | **Claude** | Anthropic | Hỗ trợ tham vấn cấu trúc kịch bản kiểm thử (test cases) và tối ưu hóa cách xử lý ngoại lệ cho các trường hợp thiếu dữ liệu (`missing` / `invalid`). | **Tham khảo & Chỉnh sửa**: Thành viên nhóm chọn lọc, tinh chỉnh lại để khớp tuyệt đối với 5 quy tắc làm rõ của đề bài. |