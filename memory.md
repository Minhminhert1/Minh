# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*
- [2026-06-25] Macro VN "nóng + đối ngoại căng": GDP Q1 +7.83%, CPI T5 +5.60% (vượt mục tiêu 4.5% theo tháng), nhập siêu T5 5.21 tỷ USD (kỷ lục từ 1990). 3 lực cùng đẩy VND yếu: nhập siêu + lạm phát cao + thuế Mỹ 20%/40% từ tháng 8. → Chi tiết: `reports/2026-06-25-macro-vn.md`.

---

## Curve & tenor đang theo dõi
*(swap points các kỳ hạn user quan tâm: O/N, 1W, 1M, 3M, 6M, 12M…)*

---

## Bias hiện tại (2026-06-25)
- **Chênh lệch lãi suất VND–USD: ÂM và doãng rộng** (VND ON 0.30/term 3.4–3.75 vs SOFR 3.62). ⚠️ Thị trường định giá **Fed TĂNG** (~3.8% T9, ~4% cuối 2026) → van "Fed cắt nới chênh dương" ĐÃ ĐÓNG → áp lực mất giá VND mang tính **cấu trúc**.
- **Thanh khoản VND: DỒI DÀO** (ON 0.30, SBV thả ưu tiên tăng trưởng).
- **Động thái SBV: THẢ, chưa hút.** Spot 26.43 sát trần kỹ thuật ~26.44 (trung tâm 25.183 × ±5%). SBV mua thời gian bằng trườn tỷ giá trung tâm + bán USD lẻ, chưa hút VND.
- **Trục lật toàn cục:** SBV còn thả hay xoay sang hút (tín phiếu ròng / spot phá trần) — quyết định toàn bộ curve.
- Global: SOFR 3.62, Fed funds 3.63 (giữ 3.50–3.75 tại FOMC 17/06), DXY vững, USD/CNY ~6.78 đỉnh 2 năm.

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng — KỲ HẠN VẮT QUA chốt quý (1W/2W) bật, ON có thể RỚT (tiền không vắt qua = thừa) | ✅ ĐÚNG 2026-06-25: 1W 4.35 (+0.65), ON 0.30 |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | 0.30% (rớt sâu, thừa thanh khoản) 🔴 | 2026-06-25 |
| LNH 1W / 2W | 4.35% / 3.70% (+65/+40bps — phí chốt quý) 🟢 | 2026-06-25 |
| LNH 1M / 3M / 6M / 1Y | 3.40% / 3.45% / 3.60% / 3.75% | 2026-06-25 |
| Tỷ giá trung tâm | 25.183 | 2026-06-22 |
| USD/VND spot | ~26.43 (sát trần) | 2026-06-22 |
| SOFR (ON) | 3.62% | 2026-06-18 |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| *(cập nhật)* | | | | |

### Sổ chờ chấm
- **[2026-06-23] ON bật về ≥3.0% trong 3–7 phiên (quanh 26–30/06)** — Base ~55%. ⚠️ ĐANG TRƯỢT: 25/06 ON rớt về **0.30%** (ngược hướng). Kịch bản down (ON giữ thấp) đang thắng. Lý do sai: đọc nhầm hàm phản ứng SBV (kỳ vọng hút VND cứu FX, thực tế thả thanh khoản). Chốt chấm sau 30/06, nghiêng MISS.
- **[2026-06-25] 1W rớt về 2.3–2.8% quanh 02–07/07** (sau chốt quý) — Base ~45–50% (đã hạ theo Reviewer); Up ~35% nếu SBV hút (spot≥26.50 / tín phiếu ròng). Chấm 07/07.
- **[2026-06-25] ON giữ ≤1.5% tới 30/06** — ~50–60%. Trừ khi SBV lật sang bảo vệ trần tỷ giá.
- **[2026-06-25] Chênh lãi suất VND–USD 3M giữ âm nhẹ (−0.1…−0.2%) tới cuối 7/2026** — Base ~50%. Lật dương nếu SBV thắt sớm hoặc Fed cắt SOFR. Chấm cuối 7.
- **[2026-06-25] Q3 (sau thuế 8/2026): chênh VND–USD 3M bò về 0…+0.4%, term VND +10–30bp** — Base ~50%. Chấm cuối Q3.
  > Chi tiết + chiến lược: `reports/2026-06-25-forecast-strategy.md`. Reviewer: 4 CẦN SỬA + 1 BẤT ĐỒNG, không PASS thẳng. Blind spot chặn: thiếu Bid/Ask + NDF + OMO realtime.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| 2026-06-25 | Kỳ vọng ON bật ≥3.0% (dự báo 23/06) — thực tế rớt 0.30% | Đọc nhầm phản ứng SBV: tưởng áp lực FX (spot sát trần, nhập siêu) sẽ ép hút VND; SBV lại thả thanh khoản ưu tiên tăng trưởng | #bỏ-sót-SBV |
