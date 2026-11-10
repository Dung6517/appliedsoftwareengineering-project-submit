# KTPMUD Project — Repo Nộp Bài Chung Của Lớp

Repo này là nơi **sinh viên môn Kỹ Thuật Phần Mềm Ứng Dụng (KTPMUD)** nộp
bài đồ án cuối khóa theo case study đã chọn trong
[Ngân hàng Case Study](https://fossbk-spec.github.io/ktpmud-book/do_an_mon_hoc).

- **Đề bài, kịch bản, rubric:** xem tại
  [ktpmud-book](https://fossbk-spec.github.io/ktpmud-book/) — repo này
  **không** chứa lại đề bài, chỉ chứa bài làm của sinh viên.
- **Mỗi nhóm = 1 thư mục riêng** dưới `submissions/`, đặt tên theo đúng quy
  ước ở [CONTRIBUTING.md](CONTRIBUTING.md).
- **Nộp bài qua Pull Request** — không push trực tiếp vào `main`. Xem quy
  trình đầy đủ trong [CONTRIBUTING.md](CONTRIBUTING.md); làm lần đầu thì theo
  [HUONG_DAN_NOP_BAI.md](HUONG_DAN_NOP_BAI.md) (từng bước, có ví dụ).

## Vì sao dùng Pull Request thay vì push trực tiếp?

1. **Cách ly giữa các nhóm** — mỗi PR chỉ được phép đổi file trong đúng 1
   thư mục `submissions/<case_study_slug>_<ma_nhom>/` của nhóm đó. CI tự
   động chặn PR nếu đụng vào thư mục của nhóm khác (xem
   `.github/workflows/validate-submission.yml`).
2. **Không mất bài** — lịch sử Git giữ nguyên toàn bộ commit của từng nhóm;
   `main` chỉ nhận bản đã qua kiểm tra tự động + giảng viên duyệt.
3. **Không nộp nhầm/nộp thiếu** — CI kiểm tra cấu trúc thư mục, file bắt
   buộc (`submission.json`, `README.md`), và chặn các mẫu hình dữ liệu
   nhạy cảm phổ biến (khóa API, thông tin bệnh nhân thật) trước khi merge.

## Cấu trúc repo

```
ktpmud-project/
├── submissions/
│   ├── _TEMPLATE/                  ← Copy thư mục này để bắt đầu nộp bài
│   │   ├── submission.json         ← Thông tin nhóm + case study (bắt buộc)
│   │   ├── README.md               ← Tóm tắt bài làm (bắt buộc)
│   │   ├── report/                 ← Báo cáo (PDF/Markdown), SRS, C4 diagram
│   │   ├── src/                    ← Mã nguồn
│   │   └── slides/                 ← Slide thuyết trình (tuỳ chọn)
│   │
│   └── <case_study_slug>_<ma_nhom>/  ← 1 thư mục nộp bài của 1 nhóm
│       └── ... (giống cấu trúc _TEMPLATE)
│
├── scripts/validate_submission.py  ← Script CI dùng để kiểm tra PR
├── .github/workflows/validate-submission.yml
├── CONTRIBUTING.md                 ← Hướng dẫn nộp bài chi tiết từng bước
└── CODEOWNERS                      ← Định tuyến review PR tới giảng viên/TA
```

## Case study hiện có

| Slug | Case Study | Ghi chú |
|---|---|---|
| `may_day` | CS-1: Dr May Day v2.0 | Có 2 kịch bản: `mayday_sim` (mô phỏng) hoặc `mayday_tichhop` (tích hợp thật) — ghi rõ kịch bản trong `submission.json` |
| `suy_tim` | CS-2: AI-CDSS Suy tim (HF-CDSS) | |
| `alzheimer` | CS-3: AI-CDSS Alzheimer | |
| `dreye` | CS-4: Phần mềm điều khiển thiết bị Edge AI (DrEye) | Phần mềm nhúng/di động — khác lớp CS-2/CS-3 (CDSS server/web) |
| `dai_thao_duong` | CS-5: Hỗ trợ người chăm sóc theo dõi điều trị ngoại trú đái tháo đường type 2 | Đề nhóm đề xuất, giảng viên đã duyệt |
| `nha_cho_thue` | CS-6: Phần mềm quản lý nhà cho thuê (nhà trọ, chung cư mini) | Đề ngoài y tế, nhóm đề xuất, giảng viên đã duyệt |
| `ban_do_lich_su` | CS-7: Website Bản đồ Lịch sử Việt Nam | Đề ngoài y tế, nhóm đề xuất, giảng viên đã duyệt |
| `ke_hoach_hoc_tap` | CS-8: Hệ thống hỗ trợ theo dõi tiến độ và lập kế hoạch học tập cho sinh viên | Đề ngoài y tế, nhóm đề xuất, giảng viên đã duyệt |
| `quan_ly_thiet_bi_y_te` | CS-9: Hệ thống quản lý thiết bị y tế | Đề nhóm đề xuất (nhom49), giảng viên đã duyệt 10/11/2026 |

Slug phải khớp đúng tên trong
[bảng case study](https://fossbk-spec.github.io/ktpmud-book/do_an_mon_hoc).
