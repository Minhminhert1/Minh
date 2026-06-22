# Memory — Strategy Agent

## Setup đã thắng & lý do

*(cập nhật sau khi biết kết quả)*

---

## Setup đã thua & lý do

*(cập nhật sau khi biết kết quả — quan trọng hơn setup thắng)*

---

## Rule đã học

- **Break-even roll = forward-implied rate (no-arbitrage)**: khi sell kỳ dài rồi roll kỳ ngắn, mức hòa vốn của chân ngắn kế tiếp CHÍNH LÀ lãi suất forward mà curve đã định giá sẵn. VD curve 22/6: sell 1M 4,10 + bid 2W 4,20 → hòa khi 2W kế ≤ 4,00 (đúng = forward 2W implied ~3,99). ⇒ Roll chỉ LỜI nếu thực tế dịu HƠN kỳ vọng curve; HÒA nếu curve thành hiện thực; LỖ nếu rate kẹt cao.
- **Đọc curve đảo front để biết kỳ vọng**: 2W (4,20) > 1M (4,10) > bụng (3,90) = thị trường định giá front sẽ dịu. Nhưng nếu giá thực hằng ngày đang TĂNG (ON/1W nhảy) → momentum ngược kỳ vọng → đừng tin curve sẽ tự dịu.
- **Nghịch lý hướng-vs-carry của USD/VND (rất quan trọng)**: nếu long USD + roll 2W cùng lúc → USD mạnh/PCE nóng = tốt vế hướng nhưng 2W kẹt cao = lỗ vế carry; USD dịu = ngược lại. Hai vế tự triệt tiêu. SBV cố tình dùng lãi suất ngắn để người cược VND mất giá phải trả phí cao.
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
