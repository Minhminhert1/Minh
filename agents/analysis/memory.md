# Memory — Analysis Agent

## Pattern kỹ thuật đã học

- **Đọc đường cong lãi suất USD/VND (forward-implied) cho phái sinh**: chia 3 vùng — front (ON-1W), bướu/khúc 1-4 tuần, bụng (2-6M), đuôi (1Y).
  - Front nhảy mạnh + bụng trũng = **đường cong đảo ở front** → SBV siết thanh khoản ngắn để phòng thủ VND, kỳ vọng dịu sau 2-3M. (Dashboard 22/6: ON 2,80 +0,30; 1W 3,50 +0,50; 2W 4,20; 1M 4,10 −0,10; 2-6M 3,90; 1Y 4,10.)
  - Long USD kỳ hạn = trả lãi tại tenor đó → **rẻ nhất ở bụng 3-6M, đắt nhất 2W-1M**. Thu carry → bán ở đỉnh điểm 2W.
  - Front-end ĐẢO (2W > 6M) ⇒ **roll ngắn (2W+2W) ĐẮT hơn khóa thẳng 1M** → ưu tiên khóa kỳ hạn dài hơn lăn ngắn.
  - Luôn xem cả Bid để có spread/tenor (front-end spread rộng nhất) → mới ra carry ròng thực.

- **Funding yếu → bid target cao (logic carry)**: đúng KHI funding yếu trật tự & kỳ vọng còn tiếp diễn. Bẫy: funding yếu + vị thế crowded → "bid cao nhất" = rủi ro unwind lớn nhất (funding bật mạnh → đóng lệnh hàng loạt). Phân biệt funding yếu *chủ động* (dovish, theo được) vs *bị động/quá đà* (sắp đảo, cảnh giác).
- **USD/VND KHÁC khung carry**: bid dồn vào USD do kỳ vọng tỷ giá tăng (depreciation), KHÔNG do swap (VND mới là đồng lãi cao). Không áp thẳng "funding yếu → bid cao" cho USD/VND.

---

## Macro relationship đã xác nhận

- **DXY mạnh → áp lực tăng lên USD/VND** (22/6/2026: DXY đỉnh 13 tháng trùng giai đoạn NHTM kịch trần 26.433).
- **Fed hawkish + lạm phát US cao → USD mạnh** → kéo cả rổ EM yếu, gồm VND.
- **Core PCE** là chỉ báo lạm phát Fed dùng chính → là catalyst lớn nhất cho hướng USD ngắn hạn.

---

## Nhận định đã sai & nguyên nhân

*(ghi sau khi biết kết quả thực tế — quan trọng nhất để học)*

---

## Indicator nào hoạt động tốt nhất với user này

*(cập nhật theo phản hồi của user)*
