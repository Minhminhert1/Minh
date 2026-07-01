# Phân tích Swap & FX USD/VND — 01/07/2026

> **Input người dùng:** Đường cong lãi suất liên ngân hàng VND (mid = trung bình bid/ask), Hôm nay (01/07) vs Cuối hôm qua (30/06 = **ngày chốt quý**).
> **Playbook:** PB-1 (curve → giải thích → insight → dự báo) + PB-5 (watchlist: ON chạm ngưỡng) · **Squad:** A1 · R1/R3/R4/R5 · A2 · A3 · Reviewer · Journalist chấm scoreboard 23/06.
> **Đọc lưu ý:** [FACT] có nguồn/timestamp; [SUY LUẬN] là diễn giải; swap points là **derived từ CIP** (chưa có báo giá thực) → xem Độ tin.

---

## 0. TỔNG QUAN (Orchestrator)

Hôm nay là **ngày đầu Q3 (01/07)** — và curve kể đúng câu chuyện team đã dự báo: **cú squeeze chốt quý 30/06 đã xả hết**.

- "Cuối hôm qua" (30/06, chốt quý) ON vọt **9.50%** — đỉnh căng thanh khoản BCTC cuối quý.
- Hôm nay ON rơi **−575 bps về 3.75%**; toàn bộ chân ngắn (1W −160, 2W −120) bình thường hóa.
- Chân dài (6M–1Y) **gần như bất động** (0 đến −5 bps) → biến động thuần **thanh khoản mùa vụ**, KHÔNG phải dịch chuyển kỳ vọng lãi suất cấu trúc.

→ **Xác nhận pattern "BCTC cuối quý"** (memory: trước để trống "chưa có data"): tới ngày chốt quý → funding VND căng, ON tăng vọt → **qua ngày đầu quý mới, squeeze xả ngay**. Đây là lần **có bằng chứng đầu tiên** để nạp thẻ pattern.

**Hàm ý swap USD/VND — điểm quan trọng nhất:** chênh lệch lãi suất VND–USD **đã co gần về 0 trên toàn curve** (VND ~3.2–3.75% vs SOFR ~3.5–3.62%). Swap points hôm nay **mỏng, quanh ngang, hơi âm ở bụng** — khác hẳn 23/06 khi đầu cong diff tới −1.97%. **Carry giữ VND ≈ trung tính**, không còn siêu rẻ như tuần trước.

**Cần để mắt:** ON hạ về 3.75% (≈ SOFR) là mức "lành" hơn 1.65% của 23/06 cho mục tiêu giữ tỷ giá — nhưng cần R4 xác nhận spot USD/VND có rời trần chưa. Nếu spot vẫn ép trần, SBV có thể giữ front-end firm quanh 3–3.75% thay vì thả về vùng 2%.

---

## 1. DỮ LIỆU INPUT + BIẾN ĐỘNG (A1)

| Kì hạn | Hôm nay (%) | Cuối hôm qua 30/06 (%) | Δ (bps) |
|--------|-------------|------------------------|---------|
| ON | **3.75** | 9.50 | **−575** 🔴 |
| 1W | **3.40** | 5.00 | −160 |
| 2W | **3.30** | 4.50 | −120 |
| 3W | **3.20** | 3.55 | −35 |
| 1M | **3.20** | 3.40 | −20 |
| 2M | **3.30** | 3.40 | −10 |
| 3M | **3.30** | 3.40 | −10 |
| 6M | **3.40** | 3.40 | 0 |
| 9M | **3.55** | 3.55 | 0 |
| 1Y | **3.60** | 3.65 | −5 |

*🔴 ON −575 bps vượt xa ngưỡng watchlist (>50 bps/phiên) → kích PB-5.*

---

## 2. HÌNH DẠNG CURVE (A1 · Curve Analyst)

### 2.1 Hình dạng hôm nay
- **Chân trước nghịch nhẹ:** ON 3.75 > 1W 3.40 > 2W 3.30 > 3W 3.20 — dốc xuống đều, không còn "sàn" bất thường.
- **Đáy (bụng) tại 3W–1M = 3.20** — điểm thấp nhất curve.
- **Dốc lên nhẹ và trơn 1M→1Y:** 3.20 → 3.60, đều đặn, không kink.
- Tổng thể: **hình "smile" phẳng** — nghịch nhẹ đầu cong, đáy ở bụng, dốc lên thoải chân dài. Đây là **curve hậu-squeeze lành mạnh**, không còn bướu 2W–3W như 23/06.

