# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

---

## Curve & tenor đang theo dõi
*(swap points các kỳ hạn user quan tâm: O/N, 1W, 1M, 3M, 6M, 12M…)*

**Snapshot 2026-06-29 (lãi suất ngụ ý % năm, Bid/Ask):**
| Tenor | Bid | Ask | Mid |
|------|-----|-----|-----|
| ON | 0.20 | 0.60 | 0.40 |
| **1W** | **4.50** | **5.50** | **5.00 ← gai turn chốt quý** |
| 2W | 3.70 | 4.20 | 3.95 |
| 3W | 3.30 | 3.70 | 3.50 |
| 1M | 3.30 | 3.70 | 3.50 |
| 2M | 3.30 | 3.70 | 3.50 |
| 3M | 3.30 | 3.80 | 3.55 |
| 6M | 3.40 | 3.90 | 3.65 |
| 9M | 3.50 | 3.90 | 3.70 |
| 1Y | 3.50 | 3.90 | 3.70 |

Đọc: đáy ON → spike 1W (spread rộng nhất 100bps) → plateau phẳng 3.3–3.9% → dốc lên rất nhẹ. Chuỗi pha loãng 1W 5.0 → 2W 3.95 → 3W 3.5 = cú căng điểm-thời-gian (turn 30/06) bị annualize.

---

## Bias hiện tại
- Chênh lệch lãi suất VND–USD: gần trung tính ở plateau (~3.3–3.9% ngụ ý 1M–1Y); ON cực thấp.
- Thanh khoản VND hệ thống: overnight dư, **nhưng căng cục bộ ở turn chốt quý 30/06** (1W spike) → **NHNN đã can thiệp BƠM VND**.
- Động thái SBV gần nhất: **29/06 chào hoán đổi FX 7 ngày, MUA USD giao ngay/BÁN USD kỳ hạn (= bơm VND qua turn), tối đa 1 tỷ USD, spot 23.991 / fwd 23.997 (+6đ ≈ 1,29%/năm), value T+1.** Đây là công cụ thanh khoản (USD quay vòng, trung tính FX), KHÔNG phải can thiệp mức tỷ giá.
- ⚠️ **Mâu thuẫn chưa giải:** spot swap NHNN 23.991 vs memory "spot ~26.43 sát trần" (as-of 22/06) lệch ~10% → khác mốc/sai. Cần R4 xác minh regime tỷ giá 29/06 trước khi dùng level.

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N tăng | (chưa có data) |
| **Turn-spike 1W** | tenor 1W ôm mốc chốt quý/năm | **gai annualize ở 1W (ON vẫn rẻ), pha loãng dần 1W→2W→3W** | ✅ xác nhận 29/06 (NHNN can thiệp) |
| **NHNN swap mua-giao-ngay/bán-kỳ-hạn** | turn căng VND, kỳ hạn 7d ôm mốc | **= BƠM VND tạm thời (OMO qua kênh FX), USD quay vòng → trung tính FX; đè phí turn ở 1W** | 29/06 (chờ chấm hiệu lực 1W) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | 1.65% (−125bps/phiên) 🔴 | 2026-06-23 |
| LNH 1W / 2W | 1.80% / 3.55% (−125/−135bps) 🔴 | 2026-06-23 |
| LNH 1M / 3M / 1Y | 3.55% / 3.70% / 3.80% (gần như đứng) | 2026-06-23 |
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
  - *Lưu ý 29/06:* swap ON vẫn ~0.40% mid (chưa ≥3.0%); căng đang thể hiện ở 1W thay vì ON.
- **[2026-06-29] 1W swap tụt từ ~5.0% về plateau 3.3–3.7% trong 2–5 phiên (≈03–07/07)** — Base **~80%** (nâng từ 70% sau khi NHNN công bố bơm VND 7d đúng cửa sổ turn). Chấm sau 07/07.
  - Up-risk ~12%: cầu VND vượt xa 1 tỷ USD (~24k tỷ) hoặc NHNN đảo sang hút → 1W giữ >4.5% qua 07/07.
  - Theo dõi: mức ĐĂNG KÝ thực tế / 1 tỷ USD (đầy = căng thật lan rộng; nhỏ giọt = turn kỹ thuật).
  - Pre-mortem nếu sai: căng cấu trúc sâu hơn turn (áp lực USD/tỷ giá lấn át dù NHNN bơm).

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| 2026-06-29 | GT2 đoán "spot sát trần → NHNN HÚT VND bảo vệ tỷ giá" — sai chiều. Thực tế NHNN BƠM VND (swap mua-giao-ngay/bán-kỳ-hạn). | Nhầm căng-thanh-khoản-turn thành phòng-thủ-tỷ-giá. Swap quay vòng USD nên trung tính FX. | `#bỏ-sót-SBV` `#suy-diễn-quá` |
