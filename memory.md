# Memory — Swap USD/VND Research Team

> Bộ nhớ tổng toàn team. Cập nhật sau mỗi session. Đây là tài sản làm team "giỏi lên".

---

## Bài học tổng hợp
*(cập nhật sau mỗi turn — pattern thị trường VN, cách phối hợp agent)*

- **[2026-06-24] SELF-REVIEW (vì sao chất lượng tụt so với 06-23):** Bản 06-23 tốt vì **neo dữ liệu
  thật có nguồn + URL** (SOFR/FRED, spot, tin ON 11%, VDSC) và **ngắn, ra quyết định**. Bản 06-24
  tệ vì: (1) **không tra web** — spawn 5 Opus suy từ cutoff rồi đóng dấu [ƯỚC LƯỢNG] → độn chữ;
  (2) **nghi thức (3 wave + red-team) thay tư duy** — vẫn để lọt lỗi trừ i_USD hai lần;
  (3) **dài hơn nhưng loãng hơn**; (4) **lật convention input 3 lần** vì không chốt định nghĩa.
  → Đòn bẩy chất lượng = **DATA neo + 1 lượt phân tích sắc**, KHÔNG phải model tier hay số agent.
  Đã ban luật #8–#13 + `system/sources.md` + checklist Reviewer tái-tính-số. **Đây là luật, không phải gợi ý.**

- **[2026-06-24] v3.0 — quay về đơn giản của v1.** Chẩn đoán (bằng chứng repo): v2.0 (`368722e`)
  làm tụt chất lượng vì (1) đập vụn 1 bộ não Opus → A1/A2/A3 (A3 còn hạ Sonnet) → mất xương sống
  tự sự; (2) cho **Strategy ngủ** → mất layer setup (nửa giá trị bản 19/06); (3) bó hẹp sứ mệnh vào
  swap-rates; (4) thêm giàn giáo (schema cứng, model-cap) thay tư duy. Bản vàng 19/06 do **v1: 1
  Analysis Opus dệt macro+kỹ thuật+bull/bear + 1 Strategy active**. → v3: gộp bộ não, **đánh thức
  Strategy**, hạ swap xuống PB-SWAP, R/A sub thành lăng kính tùy chọn; giữ luật #8–#15 + template +
  system/. **Luật #15: không tái lập team — tiến hóa qua memory/luật, không reorg.**

