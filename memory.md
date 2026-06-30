# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

- **[2026-06-30] Cú spike ON chốt quý:** ON 0.40% → 9.50% (+910bps) đúng ngày 30/06. Quy tắc đọc curve: front-end nổ nhưng **belly ≥1M GIẢM** → kỹ thuật cuối quý (window-dressing BCTC), KHÔNG phải tightening cấu trúc. Phân biệt với "SBV hút VND" bằng dấu hiệu belly: SBV siết thật thì 1M+ phải tăng theo.
- **Whiplash thanh khoản:** trước chốt quý ON gần 0 (cực dồi dào) rồi sập lên 9.5% — độ giật càng lớn càng xác nhận tính kỹ thuật + thiếu đệm thanh khoản cuối quý.

---

## Curve & tenor đang theo dõi
*(swap points các kỳ hạn user quan tâm: O/N, 1W, 1M, 3M, 6M, 12M…)*

- **[2026-06-30] Curve lãi suất USD/VND (mid):** ON 9.50 · 1W 5.00 · 2W 4.50 · 3W 3.55 · 1M–3M 3.40 · 6M 3.40 · 9M 3.55 · 1Y 3.65. Hình dạng: twist — front bốc cháy, belly/back hạ 10–15bps. Belly < SOFR ~20bps → swap points 1M–6M âm nhẹ/sát 0.

---

## Bias hiện tại
- Chênh lệch lãi suất VND–USD: **belly âm nhẹ** (VND ~3.40% < SOFR ~3.62%, ~−20bps) → swap points 1M–6M sát phẳng/chiết khấu nhẹ.
- Thanh khoản VND hệ thống: **whiplash** — dồi dào trước chốt quý → căng đột biến đúng 30/06 (ON 9.50%). Chờ xác nhận có normalize sau 30/06.
- Động thái SBV gần nhất: *(chưa có data OMO/tín phiếu 30/06 — `#thiếu-data`, cần R1/R4)*

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N tăng | ✅ Đúng 30/06/26: ON 0.4→9.5% |
| Spike ON kỹ thuật | ON nổ NHƯNG belly ≥1M giảm | căng transient, normalize 1–3 phiên sau chốt | (chờ chấm sau 03/07) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **9.50% (+910bps/phiên)** 🔴🔴 | 2026-06-30 |
| LNH 1W / 2W | 5.00% / 4.50% (0 / +55bps 🔴) | 2026-06-30 |
| LNH 1M / 3M / 1Y | 3.40% / 3.40% / 3.65% (−10/−10/−5bps) | 2026-06-30 |
| Tỷ giá trung tâm | 25.183 | 2026-06-22 |
| USD/VND spot | ~26.43 (sát trần) | 2026-06-22 |
| SOFR (ON) | 3.62% | 2026-06-18 |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| *(cập nhật)* | | | | |

### Đã chấm
- **[2026-06-23] ON ≥3.0% quanh 26–30/06 (base 55%)** → ✅ **HIT** mạnh: ON 9.50% ngày 30/06, rơi vào nhánh **up-risk** (SBV/chốt quý → 4–6%+). Calibration: định hướng đúng, nhưng under-estimate biên độ — cú spike chốt quý có thể >>4–6%.

### Sổ chờ chấm
- **[2026-06-30] Base: ON normalize ≤3.0% trong 1–3 phiên (đến ~03/07), belly 3.30–3.45** — ~65%. Chấm sau 03/07.
  - Up-risk ~25%: SBV giữ chặt trần → ON >4% tới giữa T7, belly +10–20bps.
  - Down ~10%: ON về 1–2% trong 1–2 phiên, belly ~3.2%.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| *(ghi khi sai)* | | | |
