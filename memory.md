# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

### Session 28/06 — Chuẩn bị chốt Q2
- **Kiểu phân tích R1:** Dữ liệu 23/06 cho baseline; 24–28/06 suy luận từ pattern cuối quý (BCTC, mục đích hạn, OMO/tín phiếu) thay vì live crawl. Độ tin "hướng" cao, "con số" trung bình khi thiếu data OMO hôm nay.
- **Watchlist key:** Spot sát trần (26.433 vs 26.442) → risk trigger ALERT nếu ON >4% hoặc spot ≥26.44.
- **A1/A3 input:** R1 FACT SHEET 28/06 cho hướng cuối quý; chưa có snapshot curve hôm nay (cần web/Bloomberg live để mổ).
- **Next checkpoint:** 29–30/06 — chốt quý + xác nhận dự báo base vs up-risk.

---

## Curve & tenor đang theo dõi
*(swap points các kỳ hạn user quan tâm: O/N, 1W, 1M, 3M, 6M, 12M…)*

---

## Bias hiện tại
- Chênh lệch lãi suất VND–USD: **ON 1.65% << SOFR 3.62% (diff −1.97%)** → carry VND xấu ở đầu cong; chân dài 3.70–3.80% ~ 3.5–3.6% (dương/ngang).
- Thanh khoản VND hệ thống: **Cuối 23/06 dồi dào ở front-end** (ON rơi xuống 1.65%, cú bơm/easing); **28/06 dự báo sẽ căng dần** (nhu cầu BCTC, mục đích hạn).
- Động thái SBV gần nhất: **23/06 bơm OMO, để ON xuống**; **24–28/06 dự báo quay hút** theo nhu cầu cuối quý; **Rủi ro cao:** Spot sát trần (26.433) → SBV có thể hút VND nóng → ON bật ↑↑ (up-risk scenario).

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng, O/N tăng | (Q2/2026 testing — 28/06 chưa chốt, dự báo base ~55%) |
| Bươu 2W–3W trước chốt | 23–30/06 kỳ hạn bắc qua ngày chốt | Premium giữ tiền cuối quý (3W >2W >1M) | (Q2 thể hiện, hạ dần khi OMO bơm) |
| OMO bơm → ON sụp | flush thanh khoản trước chốt quý | ON rơi nhanh (125 bps/phiên có thể) | (Q2/23/06 validate) |
| Spot sát trần → SBV hút | USD/VND chạm trần nhiều phiên | ON bật ↑↑ (4–6%+), swap points dương hơn | (Q2 risk, chưa kích hoạt) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of | Trạng thái |
|--------|------------------|-------|-----------|
| LNH O/N | 1.65% (−125bps/phiên) | 2026-06-23 | 🟡 **Dự báo ↑ 2.5–3.5%** qua chốt quý |
| LNH 1W / 2W | 1.80% / 3.55% (−125/−135bps) | 2026-06-23 | 🟡 **Dự báo tương tự** |
| LNH 1M / 3M / 1Y | 3.55% / 3.70% / 3.80% (gần như đứng) | 2026-06-23 | 🟢 Dự báo ≈ đứng ±10bps |
| Tỷ giá trung tâm | 25.183 | 2026-06-22 | 🟢 Ổn định |
| USD/VND spot | ~26.43 (sát trần 26.442) | 2026-06-22 | 🔴 **ALERT risk** — sát trần → SBV hút VND → ON ↑↑ |
| SOFR (ON) | 3.62% | 2026-06-18 | 🟢 Ổn định (Fed hold) |

---

## Scoreboard dự báo (Journalist tổng hợp)
| Tenor/loại | Số dự báo | Đúng | Hit-rate | Ghi chú calibration |
|------------|-----------|------|----------|---------------------|
| *(cập nhật)* | | | | |

### Sổ chờ chấm
- **[2026-06-23] ON bật về ≥3.0% trong 3–7 phiên (quanh 26–30/06)** — Base ~55%. Chấm sau 30/06.
  - Up-risk ~30%: nếu spot ép trần → SBV hút VND → ON 4–6%+ trong 1–2 tuần.
  - Down ~15%: ON giữ 1.5–2.5% kéo dài qua chốt quý.

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| *(ghi khi sai)* | | | |
