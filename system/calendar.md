# calendar.md — Lịch sự kiện chủ động

> R4 (Policy & SBV) giữ file này. Trước sự kiện **1–2 ngày**, team tự nhắc +
> dựng kịch bản tác động lên swap curve. Cập nhật ngày cụ thể khi biết.

---

## Định kỳ — Việt Nam
| Sự kiện | Tần suất | Tác động chính |
|---------|----------|----------------|
| Cuối quý (BCTC) | 31/3, 30/6, 30/9, 31/12 | DN giữ tiền làm BCTC → **funding VND căng**, O/N tăng |
| Cuối năm tài chính | 31/12 | Căng thanh khoản mạnh nhất |
| Tết Nguyên Đán | T1–T2 | Cầu tiền mặt tăng → thanh khoản căng trước Tết |
| Kỳ nộp thuế (VAT, TNDN) | hàng tháng/quý | Hút VND khỏi hệ thống tạm thời |
| Đáo hạn tín phiếu SBV | theo đợt phát hành | Bơm VND lại khi đáo hạn |
| Đáo hạn OMO/repo | hàng tuần | Thay đổi thanh khoản ngắn hạn |
| Số liệu CPI/GDP/tín dụng (GSO/SBV) | hàng tháng/quý | Định hướng chính sách |

## Định kỳ — Thế giới
| Sự kiện | Tần suất | Tác động |
|---------|----------|----------|
| FOMC (Fed) | 8 lần/năm | SOFR/kỳ vọng lãi suất USD → chân USD của swap |
| US CPI | giữa tháng | Kỳ vọng Fed |
| NFP | thứ 6 đầu tháng | DXY, risk sentiment |
| PBoC (CNY fixing/LPR) | hàng tháng | Áp lực CNY → VND |
| ECB / BOJ | 8 lần/năm | DXY |

---

## Sắp tới (cập nhật thủ công/định kỳ)
```
- [YYYY-MM-DD] [sự kiện] — kỳ vọng: [...] — kịch bản tác động curve: [...]
```
*(R4 điền khi có ngày cụ thể; trước 1–2 ngày Orchestrator nhắc bạn.)*

---

## Quy tắc
- Trước sự kiện lớn: A3 dựng sẵn 2–3 kịch bản (base/up/down) cho curve.
- Sau sự kiện: Journalist ghi thực tế vs kịch bản → chấm điểm dự báo.
