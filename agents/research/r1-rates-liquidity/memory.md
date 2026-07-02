# Memory — R1 Rates & Liquidity

## Nguồn đáng tin
- **Vietstock chuyên mục tuần OMO** ("Tuần DD-DD/MM: NHNN bơm/hút ròng...") — số OMO ròng, kỳ hạn, lãi suất, lưu hành. Ra đầu tuần kế tiếp.
- **Dân trí & VnExpress kinh doanh** — LNH theo phiên khi có biến động (bài 01/07 cho đủ ON/1W/2W/1M phiên 30/06 + chi tiết swap SBV).
- **TBTCVN & VTV Money** — tỷ giá trung tâm hằng ngày + tóm tắt tiền tệ tuần.

## Nguồn không đáng tin / chậm
- ⚠️ **Proxy môi trường chặn fetch trực tiếp (403) toàn bộ site VN** (sbv.gov.vn, CafeF, Vietstock...) — chỉ đọc được trích xuất search → trần độ tin 4, không đối chiếu được bản gốc.
- LNH phiên T chỉ được index từ sáng T+1 — data "hôm nay" gần như không lấy được qua search.
- Swap points USD/VND theo tenor & NDF: **không có nguồn public** — mảng mù kinh niên, cần quote từ user/terminal.

## Hiệu chỉnh ngưỡng watchlist
- 2026-07-02: Ngưỡng "ON đổi >50bps/phiên" kêu đúng (30/06: +940bps) nhưng vô nghĩa quanh chốt quý/kỳ thuế — đề xuất: quanh 5 ngày cuối quý & hạn thuế, chỉ ALERT khi **belly 1M đổi >50bps** (tín hiệu cấu trúc), ON để ngưỡng nới 300bps.

## Ghi chú thanh khoản theo phiên
- 30/06/2026: ON 13% (khóa sổ Q2) dù SBV bơm ròng ~14.600 tỷ + swap FX 7d → cầu chốt quý nuốt trọn lượng bơm; áp lực dịch sang 1W (khoản vay bắc qua khóa sổ).
- Tuần 22–26/06: SBV đảo chiều bơm ròng ~3.962 tỷ bằng kỳ hạn DÀI 35–56d @4,5% — bơm dài trước sự kiện là tín hiệu SBV chuẩn bị trước cho chốt quý + kỳ thuế.
- Chuỗi ON tháng 6: 11% (01/06) → 5,4–5,78% → ~3,5% (12/06) → thấp → 3,6% (29/06) → 13% (30/06). Biến động 2 chiều cực mạnh là đặc trưng 2026.
- Gap OMO 4,5% vs LNH 8% (+350bps) không tự khép → nghi cạn collateral GTCG / phân mảng bank lớn–nhỏ.
