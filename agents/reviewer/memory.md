# Memory — Reviewer Agent

## Blind spot đã phát hiện trong team

*(ghi khi tìm ra lỗ hổng mà Analysis/Strategy không thấy)*
- [2026-06-25] **Không có cột BID/ASK** — toàn team đọc curve ở mid. Strategy flattener cuối quý (pay 1W ask / receive 1M bid) kẹp hai spread, lúc spread giãn rộng nhất năm → "cạnh thực" có thể bị spread nuốt sạch. CHẶN: chưa có bid/ask thì không gọi trade nào "cạnh thực". `#thiếu-data`
- [2026-06-25] **Thiếu data NDF offshore** — spot sát trần, NDF points thường dẫn dắt onshore swap khi căng FX; team phân tích onshore mà bỏ kênh phát hiện áp lực sớm nhất.
- [2026-06-25] **Bỏ kết cấu KỲ HẠN can thiệp SBV** — chỉ hỏi "bơm/hút", không theo dõi SBV bán USD forward kỳ hạn nào (đè trực tiếp swap points đoạn đó).
- [2026-06-25] **Chưa định lượng outflow chuyển lợi nhuận FDI cuối quý** — cộng hưởng nhập siêu kỷ lục, đẩy cầu USD đúng lúc spot sát trần → ép SBV về phía hút VND.

---

## Lỗi lặp lại của team

*(ghi khi cùng loại lỗi xuất hiện nhiều lần)*
- [2026-06-25] **Anchoring vào lỗi gần nhất (đảo dấu)** — 23/06 sai vì tưởng SBV hút; 25/06 Forecast lại neo Base 60% = "SBV tiếp tục thả". Cùng blind spot `#bỏ-sót-SBV`, chỉ đổi dấu. Hàm phản ứng SBV vẫn chưa mô hình hóa được mà cứ đặt xác suất cao lên nó.
- [2026-06-25] **Hedge mọi hướng sau cú trượt** — Strategy #2 (receive 3M-6M) vs #4 (pay 1M-3M) chống nhau trên cùng đoạn curve, đốt carry hai chiều = trả tiền để không có view. Triệu chứng sợ-sai sau 23/06.

---

## Setup đã REJECT nhưng thực ra đúng

*(quan trọng — để calibrate độ khắt khe)*

---

## Setup đã APPROVE nhưng thực ra sai

*(quan trọng nhất — để cải thiện checklist)*