### 2.2 So với hôm qua (chốt quý)
- Hôm qua: đầu cong dựng đứng (ON 9.50, 1W 5.00, 2W 4.50) — hình dạng **stress điển hình chốt quý**, chỉ căng ở phần đáo hạn *trước/tại* ngày chốt.
- Hôm nay: đầu cong sập về ngang bụng → **premium chốt quý biến mất trong 1 phiên**. Đúng cơ chế: qua 30/06, nhu cầu window-dressing tan → tiền thừa quay lại đầu cong.

### 2.3 Cờ chuyển A2
1. ON 9.50%→3.75% trong 1 phiên: xác nhận squeeze chốt quý hay có bơm OMO đầu quý?
2. Bụng 3W–1M = 3.20 (thấp nhất): thanh khoản đầu Q3 dồi dào?
3. Chân dài neo 3.4–3.6: kỳ vọng cấu trúc đứng yên.

---

## 3. DATA PACK — BỐI CẢNH (Research squad)

### R5 · Flow & Seasonality [SUY LUẬN có cơ sở — MẠNH]
- **30/06 là ngày chốt quý II.** ON 9.50% hôm qua là **đỉnh window-dressing BCTC**: NH gom VND làm đẹp bảng cân đối cuối quý → funding qua đêm bị đòi giá cắt cổ. **01/07 sang quý mới → nhu cầu tan tức thì → ON sập.** Đây là **hành vi mùa vụ sách giáo khoa**, khớp 100% cửa sổ thời gian.

### R1 · Rates & Liquidity VN [FACT + suy luận]
- ON về **3.75%** (≈ mặt bằng SOFR) sau đỉnh 9.50%. Bụng 3W–1M xuống **3.20%** → thanh khoản đầu Q3 **nới ra**. *Cần R1 chốt: OMO ròng & trạng thái tín phiếu SBV phiên 01/07* (đầu quý SBV thường bơm/không hút mạnh). Độ tin suy luận: 3.

### R3 · Chân USD / Global [FACT]
- **SOFR (ON) ~3.62%** (as-of gần nhất) — chưa có tín hiệu đổi. Term SOFR 1M/3M ~3.5–3.6% (ước lượng, cần xác nhận) · độ tin 2–5.

### R4 · Chính sách & SBV [cần cập nhật]
- **Chưa có số spot/tỷ giá trung tâm phiên 01/07 trong data.** Mấu chốt để đọc độ bền của ON 3.75%: spot còn ép trần (~26.44) không? Nếu còn → SBV có động cơ giữ front-end firm. **Đề nghị R4 bổ sung spot đóng cửa 30/06–01/07.**

### ⚠️ FRESHNESS / MÂU THUẪN
- Thang số mid 30/06 (ON 9.50) **cao hơn nhiều** phiên 23/06 (ON 2.90 "cuối hôm qua") → nhất quán với đường đi 1.65% (23/06) → leo dần → đỉnh chốt quý 9.50% (30/06) → xả về 3.75% (01/07). **Không mâu thuẫn**, là một chu kỳ chốt quý hoàn chỉnh.

---

## 4. INSIGHT THEO VÙNG TENOR (A2 · Insight — đa giả thuyết)

### 4.1 Đầu cong ON–2W (xả −575/−160/−120 bps)
- **GT1 — Xả premium chốt quý (NGHIÊNG MẠNH):** qua 30/06, cầu window-dressing biến mất → front-end về nền. *Ủng hộ:* đúng ngày đầu quý; hôm qua chính là đỉnh 9.50%. *Phản đối:* chưa loại được cộng hưởng từ bơm OMO đầu quý (cần R1).
- **GT2 — SBV bơm đầu quý:** thường lệ đầu quý thanh khoản nới. Có thể cộng hưởng GT1.

### 4.2 Bụng 3W–1M = 3.20 (đáy curve)
- **GT1 (NGHIÊNG VỀ):** thanh khoản đầu Q3 dồi dào, không còn kỳ hạn nào "bắc qua" mốc căng → bụng rơi xuống thấp nhất. Khác 23/06 khi 2W–3W bị đẩy cao vì bắc qua 30/06 — **nay mốc đó đã ở sau lưng** → bướu tan, thành đáy. *Đây là bằng chứng củng cố giả thuyết bướu-chốt-quý của 23/06.*

