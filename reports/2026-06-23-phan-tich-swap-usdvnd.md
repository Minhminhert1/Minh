# Phân tích Swap & FX USD/VND — 23/06/2026

> **Input người dùng:** Đường cong lãi suất liên ngân hàng VND (giá trị **trung bình bid/ask = mid**), Hôm nay vs Cuối hôm qua.
> **Playbook chạy:** PB-1 (curve → giải thích → insight → dự báo) · **Squad:** A1 Curve · R1/R3/R4/R5 · A2 Insight · A3 Forecast · Reviewer.
> **Lưu ý đọc:** Phần [FACT] có nguồn + timestamp. Phần [SUY LUẬN] là diễn giải của team. Phần swap points là **suy ra từ CIP** (chưa có báo giá swap points trực tiếp) → xem mục Độ tin.

---

## 0. TỔNG QUAN (Orchestrator)

Hôm nay thị trường tiền tệ VND chứng kiến **chân ngắn của đường cong sụp mạnh**: lãi suất qua đêm (ON) rơi **−125 bps** (2.90% → **1.65%**), 1W rơi **−125 bps**, 2W rơi **−135 bps**. Trong khi đó **chân dài gần như đứng yên** (3M..1Y chỉ đổi 0 đến −5 bps).

→ Đây là một **cú bơm/easing thanh khoản VND mang tính nhất thời ở đầu đường cong**, KHÔNG phải dịch chuyển kỳ vọng lãi suất cấu trúc. Bức tranh khớp với bối cảnh tháng 6/2026: thanh khoản hệ thống vừa trải qua giai đoạn căng (ON từng vọt ~11% đầu tháng) nay hạ nhiệt nhờ thanh khoản dồi dào trở lại.

**Hàm ý swap USD/VND:** chênh lệch lãi suất VND–USD ở đầu đường cong **âm sâu thêm** (i_VND ON 1.65% << SOFR ON 3.62%) → **swap points ngắn hạn âm hơn (forward discount nới rộng)**; chân dài gần như không đổi.

**Căng thẳng cần để mắt:** spot USD/VND đang **ép sát trần** (~26.433 vs trần ~26.442) dù tỷ giá trung tâm ổn định → áp lực mất giá còn đó. Lãi suất VND đầu đường cong rơi quá thấp **làm xấu carry giữ VND** → mâu thuẫn với mục tiêu giữ tỷ giá. Đây là lý do team nghi ngờ mức ON 1.65% **khó kéo dài**.

---

## 1. DỮ LIỆU INPUT + BIẾN ĐỘNG (A1)

| Kì hạn | Hôm nay (%) | Cuối hôm qua (%) | Δ (bps) |
|--------|-------------|------------------|---------|
| ON | **1.65** | 2.90 | **−125** |
| 1W | **1.80** | 3.05 | **−125** |
| 2W | **3.55** | 4.90 | **−135** |
| 3W | **3.80** | 4.25 | −45 |
| 1M | **3.55** | 3.85 | −30 |
| 2M | **3.70** | 3.80 | −10 |
| 3M | **3.70** | 3.75 | −5 |
| 6M | **3.75** | 3.75 | 0 |
| 9M | **3.75** | 3.75 | 0 |
| 1Y | **3.80** | 3.85 | −5 |

*Giá trị là mid (trung bình bid/ask) — phản ánh mặt bằng funding chỉ báo, chưa thể hiện độ rộng bid/ask.*

---

## 2. PHÂN TÍCH HÌNH DẠNG CURVE (A1 · Curve Analyst)

### 2.1 Hình dạng tổng thể
- **Chân ngắn bị nén sâu:** ON 1.65 → 1W 1.80 — gần như “sàn”, thấp hơn hẳn phần còn lại.
- **Dốc dựng đứng từ 1W → 2W:** +175 bps (1.80 → 3.55) chỉ trong một bước kỳ hạn — bất thường.
- **Bướu (hump/kink) tại 2W–3W:** 3W = **3.80** là đỉnh cục bộ, cao hơn cả 2W (3.55) lẫn 1M (3.55).
- **Chân dài phẳng và ổn định:** 1M..1Y dao động hẹp 3.55–3.80, gần như nằm ngang quanh **3.7–3.8%**.

