# Memory — Strategy Agent

## Setup đã thắng & lý do

*(cập nhật sau khi biết kết quả)*

---

## Setup đã thua & lý do

*(cập nhật sau khi biết kết quả — quan trọng hơn setup thắng)*

---

## Rule đã học

- **Break-even khi roll kỳ hạn (term vs roll)**: khóa kỳ dài = ghép các kỳ ngắn → trung bình các kỳ ngắn phải bằng kỳ dài.
  - Nhẩm nhanh (lãi đơn, 2 kỳ cân bằng): `X = 2×r_dài − r_ngắn_đầu`. VD: sell 1m 4.2, bid 2w 5.6 → X = 2.8%.
  - Chuẩn Act/365 + lãi kép: `X = [(1 + r_1m·D/365)/(1 + r1·d1/365) − 1]·365/d2`. Cùng VD (28d) → **2.79%**.
  - Tenor ngắn (≤2w): hiệu ứng lãi kép ~0.01% → nhẩm trung bình là đủ; day-count chỉ tinh chỉnh phần lẻ.
  - Cẩn thận khớp số ngày: 1m=30d mà 2 chân chỉ phủ 28d → hụt 2 ngày, đổi kết quả (chân sau 16d → ~2.97%).
- **Không dùng carry "giữ VND ăn lãi" khi DXY mạnh** — lỗ tỷ giá ăn sạch lãi chênh (22/6/2026).
- **Khi đồng funding (JPY) đang tăng lãi → giảm tỷ trọng carry xJPY** — gap teo + rủi ro unwind.
- **Carry không bao giờ là "free swap"**: luôn check rủi ro can thiệp NHTW (vd USD/JPY >161 → Nhật dễ can thiệp) và risk-off.
- **Tín hiệu thoát carry**: JPY mạnh lên đột ngột = dấu hiệu unwind bắt đầu.

---

## Winrate theo loại setup

*(cập nhật dần để biết loại setup nào hiệu quả nhất)*
