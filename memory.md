# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
- **[2026-07-02] Đọc curve 2 tầng:** spike ON (chốt quý/thuế) là nhiễu — xẹp 1–3 phiên khi SBV bơm; **belly 1M–3M mới là tín hiệu cấu trúc** (test: spike kỹ thuật thì belly không đuổi theo ON trong phiên).
- **[2026-07-02] Không trộn nguồn curve:** mid quote màn hình (user) ≠ bình quân gia quyền báo chí/SBV — lệch được vài trăm bps. Mọi so sánh Δ phải cùng nguồn + cùng metric + cùng timestamp. Luôn hỏi user metric của bộ số.
- **[2026-07-02] Bộ công cụ "câu giờ" của SBV (không tốn dự trữ):** swap USD/VND 7–14d (3 lần trong 5 tuần: 26/05, 01/06, 30/06) + OMO kỳ hạn dài 35–56d + forward 180d treo giá 26.850 + trần hành chính. Theo dõi **ngày đáo swap** (roll hay không) là tín hiệu sớm nhất.
- **[2026-07-02] Phối hợp agent:** proxy môi trường chặn fetch trực tiếp báo VN (403) → researcher phải dựa trích xuất search, trần độ tin 4. Subagent có thể chạm session limit — tầng Analysis chạy inline trong phiên chính vẫn đạt chất lượng nếu data pack đủ.

---

## Curve & tenor đang theo dõi
- **LNH VND 30/06 (bình quân, báo chí):** ON 13,0 / 1W 8,5 / 2W 8,0 / 1M 8,1 / 3M ~7,75–8,1 / 6M–1Y mất quote. Front inverted (chốt quý), belly ~8% bền cả tháng 6.
- **Swap points USD/VND [DERIVED, spot 26.466]:** 1M ~+97đ (spread +4,5đpt) / 3M ~+265–290đ / anchor 6M forward SBV 26.850 = +384đ ≈ 2,94%/năm (nghi giá trợ giá, không dùng làm fair value).
- **Đảo dấu lịch sử:** đầu cong từ âm (~−2đpt, 23/06) sang dương (+9,3đpt tại ON, 30/06).
- **Tenor rủi ro repricing:** 1W–2W (bắc qua đáo swap 07/07 + VAT 20/07) và mọi kỳ hạn bắc qua ~24/07 (thuế quan).

---

## Bias hiện tại (as-of 2026-07-02)
- Chênh lệch lãi suất VND–USD: **DƯƠNG LỚN** (1M ~+4,5đpt; ON spike +9,3đpt sẽ xẹp). Chân USD khó hạ: Fed dot plot hàm ý TĂNG (CPI Mỹ 4,2%).
- Thanh khoản VND hệ thống: **căng cấu trúc** (tín dụng +18,26% YoY > huy động; OMO lưu hành ~244.000 tỷ; belly 8% cả tháng) + spike chốt quý 30/06 đã qua.
- Động thái SBV gần nhất: bơm ròng OMO kỳ hạn dài 35–56d @4,5% (~14.600 tỷ phiên 30/06) + swap USD/VND 7d (30/06, đáo ~07/07) + trung tâm tăng chậm (25.206, tuần thứ 7) + CHƯA bán USD spot (độ tin 3).
- FX: spot **kịch trần 26.466**; tự do premium 150–250đ; vàng SJC +14,6% — kỳ vọng phá giá + flow (nhập siêu 16,8 tỷ, ngoại rút 3 tỷ) đang thắng carry.
- **[2026-07-02, data nội bộ độ tin 5] Funding gap CẤU TRÚC xác nhận bằng số cứng:** TD toàn HT +7,08% ytd (24/06) vs HĐV TT1 +5,02% ytd → GAP TT1 −378k tỷ ytd, đang mở rộng. CV ngoại tệ +39,6% ytd vs HĐ NT +5,02% ytd → gap CV−HĐ ngoại tệ **−7,32 tỷ USD**. Đây là driver cấu trúc chính khiến belly LNH đứng ~8% VÀ USD demand cao (thêm chân nội sinh từ NHTM tự cân đối trạng thái ngoại tệ, không chỉ từ nhập khẩu/đầu tư).

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N tăng | ✅ **XÁC NHẬN 30/06/2026**: ON 3,6→13% đúng phiên khóa sổ Q2, dù SBV bơm kỷ lục |
| Spike ON xẹp nhanh | ON spike + SBV bơm ròng | ON về mặt bằng cũ sau 1–3 phiên | ✅ 3/3 tiền lệ 2026 (17% T2 → 9,5–10%; 11% 01/06 → 5,4% sau 2 phiên; chờ chấm lần 30/06) |
| Kỳ thuế hút VND | hạn VAT 20 hằng tháng, TNDN cuối quý | ON/1W bật tạm thời (tiền vào KBNN) | ✅ tiền lệ 03/02/2026 (ON 7,9→17%); lưu ý 2026 có gia hạn thuế làm nhẹ |
| SBV swap FX khi ON căng + spot sát trần | ON spike mà không muốn tốn dự trữ | bơm VND 7–14d, ON hạ 1–2 phiên | ✅ 3 lần: 26/05, 01/06, 30/06 — theo dõi ngày đáo (roll?) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **13,0%** (+940bps, chốt quý) 🔴 | 2026-06-30 |
| LNH 1W / 2W | 8,5% / 8,0% | 2026-06-30 |
| LNH 1M / 3M | 8,1% / ~7,75–8,1% (3M data cũ) | 2026-06-30 |
| LNH 6M–1Y | mất quote | — |
| Tỷ giá trung tâm | 25.206 (tuần tăng thứ 7) | 2026-07-02 |
| USD/VND spot (VCB bán) | **26.466 = KỊCH TRẦN** 🔴 | 2026-07-02 |
| USD/VND tự do | 26.610–26.720 (premium 150–250đ) | 2026-07-01 |
| SOFR (ON) | 3,68% | 2026-06-30 |
| OMO lưu hành | ~244.000 tỷ | 2026-06-26 |
| DXY | 101,4 | 2026-07-01 |
| ⚠️ Lưu ý | Bộ mid user 23/06 (ON 1,65%) **không tương thích** chuỗi bình quân báo chí — chờ user xác nhận metric | |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| ON front-end | 1 | 1 | 100% (n=1) | Đúng hướng + cửa sổ; **biên độ quá hẹp** (thực tế 13% vượt cả up-risk 4–6%); cơ chế lệch (spike do cầu chốt quý khi SBV BƠM, không phải SBV hút) |