→ Hình dạng: **front-end depressed + humped giữa + chân dài neo phẳng**. So với hôm qua, toàn bộ phần ngắn hạ mạnh nhưng **giữ nguyên cấu trúc bướu** (hôm qua bướu còn gắt hơn: 2W 4.90, 3W 4.25).

### 2.2 Cờ bất thường chuyển A2
1. **Vì sao ON/1W rơi 125 bps cùng lúc?** (cú bơm thanh khoản qua đêm)
2. **Vì sao 2W–3W vẫn “bướu” cao trong khi ON sụp?** (nghi phần kỳ hạn **bắc qua chốt quý 30/06** mang premium)
3. **Vì sao chân dài bất động?** (kỳ vọng lãi suất cấu trúc không đổi)

---

## 3. DATA PACK — BỐI CẢNH (Research squad)

### R3 · Chân USD / Global [FACT]
- **SOFR (ON): 3.62%** — as-of 18/06/2026 · nguồn: NY Fed/FRED · độ tin 5.
- Term SOFR 1M/3M: quanh **~3.5–3.6%** (ước lượng từ mặt bằng SOFR, *cần xác nhận số chính xác*) · độ tin 2.

### R4 · Chính sách & SBV [FACT]
- **Tỷ giá trung tâm: 25.183** (22/06/2026), chỉ +0.25% — neo ổn định · độ tin 5.
- **Spot ~26.325–26.433**, NHTM niêm yết bán **sát trần ~26.433** (trần ~26.442) · độ tin 4.
- **Lãi suất tái cấp vốn SBV: 4.50%** (không đổi) · độ tin 5.
- [SUY LUẬN] Spot ép trần ⇒ áp lực mất giá VND còn nguyên, dù trung tâm “đứng”.

### R1 · Rates & Liquidity VN [FACT + bối cảnh]
- Đầu tháng 6 ON từng **vọt ~11%** (căng thanh khoản), sau đó có nhịp **“đáy 16 tháng nhờ thanh khoản dồi dào”** → môi trường **biến động mạnh hai chiều**. Số hôm nay (ON 1.65%) nằm ở pha **dồi dào**. Nguồn báo chí · độ tin 3.
- [QUAN ĐIỂM bên thứ 3] VDSC: OMO & FX swap **không tạo thanh khoản gốc**, chỉ “mua thời gian” khi LDR cao.

### R5 · Flow & Seasonality [SUY LUẬN có cơ sở]
- **Hôm nay 23/06 → chốt quý 30/06 cận kề.** Kỳ hạn **bắc qua 30/06** (2W đáo ~07/07, 3W đáo ~14/07) là nơi nhu cầu giữ tiền làm **BCTC cuối quý** dồn vào ⇒ giải thích vì sao **2W–3W bị đẩy cao** trong khi ON (đáo hạn ngay, chưa chạm chốt quý) lại rẻ.

### ⚠️ FRESHNESS / MÂU THUẪN
- Có nguồn ghi VNIBOR ON ~9.35% trong tháng 6 — **lệch hẳn** số mid 1.65% của bạn → nhiều khả năng là **ảnh chụp ở thời điểm/pha khác** (đợt căng đầu tháng), không phải hôm nay. Team **ưu tiên số bạn cung cấp** cho phiên hôm nay, dùng nguồn ngoài chỉ làm bối cảnh.
- Term SOFR theo tenor: chưa có số chính xác → phần swap points theo tenor là **định tính**.

---

## 4. INSIGHT THEO TỪNG VÙNG TENOR (A2 · Insight — đa giả thuyết)

