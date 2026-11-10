# Góp ý — nhom49 (Quản lý thiết bị y tế)

- **Bài nộp:** PR #1 `docs: Cập nhật link Google Docs tài liệu SRS` (nhánh `submit/quan_ly_thiet_bi_y_te-nhom49`, mở 20/09/2026)
- **Ngày góp ý:** 21/10/2026
- **Kết quả kiểm tra tự động:** ❌ chưa hợp lệ (`scripts/validate_submission.py`)

## Cần sửa trước khi được review nội dung

1. **Thiếu file bắt buộc.** Thư mục `submissions/quan_ly_thiet_bi_y_te_nhom49/` chưa có
   `submission.json` và `README.md`. Copy từ `submissions/_TEMPLATE/` rồi điền đủ các trường
   theo [CONTRIBUTING.md](../CONTRIBUTING.md#2-schema-submissionjson).
2. **Đề tài chưa nằm trong ngân hàng case study.** Slug hợp lệ hiện chỉ gồm `may_day`,
   `suy_tim`, `alzheimer`, `dreye`. Đề "Quản lý thiết bị y tế" chưa có trong danh sách, nên dù
   có `submission.json` bài vẫn bị CI từ chối. Nhóm trao đổi lại với giảng viên: chọn một case
   study có sẵn, hoặc chờ giảng viên bổ sung đề này vào danh sách.
3. **Link tài liệu làm lộ danh tính.** Link trong `report/SRS_v1.0.md` là OneDrive cá nhân, đường
   dẫn chứa tên và MSSV của thành viên. Repo này công khai vĩnh viễn, nên theo
   [quy tắc quyền riêng tư](../CONTRIBUTING.md#3-quy-tắc-bắt-buộc-về-quyền-riêng-tư-ci-sẽ-chặn-nếu-vi-phạm)
   hãy dùng link không chứa thông tin cá nhân và mở quyền xem cho người ngoài trường, hoặc tốt
   hơn là đưa SRS dạng Markdown/PDF thẳng vào `report/`. Tiêu đề PR ghi "Google Docs" nhưng
   link thực tế là OneDrive — sửa lại cho khớp.
4. **Lỗi định dạng nhỏ:** xoá dòng thừa `.*` ở cuối `report/SRS_v1.0.md`.

## Cách nộp lại

Sửa trên cùng nhánh rồi push, PR #1 tự cập nhật. Trước khi push, chạy:

```
python scripts/validate_submission.py submissions/<thu_muc_nhom>
```

Nếu đổi case study thì đổi cả tên thư mục và tên nhánh theo quy ước
`submissions/<case_study_slug>_nhom49/` và `submit/<case_study_slug>-nhom49`.

## Cập nhật 10/11/2026

Giảng viên đã duyệt đề "Hệ thống quản lý thiết bị y tế" thành **CS-9**, slug `quan_ly_thiet_bi_y_te`
(trả lời issue #24). Mục 2 ở trên không còn áp dụng. PR #1 đã đóng; nhóm nộp bài tập lớn bằng PR mới, thư mục
`submissions/quan_ly_thiet_bi_y_te_<ma_nhom>/`, `submission.json` có `"case_study_slug": "quan_ly_thiet_bi_y_te"`
và `"case_study_id": "CS-9"`. Bài Hack Marathon vẫn dùng slug `may_day_sprint`.
