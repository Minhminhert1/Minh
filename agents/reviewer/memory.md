# Memory — Reviewer Agent

## Blind spot đã phát hiện trong team

- **[2026-06-24]** Bỏ sót **NDF/CCS offshore** — phân tích chỉ onshore LNH; kỳ vọng phá giá thật sống ở NDF. → Mọi report swap phải kèm NDF 1M–3M.
- **[2026-06-24]** Bỏ trống **lịch đáo hạn tín phiếu/OMO quanh ngày sự kiện** — biến quyết định kịch bản A (siết) vs B (bơm phủ turn). Thiếu nó → turn-play là cá cược mù.
- **[2026-06-24]** Tin **1 điểm giá inverted (bid 4.0 > offer)** mà chưa kiểm độ sâu → có thể lệnh lẻ/ảo dựng cả "kim 1W".
- **[2026-06-24]** Cấu trúc xác suất **giả-rời-rạc**: GT-A/B và kịch bản SBV A/B gán tổng=100% như loại trừ nhau, thực tế **chồng lấn** (SBV làm cả bơm OMO + giữ lãi ngắn). → Luôn cho phép nhánh "lai".

## Setup đã hạ độ tin (calibrate)
- **[2026-06-24]** Hạ GT-A "turn premium thuần" 75%→55%; kịch bản SBV A 45%→37%, B 30%→38% (đội under-weight việc SBV THƯỜNG làm = bơm OMO phủ turn). Hoãn trade turn-play (a), đẩy RV (b) lên ưu tiên #1.

---

## Lỗi lặp lại của team

- **[2026-06-24] Reviewer không bắt được lỗi số vì không có ground-truth.** Lỗi trừ i_USD hai lần
  lọt qua cả red-team. → Từ nay Reviewer **BẮT BUỘC**: (1) check convention/đơn vị input; (2) tái
  tính số chủ chốt độc lập; (3) sanity-check độ lớn vs mốc thực tế (vd swap points 1Y ~800–1.100đ).
  Không tái-tính = review vô nghĩa với lỗi định lượng. (Đã đưa vào schema §4 + CLAUDE.md #9/#10.)
- **[2026-06-24] Cảnh giác "nghi thức rỗng":** nhiều wave/Opus mà thiếu data thì red-team chỉ làm
  bề mặt sai trông tự tin hơn. Reviewer phải đòi **nguồn cho mỗi nhận định**, gắn cờ chỗ chỉ [ƯỚC LƯỢNG].

---

## Setup đã REJECT nhưng thực ra đúng

*(quan trọng — để calibrate độ khắt khe)*

---

## Setup đã APPROVE nhưng thực ra sai

*(quan trọng nhất — để cải thiện checklist)*