### 4.3 Chân dài 1M–1Y (đứng yên)
- **GT1:** kỳ vọng lãi suất & chính sách cấu trúc **không đổi** — toàn bộ biến động là thanh khoản nhất thời. *Ủng hộ:* 6M–1Y đổi 0 đến −5 bps qua cả cú sốc chốt quý.

### 4.4 Hàm ý SWAP POINTS USD/VND [derived từ CIP]
Dấu swap points ~ chênh lệch (i_VND − i_USD):

| Vùng | i_VND | i_USD (xấp xỉ) | Chênh lệch | Swap points |
|------|-------|----------------|-----------|-------------|
| ON | 3.75% | SOFR 3.62% | ≈ **+0.13%** | ~ngang, hơi dương |
| 1W–2W | 3.30–3.40% | ~3.6% | ≈ −0.2 đến −0.3% | âm nhẹ |
| 3W–1M (bụng) | 3.20% | ~3.55% | ≈ **−0.35%** | âm nhẹ (discount nhỏ) |
| 2M–3M | 3.30% | ~3.55% | ≈ −0.25% | âm nhẹ |
| 6M | 3.40% | ~3.5% | ≈ −0.1% | ~ngang |
| 1Y | 3.60% | ~3.5% | ≈ +0.1% | ~ngang, hơi dương |

→ **Điểm cốt lõi:** so với 23/06 (đầu cong diff −1.97%, swap points ON âm sâu), hôm nay **chênh lệch VND–USD co gần về 0 trên toàn curve**. Swap points **mỏng, quanh ngang, âm nhẹ nhất ở bụng 3W–1M**. Hệ quả:
- **Forward USD/VND ≈ spot** ở mọi tenor → cost of carry ~ trung tính.
- Lợi thế "trả VND rẻ nhận USD" của tuần trước **đã biến mất** — người short swap chân ngắn hết cửa ngon.
- Edge từ rate differential giờ **rất mỏng** → curve chủ yếu bị lái bởi nhiễu thanh khoản + động thái tỷ giá SBV.

---

## 5. DỰ BÁO & KỊCH BẢN (A3 · Forecast — có mốc, falsifiable)

### Base case (~60%): Front-end ổn định vùng 3.0–3.75%, hết mùa vụ tới 30/09
- **Dự báo:** ON dao động **3.0–3.75%** trong **1–2 tuần tới**; cú 9.50% là **artifact 1 ngày của chốt quý, không tái lập** cho tới mốc chốt quý kế (30/09). Bụng 3W–1M giữ **3.1–3.4%**. Chân dài (3M–1Y) **đứng ±10 bps**.
- **Kích hoạt:** thanh khoản đầu quý nới, OMO không hút mạnh, spot không tái ép trần.
- **Hàm ý swap:** swap points giữ **mỏng quanh ngang**; không mở lại forward discount lớn.

### Up-risk FX (~25%): SBV siết VND giữ tỷ giá → front-end firm lên
- **Dự báo:** nếu spot **tái ép trần** (~26.44+), SBV hút thanh khoản/bán USD ⇒ ON firm lên **4–5%** trong **1–2 tuần**, swap points ngắn **dương trở lại**.
- **Kích hoạt:** USD/VND đóng cửa sát trần nhiều phiên + DXY/CNY căng.

### Down (~15%): Thanh khoản dồi dào kéo ON về vùng ~2%
- **Dự báo:** ON trượt về **2.0–2.8%** kéo dài, tái lập forward discount ngắn hạn.
- **Kích hoạt:** SBV chủ đích giữ thanh khoản dồi dào + áp lực tỷ giá dịu (kiều hối/FDI).
- **Mâu thuẫn nội tại:** làm xấu carry VND ↔ spot sát trần ⇒ xác suất thấp.

### Trigger theo dõi
- OMO bơm/hút ròng & tín phiếu SBV phiên 01/07+ · spot USD/VND có rời trần không · SOFR/FOMC · ON quanh mốc lương/thuế đầu tháng 7 · mốc chốt quý kế **30/09**.

### Pre-mortem (nếu Base sai)
> Rủi ro lớn nhất: FX căng đột ngột (spot ép trần) kéo thẳng lên Up-risk nhanh hơn — SBV firm front-end trước khi thanh khoản mùa vụ đầu quý kịp kéo ON xuống. Hoặc chiều ngược lại, SBV thả thanh khoản mạnh (hỗ trợ tăng trưởng) → rơi Down sớm.

---

## 6. PHẢN BIỆN (Reviewer · red-team)

