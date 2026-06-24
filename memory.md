# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

- **[2026-06-24]** Front-end LNH VND sụp (ON 0.55%, 1W 1.15%) NGAY trước chốt quý 30/06 —
  ngược kỳ vọng seasonality "cuối quý funding căng → ON tăng". Bài học: seasonality KHÔNG
  override thanh khoản thực; khi dòng tiền/SBV bơm dư, front-end vẫn flush dù sát chốt quý.
- **[2026-06-24]** Đọc curve qua "kink 1W→2W": điểm gãy +215bps là **turn premium** —
  kỳ hạn bắc qua 30/06 (2W+) mang phí funding ~3.3%+, còn ON/1W (đáo trước turn) flush.
- **[2026-06-24]** ON rẻ (0.55%) + spot sát trần (~26.43) = **lò xo nén**: VND rẻ nuôi carry
  short VND → ép spot → SBV nhiều khả năng hút (tín phiếu) đỡ đồng → ON có thể bật ngược dữ.

---

## Curve & tenor đang theo dõi
*(lãi suất LNH/implied VND theo kỳ hạn — snapshot mới nhất, mid %)*

| as-of | ON | 1W | 2W | 1M | 3M | 6M | 1Y | Hình dạng |
|-------|----|----|----|----|----|----|----|-----------|
| 2026-06-24 | 0.55 | 1.15 | 3.30 | 3.35 | 3.35 | 3.65 | 3.80 | front flush + kink 1W→2W (turn premium); belly phẳng ~3.3–3.5; đuôi dốc nhẹ lên |
| 2026-06-23 | 1.65 | 1.80 | 3.55 | 3.55 | 3.70 | — | 3.80 | — |

---

## Bias hiện tại
- Chênh lệch lãi suất VND–USD: **front âm sâu** (ON: 0.55−3.62 ≈ −307bps) → thu hẹp về
  **gần phẳng ở 1Y** (3.80 vs USD ~3.9–4.2 ≈ −10/−40bps). ⇒ swap points âm toàn dải,
  âm sâu nhất ở front, gần CIP-flat ở đuôi. *(USD term rate là ước lượng — FRESHNESS FLAG)*
- Thanh khoản VND hệ thống: **dồi dào ở front (ON–1W)**, term (2W+) vẫn neo ~3.3–3.8% →
  thị trường KHÔNG pricing squeeze chốt quý lớn.
- Động thái SBV gần nhất: *(chưa có data OMO/tín phiếu hôm nay — cần R1/R4 xác nhận)* —
  ON 0.55% gợi ý SBV đang để dư/đáo hạn tín phiếu bơm lại; rủi ro đảo chiều nếu SBV hút đỡ tỷ giá.

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N tăng | ⚠️ 2026-06-24 SAI ngược: ON sụp 0.55% sát chốt quý → seasonality bị thanh khoản dư override |
| Kink 1W→2W = turn premium | curve có bậc nhảy ở tenor bắc qua chốt quý | đo được phí qua-turn = bậc nhảy (bps) | mới (2026-06-24, +215bps) |
| Lò xo nén front-flush + spot trần | ON < 1% đồng thời spot sát trần | SBV dễ hút → ON bật ngược; theo dõi tín phiếu | chờ chấm (30/06) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **0.55%** (−110bps/phiên) 🔴 ALERT (thủng 1.0%) | 2026-06-24 |
| LNH 1W / 2W | 1.15% / 3.30% (−65 / −25bps) | 2026-06-24 |
| LNH 1M / 3M / 1Y | 3.35% / 3.35% / 3.80% (−20 / −35 / 0bps) | 2026-06-24 |
| Tỷ giá trung tâm | 25.183 | 2026-06-22 |
| USD/VND spot | ~26.43 (sát trần) | 2026-06-22 |
| SOFR (ON) | 3.62% | 2026-06-18 |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| *(cập nhật)* | | | | |

### Sổ chờ chấm
- **[2026-06-23] ON bật về ≥3.0% trong 3–7 phiên (quanh 26–30/06)** — Base ~55%. Chấm sau 30/06.
  - Up-risk ~30%: nếu spot ép trần → SBV hút VND → ON 4–6%+ trong 1–2 tuần.
  - Down ~15%: ON giữ 1.5–2.5% kéo dài qua chốt quý.
  - 🔻 **Cập nhật 2026-06-24:** ON KHÔNG bật mà SỤP về 0.55% → nhánh Base (gradual bounce)
    đang sai; nhánh Down còn cực đoan hơn dự kiến (xuống dưới 1.0%). Cửa sổ vẫn mở tới 30/06 →
    nhánh **Up (SBV hút đỡ tỷ giá) vẫn sống** và là rủi ro chính hiện nay. Chấm chốt sau 30/06.

- **[2026-06-24] Curve front-flush: ON giữ < 2.0% xuyên chốt quý tới 30/06; KHÔNG có squeeze lớn**
  — Base ~50%. Điều kiện huỷ: SBV phát hành tín phiếu hút ròng → ON > 3% trong 1–3 phiên.
  - Up-risk ~30%: SBV hút đỡ đồng (spot sát trần) → ON bật 3–5%+ trong vài phiên.
  - Down ~20%: dư cấu trúc kéo dài, ON 0.3–1.0% sang đầu T7. Chấm sau 03/07.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| *(ghi khi sai)* | | | |
