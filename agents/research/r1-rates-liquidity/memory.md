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

## Nguồn nội bộ mới (2026-07-02)
- **Bản tin treasury/dealing desk** (user cung cấp, không phải public) — độ tin CAO NHẤT trong mọi nguồn R1 từng có, dùng thuật ngữ TT1/TT2, GAP TT1, TgKB, Citad. Chứa: TD/HĐV toàn hệ thống %ytd, CV/HĐ ngoại tệ, TGKB tại SBV & NHTM, OMO ròng theo tuần, CITAD toàn hệ thống, chi tiết khối lượng/lãi suất SBV FX swap.
- ⚠️ Bản tin dạng này có thể kèm bảng/hình không truyền qua text khi copy-paste — luôn verify chéo số liệu (vd: quy đổi VND/USD phải khớp tỷ giá đang dùng ở chỗ khác trong CÙNG bản tin) trước khi tin.
- **CITAD** (số dư thanh toán bù trừ liên NH) là chỉ số thanh khoản mới, nên thêm vào watchlist theo dõi định kỳ nếu có nguồn lặp lại.
- **TGKB (tiền gửi kho bạc) tại SBV & NHTM**: giảm = KBNN bơm tiền ra nền kinh tế (hỗ trợ thanh khoản); tăng = hút về.

## Ghi chú thanh khoản theo phiên
- 30/06/2026: ON 13% (khóa sổ Q2) dù SBV bơm ròng ~14.600 tỷ + swap FX 7d → cầu chốt quý nuốt trọn lượng bơm; áp lực dịch sang 1W (khoản vay bắc qua khóa sổ).
- Tuần 22–26/06: SBV đảo chiều bơm ròng ~3.962 tỷ bằng kỳ hạn DÀI 35–56d @4,5% — bơm dài trước sự kiện là tín hiệu SBV chuẩn bị trước cho chốt quý + kỳ thuế.
- Chuỗi ON tháng 6: 11% (01/06) → 5,4–5,78% → ~3,5% (12/06) → thấp → 3,6% (29/06) → 13% (30/06). Biến động 2 chiều cực mạnh là đặc trưng 2026.
- Gap OMO 4,5% vs LNH 8% (+350bps) không tự khép → nghi cạn collateral GTCG / phân mảng bank lớn–nhỏ.
- **[SỬA 02/07] OMO tuần 22–26/06:** con số Vietstock "bơm ròng ~3.962 tỷ" ĐÚNG bậc độ lớn (data nội bộ xác nhận tuần liền kề 19–24/06 bơm ròng ~+8k tỷ) — phép trừ thô "30.962 mới − 72.000 đáo hạn = −41.038" mà R1 từng nghi ngờ là SAI vì con số "72.000 đáo hạn" gộp cả kênh khác (tín phiếu?) ngoài OMO reverse repo thuần. Bài học: khi thấy phép trừ tự tính lệch xa số headline nguồn báo, ưu tiên tin headline + tìm nguồn thứ 2 xác nhận, đừng tự suy luận số liệu.
- **[MỚI 02/07] GAP TT1 & GAP CV/HĐ ngoại tệ là driver cấu trúc mạnh nhất đã xác nhận** cho mặt bằng LNH 8%: TD +7,08% ytd vs HĐV +5,02% ytd (gap −378k tỷ); CV NT +39,6% ytd vs HĐ NT +5,02% ytd (gap −7,32 tỷ USD). Đây là số cứng từ treasury desk, độ tin 5 — ưu tiên hỏi user xin cập nhật định kỳ.
