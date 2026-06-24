# Memory — A1 Curve Analyst

## Range lịch sử lãi suất LNH/implied VND theo tenor (mid %)
| Tenor | Range đã thấy | Ghi chú |
|-------|---------------|---------|
| O/N | 0.55 → 1.65 | 2026-06-24 sụp 0.55 (same-day flush); 06-23 1.65 |
| 1W | 1.80 → 3.70 | 06-24 spike 3.70 (>2W–3M) = turn premium dồn vào 1W qua 30/06 |
| 2W | 3.30 → 3.55 | điểm nhạy chốt quý |
| 1M | 3.35 → 3.55 | |
| 3M | 3.35 → 3.70 | |
| 6M | 3.65 | (06-24) |
| 12M | 3.80 | neo ổn định 2 phiên — đuôi curve "dính" |

## Hình dạng curve điển hình đã thấy
- **ON dip + spike 1W (2026-06-24):** ON sụp 0.55 (same-day flush), **1W vọt 3.70 > 2W(3.30)–3M(3.35)**
  → bướu cô lập tại 1W, belly phẳng 2W–3M (~3.3–3.5), đuôi dốc nhẹ lên 1Y (3.80). Spike 1W =
  **turn premium dồn vào tenor ngắn nhất bắc qua chốt quý 30/06**. Đo phí turn = đỉnh spike.
- ⚠️ **ĐÍNH CHÍNH bản chất:** bảng niêm yết CHÍNH LÀ chênh lãi (i_VND−i_USD), KHÔNG trừ i_USD nữa.
  Tất cả DƯƠNG → swap points DƯƠNG (USD forward premium): ON +0.4đ, 1W +19đ, 1M +74đ, 3M +221đ,
  6M +482đ, 1Y +1.004đ. 1W là ĐỈNH chênh lãi short-end (turn), KHÔNG phải "lõm về 0".
  (Lỗi trước: coi bảng là i_VND tuyệt đối rồi trừ i_USD lần nữa → sai dấu.)

## Bài học mổ curve
- **CẢNH BÁO neo nhầm tenor (2026-06-24):** thoạt đầu đọc 1W=1.15 → kết luận "front flush"; thực
  tế 1W=3.70 → đảo hẳn thành "ON dip + 1W spike". Bài học: kiểm tra lại giá 1W/2W trước khi phán
  hình dạng front; sai 1 điểm đổi cả luận điểm.
- Bướu cô lập ở tenor ngắn nhất bắc qua mốc lịch (chốt quý/Tết) = **phí sự kiện**; ON có thể vẫn
  rất thấp cùng lúc (bank dư same-day nhưng hoard để vuông sổ qua ngày chốt).
- Bid/ask rộng ở belly (1M, 3M = 50bps) vs front (ON 30bps) = độ chắc chắn thấp ở belly quanh turn.
