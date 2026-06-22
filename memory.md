# Memory — FX Research Team

> File này là bộ nhớ tổng của toàn team. Claude cập nhật sau mỗi session.

---

## Bài học tổng hợp

### Nghịch lý cốt lõi USD/VND (22/6/2026) — chìa khóa hiểu toàn bộ
- **Kinh tế VN khỏe bề ngoài nhưng dòng USD ngắn hạn yếu**: GDP Q1 +7,83% (cao nhất 15 năm), FDI đăng ký Q1 15,2 tỷ (+42,9%) → đỡ VND dài hạn. NHƯNG cán cân TM lật từ thặng dư 3,57 tỷ → thâm hụt 7,9 tỷ (đến 15/4, nhập khẩu +28%), kiều hối HCM Q1 −16,9% → cung USD ngắn hạn cạn.
- **SBV bị TRÓI TAY → buộc dùng vũ khí lãi suất**: (1) dự trữ mỏng (109,6 tỷ 1/2022 → 83,6 tỷ 12/2025; M2/dự trữ >940% vs an toàn <400%; phủ nhập khẩu thấp nhất 10 năm) → không thể đốt dự trữ; (2) Mỹ áp thuế 20% + USTR dán nhãn thao túng tiền tệ → không thể phá giá công khai. ⇒ chỉ còn đẩy lãi suất VND để phạt short-VND. Đây là lý do gốc front-end đường cong vọt lên.
- **Hệ quả phái sinh**: vol bị nén ở spot, DỒN sang front-end đường cong + chênh NDF offshore/onshore. Săn biến động ở đó, không ở tỷ giá.
- Report toàn diện: `reports/2026-06-22-usdvnd-phan-tich-toan-dien.md`.

---

## Các cặp tiền đang theo dõi

- **CHỈ USD/VND** — user chốt focus duy nhất (22/6/2026). Không phân tích cặp khác trừ khi được yêu cầu.
- DXY, USD/JPY: chỉ dùng làm **tham chiếu driver** cho USD/VND, không trade riêng.

### Khung phân tích USD/VND (đặc thù — KHÔNG áp khung carry cổ điển)
- Là **thả nổi có quản lý**: SBV đặt **tỷ giá trung tâm** + biên độ → giá NHTM kịch trần là tín hiệu căng.
- Driver chính của **spot**: kỳ vọng tỷ giá (DXY/USD mạnh → áp lực tăng), cung-cầu USD nội địa, can thiệp/điều hành SBV.
- Gap lãi suất áp vào qua **điểm kỳ hạn (forward points) & NDF offshore**: chênh lãi VND–USD = giá forward. Đây là cầu nối với nghiệp vụ phái sinh.
- Bài học đã chốt: gap lãi suất KHÔNG cứu spot khi DXY mạnh (lỗ tỷ giá ăn sạch lãi chênh).

### ANGLE CHỐT (22/6/2026): USD/VND PHÁI SINH — Forward/NDF
- Công thức: `Điểm kỳ hạn ≈ S × (r_VND − r_USD) × t/360`. Lãi VND > USD → forward LUÔN dương điểm. Long USD forward = trả trước phần chênh lãi (carry âm).
- **Cú twist SBV (quan trọng nhất)**: SBV đẩy lãi suất VND lên để PHẠT short-VND → điểm kỳ hạn phình to → long USD forward ngắn hạn rất đắt/dễ bị siết. Đây là cơ chế đặc thù USD/VND.
- Data 22/6: VND O/N liên NH vọt 6,97%→**11%** (1/6), USD O/N 3,65% → gap ngắn ~7,3% → điểm kỳ hạn ngắn đắt. SBV bơm OMO >35.000 tỷ @4,5% (tín dụng 4,42% > huy động 2,6% → căng thanh khoản).
- **View forward/NDF**: 🔴 không long USD forward ≤1M (carry âm đỉnh, squeeze); 🟡 view mất giá cấu trúc → ưu tiên 3–6M; 🟢 canh chênh NDF offshore vs onshore = thước đo áp lực đầu cơ thật.
- Van 2 chiều ngược nhau trên cùng vị thế: PCE nóng → spot ép lên (tốt long USD) NHƯNG SBV siết lãi VND → điểm kỳ hạn càng đắt.
- **Còn thiếu để định lượng**: đường cong forward points USD/VND theo tenor + level NDF offshore (nguồn public không ra số; cần Bloomberg/Reuters/desk).

---

## Bias thị trường hiện tại

*(session 22/6/2026)*
- **USD: mạnh** — DXY vùng 99–101, đỉnh 13 tháng. Driver: Fed hawkish (½ thành viên nghiêng tăng lãi 2026) + lạm phát dai dẳng (CPI 3,8%, core PCE 3,3%).
- **USD/VND: nghiêng tăng** — trung tâm NHNN 25.181 (19/6), NHTM kịch trần 26.433, chợ đen ~26.31–26.41k. Dự báo Q3 ~26.500.

---

## Sự kiện quan trọng sắp tới

*(tuần 22–28/6/2026)*
- T2: PBoC, CPI Canada
- T3: Flash PMI Đức/EU/Anh/Mỹ
- T4: CPI Úc
- **T5: US Core PCE + GDP final + CPI Nhật ← tâm điểm cho USD & USD/VND**

---

## Pattern đã học

- **Carry trade 2026 = vùng nguy hiểm, không phải mùa đẹp**: BoJ nâng lãi (16/6) → JPY funding đắt lên → gap co lại; ~500 tỷ USD short JPY treo lơ lửng → rủi ro unwind cao (tiền lệ 8/2024: Nikkei −12%, S&P −6%).
- **Gap lãi suất KHÔNG cứu được VND**: giữ VND lãi cao hơn USD (carry dương trên giấy) nhưng USD/VND leo về 26.500 → lỗ tỷ giá ăn sạch lãi → giữ USD vẫn thắng. Logic tỷ giá > logic lãi suất khi DXY mạnh.
- **Bản đồ lãi suất 6/2026**: Fed 4,25–4,50% (giữ, hawkish), Banxico 6,50% (dừng hạ), ECB +25bp, BoJ +25bp, BoC kẹt.
- **2 van liên thông quyết carry + EM**: PCE Mỹ (hướng USD) & BoJ/can thiệp JPY (carry unwind). USD mạnh + JPY giật = xấu nhất cho carry & VND.

---

## Lỗi hệ thống đã gặp

*(ghi khi team đưa ra nhận định sai, phân tích nguyên nhân)*