- **[2026-06-24] CHUẨN VÀNG = báo cáo USDVND 19/06** (`benchmarks/2026-06-19-USDVND-gold-standard.pdf`).
  DNA làm nó hay: (1) thesis-first box; (2) **xương sống tự sự đáng nhớ** ("3 làn sóng", "đường biên
  26.550"); (3) **đào tín hiệu ẩn** (forward hủy ngang = trần ngầm câu giờ); (4) mọi số neo nguồn+ngày;
  (5) một "trái tim" (gap lãi suất thực); (6) ma trận kịch bản+EV; (7) Reviewer N lỗ hổng có mức độ +
  kịch bản đảo chiều; (8) dashboard trigger; (9) phân khúc hành động. → Đã codify vào
  `system/report-template.md` + luật #14. **Hay = tự sự + insight ẩn neo trên data, KHÔNG phải dài.**

- **[2026-06-24]** ON sụp 0.55% nhưng **1W vọt 3.70%** (>2W–3M) → KHÔNG phải "front flush".
  Overnight thật (đáo trước 30/06) dư; còn **funding bắc qua chốt quý căng ~3.7%**, dồn vào 1W.
  Bài học: đọc seasonality cuối quý ở **tenor bắc qua turn (1W/2W)**, đừng nhìn ON. ON thấp +
  1W cao cùng lúc = bank hoard thanh khoản để vuông sổ QUA ngày chốt, đẩy giá 1W phủ 30/06.
- **[2026-06-24]** Turn premium **dồn vào 1W** (spike 1W 3.70 > 2W 3.30): 1W là kỳ hạn ngắn nhất
  "all-in" qua turn → phí chốt quý chia trên ít ngày → lãi quy năm cao nhất. Đo phí turn = đỉnh spike.
- **[2026-06-24]** Spot sát trần (~26.43) + thị trường ĐÃ pricing funding turn căng (1W 3.70) →
  rủi ro SBV hút giảm bớt so với kịch bản "ON còn 0.5% ngây thơ"; nhưng nếu spot vẫn ép trần,
  SBV vẫn có thể hút đẩy cả ON lẫn term lên.

---

## Curve & tenor đang theo dõi
*(lãi suất LNH/implied VND theo kỳ hạn — snapshot mới nhất, mid %)*

| as-of | ON | 1W | 2W | 1M | 3M | 6M | 1Y | Hình dạng |
|-------|----|----|----|----|----|----|----|-----------|
| 2026-06-24 | 0.55 | **3.70** | 3.30 | 3.35 | 3.35 | 3.65 | 3.80 | ON dip + **spike 1W** (turn premium dồn vào 1W qua 30/06, 1W>2W–3M); belly phẳng ~3.3–3.5; đuôi dốc nhẹ |
| 2026-06-23 | 1.65 | 1.80 | 3.55 | 3.55 | 3.70 | — | 3.80 | — |

---

## Bias hiện tại
- **Chênh lệch lãi suất VND–USD = CHÍNH bảng niêm yết** (đường cong đã LÀ i_VND−i_USD, KHÔNG trừ
  thêm i_USD). Tất cả DƯƠNG: ON +0.55% → 1W +3.70% (đỉnh turn) → belly +3.3–3.5% → 1Y +3.80%.
  ⇒ swap points DƯƠNG toàn dải (USD forward premium): ON +0.4đ, 1W +19đ, 1M +74đ, 3M +221đ,
  6M +482đ, 1Y **+1.004đ**. KHÔNG phải forward discount. (Forward 1Y ≈ 27.434.)
- Thanh khoản VND hệ thống: **overnight dư** (ON 0.55%) nhưng **funding qua chốt quý CĂNG** (1W 3.70%)
  → squeeze chốt quý CÓ thật, dồn vào tenor bắc qua 30/06; ON thấp chỉ là same-day.
- Động thái SBV gần nhất: *(chưa có data OMO/tín phiếu hôm nay — cần R1/R4 xác nhận)* —
  ON 0.55% gợi ý SBV đang để dư/đáo hạn tín phiếu bơm lại; rủi ro đảo chiều nếu SBV hút đỡ tỷ giá.

---

## Pattern đã học (thẻ tra cứu)
> Mỗi pattern: điều kiện kích hoạt + lần đúng/sai. Researcher nạp thẻ liên quan thay vì đọc cả memory.

| Pattern | Điều kiện kích hoạt | Tác động | Đúng/Sai |
|---------|---------------------|----------|----------|
| BCTC cuối quý | tới 25–31 cuối Q | funding VND căng — nhưng ở tenor bắc qua turn, KHÔNG nhất thiết ở ON | ✅ 2026-06-24 xác nhận: 1W spike 3.70% (ON vẫn 0.55%) |
| Spike turn dồn vào 1W | curve có bướu ở tenor ngắn nhất bắc qua chốt quý | đo phí turn = đỉnh spike; ON có thể vẫn thấp | mới (2026-06-24, 1W 3.70 > 2W 3.30) |
| Lò xo nén ON-thấp + spot trần | ON < 1% đồng thời spot sát trần | SBV có thể hút đỡ đồng; nhưng nếu 1W đã căng thì rủi ro hút giảm | chờ chấm (30/06) |
| *(thêm khi phát hiện)* | | | |

---

## Watchlist — trạng thái gần nhất
*(R1 cập nhật giá trị mới nhất các chỉ số trong system/watchlist.md để so phiên)*

| Chỉ số | Giá trị gần nhất | as-of |
|--------|------------------|-------|
| LNH O/N | **0.55%** (−110bps/phiên) 🔴 ALERT (thủng 1.0%) | 2026-06-24 |
| LNH 1W / 2W | **3.70% → bid 4.0 xuyên offer cũ 3.80** (turn squeeze nóng lên) / 2W 3.30% | 2026-06-24 |
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
  - 🔻 **Cập nhật 2026-06-24:** ON literal vẫn 0.55% (chưa ≥3.0%) → đo theo ON thì Base chưa đạt;
    NHƯNG tinh thần "funding căng quanh chốt quý" ĐÚNG — hiện ở **1W spike 3.70%** (+190bps).
    Cảnh giác: dự báo cũ neo nhầm vào ON; turn squeeze biểu hiện ở 1W. Chấm chốt sau 30/06.

- **[2026-06-24] Turn premium giữ ở 1W: lãi 1W ≥ 3.5% tới 30/06; ON có thể vẫn < 1.5%** — Base ~55%.
  Điều kiện huỷ: SBV bơm mạnh phủ cả turn → 1W về < 3.0%. Chấm sau 30/06.
  - Up-risk ~25%: spot ép trần → SBV hút tín phiếu → đẩy cả ON + term lên đồng loạt (>4%).
  - Down ~20%: turn qua êm, 1W xẹp nhanh về ~3.3% ngay sau 30/06 (phí turn biến mất). Chấm sau 03/07.

- **[2026-06-24] (report đầy đủ, đã red-team) — sổ chấm:**
  - DB-1: ON đêm 30/06 bắn 2 chữ số rồi về <3% ≤02/07 (60%). Huỷ nếu ON đêm <8% hoặc >5% sau 02/07.
  - DB-2: 1W xẹp về 2.8–3.4 trong 02–04/07 (60%). Huỷ nếu 1W >3.5% ngày 04/07.
  - DB-5: spot dán trần, KHÔNG đóng dưới (trần−0.3%) quá 3 phiên liên tiếp trước 31/07 (60%).
  - DB-6: SBV nới tâm trong 3 tháng ~25% (cao hơn nếu CNH>7.30/DXY>103).
  - **Điểm phân định A vs B: lãi 1W ngày 03/07.** Cờ đỏ ngoại: DXY>103, USD/CNH>7.30.
  - File: reports/2026-06-24-USDVND-full-report.md

---

## Sổ lỗi (gắn tag để vá đúng chỗ)
> Tag: `#thiếu-data` `#bỏ-sót-SBV` `#suy-diễn-quá` `#seasonality-sai` `#data-cũ`

| Ngày | Nhận định sai | Nguyên nhân | Tag |
|------|---------------|-------------|-----|
| 2026-06-24 | Tính swap points ÂM (forward discount, 1Y −79đ); coi bảng là i_VND tuyệt đối | **Trừ i_USD hai lần** — bảng niêm yết ĐÃ là chênh lãi (i_VND−i_USD). Đúng: swap points DƯƠNG, 1Y +1.004đ | `#sai-bản-chất` `#double-counting` |

> **Thẻ tra cứu (đọc trước khi mổ curve):** đường cong swap niêm yết = **(i_VND − i_USD) annualized** sẵn.
> Swap points (đồng) = `Spot × giá_trị_bảng/100 × days/360`. **KHÔNG trừ i_USD lần nữa.** Dương = USD
> forward premium = VND mất giá kỳ hạn (bình thường vì VND lãi cao hơn USD).