### 4.1 Đầu đường cong ON–1W (rơi 125 bps)
**Hiện tượng:** ON 1.65%, 1W 1.80% — nén sát sàn.
- **GT1 — Bơm thanh khoản qua đêm (NGHIÊNG VỀ):** OMO bơm ròng / tín phiếu SBV đáo hạn / chi NSNN ra nền kinh tế làm dư VND tức thời. *Ủng hộ:* cú rơi đồng loạt 125 bps chỉ ở chân siêu ngắn; bối cảnh “thanh khoản dồi dào trở lại”. *Phản đối:* chưa có xác nhận số OMO hôm nay (cần R1 chốt).
- **GT2 — Đảo chiều sau cú căng đầu tháng:** sau khi ON chạm ~11%, dòng tiền dồn trở lại đẩy lãi suất xuống quá đà. *Ủng hộ:* biên độ dao động lớn gần đây. *Phản đối:* không loại trừ GT1, hai cái có thể cộng hưởng.
- **Base rate:** các pha “flush” thanh khoản đầu đường cong ở VN thường **kéo dài vài phiên rồi đảo**, hiếm khi là trạng thái bền.

### 4.2 Bướu 2W–3W (vẫn cao dù ON sụp)
**Hiện tượng:** 3W 3.80 > 2W 3.55 > 1M 3.55; ON/1W thấp hơn ~190 bps.
- **GT1 — Premium bắc qua chốt quý 30/06 (NGHIÊNG VỀ MẠNH):** tiền vay phủ qua ngày chốt BCTC bị đòi giá cao. *Ủng hộ:* đúng cửa sổ thời gian (23/06 → 30/06); hôm qua bướu còn gắt hơn (2W 4.90) đang hạ dần khi thanh khoản vào. *Phản đối:* 1M (cũng phủ chốt quý) lại thấp hơn 3W → có thể do hiệu ứng trung bình hóa kỳ hạn dài hơn, hoặc nhiễu dữ liệu.
- **GT2 — Nhiễu/thanh khoản mỏng ở 2W–3W:** các điểm kỳ hạn lẻ ít giao dịch, mid dễ giật. *Ủng hộ:* 2W đổi −135 bps một phiên. *Phản đối:* bướu tồn tại cả hôm qua lẫn hôm nay → có tính hệ thống hơn là nhiễu.

### 4.3 Chân dài 1M–1Y (bất động)
**Hiện tượng:** 3M..1Y ~3.7–3.8%, đổi 0 đến −5 bps.
- **GT1 (NGHIÊNG VỀ):** kỳ vọng lãi suất & chính sách cấu trúc **không đổi** — biến động hôm nay thuần **thanh khoản nhất thời**, không lan ra kỳ vọng. *Ủng hộ:* tái cấp vốn SBV neo 4.50%; dự báo interbank “dính” trên ~6% cả năm phản ánh kỳ vọng vẫn cao về dài hạn (chú ý: số dự báo đó cao hơn mặt bằng mid hiện tại → xem Reviewer).

### 4.4 Hàm ý SWAP POINTS USD/VND [SUY LUẬN từ CIP]
Công thức: `Forward ≈ Spot × (1 + i_VND·t/360) / (1 + i_USD·t/360)`. Dấu swap points theo **chênh lệch (i_VND − i_USD)**:

| Vùng | i_VND | i_USD (xấp xỉ) | Chênh lệch | Swap points |
|------|-------|----------------|-----------|-------------|
| ON | 1.65% | SOFR 3.62% | **≈ −1.97%** | **âm sâu** (forward discount lớn) |
| 1W | 1.80% | ~3.6% | ≈ −1.8% | âm sâu |
| 2W–3W | 3.55–3.80% | ~3.6% | ≈ 0 | quanh ngang |
| 3M | 3.70% | Term SOFR ~3.55% | ≈ +0.15% | hơi dương |
| 1Y | 3.80% | ~3.5% | ≈ +0.3% | dương nhẹ |

