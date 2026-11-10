# Hướng dẫn nộp bài lên GitHub từng bước

Dành cho nhóm chưa quen Git/GitHub. Quy định đầy đủ xem [CONTRIBUTING.md](CONTRIBUTING.md);
file này chỉ đi qua các thao tác, lấy **nhóm N01 lớp 173820 (CS-5 Đái tháo đường type 2)** làm
ví dụ. Nhóm khác thay tên thư mục, slug, MSSV cho đúng của mình.

## 0. Chuẩn bị (một lần)

1. Mỗi thành viên có tài khoản GitHub. Một bạn làm **đại diện nộp**.
2. Đại diện **fork** repo: mở https://github.com/fossbk-spec/ktpmud-project → bấm **Fork** →
   **Create fork**. Được bản sao `https://github.com/<tai-khoan>/ktpmud-project`.
3. (Tuỳ chọn) Trong fork: **Settings → Collaborators → Add people** để thêm các thành viên còn lại.

## 1. Đặt tên đúng chuẩn

| Thành phần | Quy tắc | Ví dụ N01 |
|---|---|---|
| Thư mục nộp | `submissions/<case_study_slug>_<mã lớp>_<số nhóm>/` | `submissions/dai_thao_duong_173820_n01/` |
| Nhánh (branch) | `submit/<case_study_slug>-<mã lớp>_<số nhóm>` | `submit/dai_thao_duong-173820_n01` |
| Tên file | Không dấu, không khoảng trắng, **không họ tên** | `report/BaoCao_Tuan6.docx` |

Slug hợp lệ: `may_day`, `suy_tim`, `alzheimer`, `dreye`, `dai_thao_duong`, `nha_cho_thue`, `ban_do_lich_su`, `ke_hoach_hoc_tap`, `quan_ly_thiet_bi_y_te`. Chỉ chữ thường, số,
gạch dưới.

Cấu trúc thư mục:

```
submissions/dai_thao_duong_173820_n01/
├── submission.json      ← bắt buộc
├── README.md            ← bắt buộc
├── report/              ← báo cáo, SRS, C4, test report (.docx/.pdf/.md)
├── slides/              ← slide thuyết trình
└── src/                 ← mã nguồn (khi có)
```

`submission.json` của N01:

```json
{
  "case_study_slug": "dai_thao_duong",
  "case_study_id": "CS-5",
  "group_code": "173820_n01",
  "members": ["202413994", "202414357", "202414408"],
  "scenario": "khong_ap_dung",
  "submitted_at": "2026-10-21"
}
```

`members` ghi **MSSV**, không ghi họ tên. `scenario` chỉ dùng cho CS-1; đề khác ghi
`khong_ap_dung`.

> **Thư mục nhóm đã có sẵn trên `main`?** Lớp 173820: bài tuần 6 của các nhóm N01, N02, N03,
> N27, N43 đã được giảng viên đưa lên. Các tuần sau chỉ cần tạo nhánh, **thêm file mới** vào đúng
> thư mục đó (bỏ qua bước tạo `submission.json`/`README.md`) rồi mở PR như bước 3.

## 2a. Nộp bằng trình duyệt (dễ nhất, không cần cài gì)

1. Vào **fork của nhóm** → nút nhánh `main` ở góc trái → gõ `submit/dai_thao_duong-173820_n01`
   → **Create branch**.
2. Đang ở nhánh mới, bấm **Add file → Create new file**. Ô tên gõ đúng
   `submissions/dai_thao_duong_173820_n01/submission.json` (gõ dấu `/` sẽ tự tạo thư mục) → dán
   nội dung JSON ở trên → **Commit changes**.
3. Làm tương tự cho `submissions/dai_thao_duong_173820_n01/README.md` (xem mẫu ở
   `submissions/_TEMPLATE/README.md`).
4. Mở thư mục `submissions/dai_thao_duong_173820_n01/` → **Add file → Upload files** → kéo thả
   **cả thư mục** `report` và `slides` từ máy (đã chứa sẵn file) vào khung — GitHub giữ nguyên cấu
   trúc thư mục → **Commit changes**. Mỗi file **< 10MB**.
5. Sang bước 3 (mở Pull Request).

## 2b. Nộp bằng Git (nếu đã cài Git)

```bash
git clone https://github.com/<tai-khoan>/ktpmud-project.git
cd ktpmud-project
git checkout -b submit/dai_thao_duong-173820_n01
cp -r submissions/_TEMPLATE submissions/dai_thao_duong_173820_n01
# sửa submission.json, README.md; chép báo cáo vào report/, slide vào slides/

python scripts/validate_submission.py submissions/dai_thao_duong_173820_n01
# phải in: [PASSED] Nộp bài hợp lệ.

git add submissions/dai_thao_duong_173820_n01
git commit -m "submit: N01 lop 173820 - bao cao tuan 6"
git push -u origin submit/dai_thao_duong-173820_n01
```

Chỉ `git add` thư mục của nhóm mình — không sửa file nào khác của repo.

## 3. Mở Pull Request

1. Vào fork trên GitHub, sẽ thấy dải vàng **Compare & pull request** → bấm vào.
   (Hoặc tab **Pull requests → New pull request**.)
2. Kiểm tra: **base repository** `fossbk-spec/ktpmud-project`, **base** `main`;
   **head** là fork của nhóm, nhánh `submit/dai_thao_duong-173820_n01`.
3. Tiêu đề: `submit: N01 lớp 173820 – báo cáo tuần 6`. Mô tả: nội dung nộp tuần này.
4. Bấm **Create pull request**.

## 4. Sau khi mở PR

- **CI tự kiểm tra** trong khoảng 1 phút, rồi **bot bình luận kết quả** ngay trên PR:
  - ✅ *Bài nộp hợp lệ về cấu trúc* → chờ giảng viên/TA review nội dung.
  - ❌ *Bài nộp chưa hợp lệ* → đọc danh sách lỗi, sửa trên **cùng nhánh** rồi push/commit tiếp.
    PR và bình luận tự cập nhật, **không mở PR mới**.
- Nếu PR hiện *"Workflow awaiting approval"*: tài khoản GitHub còn mới, chờ giảng viên bấm duyệt
  một lần.
- Giảng viên góp ý bằng bình luận trên PR; góp ý tổng hợp lưu ở `feedback/<thư mục nhóm>.md`.
- Khi giảng viên **approve**, PR được merge vào `main`. Sau khi merge **không sửa qua PR thường
  được nữa** — tuần sau nộp tiếp bằng PR mới (thêm file mới, ví dụ `report/BaoCao_Tuan8.docx`).

## 5. Lỗi hay gặp

| Bot báo | Cách sửa |
|---|---|
| Thiếu file `submission.json` / `README.md` | Tạo đủ hai file ngay trong thư mục nhóm (không nằm trong `report/`) |
| `case_study_slug` không hợp lệ | Dùng đúng một slug trong danh sách ở mục 1 |
| Tên thư mục không đúng quy ước | Chỉ chữ thường, số, gạch dưới: `dai_thao_duong_173820_n01` |
| PR sửa file ngoài `submissions/` | Bỏ thay đổi ở file khác (README gốc, scripts…) khỏi nhánh |
| PR đụng nhiều thư mục nộp bài | Mỗi PR chỉ cho đúng một nhóm |
| File nặng > 10MB | Nén ảnh / xuất PDF nhẹ hơn, hoặc để link Drive trong `README.md` |
| Nghi vấn secret | Xoá khoá API/token khỏi file, không commit `.env` |