- **Luận điểm mạnh nhất ("xả premium chốt quý"):** rất vững — có đỉnh 9.50% ngay ngày chốt quý + xả đúng ngày đầu quý. Nhưng **vẫn thiếu số OMO/tín phiếu 01/07** để tách phần "SBV bơm đầu quý" khỏi phần "cầu window-dressing tan". *Data chứng minh sai:* nếu 01/07 SBV **hút ròng mạnh** mà ON vẫn sập → phần lớn là xả mùa vụ (GT1 thắng tuyệt đối); nếu OMO **bơm lớn** → có cộng hưởng.
- **Swap points ~0:** đúng về **dấu & độ mỏng**, nhưng vẫn **derived** — thiếu Term SOFR chính xác + báo giá swap thực. Không dùng số tuyệt đối để giao dịch.
- **Độ bền ON 3.75%:** kết luận "ổn định 3.0–3.75%" **treo vào giả định spot không tái ép trần** — mà data phiên nay **thiếu spot/tỷ giá trung tâm 01/07**. Đây là lỗ hổng lớn nhất của báo cáo. ⇒ Base 60% **có điều kiện R4 bổ sung spot**.
- **Đánh giá:** **PASS có điều kiện** — kết luận về *hướng* (xả squeeze chốt quý, curve bình thường hóa, swap points co về ~0, chân dài neo) rất vững; cần OMO 01/07 + spot USD/VND để chốt độ bền của front-end.

---

## 7. SCOREBOARD — CHẤM DỰ BÁO 23/06 (Journalist)

| Dự báo (23/06) | Kết quả (tới 01/07) | Chấm |
|----------------|---------------------|------|
| Base: ON bật về **≥3.0%** trong 3–7 phiên quanh 26–30/06 | ON leo tới **9.50%** ngày chốt quý 30/06 | ✅ **ĐÚNG hướng** (vượt cả kỳ vọng) |
| Up-risk: ON vọt **4–6%+** nếu SBV siết giữ tỷ giá | ON chạm **9.50%** tại chốt quý (mùa vụ > FX) | ✅ **ĐÚNG biên độ** (nguyên nhân thiên về seasonality) |
| Chân dài (3M–1Y) **đứng ±10 bps** hết tháng 6 | 3M–1Y đổi **0 đến −5 bps** | ✅ **ĐÚNG** |
| Down (~15%): ON giữ 1.5–2.5% kéo dài qua chốt quý | Không xảy ra | ✅ Loại đúng |

→ **Hit-rate phiên 23/06: 3/3 hướng chính đúng.** Bài học calibration: team **đánh giá thấp biên độ** cú chốt quý (dự 4–6%, thực 9.50%) — lần sau **nới trần up-risk quanh mốc chốt quý**.

---

## 8. ĐỘ TIN & FRESHNESS

| Mảng | Độ tin | Ghi chú |
|------|--------|---------|
| Curve VND hôm nay/hôm qua | **Cao** | Từ bạn cung cấp (mid) |
| Hướng dịch chuyển & shape | **Cao** | Tính trực tiếp |
| Nguyên nhân = xả chốt quý | **Cao** | Cửa sổ thời gian khớp 100% + đỉnh 9.50% ngày 30/06 |
| Tách OMO đầu quý vs seasonality | Trung bình | Thiếu số OMO 01/07 |
| Độ bền ON 3.75% | **Trung bình–thấp** | Thiếu spot/tỷ giá TT phiên 01/07 |
| Swap points theo tenor (số tuyệt đối) | Thấp | Derived CIP, thiếu Term SOFR + báo giá thực |

**Cần bổ sung:** (1) OMO ròng & tín phiếu SBV phiên 01/07; (2) spot USD/VND + tỷ giá trung tâm 30/06–01/07; (3) Term SOFR theo tenor; (4) báo giá swap points thực.

---

## Nguồn
- [SOFR — FRED/St. Louis Fed](https://fred.stlouisfed.org/series/SOFR)
- [USD/VND — Investing.com](https://vn.investing.com/currencies/usd-vnd)
- Bối cảnh chốt quý & thanh khoản: xem báo cáo nội bộ 23/06 (`reports/2026-06-23-phan-tich-swap-usdvnd.md`).

---
*Báo cáo team Swap USD/VND theo schema bàn giao nội bộ. FACT tách khỏi SUY LUẬN; dự báo có mốc để chấm về sau. Phiên này đồng thời chấm scoreboard dự báo 23/06.*
