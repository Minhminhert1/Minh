# Memory — Reviewer Agent

## Blind spot đã phát hiện trong team

*(ghi khi tìm ra lỗ hổng mà Analysis/Strategy không thấy)*

### Session 28/06
- **CNY/CNH không được theo dõi:** Kênh truyền dẫn quan trọng từ thị trường châu Á sang VND (carry từ CNY yếu → VND bị áp lực). Cần thêm R3 monitör CNY spot + NDF para tiên xem xu hướng.
- **Đáo hạn FX Swap SBV không được dự báo chính xác:** Cú hút sau 01/07 có thể gây ON spike (không phải reset êm như dự báo base). Cần R4 xác nhận quy mô FX Swap còn lại + hạn chót.
- **Quy mô dự trữ ngoại hối không được kiểm tra:** SBV dùng FX Swap thay bán spot → dự trữ giữ lại. Cần proxy (ví dụ: spot có hạ không khi ON thấp) để kiểm chứng chiến lược hy sinh lãi suất.

---

## Lỗi lặp lại của team

*(ghi khi cùng loại lỗi xuất hiện nhiều lần)*

### Pattern lỗi A2
- **1M–3M phẳng ≠ ổn định:** A2 dễ vội kết luận curve phẳng = kỳ vọng ổn định. Thực tế: thị trường mỏng (volume thấp) → mũi tên không di chuyển không phải vì fundamental yên tĩnh. Tag: `#suy-diễn-quá`

### Pattern lỗi data
- **Spot anchor cũ/mới lẫn lộn:** A3 cần xác nhận spot mỗi turn. Ví dụ: 26.43 vs 26.30 = sai 130pip (lớn), ảnh hưởng risk scenario. Tag: `#data-cũ`

---

## Setup đã REJECT nhưng thực ra đúng

*(quan trọng — để calibrate độ khắt khe)*

- (chưa có 28/06)

---

## Setup đã APPROVE nhưng thực ra sai

*(quan trọng nhất — để cải thiện checklist)*

- **[28/06] A2 "1M–3M phẳng = kỳ vọng ổn định" → REJECT:** Cần phân tách thị trường mỏng vs fundamental (không có source). A3 dự báo dạo này dựa vào seasonality ≠ curve shape → setup cần sửa.
- **[28/06] Dự báo O/N peak 30/06 mà không kiểm FX Swap maturity:** Đáo hạn sau 01/07 có thể gây ON spike 30/06 EOD. Cần R4 xác nhận → adjust kịch bản BEAR/BULL.