→ **Điểm cốt lõi:** hôm nay chênh lệch đầu đường cong **âm thêm ~125 bps** (hôm qua ON diff ≈ −0.72%, hôm nay ≈ −1.97%) ⇒ **swap points ON/1W tụt mạnh (USD forward discount nới rộng)**. Ai **trả VND nhận USD kỳ ngắn** (sell/buy USD swap) được lợi từ funding VND siêu rẻ; ngược lại **carry giữ VND ngắn hạn xấu đi rõ**.

---

## 5. DỰ BÁO & KỊCH BẢN (A3 · Forecast — có mốc, falsifiable)

### Base case (~55%): Flush thanh khoản nhất thời, ON bật lại trước/qua chốt quý
- **Dự báo:** ON **không giữ được 1.65%**, bật về vùng **≥ 3.0%** trong **3–7 phiên tới** (tức quanh 26–30/06), đặc biệt khi nhu cầu chốt quý dồn vào. Chân dài (3M..1Y) **đứng yên ±10 bps** đến hết tháng 6.
- **Điều kiện kích hoạt:** OMO chuyển hút ròng / SBV phát hành lại tín phiếu / cầu VND chốt quý tăng.
- **Hàm ý swap:** swap points ON/1W **thu hẹp đà âm** khi i_VND đầu cong hồi lên.

### Up-risk lãi suất (~30%): SBV phải hút VND để giữ tỷ giá
- **Dự báo:** nếu spot **tiếp tục ép trần** (~26.43+), SBV hút thanh khoản/bán USD ⇒ ON **vọt lên 4–6%+** trong **1–2 tuần**.
- **Điều kiện:** USD/VND đóng cửa sát/chạm trần nhiều phiên + DXY/CNY căng.
- **Đây là kịch bản “xấu cho người đang hưởng VND rẻ”** — cần theo sát nhất.

### Down/kéo dài (~15%): Thanh khoản dồi dào bền hơn dự kiến
- **Dự báo:** ON nằm vùng **1.5–2.5%** kéo dài **>1 tuần** qua cả chốt quý.
- **Điều kiện:** SBV chủ đích duy trì thanh khoản dồi dào + áp lực tỷ giá dịu (FDI/kiều hối mạnh).
- **Mâu thuẫn nội tại:** kịch bản này **làm xấu carry VND** → khó dung hòa với spot sát trần ⇒ xác suất thấp.

### Trigger theo dõi (xác nhận/bác bỏ)
- OMO bơm/hút ròng hằng phiên · phát hành lại tín phiếu SBV · USD/VND có rời trần không · SOFR & FOMC · diễn biến ON quanh 27–30/06.

### Pre-mortem (nếu Base sai)
> Khả năng cao nhất khiến Base sai: SBV **chủ động giữ thanh khoản dồi dào** (ưu tiên hỗ trợ tăng trưởng/giảm chi phí vốn) và chấp nhận VND rẻ ở đầu cong, khiến ON **không bật lại** như kỳ vọng → rơi vào kịch bản Down. Hoặc ngược lại, FX căng đột ngột đẩy thẳng lên Up-risk nhanh hơn mốc 1–2 tuần.

---

## 6. PHẢN BIỆN (Reviewer · red-team)

