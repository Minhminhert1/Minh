# Memory — A1 Curve Analyst

## Range lịch sử swap points theo tenor (lãi suất ngụ ý % năm)
| Tenor | Range gần đây | Ghi chú |
|-------|---------------|---------|
| O/N | mid 0.40 (29/06) | đáy, overnight dư thanh khoản |
| 1W | mid 5.00 (29/06) | spike turn chốt quý |
| 1M | mid 3.50 (29/06) | plateau |
| 3M | mid 3.55 (29/06) | |
| 6M | mid 3.65 (29/06) | |
| 12M | mid 3.70 (29/06) | dốc lên rất nhẹ |

## Hình dạng curve điển hình đã thấy
*(vd: backwardation khi i_VND < i_USD; kink 1M lúc cuối quý)*
- **Turn-spike 1W (29/06):** đáy ON → gai 1W → plateau phẳng 3W+. Chuỗi pha loãng 1W>2W>3W = dấu hiệu cú căng điểm-thời-gian bị annualize. Spread rộng nhất ở tenor ôm turn.
- **Mẹo đọc đơn vị:** swap points tuyệt đối (đồng) PHẢI đơn điệu tăng theo tenor. Nếu bảng KHÔNG đơn điệu → đang là lãi suất ngụ ý/năm, không phải points tích lũy.

## Khung "4 đoạn" để mổ curve VN (regime gap dương 2026)
1. **ON** ghìm sát 0 = điểm NHNN can thiệp trực tiếp nhất (OMO/swap) → thấp ≠ dư thật, dễ giật.
2. **Gai 1W** = phí phòng thủ cửa sổ thanh khoản (turn/thuế/đáo hạn tín phiếu); spread rộng = stress dồn đầu đường cong.
3. **Bụng 3W–2M phẳng** = gap CẤU TRÚC thật (~3,3–3,5%); phẳng = không kỳ vọng giải căng trong 1–3 tháng.
4. **Đuôi 3M→1Y dốc lên** = phần bù mất giá nới dần (cài sẵn kỳ vọng VND yếu thêm).
- **Suy swap points:** F = S·(1+r_vnd·t/360)/(1+r_usd·t/360). Bản giản lược `S·gap·t/360` lệch <4% với S~26.300, tenor ≤1Y → dùng nhanh được.
- **CIP ≠ kỳ vọng:** forward premium = chênh lãi suất (arbitrage), chỉ = kỳ vọng mất giá nếu UIP đúng. Đừng coi gap là "bằng chứng độc lập" về mất giá.

## Bài học mổ curve
*(lỗi từng mắc khi đọc fair value / dấu swap points)*
