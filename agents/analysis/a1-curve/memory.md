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

## Bài học mổ curve
*(lỗi từng mắc khi đọc fair value / dấu swap points)*
