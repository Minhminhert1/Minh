# Memory — A1 Curve Analyst

## Range lịch sử swap points theo tenor
| Tenor | Range gần đây | Ghi chú |
|-------|---------------|---------|
| O/N | ~−1.4đ/ngày (23/06, derived) → +6.8đ/ngày (30/06, derived) | Đảo dấu trong 1 tuần theo spread VND–USD |
| 1M | ~97đ (30/06, derived, spread +4.45pp) | Chưa có quote thật |
| 3M | ~265–290đ (30/06, derived) | Chưa có quote thật |
| 6M | ~384đ = 2.94%/năm (forward SBV 26.850 vs spot 26.466) | Anchor duy nhất; nghi giá "trợ giá", KHÔNG dùng làm fair value CIP |
| 12M | — | Mất quote sau 23/06 |

## Hình dạng curve điển hình đã thấy
- **30/06/2026 (chốt Q2):** inverted front cực gắt (ON 13 vs 1W 8.5, −450bps) + belly phẳng ~8% (1W–3M), micro-kink trũng ở 2W. Level shift belly +450bps xảy ra TRƯỚC chốt quý (tuần 22–26/06).
- **Tiền lệ spike ON 2026:** T2: 17→9.5–10%; 01/06: 11→5.4% sau 2 phiên; mọi spike xẹp 1–3 phiên khi SBV bơm. Test kỳ hạn: spike kỹ thuật thì 1W–3M KHÔNG đuổi theo ON (30/06 belly chỉ +40–90bps trong phiên).
- **23/06:** curve dốc dương có hump lạ 2W–3W (3.55–3.80 > 1M 3.55).

## Bài học mổ curve
- **Tách 2 tầng khi đọc spike:** ON = kỹ thuật (nhìn spread ON−belly + phản ứng kỳ hạn dài); belly dịch chuyển bền mới là tái định giá cấu trúc.
- **Mâu thuẫn "mid vs bình quân":** mid quote màn hình 1 thời điểm ≠ VWAP giao dịch cả ngày; ngày biến động mạnh lệch nhau vài trăm bps là bình thường. Luôn hỏi R1 metric + timestamp trước khi kết luận Δ.
- **Gap OMO 4.5% vs LNH 8% (chênh +350bps) không tự khép** → nghi cạn collateral / phân mảng bank lớn-nhỏ; không giả định arbitrage hoàn hảo trên LNH VN.
- **Forward SBV kỳ hạn dài mở từ lâu (24/03 @26.850)** có thể stale khi spot đã chạy — kiểm tra ngày mở giá trước khi dùng làm anchor CIP.
- **Lỗ hổng data lặp lại:** 6M–1Y mất quote khi thị trường căng — cần R1 chủ động vét quote dài trước cuối quý.