### Sổ chờ chấm (đặt 2026-07-02, xem chi tiết reports/2026-07-02-*.md §4)
- **ON về 4–7% trong 1–4 phiên sau chốt quý (chậm nhất 08/07)** — Base 65%. Chấm 08/07. Gót chân: đáo swap 7d ngày 07/07.
- **Spot bám/sát trần suốt T7 (chênh trần <80đ); trung tâm 25.250–25.310 cuối T7; SBV chưa bán USD spot** — Base 60%. Chấm 31/07. Up-risk 25% nếu thuế quan xấu (07/07 / ~24/07).
- **Belly 1M–3M giữ 7,5–8,5% qua kỳ thuế T7; swap points 3M ~+250–320đ** — Base 55%. Chấm 31/07. Trigger phân xử bất đồng A2↔Reviewer: belly sau 24/07 còn ≥7,5%?

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| 2026-07-02 | Báo cáo 23/06 mô tả "front-end depressed 1,65%" như trạng thái thị trường trong khi bình quân LNH cùng ngày ~6% — có thể đã phân tích trên bộ số không đại diện | Không hỏi metric/nguồn của bộ mid user; không đối chiếu ngay với bình quân SBV/báo chí | `#data-cũ` `#thiếu-data` |
| 2026-07-02 | Kịch bản up-risk 23/06 gộp chung "ON tăng do SBV hút" — thực tế ON tăng 13% khi SBV đang bơm kỷ lục (cầu mùa vụ) | Thiếu tách cơ chế: siết chính sách ≠ cầu mùa vụ | `#suy-diễn-quá` |
| 2026-07-02 | Báo cáo 02/07 §7 tự chấm "✅ ĐÚNG, hit-rate 1/1" cho dự báo 23/06 dù chính báo cáo (§2.2) đã cảnh báo baseline (ON 1,65%) không tương thích data độc lập — mâu thuẫn logic, không được ép ra 1 kết luận sạch khi chưa xác nhận baseline | Không kiểm tra chéo giữa các mục trong cùng báo cáo trước khi chốt scoreboard | `#suy-diễn-quá` `#thiếu-data` |
| 2026-07-02 | OMO tuần 22–26/06 "bơm ròng ~3.962 tỷ" trích Vietstock nhưng phép trừ thô (30.962−72.000=−41.038) không khớp, caveat này bị rơi khi tổng hợp vào báo cáo cuối (§1.3 gốc) dù R1 đã tự flag | Synthesis không carry-forward FRESHNESS FLAGS đầy đủ theo đúng schema.md | `#thiếu-data` |
