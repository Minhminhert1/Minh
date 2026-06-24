# sources.md — Data manifest (đi lấy số THẬT mỗi phiên)

> Luật #8 (GROUNDING GATE): Research tra nguồn thật TRƯỚC khi Analysis chạy.
> File này = danh sách cứng các số cần kéo + nguồn, để research có hệ thống, không ad hoc.
> Mỗi số ghi theo schema §1: `[chỉ số]: [giá trị] | nguồn | as-of YYYY-MM-DD HH:mm ICT | độ tin 1–5`.

---

## BẮT BUỘC mỗi phiên (thiếu = hạ độ tin kết luận, nêu rõ)

| # | Chỉ số | Agent | Nguồn gợi ý |
|---|--------|-------|-------------|
| 1 | Đường cong LNH VND theo tenor (bid/ask) + **convention** (i_VND? chênh lãi?) | R1 | đại lý/Refinitiv; **hỏi rõ nếu input mơ hồ** |
| 2 | OMO bơm/hút ròng + trạng thái tín phiếu SBV (phát hành/đáo hạn) | R1 | SBV, báo tài chính |
| 3 | **Lịch đáo hạn tín phiếu/OMO** quanh mốc sự kiện (chốt quý/Tết) | R1 | SBV |
| 4 | Tỷ giá trung tâm + USD/VND spot + room còn lại tới trần | R4 | SBV, Investing.com |
| 5 | SOFR ON + **Term SOFR 1W/1M/3M/6M/1Y** | R3 | FRED, CME Term SOFR |
| 6 | DXY, USD/CNH | R3 | Investing.com |
| 7 | **NDF USD/VND offshore 1M/3M** vs onshore forward (blind spot 06-24) | R6 | đại lý/Bloomberg |

## THEO SỰ KIỆN (kéo khi liên quan)
- CPI/GDP/tín dụng/BoP/FDI/kiều hối VN — R2 (GSO/SBV) khi hỏi vĩ mô VN.
- FOMC/dot plot, US CPI, NFP — R3 quanh lịch (xem `calendar.md`).
- PBoC LPR/RRR/fixing — R3 khi CNH biến động.

---

## QUY TẮC
- **Convention trước tiên (luật #9):** xác nhận đường cong là gì trước khi tính 1 phép nào.
- Số thiếu/không lấy được → ghi `THIẾU` rõ ràng + hạ độ tin mục liên quan; **không thay bằng ước lượng rồi kết luận như thật**.
- Số tính ra (swap points, forward) → **sanity-check độ lớn (luật #10)** trước khi đưa vào báo cáo.
