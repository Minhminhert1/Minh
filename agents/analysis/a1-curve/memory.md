# Memory — A1 Curve Analyst

## Range lịch sử lãi suất LNH/implied VND theo tenor (mid %)
| Tenor | Range đã thấy | Ghi chú |
|-------|---------------|---------|
| O/N | 0.55 → 1.65 | 2026-06-24 sụp 0.55 (flush); 06-23 1.65 |
| 1W | 1.15 → 1.80 | |
| 2W | 3.30 → 3.55 | điểm "turn premium" — nhạy với chốt quý |
| 1M | 3.35 → 3.55 | |
| 3M | 3.35 → 3.70 | |
| 6M | 3.65 | (06-24) |
| 12M | 3.80 | neo ổn định 2 phiên — đuôi curve "dính" |

## Hình dạng curve điển hình đã thấy
- **Front-flush + kink 1W→2W (2026-06-24):** ON/1W sụp (0.55/1.15), nhảy +215bps lên 2W (3.30),
  belly phẳng 2W–3M (~3.3–3.5), đuôi dốc nhẹ lên 1Y (3.80). Bậc nhảy 1W→2W = **turn premium**
  (kỳ hạn bắc qua chốt quý 30/06). Đo phí qua-turn = độ cao bậc nhảy.
- i_VND < i_USD toàn dải → swap points âm; âm sâu nhất ở front (~−307bps tại ON),
  thu hẹp về gần CIP-flat ở 1Y (~−10/−40bps).

## Bài học mổ curve
- Đọc bậc nhảy giữa 2 tenor liền kề bắc qua mốc lịch (chốt quý/Tết) như **phí sự kiện**,
  đừng đọc thành "lãi suất term cao hơn" thuần tuý.
- Bid/ask rộng ở belly (1M, 3M = 50bps) vs front (ON 30bps) = thanh khoản/độ chắc chắn
  thấp ở belly quanh turn, KHÔNG phải mid đáng tin hơn.
