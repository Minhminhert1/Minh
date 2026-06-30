# Phân tích curve — 2026-06-30 (chốt quý BCTC) — PB-1

> Input: bảng lãi suất USD/VND (mid) ON→1Y. Bối cảnh: đúng ngày chốt quý 30/06.

## Data (mid)
| Tenor | Hôm nay | Cuối hôm qua | Δ |
|-------|---------|--------------|---|
| ON | 9.50 | 0.40 | +9.10 🔴🔴 |
| 1W | 5.00 | 5.00 | 0.00 |
| 2W | 4.50 | 3.95 | +0.55 🔴 |
| 3W | 3.55 | 3.50 | +0.05 |
| 1M | 3.40 | 3.50 | −0.10 |
| 2M | 3.40 | 3.50 | −0.10 |
| 3M | 3.40 | 3.50 | −0.10 |
| 6M | 3.40 | 3.55 | −0.15 |
| 9M | 3.55 | 3.70 | −0.15 |
| 1Y | 3.65 | 3.70 | −0.05 |

## A1 · Curve
- Twist: front-end bốc cháy (ON 9.50), belly/back hạ 10–15bps. Đảo dốc gắt ON→1M (−610bps).
- 1W dính 5.0 (cửa sổ bắc qua chốt quý). Belly phẳng ~3.40, dốc lên nhẹ tới 1Y 3.65.
- Hôm qua price-in căng vào 1W+2W; hôm nay hiện thực ở ON, còn ≥1M giảm → kỹ thuật cuối quý, KHÔNG phải tightening cấu trúc.
- Fair value: belly 3.40% < SOFR ~3.62% → swap points 1M–6M âm nhẹ/sát 0.

## A2 · Insight (ON=9.50)
- GT1 kỹ thuật chốt quý BCTC ~70% (ủng hộ: đúng 30/06, ≥1M không tăng).
- GT2 SBV hút VND giữ trần ~25% (spot sát trần 26.43; phản đối: belly không tăng theo).
- GT3 kẹt cục bộ ~5%. Nghiêng GT1, canh GT2.
- Hàm ý swap: ON/TN transient bỏ qua; 1M–3M carry âm nhẹ (VND<USD ~20bps), forward points sát phẳng.

## A3 · Forecast
- Base ~65%: ON ≤3.0% trong 1–3 phiên (đến ~03/07), belly 3.30–3.45.
- Up-risk ~25%: SBV giữ chặt → ON >4% tới giữa T7, belly +10–20bps.
- Down ~10%: ON về 1–2% trong 1–2 phiên, belly ~3.2%.
- Chốt cũ [06-23] "ON ≥3.0% quanh 26–30/06" → HIT (nhánh up-risk).

## Reviewer
- PASS có điều kiện. `#thiếu-data`: cần R1/R4 xác nhận OMO ròng + spot vs trần phiên 30/06 để phân định GT1/GT2.
