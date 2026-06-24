# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

- **[2026-06-24]** ON sụp 0.55% nhưng **1W vọt 3.70%** (>2W–3M) → KHÔNG phải "front flush".
  Overnight thật (đáo trước 30/06) dư; còn **funding bắc qua chốt quý căng ~3.7%**, dồn vào 1W.
  Bài học: đọc seasonality cuối quý ở **tenor bắc qua turn (1W/2W)**, đừng nhìn ON. ON thấp +
  1W cao cùng lúc = bank hoard thanh khoản để vuông sổ QUA ngày chốt, đẩy giá 1W phủ 30/06.
- **[2026-06-24]** Turn premium **dồn vào 1W** (spike 1W 3.70 > 2W 3.30): 1W là kỳ hạn ngắn nhất
  "all-in" qua turn → phí chốt quý chia trên ít ngày → lãi quy năm cao nhất. Đo phí turn = đỉnh spike.
- **[2026-06-24]** Spot sát trần (~26.43) + thị trường ĐÃ pricing funding turn căng (1W 3.70) →
  rủi ro SBV hút giảm bớt so với kịch bản "ON còn 0.5% ngây thơ"; nhưng nếu spot vẫn ép trần,
  SBV vẫn có thể hút đẩy cả ON lẫn term lên.

---

## Curve & tenor đang theo dõi
*(lãi suất LNH/implied VND theo kỳ hạn — snapshot mới nhất, mid %)*

| as-of | ON | 1W | 2W | 1M | 3M | 6M | 1Y | Hình dạng |
|-------|----|----|----|----|----|----|----|-----------|
| 2026-06-24 | 0.55 | **3.70** | 3.30 | 3.35 | 3.35 | 3.65 | 3.80 | ON dip + **spike 1W** (turn premium dồn vào 1W qua 30/06, 1W>2W–3M); belly phẳng ~3.3–3.5; đuôi dốc nhẹ |
| 2026-06-23 | 1.65 | 1.80 | 3.55 | 3.55 | 3.70 | — | 3.80 | — |

---

## Bias hiện tại
- Chênh lệch lãi suất VND–USD: ON âm sâu (0.55−3.62 ≈ −307bps) → **1W bật gần phẳng** (3.70 vs
  USD 1W ~3.6 ≈ ~0) → belly/đuôi âm nhẹ (3.3–3.8 vs USD 3.6–4.2). ⇒ swap points âm sâu nhất ON,
  **gần zero ở 1W (do spike turn)**, âm nhẹ phần còn lại. *(USD term là ước lượng — FRESHNESS FLAG)*
- Thanh khoản VND hệ thống: **overnight dư** (ON 0.55%) nhưng **funding qua chốt quý CĂNG** (1W 3.70%)
  → squeeze chốt quý CÓ thật, dồn vào tenor bắc qua 30/06; ON thấp chỉ là same-day.
- Động thái SBV gần nhất: *(chưa có data OMO/tín phiếu hôm nay — cần R1/R4 xác nhận)* —
  ON 0.55% gợi ý SBV đang để dư/đáo hạn tín phiếu bơm lại; rủi ro đảo chiều nếu SBV hút đỡ tỷ giá.

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng — nhưng ở tenor bắc qua turn, KHÔNG nhất thiết ở ON | ✅ 2026-06-24 xác nhận: 1W spike 3.70% (ON vẫn 0.55%) |
| Spike turn dồn vào 1W | curve có bướu ở tenor ngắn nhất bắc qua chốt quý | đo phí turn = đỉnh spike; ON có thể vẫn thấp | mới (2026-06-24, 1W 3.70 > 2W 3.30) |
| Lò xo nén ON-thấp + spot trần | ON < 1% đồng thời spot sát trần | SBV có thể hút đỡ đồng; nhưng nếu 1W đã căng thì rủi ro hút giảm | chờ chấm (30/06) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **0.55%** (−110bps/phiên) 🔴 ALERT (thủng 1.0%) | 2026-06-24 |
| LNH 1W / 2W | **3.70% → bid 4.0 xuyên offer cũ 3.80** (turn squeeze nóng lên) / 2W 3.30% | 2026-06-24 |
| LNH 1M / 3M / 1Y | 3.35% / 3.35% / 3.80% (−20 / −35 / 0bps) | 2026-06-24 |
| Tỷ giá trung tâm | 25.183 | 2026-06-22 |
| USD/VND spot | ~26.43 (sát trần) | 2026-06-22 |
| SOFR (ON) | 3.62% | 2026-06-18 |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| *(cập nhật)* | | | | |

### Sổ chờ chấm
- **[2026-06-23] ON bật về ≥3.0% trong 3–7 phiên (quanh 26–30/06)** — Base ~55%. Chấm sau 30/06.
  - Up-risk ~30%: nếu spot ép trần → SBV hút VND → ON 4–6%+ trong 1–2 tuần.
  - Down ~15%: ON giữ 1.5–2.5% kéo dài qua chốt quý.
  - 🔻 **Cập nhật 2026-06-24:** ON literal vẫn 0.55% (chưa ≥3.0%) → đo theo ON thì Base chưa đạt;
    NHƯNG tinh thần "funding căng quanh chốt quý" ĐÚNG — hiện ở **1W spike 3.70%** (+190bps).
    Cảnh giác: dự báo cũ neo nhầm vào ON; turn squeeze biểu hiện ở 1W. Chấm chốt sau 30/06.

- **[2026-06-24] Turn premium giữ ở 1W: lãi 1W ≥ 3.5% tới 30/06; ON có thể vẫn < 1.5%** — Base ~55%.
  Điều kiện huỷ: SBV bơm mạnh phủ cả turn → 1W về < 3.0%. Chấm sau 30/06.
  - Up-risk ~25%: spot ép trần → SBV hút tín phiếu → đẩy cả ON + term lên đồng loạt (>4%).
  - Down ~20%: turn qua êm, 1W xẹp nhanh về ~3.3% ngay sau 30/06 (phí turn biến mất). Chấm sau 03/07.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| *(ghi khi sai)* | | | |