- **Đòn vào luận điểm mạnh nhất (“flush nhất thời, ON sẽ bật lại”):** chưa có **xác nhận OMO/tín phiếu hôm nay** — GT1 mục 4.1 đang dựa vào suy luận + bối cảnh, không phải số chốt. ⇒ **CẦN R1 bổ sung số OMO ròng & trạng thái tín phiếu** để nâng độ tin. *Data chứng minh SAI:* nếu OMO hôm nay **hút ròng mạnh** mà ON vẫn rơi → GT1 sai, phải nghiêng GT “đảo chiều sau căng”.
- **Bướu 2W–3W = chốt quý:** thuyết phục nhưng **1M thấp hơn 3W** làm yếu lập luận. Chưa loại được khả năng nhiễu thanh khoản mỏng. Giữ ở mức **giả thuyết dẫn**, chưa phải kết luận.
- **Mâu thuẫn dữ liệu cần nêu thẳng:** dự báo bên ngoài “interbank dính trên 6% cả năm” **lệch mạnh** với mặt bằng mid 3.7–3.8% (term) và ON 1.65% hôm nay. ⇒ Hoặc nguồn ngoài lỗi thời, hoặc bộ số mid của bạn ở thang khác/thời điểm khác. **Không trộn hai nguồn để kết luận**; phần dài hạn để mức tin trung bình.
- **Swap points theo tenor là DERIVED:** thiếu Term SOFR chính xác và **báo giá swap points thực tế**. Mục 4.4 đúng về **dấu & hướng**, nhưng **không nên dùng con số tuyệt đối** để giao dịch.
- **Đánh giá:** **PASS có điều kiện** — kết luận về *hướng* (front-end flush, swap points ngắn âm thêm, chân dài neo) vững; cần bổ sung OMO/tín phiếu + Term SOFR + báo giá swap points để lên mức tin cao.

---

## 7. ĐỘ TIN & FRESHNESS

| Mảng | Độ tin | Ghi chú |
|------|--------|---------|
| Curve VND hôm nay/hôm qua | **Cao** | Từ bạn cung cấp (mid) |
| Hướng dịch chuyển & shape | **Cao** | Tính trực tiếp từ data |
| SOFR ON 3.62% / SBV rates / spot | Khá | Nguồn công khai, as-of 18–22/06 |
| Nguyên nhân ON sụp (OMO) | **Trung bình** | Suy luận — thiếu số OMO hôm nay |
| Bướu 2W–3W = chốt quý | Trung bình | Giả thuyết dẫn, chưa chốt |
| Swap points theo tenor (số tuyệt đối) | **Thấp** | Suy từ CIP, thiếu Term SOFR + báo giá thực |

**Cần bổ sung để nâng chất:** (1) OMO bơm/hút ròng & tín phiếu SBV hôm nay; (2) Term SOFR 1W/2W/1M/3M; (3) báo giá swap points USD/VND thực tế theo tenor; (4) USD/VND spot đóng cửa mấy phiên gần nhất.

---

## Nguồn
- [SOFR — FRED/St. Louis Fed](https://fred.stlouisfed.org/series/SOFR) · [SOFR Rate Today 3.62%](https://www.sofrrate.com/)
- [USD/VND — Investing.com](https://vn.investing.com/currencies/usd-vnd) · [Nhập siêu kéo dài, tỷ giá đứng vững — Thời báo Tài chính](https://thoibaotaichinhvietnam.vn/nhap-sieu-keo-dai-ty-gia-usdvnd-van-dung-vung-nhung-lai-suat-kho-ha-nhiet-199455.html)
- [VDSC: OMO không giải quyết gốc rễ thanh khoản — Investing.com](https://vn.investing.com/news/economy-news/vdsc-omo-khong-giai-quyet-duoc-goc-re-bai-toan-thanh-khoan-ngan-hang-2647069)
- [Overnight rate hits 11% in early June — Vietnam News](https://vietnamnews.vn/economy/1782665/overnight-rate-hits-11-per-cent-in-early-june.html) · [ON đáy 16 tháng nhờ thanh khoản dồi dào — VietnamPlus](https://en.vietnamplus.vn/overnight-interbank-interest-rate-hits-16-month-low-thanks-to-abundant-liquidity-post321533.vnp)
- [VNIBOR ON — CEIC](https://www.ceicdata.com/en/vietnam/vietnam-interbank-offered-rate/state-bank-of-vietnam-vnibor-interbank-vnd-overnight) · [DBS: interbank rate pressures to ease](https://www.dbs.bank.in/in/treasures/aics/templatedata/article/generic/data/en/GR/macro_strategy/012026/261009_vietnam.xml)

---
*Báo cáo do team Swap USD/VND tạo theo schema bàn giao nội bộ. FACT tách khỏi SUY LUẬN; mọi dự báo có mốc thời gian để Journalist chấm điểm về sau.*
