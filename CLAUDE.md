# CLAUDE.md — Swap USD/VND Research Team

## Mục đích repo
Hệ thống multi-agent phục vụ **nghiên cứu & phân tích giao dịch FX Swap USD/VND**.
Trọng tâm giai đoạn này: **HỌC** — thu thập sâu → phân tích → bóc insight cho từng
tenor → dự báo curve. Chưa auto-trade, chưa risk/compliance.

> Bản chất sản phẩm: Swap USD/VND = đặt view lên **chênh lệch lãi suất VND–USD**
> và **hình dạng swap curve theo tenor**. Rủi ro spot bị triệt tiêu (2 leg ngược
> chiều cùng notional). Biến số lớn nhất: **thanh khoản VND + động thái SBV**.
> Giá nằm ở **swap points = Forward − Spot ≈ chênh lệch lãi suất theo kỳ hạn**.

---

## NGUYÊN TẮC BẮT BUỘC (đọc trước mỗi turn)

1. **Đọc `memory.md` ở root trước** — bài học tích lũy toàn hệ thống
2. **Đọc `agents/<role>/memory.md`** của agent liên quan trước khi kích hoạt
3. **Đọc `system/` khi cần** — schema bàn giao, playbooks, watchlist, calendar
4. **Sau mỗi turn, cập nhật memory** — không để bài học bị mất
5. **Tách FACT vs OPINION** — Research chỉ nêu fact + nguồn; suy diễn để Analysis lo
6. **Không bao giờ bỏ qua REVIEWER** — mọi insight/dự báo phải qua phản biện
7. **Dự báo phải falsifiable** — luôn kèm *con số + mốc thời gian + điều kiện*

---

## CẤU TRÚC HỆ THỐNG

```
CLAUDE.md              ← luật hệ thống (file này)
memory.md              ← bộ nhớ tổng + watchlist + sổ lỗi
system/
├── schema.md          ← hợp đồng bàn giao giữa agent (format cứng)
├── playbooks.md       ← đường ray theo loại câu hỏi
├── watchlist.md       ← ngưỡng cảnh báo (spike/drop nóng)
└── calendar.md        ← lịch sự kiện chủ động (R4 giữ)
reports/               ← báo cáo tự động 5h sáng đổ vào đây
agents/
├── orchestrator/      ← điều phối, tổng hợp            [Sonnet]
├── research/          ← Research Lead (chuẩn hóa data)  [Sonnet]
│   ├── r1-rates-liquidity/  ← LNH, OMO, tín phiếu, CITAD [Haiku]
│   ├── r2-macro-vn/         ← CPI, GDP, BoP, FDI, XNK    [Haiku]
│   ├── r3-macro-global/     ← Fed/SOFR, UST, DXY, CNY    [Haiku]
│   ├── r4-policy-sbv/       ← tỷ giá TT, can thiệp, văn bản [Sonnet]
│   ├── r5-flow-seasonality/ ← BCTC cuối quý, Tết, thuế   [Sonnet]
│   └── r6-others/           ← tin bất thường, NDF, địa CT  [Haiku]
├── analysis/
│   ├── a1-curve/      ← mổ curve: slope, kink, fair value [Opus]
│   ├── a2-insight/    ← giải thích lý do từng tenor        [Opus]
│   └── a3-forecast/   ← kịch bản & dự báo (có mốc)         [Sonnet]
├── reviewer/          ← phản biện / red-team               [Opus]
├── journalist/        ← ghi chép, scoreboard, sổ lỗi       [Haiku]
└── strategy/          ← NGỦ (bật sau giai đoạn học)        [—]
```

---

## PHÂN BỔ MODEL (tiết kiệm token)

> **Haiku gom/ghi · Sonnet điều phối + phân tích vừa · Opus chỉ cho nút não.**
> Khi spawn subagent qua Agent tool, set `model` đúng theo nhãn ở đầu mỗi `prompt.md`.

| Tầng | Agent | Model |
|------|-------|-------|
| Điều phối | Orchestrator, Research Lead | Sonnet |
| Gom data | R1, R2, R3, R6 | Haiku |
| Diễn giải data | R4, R5 | Sonnet |
| Nút não | A1 Curve, A2 Insight, Reviewer | **Opus** |
| Dự báo | A3 Forecast | Sonnet (→ Opus khi tín hiệu mâu thuẫn) |
| Ghi chép | Journalist | Haiku |

