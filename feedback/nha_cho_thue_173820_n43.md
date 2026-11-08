# Góp ý — 173820_n43 (CS-6: Quản lý nhà cho thuê)

- **Bài nộp:** báo cáo quá trình tuần 6 + slide — giảng viên đã đưa lên [`submissions/nha_cho_thue_173820_n43/`](../submissions/nha_cho_thue_173820_n43/) theo template chuẩn
- **Ngày góp ý:** 21/10/2026
- **Kết quả kiểm tra tự động:** ✅ hợp lệ (`scripts/validate_submission.py`)

## Đề tài đã được duyệt

Đề "Xây dựng phần mềm quản lý nhà cho thuê" đã được thêm vào
[ngân hàng case study](https://fossbk-spec.github.io/ktpmud-book/do_an_mon_hoc) là **CS-6**, slug
`nha_cho_thue` (đề ngoài y tế). Trang chi tiết của CS-6 trỏ tới thư mục bài nộp của nhóm, nên link
chỉ mở được sau khi PR của nhóm được merge.

## Bài nộp và các tuần sau

Bài tuần 6 của nhóm **đã có trong repo** tại [`submissions/nha_cho_thue_173820_n43/`](../submissions/nha_cho_thue_173820_n43/), đúng
template chuẩn (`submission.json`, `README.md`, `report/`, `slides/`, `src/`):

- [`README.md`](../submissions/nha_cho_thue_173820_n43/README.md)
- [`report/BaoCao_Tuan6.docx`](../submissions/nha_cho_thue_173820_n43/report/BaoCao_Tuan6.docx)
- [`slides/Slide_Tuan6.pptx`](../submissions/nha_cho_thue_173820_n43/slides/Slide_Tuan6.pptx)
- [`submission.json`](../submissions/nha_cho_thue_173820_n43/submission.json)

Nhóm kiểm tra lại `submission.json` (MSSV, thành viên) và `README.md`; nếu sai thì sửa qua PR như
bên dưới.

**Từ tuần sau**, nhóm tự nộp bằng Pull Request từ fork theo
[HUONG_DAN_NOP_BAI.md](../HUONG_DAN_NOP_BAI.md):

1. Fork `fossbk-spec/ktpmud-project` (fork cũ thì bấm **Sync fork** trước), tạo nhánh
   `submit/nha_cho_thue-173820_n43`.
2. **Thêm file mới** vào đúng thư mục `submissions/nha_cho_thue_173820_n43/` (vd `report/BaoCao_Tuan8.docx`, mã nguồn
   trong `src/`), cập nhật `README.md` nếu cần. Không sửa thư mục của nhóm khác.
3. Mở Pull Request vào `main`. Bot bình luận ✅/❌ trong khoảng 1 phút; nếu ❌ thì sửa và push lên
   **cùng nhánh**, không mở PR mới.

## Cần cập nhật

1. **Chương 2 (công nghệ, cơ sở lý thuyết) còn trống**, và mục 1.7 để trống Frontend / Backend /
   Database. Chốt công nghệ, ghi lựa chọn và lý do.
2. **Bổ sung đặc tả theo chuẩn môn học** (xem [chương 2 của sách](https://fossbk-spec.github.io/ktpmud-book/ch02_yeu_cau_thiet_ke_c4)):
   user story + tiêu chí nghiệm thu, ma trận truy vết yêu cầu (RTM), kiến trúc C4 (ít nhất C1–C2),
   thiết kế dữ liệu (ERD).
3. **Trang bìa** còn ghi "9/2026"; cập nhật mục lục (*Update Field*) sau khi bổ sung nội dung.
4. **Dữ liệu người thuê:** hệ thống lưu họ tên, số điện thoại người thuê — khi demo và kiểm thử chỉ
   dùng dữ liệu giả lập, không dùng thông tin người thuê thật của nhà cho thuê đã khảo sát.
5. **Mã nguồn và cách chạy lại:** khi bắt đầu xây dựng, đưa mã nguồn vào `src/` và điền mục "Cách
   chạy lại" trong `README.md`.
6. **Các tuần sau nộp bằng PR mới**, thêm file mới (vd `report/BaoCao_Tuan8.docx`). Bài đã merge
   không sửa được qua PR thường. Tên file không dấu, không khoảng trắng, không họ tên; mỗi file
   < 10MB.

---

## Tuần 7 — PR #13 (góp ý 08/11/2026)

- **Bài nộp:** `report/BaoCao_Tuan7.docx`, `slides/Slide_Tuan7.pptx` (PR #13)
- **Kiểm tra tự động:** ✅ hợp lệ

### Đã làm theo góp ý tuần 6

- ✅ Chương 2 đã viết. Công nghệ đã chốt (React + Vite + Tailwind / Node.js + Express / PostgreSQL), có lý do lựa chọn.
- ✅ Có 29 user story, 32 yêu cầu chức năng, 11 yêu cầu phi chức năng có điều kiện đo, ma trận RTM (FR → US → Use Case), C4 mức C1–C2, ERD kèm mô tả bảng và ràng buộc.
- ✅ Trang bìa đã cập nhật thành 10/2026.

### Cần cập nhật

1. **Địa chỉ thật.** Tiêu đề báo cáo và slide 1 ghi "(Nhà 57 Giảng Võ)". Repo này công khai vĩnh viễn. Nhóm bỏ địa chỉ này, thay bằng mô tả chung, ví dụ "một khu nhà trọ/chung cư mini (bối cảnh mô phỏng)". Dữ liệu demo và kiểm thử chỉ dùng người thuê giả lập.
2. **User story chưa có tiêu chí nghiệm thu.** Mỗi US (ít nhất các US mức Must) cần 2–3 tiêu chí kiểm chứng được, viết dạng *Given/When/Then* hoặc danh sách điều kiện. Ví dụ US13: tạo hợp đồng thì phòng chuyển sang "Đang thuê"; phòng không trống thì bị từ chối kèm thông báo lỗi. RTM nên thêm cột **mã test** để điền dần khi viết test.
3. **Quy mô NFR không khớp phạm vi.** NFR01–NFR02 đặt điều kiện 10.000 phòng / 20.000 người thuê / 10.000 hóa đơn, trong khi phạm vi đề tài là nhà trọ, chung cư mini quy mô nhỏ (mục 1.6). Nhóm chọn quy mô sát thực tế (vd 200 phòng) hoặc giải thích lý do chọn số lớn. Nhóm cũng cần nêu cách tạo dữ liệu mẫu và công cụ đo (vd k6, JMeter).
4. **Một số điểm còn mâu thuẫn hoặc chưa chốt:**
   - Bảng 3-1 ghi Người thuê "Thanh toán ✓", nhưng không có FR nào cho người thuê thanh toán trên hệ thống. FR23 chỉ cho Chủ nhà xác nhận. Nhóm cần chốt: thanh toán ngoài hệ thống (Chủ nhà xác nhận) hay có thanh toán online.
   - Mục 1.6 gọi Người thuê là "Observer (giám sát)", nhưng người thuê vẫn gửi sự cố, sửa hồ sơ. Nên đổi tên vai trò, vd "Tenant".
   - Ràng buộc hợp đồng đang ghi điều kiện "*nếu* nghiệp vụ chỉ cho phép một người thuê chính mỗi phòng". Nhóm cần chốt: một phòng có cho nhiều người thuê cùng một hợp đồng hay không. Nếu cho phép, một hợp đồng sẽ gắn với nhiều người thuê, và cần thêm bảng trung gian giữa `contracts` và `tenants`.
   - FR17 (đơn giá và danh mục phí dịch vụ) chưa có bảng lưu trong ERD. `utility_readings` chỉ có đơn giá điện nước. Nhóm thêm bảng danh mục phí/đơn giá, hoặc ghi rõ phí dịch vụ được lưu ở đâu.
   - FR31–FR32 "gửi thông báo" cần chốt kênh gửi: trong ứng dụng, email hay Zalo. Chỉ ghi "tự động gửi" thì chưa kiểm thử được.
5. **Slide:** slide 1 vẫn ghi "BÁO CÁO QUÁ TRÌNH TUẦN 5", cần sửa thành tuần 7. Sửa lỗi chính tả "than toán" ở slide Activity.
6. **Tài liệu tham khảo [4]** là một thư mục Google Drive. Nhóm kiểm tra xem người ngoài có mở được không và tên file trong đó có chứa họ tên/MSSV không. Nếu có, bỏ link này hoặc đưa tài liệu thẳng vào repo.
7. **Mã nguồn:** `src/` vẫn trống. Theo mô hình tăng dần ở mục 2.2.1, nhóm nên bắt đầu Giai đoạn 1 (đăng nhập, phân quyền): đưa mã vào `src/` và điền mục "Cách chạy lại" trong `README.md`.
