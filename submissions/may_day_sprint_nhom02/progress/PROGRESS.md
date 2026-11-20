# PROGRESS — n02 — Track A

- Starter: ktpmud-bkt-ruleengine-starter · tag bkt-2026-v1 (hoặc v1.1)
- Fork: ⟨ĐIỀN URL fork công khai⟩

## PC-1 — 11/11/2026

### 1.1. Tiến độ theo acceptance criteria
<!-- Track A: A-01…A-11 · Track B: B-01…B-12 (đề thi Mục 7.3 / 8.3). Đủ mọi mã. -->
| Mã | Trạng thái (Chưa / Đang / Xong) | Bằng chứng (commit / CI / file) | Ghi chú |
|---|---|---|---|
| A-01 | Đang |
| A-02 | Đang |
| A-03 | Đang |
| A-04 | Đang |
| A-05 | Đang |
| A-06 | Đang |
| A-07 | Đang |
| A-08 | Đang |
| A-09 | Đang |
| A-10 | Đang |
| A-11 | Xong | README.md | |

### 1.2. Sửa đổi bắt buộc từ Checkpoint 1
<!-- Các mục ❗ trong nhận xét Checkpoint 1 của nhóm. Nếu không có, ghi "Không có". -->
| Mục | Trạng thái | Bằng chứng |
|---|---|---|
| REQUIREMENTS.md | Xong | |
| decision-table.md | Xong | |
| README.MD | Xong | |
| source-ref.json | Xong | |

### 1.3. Timeline dự kiến đến khi hoàn thành
| Việc | Vai trò phụ trách | Mốc (CP2 15/11 · M3 · Freeze 19/11 · M4 20/11) | Ngày dự kiến |
|---|---|---|---|
| Hoàn thành trước Checkpoint 2 | Demo nội bộ | Checkpoint 2 | 17/11 |

### 1.4. Rủi ro / đang vướng
- Cách tạo các file như PROGRESS.md, AI_USE.MD, ...

### 1.5. Câu hỏi cho GV
- Q1: 

### 1.6. Phân công (alias hoặc vai trò, KHÔNG ghi họ tên/MSSV)
| Alias / vai trò | Đầu việc chính | Commit/PR tiêu biểu |
|---|---|---|
| Code/case | Hỗ trợ chạy thuật toán | bc7df5fa2ecbb6f880a703abf5c043ffaf70ae0b |
| Nộp bài | Nộp bài, kiểm tra file nộp | This file |

## PC-2 — 18/11/2026

### 2.1. Đối chiếu timeline PC-1
| Việc (theo bảng 1.3) | Kế hoạch | Thực tế | Lệch & lý do |
|---|---|---|---|
| Checkpoint 1 | 8/11 | 10/11 | Vướng lịch trình thi giữa kỳ |
| Hoàn thành trước Checkpoint 2 (demo nội bộ) | 17/11 | 17/11 |  |

### 2.2. Tiến độ theo acceptance criteria (cập nhật toàn bộ bảng 1.1)
> Điều chỉnh so với PC-1: bảng 1.1 ghi nhầm mã Track B (B-01…B-12). Nhóm làm **Track A** nên bảng này dùng đúng mã A-01…A-11 (đề thi Mục 7.3).

| Mã | Trạng thái | Bằng chứng | Ghi chú |
|---|---|---|---|
| A-01 | Đang |
| A-02 | Đang |
| A-03 | Đang |
| A-04 | Đang |
| A-05 | Đang |
| A-06 | Đang |
| A-07 | Đang |
| A-08 | Đang |
| A-09 | Đang |
| A-10 | Đang |
| A-11 | Xong | README.md | |

### 2.3. Sẵn sàng nộp bài (đề thi Mục 6)
| Deliverable | Có / Chưa | Đường dẫn |
|---|---|---|
| README.md | Chưa | |
| REQUIREMENTS.md | Có | https://github.com/Dung6517/appliedsoftwareengineering-project-submit/blob/main/submissions/may_day_sprint_nhom02/artifacts/DECISIONS.md |
| DECISIONS.md / ADR | Chưa | |
| Test tự động + CI xanh | Chưa | |
| TEST_REPORT.md | Chưa | |
| SECURITY_PRIVACY_CHECKLIST.md | Chưa | |
| AI_USE.md | Có | https://github.com/Dung6517/appliedsoftwareengineering-project-submit/blob/main/submissions/may_day_sprint_nhom02/artifacts/AI_USE.md |
| CONTRIBUTIONS.md | Chưa | |
| Slide / demo script ≤ 7 phút | Chưa | |
| Draft PR vào `ktpmud-project`, check `validate` xanh | Có | https://github.com/fossbk-spec/ktpmud-project/pull/29 |

> Lưu ý: bảng này nhóm cần tự rà lại theo thực tế tại thời điểm commit PC-2. Một số file (vd REQUIREMENTS.md) PC-1 đã ghi "Xong" thì chuyển thành "Có" kèm đường dẫn.

### 2.4. Việc còn lại đến Freeze (23:59 19/11)
| Việc | Vai trò phụ trách | Hạn |
|---|---|---|
| Mở Draft PR vào `ktpmud-project`, check `validate` xanh (erratum #28) | Nộp bài | 18/11, trước 11:30 |
| Hoàn thiện `classify()` + audit + xử lý input lỗi (A-01…A-06) | Code/case | 18/11 |
| Bộ unit test normal/boundary/invalid/missing + CI xanh (A-07…A-09) | Code/case | 18/11 |
| Benchmark p50/p95, ghi vào TEST_REPORT.md (A-10) | Code/case | 19/11 |
| DECISIONS.md/ADR, TEST_REPORT.md, SECURITY_PRIVACY_CHECKLIST.md | ⟨ĐIỀN⟩ | 19/11 |
| AI_USE.md, CONTRIBUTIONS.md | Nộp bài | 19/11 |
| Slide / demo script ≤ 7 phút | ⟨ĐIỀN⟩ | 19/11 |
| Gắn tag `bkt-2026-n02-rc1`, ghi SHA vào `source-ref.json` (đủ 6 trường) | Nộp bài | 19/11, trước 23:59 |

### 2.5. Rủi ro / câu hỏi cho GV
- Rủi ro: đồ án PBL chạy song song, trùng giai đoạn tích hợp cuối; thời gian còn lại đến Freeze ngắn.
- Rủi ro: CI của starter Track A có lỗi đã được sửa ở tag `bkt-2026-v1.1` (erratum #16); cần kiểm tra fork đã áp dụng chưa.

## Kết quả cuối — Freeze 19/11/2026
- Tag: bkt-2026-n02-rc1 · SHA: ⟨ĐIỀN sau khi freeze⟩
- Trạng thái cuối từng mã AC: (cập nhật bảng 2.2 hoặc ghi "như 2.2 trừ: …")
- Những việc trong timeline chưa hoàn thành và lý do:
