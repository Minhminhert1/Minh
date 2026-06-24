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

### LUẬT CHẤT LƯỢNG (thêm sau vụ 06-24 — đọc kỹ)

8. **GROUNDING GATE — không data, không kết luận.** Mỗi nhận định neo ≥1 FACT có nguồn + timestamp.
   Research đi tra nguồn THẬT (web/đại lý) TRƯỚC khi Analysis chạy. Thiếu data → **KHÔNG độn `[ƯỚC
   LƯỢNG]` rồi kết luận như thật**; hạ độ tin + liệt kê đúng số cần lấy. (06-24 sai vì bỏ bước này.)
9. **ĐỊNH NGHĨA INPUT TRƯỚC KHI TÍNH.** Ghi rõ con số input *là gì*: đơn vị + convention
   (i_VND tuyệt đối? chênh lãi i_VND−i_USD? swap points ra đồng?). Sai bước này = sai toàn bộ.
10. **SANITY-CHECK ĐỘ LỚN.** Mọi số tính ra phải đối chiếu mốc thực tế trước khi tin
    (vd: swap points 1Y USD/VND ~3–4% spot ≈ 800–1.100đ). Số "lệch tầm" = cờ đỏ → dừng, soi lại.
11. **CHỐNG NGHI-THỨC.** KHÔNG spawn cả roster cho "dày". Spawn CHỈ để fan-out research thật
    (R1–R6 mỗi con một nguồn). **Một cái đầu CÓ data > năm cái đầu KHÔNG data.**
12. **NGẮN & RA QUYẾT ĐỊNH.** Mỗi mục phải đổi một quyết định, không thì cắt. Bỏ bảng macro độn.
13. **ĐÓNG VÒNG DỰ BÁO.** Đầu mỗi phiên, Journalist **chấm các dự báo tới hạn TRƯỚC** rồi mới
    phân tích mới. Xác suất phải dẫn **base-rate lịch sử đã chấm** (hoặc ghi rõ "prior, chưa chấm").
    Dự báo dùng **trigger 1 con số** (vd "ON > 5% giữ > 5 phiên"), tránh range không-thể-sai.

---

## CẤU TRÚC HỆ THỐNG

```
CLAUDE.md              ← luật hệ thống (file này)
memory.md              ← bộ nhớ tổng + watchlist + sổ lỗi
system/
├── schema.md          ← hợp đồng bàn giao giữa agent (format cứng)
├── playbooks.md       ← đường ray theo loại câu hỏi
├── watchlist.md       ← ngưỡng cảnh báo (spike/drop nóng)
├── calendar.md        ← lịch sự kiện chủ động (R4 giữ)
└── sources.md         ← data manifest: số THẬT cần kéo mỗi phiên (luật #8)
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

> ⚠️ **Model tier KHÔNG phải đòn bẩy chất lượng.** Đòn bẩy là **DATA được neo + 1 lượt phân tích
> sắc**. Lên Opus hết / spawn nhiều wave mà không có số thật = nói trơn tru chuyện sai (vụ 06-24).
> Chỉ spawn khi có **research thật để chạy song song**, không phải để chế thêm mục cho báo cáo dày.

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
- [ ] **Chấm dự báo tới hạn TRƯỚC (luật #13)**, rồi mới phân tích mới
- [ ] **Định nghĩa input đúng convention (luật #9)** trước khi tính phép nào
- [ ] Chọn đúng playbook, chỉ gọi researcher cần thiết — **không spawn cho dày (luật #11)**
- [ ] Research tra **nguồn THẬT** theo `sources.md`, tách fact/opinion, gắn nguồn + timestamp + độ tin
- [ ] **Sanity-check độ lớn mọi số tính ra (luật #10)**
- [ ] Analysis đa giả thuyết; A3 dự báo có **trigger 1 con số + mốc**
- [ ] Không bỏ qua REVIEWER (gồm tái tính số + check convention)
- [ ] Journalist cập nhật scoreboard + sổ lỗi
- [ ] Báo cáo **ngắn, ra quyết định (luật #12)**; cập nhật memory; commit rõ ràng

---

## LỊCH SỬ

| Ngày | Version | Thay đổi |
|------|---------|---------|
| 2026-06-19 | v1.0 | Khởi tạo FX multi-agent system (6 agent generic) |
| 2026-06-23 | v2.0 | Chuyển trọng tâm sang **Swap USD/VND**: research squad R1–R6, analysis A1–A3, model allocation, schema bàn giao, playbooks, watchlist, calendar, báo cáo 5h sáng |