Tổng: **3 Opus / 4 Sonnet / 5 Haiku**. Đặt trần **≤ 3 lần gọi Opus / turn**.

---

## LUỒNG XỬ LÝ CHUẨN

```
Bạn đưa input (curve / câu hỏi / data)
        ↓
[ORCHESTRATOR] đọc memory → chọn PLAYBOOK → chỉ gọi researcher liên quan
        ↓
[RESEARCH SQUAD] R1…R6 chạy SONG SONG → [Research Lead] gạn lọc theo schema
        ↓
[ANALYSIS] A1 mổ curve · A2 bóc insight/tenor · A3 dự báo (song song)
        ↓
[REVIEWER] red-team — 1 vòng: PASS / cần sửa gì
        ↓
[ORCHESTRATOR] tổng hợp → BÁO CÁO cho bạn
        ↓
[JOURNALIST] ghi input + insight + dự báo (có mốc) → cập nhật memory
```

Quy tắc bất đồng: A2 ↔ Reviewer mâu thuẫn không giải quyết được → **báo cáo nêu
cả 2 phía + mức tin**, KHÔNG ép ra 1 đáp án giả.

---

## TỰ ĐỘNG HÓA

| Cơ chế | File | Khi nào |
|--------|------|---------|
| **Báo cáo 5h sáng** | `.github/workflows/daily-report.yml` | 22:00 UTC = 05:00 ICT mỗi ngày → đổ vào `reports/` |
| **Lịch sự kiện** | `system/calendar.md` | R4 giữ; trước sự kiện 1–2 ngày team tự nhắc + dựng kịch bản |
| **Watchlist cảnh báo** | `system/watchlist.md` | Chạm ngưỡng (tăng/giảm nóng) → bóc nguyên do + tìm tiền lệ quá khứ |

---

## QUY TẮC CẬP NHẬT MEMORY SAU MỖI TURN

| Câu hỏi | Ghi vào |
|---------|---------|
| Team học được gì mới? | `memory.md` (root) |
| Pattern thị trường mới? | `memory.md` (mục Pattern) |
| Nhận định sai? | `memory.md` (Sổ lỗi, gắn tag) |
| Mảng research nào thiếu nguồn? | `agents/research/r#/memory.md` |
| Insight/curve có pattern mới? | `agents/analysis/a#/memory.md` |
| Reviewer phát hiện blind spot? | `agents/reviewer/memory.md` |
| Dự báo đúng/sai ra sao? | `agents/journalist/memory.md` (scoreboard) |

---

## PHONG CÁCH LÀM VIỆC

- User: Minhminhert1 · Email: minhnh.fblc@gmail.com
- Ngôn ngữ: Tiếng Việt · Phong cách: ngắn gọn, thực tế, không dài dòng
- Kỳ vọng: Claude tự làm, không hỏi thừa
- Domain: **FX Swap USD/VND Research** (rates & liquidity là trung tâm)

---

## CHECKLIST CUỐI MỖI TURN

- [ ] Đọc memory.md + memory agent liên quan trước khi làm
- [ ] Chọn đúng playbook, chỉ gọi researcher cần thiết
- [ ] Research tách fact/opinion, gắn nguồn + timestamp + độ tin
- [ ] Analysis đa giả thuyết; A3 dự báo có mốc thời gian
- [ ] Không bỏ qua REVIEWER
- [ ] Journalist cập nhật scoreboard + sổ lỗi
- [ ] Cập nhật memory; commit message rõ ràng

---

## LỊCH SỬ

| Ngày | Version | Thay đổi |
|------|---------|---------|
| 2026-06-19 | v1.0 | Khởi tạo FX multi-agent system (6 agent generic) |
| 2026-06-23 | v2.0 | Chuyển trọng tâm sang **Swap USD/VND**: research squad R1–R6, analysis A1–A3, model allocation, schema bàn giao, playbooks, watchlist, calendar, báo cáo 5h sáng |
