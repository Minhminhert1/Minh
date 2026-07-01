# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

- **[01/07/2026] Chu kỳ chốt quý hoàn chỉnh đã quan sát trọn:** ON 1.65% (23/06) → leo dần → **đỉnh 9.50% ngày chốt quý 30/06** → **xả về 3.75% ngày đầu quý 01/07**. Cơ chế: window-dressing BCTC cuối quý đẩy funding qua đêm căng cực đại đúng ngày chốt, rồi tan trong **1 phiên** sang quý mới. Chân dài (3M–1Y) bất động suốt → thuần thanh khoản mùa vụ.
- **Calibration:** team đánh giá **thấp biên độ** cú chốt quý (dự up-risk 4–6%, thực 9.50%). Lần sau **nới trần up-risk quanh mốc chốt quý (30/03, 30/06, 30/09, 31/12)**.
- **Chênh lệch VND–USD co về ~0 (01/07):** VND 3.2–3.75% ≈ SOFR 3.5–3.62% → swap points **mỏng, quanh ngang** trên toàn curve; carry giữ VND ≈ trung tính (khác hẳn 23/06 khi đầu cong diff −1.97%).

---

## Curve & tenor đang theo dõi
*(swap points các kỳ hạn user quan tâm: O/N, 1W, 1M, 3M, 6M, 12M…)*

---

## Bias hiện tại *(as-of 01/07/2026)*
- Chênh lệch lãi suất VND–USD: **≈ 0 trên toàn curve** (VND 3.2–3.75% vs SOFR 3.5–3.62%) → swap points mỏng, quanh ngang, âm nhẹ ở bụng 3W–1M.
- Thanh khoản VND hệ thống: **dồi dào trở lại** sau đỉnh căng chốt quý; bụng curve xuống đáy 3.20%.
- Động thái SBV gần nhất: *(chưa có số OMO/spot 01/07 — cần R1/R4 bổ sung)*. Rủi ro chính: spot ép trần → SBV siết VND → front-end firm lại (Up-risk ~25%).

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N **vọt tới đỉnh đúng ngày chốt** (30/06: ON 9.50%), **xả về nền trong 1 phiên** sang quý mới (01/07: 3.75%). Chỉ tác động chân ngắn; chân dài bất động. | ✅ Đúng (30/06–01/07/2026) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **3.75%** (−575bps/phiên, xả đỉnh chốt quý 9.50%) 🔴 | 2026-07-01 |
| LNH 1W / 2W | 3.40% / 3.30% (−160/−120bps) | 2026-07-01 |
| LNH bụng 3W–1M | **3.20%** (đáy curve) | 2026-07-01 |
| LNH 3M / 6M / 1Y | 3.30% / 3.40% / 3.60% (đứng ±5bps) | 2026-07-01 |
| Tỷ giá trung tâm | 25.183 (cần cập nhật) | 2026-06-22 |
| USD/VND spot | ~26.43 (sát trần, cần cập nhật) | 2026-06-22 |
| SOFR (ON) | 3.62% | 2026-06-18 |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| ON front-end (23/06) | 3 | 3 | 100% | Đúng hướng nhưng **thấp biên độ** (dự 4–6%, thực 9.50%) → nới trần quanh chốt quý |

### Sổ chờ chấm
- **[2026-07-01] ON ổn định vùng 3.0–3.75% trong 1–2 tuần; 9.50% không tái lập tới 30/09** — Base ~60%. Chấm ~15/07.
  - Up-risk ~25%: spot tái ép trần → SBV siết VND → ON firm 4–5% + swap points ngắn dương lại.
  - Down ~15%: thanh khoản dồi dào → ON trượt 2.0–2.8%, mở lại forward discount ngắn.
  - Điều kiện then chốt: spot USD/VND có rời trần không (cần R4 bổ sung).

### Đã chấm
- **[2026-06-23] ON bật về ≥3.0% quanh 26–30/06** — ✅ ĐÚNG (ON đỉnh 9.50% ngày chốt quý 30/06, chân dài đứng yên). Chi tiết: `reports/2026-07-01-...md` mục 7.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| *(ghi khi sai)* | | | |
