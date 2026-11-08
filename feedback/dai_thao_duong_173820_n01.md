# Góp ý — 173820_n01 (CS-5: Đái tháo đường type 2)

- **Bài nộp:** báo cáo quá trình tuần 6 + slide — giảng viên đã đưa lên [`submissions/dai_thao_duong_173820_n01/`](../submissions/dai_thao_duong_173820_n01/) theo template chuẩn
- **Ngày góp ý:** 21/10/2026
- **Kết quả kiểm tra tự động:** ✅ hợp lệ (`scripts/validate_submission.py`)

## Đề tài đã được duyệt

Đề "Hỗ trợ người chăm sóc theo dõi điều trị ngoại trú đái tháo đường type 2" đã được thêm vào
[ngân hàng case study](https://fossbk-spec.github.io/ktpmud-book/do_an_mon_hoc) là **CS-5**, slug
`dai_thao_duong`. Trang chi tiết của CS-5 trỏ tới thư mục bài nộp của nhóm.

## Bài nộp và các tuần sau

Bài tuần 6 của nhóm **đã có trong repo** tại [`submissions/dai_thao_duong_173820_n01/`](../submissions/dai_thao_duong_173820_n01/), đúng
template chuẩn (`submission.json`, `README.md`, `report/`, `slides/`, `src/`):

- [`README.md`](../submissions/dai_thao_duong_173820_n01/README.md)
- [`report/BaoCao_Tuan6.docx`](../submissions/dai_thao_duong_173820_n01/report/BaoCao_Tuan6.docx)
- [`slides/Slide_Tuan6.pptx`](../submissions/dai_thao_duong_173820_n01/slides/Slide_Tuan6.pptx)
- [`submission.json`](../submissions/dai_thao_duong_173820_n01/submission.json)

Nhóm kiểm tra lại `submission.json` (MSSV, thành viên) và `README.md`; nếu sai thì sửa qua PR như
bên dưới.

**Từ tuần sau**, nhóm tự nộp bằng Pull Request từ fork theo
[HUONG_DAN_NOP_BAI.md](../HUONG_DAN_NOP_BAI.md):

1. Fork `fossbk-spec/ktpmud-project` (fork cũ thì bấm **Sync fork** trước), tạo nhánh
   `submit/dai_thao_duong-173820_n01`.
2. **Thêm file mới** vào đúng thư mục `submissions/dai_thao_duong_173820_n01/` (vd `report/BaoCao_Tuan8.docx`, mã nguồn
   trong `src/`), cập nhật `README.md` nếu cần. Không sửa thư mục của nhóm khác.
3. Mở Pull Request vào `main`. Bot bình luận ✅/❌ trong khoảng 1 phút; nếu ❌ thì sửa và push lên
   **cùng nhánh**, không mở PR mới.

## Cần cập nhật

1. **Kiểm tra `submission.json`** — đúng MSSV, đủ thành viên.
2. **Chốt ngôn ngữ/framework backend.** Bảng C2 trong báo cáo ghi "ngôn ngữ cần chốt"; ghi rõ lựa
   chọn và lý do trong báo cáo tuần sau.
3. **Mã nguồn và cách chạy lại.** Từ Sprint tuần 8, đưa mã nguồn vào `src/` và điền mục "Cách chạy
   lại" trong `README.md` (cài đặt, lệnh chạy, nạp dữ liệu synthetic mẫu).
4. **Các tuần sau nộp bằng PR mới**, thêm file mới (vd `report/BaoCao_Tuan8.docx`). Bài đã merge
   không sửa được qua PR thường.
5. **Quy tắc file:** tên không dấu, không khoảng trắng, không họ tên; mỗi file < 10MB; không commit
   khoá API, token, `.env`.

---

## Slide tuần 6 bản v2 — PR #12 (góp ý 08/11/2026)

- **Bài nộp:** `slides/Slide_Tuan6_v2.pptx` (PR #12). Bổ sung file mới, bản gốc `Slide_Tuan6.pptx` giữ nguyên.
- **Kiểm tra tự động:** ✅ hợp lệ

### Thay đổi so với bản gốc

- ✅ Thêm 2 slide liệt kê đủ FR-01 → FR-20, có mức ưu tiên và truy ngược về vấn đề P1–P7.
- ✅ NFR được viết lại thành NFR-01 → NFR-11, gắn với đặc tính ISO/IEC 25010, mỗi NFR có mục tiêu định lượng và cách kiểm chứng. NFR-05 nêu rõ không lưu họ tên thật hay số định danh, và dùng mã `BN-TEST-xxx`.
- Sắp xếp lại thứ tự các slide user story.

### Cần cập nhật (bổ sung cho các mục ở trên)

1. **Backend vẫn chưa chốt ngôn ngữ/framework.** Slide C2 chỉ ghi "Backend API: Nghiệp vụ và Rule Engine". Mục 2 phía trên vẫn còn hiệu lực.
2. **Bối cảnh bệnh viện.** Slide 5 ghi phạm vi "Ngoại trú BV Hữu Nghị". Nhóm ghi rõ đây là **bối cảnh mô phỏng**: không tích hợp hệ thống bệnh viện (khớp với slide C1) và không dùng dữ liệu bệnh nhân thật. Dẫn bài báo về bệnh án điện tử của bệnh viện thì được, nhưng không nên viết như thể hệ thống được triển khai tại đó.
3. **"Kênh bệnh nhân: Chưa chốt"** (slide 5) và **ngưỡng bỏ lỡ 120 phút** ("cần ý kiến bác sĩ") cần được chốt hoặc ghi thành giả định có chủ đích, trước khi bắt đầu code các FR liên quan (FR-10, FR-12).
4. Lần sau, nếu chỉ sửa slide của tuần đã nộp, nhóm nên ghi tóm tắt thay đổi trong mô tả PR (mô tả PR #12 đang trống).
