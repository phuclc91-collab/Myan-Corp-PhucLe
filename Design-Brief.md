TÀI LIỆU ĐỊNH HƯỚNG THIẾT KẾ GIAO DIỆN VÀ TRẢI NGHIỆM (DESIGN BRIEF)  
DỰ ÁN: HỆ THỐNG CRM MYAN CORP \- GIAI ĐOẠN 1  
TÁC GIẢ: CHUYÊN GIA TƯ VẤN HỆ THỐNG UX/UI  
Tài liệu này thiết lập các tiêu chuẩn thiết kế thị giác và cấu trúc trải nghiệm người dùng dành riêng cho ứng dụng web CRM của Myan Corp. Mục tiêu tối thượng của giao diện là tối ưu hóa mật độ hiển thị dữ liệu lớn, đảm bảo tính trang trọng của môi trường doanh nghiệp và hỗ trợ người dùng ra quyết định nhanh chóng mà không bị phân tâm bởi các yếu tố đồ họa thừa.

### **1\. BẢNG MÀU CHUẨN MỰC (COLOR PALETTE)**

Hệ thống áp dụng tỷ lệ phân bổ màu sắc nghiêm ngặt nhằm tạo chiều sâu thị giác và hướng sự tập trung của mắt vào các khu vực dữ liệu quan trọng.

* **Màu chủ đạo (Primary Color):** Xanh dương đậm (Mã màu \#1E3A8A). Đại diện cho sự tin cậy, tính bảo mật và sự chuyên nghiệp. Được áp dụng cho thanh điều hướng bên trái, tiêu đề chính của trang và các nút bấm thực hiện hành động chính.  
* **Màu phụ trợ (Secondary Color):** Xám Slate trung tính (Mã màu \#475569). Dùng cho các văn bản mô tả, tiêu đề phụ và trạng thái chưa kích hoạt của các thanh điều hướng.  
* **Màu nền hệ thống (Background Colors):**  
  * Nền giao diện tổng thể: Trắng xám nhạt (Mã màu \#F8FAFC) nhằm giảm độ chói của màn hình khi làm việc thời gian dài.  
  * Nền các khối nội dung và bảng biểu: Trắng thuần (Mã màu \#FFFFFF) để tạo độ tương phản tối đa với chữ.  
* **Màu sắc chức năng định danh (Semantic Colors):**  
  * Trạng thái thành công / Phân khúc VIP: Xanh ngọc lục bảo (Mã màu \#10B981).  
  * Trạng thái đang xử lý / Phân khúc Đại lý: Vàng hổ phách (Mã màu \#F59E0B).  
  * Trạng thái quá hạn / Mức độ ưu tiên cao: Đỏ hoa hồng (Mã màu \#F43F5E).

### **2\. HỆ THỐNG CHỮ TIÊU CHUẨN (TYPOGRAPHY)**

Hệ thống CRM sử dụng duy nhất một họ phông chữ không chân hiện đại là **Inter** hoặc **Roboto**. Đây là phông chữ được tối ưu hóa cho màn hình kỹ thuật số, giữ được độ sắc nét cao ngay cả khi hiển thị ở kích thước nhỏ trong các bảng dữ liệu dày đặc.

* **Tiêu đề phân hệ lớn (Page Title):** Kích cỡ 24px, Định dạng đậm (Bold), Màu chủ đạo \#1E3A8A.  
* **Tiêu đề khối / Cột Kanban (Section Heading):** Kích cỡ 16px, Định dạng bán đậm (Semi-Bold), Màu xám đậm \#1E293B.  
* **Văn bản nội dung / Thông tin khách hàng (Body Text):** Kích cỡ 14px, Định dạng thường (Regular), Khoảng cách dòng 1.5, Màu đen xám \#334155.  
* **Ghi chú phụ / Chỉ số phụ (Caption Text):** Kích cỡ 12px, Định dạng thường hoặc in nghiêng, Màu xám phụ trợ \#64748B.

### **3\. CẤU TRÚC BỐ CỤC TRANG (LAYOUT STRUCTURE)**

Giao diện áp dụng cấu trúc khung cố định hai khối chính (Fixed Layout) nhằm tối ưu không gian làm việc trên máy tính:

* **Thanh điều hướng bên trái (Sidebar):** Chiều rộng cố định 260px. Chiếm toàn bộ chiều dọc màn hình nền bên trái. Sử dụng màu nền tối để tách biệt hoàn toàn với vùng làm việc.  
* **Thanh công cụ trên cùng (Top Bar):** Chiều cao cố định 64px, nằm ở rìa trên bên phải thanh Sidebar. Chứa đường dẫn thư mục hiện tại, bộ lọc thời gian toàn cục và khu vực thông tin tài khoản cá nhân.  
* **Vùng nội dung trung tâm (Main Workspace):** Chiếm toàn bộ không gian còn lại. Áp dụng hệ thống lưới 12 cột (12-column Grid) linh hoạt để tự động co giãn theo độ phân giải màn hình máy tính của người dùng. Dữ liệu được tổ chức theo các khối hình chữ nhật xếp cách nhau 24px.

### **4\. PHONG CÁCH CÁC CẤU PHẦN GIAO DIỆN (COMPONENT STYLE)**

Để đảm bảo tính đồng nhất trên toàn bộ web app, các cấu phần giao diện được quy chuẩn hóa cấu trúc như sau:

#### **Bảng thông số phong cách cấu phần**

| Tên cấu phần | Quy chuẩn thiết kế | Trạng thái hiển thị (States) |
| :---- | :---- | :---- |
| **Hộp nội dung (Card)** | Nền trắng \#FFFFFF, góc bo tròn nhẹ 8px. Đường viền mỏng 1px màu xám nhạt \#E2E8F0. Không dùng hiệu ứng đổ bóng dày để tránh rối mắt. | Mặc định cố định trên màn hình. |
| **Nút bấm (Button)** | Nền màu chủ đạo, chữ trắng cho hành động chính. Nền trắng viền xám cho hành động phụ. Chữ không viết hoa toàn bộ, góc bo tròn 6px. | Mặc định / Di chuột qua (Nền đậm hơn 10%) / Nhấn chọn / Bị khóa (Ẩn mờ). |
| **Ô nhập liệu (Input)** | Chiều cao chuẩn 40px. Nền trắng, viền xám \#CBD5E1. Văn bản gợi ý màu xám nhạt. | Mặc định / Tập trung con trỏ (Viền đổi sang xanh dương) / Lỗi dữ liệu (Viền đổi sang màu đỏ). |
| **Nhãn phân loại (Badge)** | Kích thước nhỏ, bo tròn góc tối đa. Sử dụng nền màu nhạt và chữ màu đậm tương ứng của màu chức năng để phân loại phân khúc khách hàng. | Cố định hiển thị cạnh tên đối tượng. |
| **Thực đơn bên (Sidebar Item)** | Dạng chữ hiển thị căn lề trái rõ ràng. Các mục menu cách nhau một khoảng đệm 8px. | Trạng thái hoạt động: Chữ trắng trên nền xanh đậm. Trạng thái thường: Chữ xám Slate. |
| **Thẻ Kanban (Kanban Card)** | Dạng Card thu nhỏ, bo góc 6px. Bên trong chứa Tên khách hàng (Đậm), Số tiền hợp đồng (Màu chủ đạo), Tên sales phụ trách (Chữ nhỏ). | Mặc định / Trạng thái đang được giữ và di chuyển (Viền nét đứt màu xanh). |

### **5\. HỆ THỐNG DỮ LIỆU MẪU CHUẨN HÓA (SAMPLE DATA)**

Dưới đây là tệp dữ liệu mẫu được xây dựng dựa trên bối cảnh doanh nghiệp thực tế tại Việt Nam để nạp vào hệ thống thử nghiệm giao diện.

#### **5.1. Danh sách 6 khách hàng tiềm năng**

| Tên khách hàng | Công ty đối tác | Phân khúc | Sản phẩm quan tâm | Giá trị dự kiến |
| :---- | :---- | :---- | :---- | :---- |
| Nguyễn Hoàng Nam | Công ty Cổ phần Sữa Việt Nam (Vinamilk) | VIP | Hệ thống Quản trị Cung ứng | 150.000.000 VND |
| Trần Tuyết Mai | Tập đoàn FPT | Đại lý | Gói Giải pháp Doanh nghiệp | 85.000.000 VND |
| Lê Phan Anh | Tập đoàn Hòa Phát | VIP | Nền tảng Quản trị Nhân sự | 320.000.000 VND |
| Phạm Hồng Đăng | Tập đoàn Masan | VIP | Tối ưu Vận hành Bán lẻ | 450.000.000 VND |
| Hoàng Thục Quyên | Công ty Cổ phần Hàng không Vietjet | Khách lẻ | Tư vấn Chuyển đổi số | 50.000.000 VND |
| Đặng Minh Quân | Tập đoàn Vingroup | VIP | Hệ thống CRM Tích hợp | 600.000.000 VND |

#### **5.2. Danh sách 5 công việc ngành tiêu biểu**

* **Công việc 1:** Gửi bản thảo báo giá chi tiết hệ thống  
  * Khách hàng liên kết: Nguyễn Hoàng Nam (Vinamilk)  
  * Mức độ ưu tiên: Cao  
  * Hạn chót hoàn thành: 05.07.2026  
* **Công việc 2:** Gọi điện tư vấn giải pháp chuyển đổi số  
  * Khách hàng liên kết: Trần Tuyết Mai (FPT)  
  * Mức độ ưu tiên: Trung bình  
  * Hạn chót hoàn thành: 02.07.2026  
* **Công việc 3:** Đàm phán các điều khoản hợp đồng kinh tế  
  * Khách hàng liên kết: Lê Phan Anh (Hòa Phát)  
  * Mức độ ưu tiên: Cao  
  * Hạn chót hoàn thành: 10.07.2026  
* **Công việc 4:** Chuẩn bị tài liệu kỹ thuật phục vụ nghiệm thu đợt 1  
  * Khách hàng liên kết: Phạm Hồng Đăng (Masan)  
  * Mức độ ưu tiên: Thấp  
  * Hạn chót hoàn thành: 15.07.2026  
* **Công việc 5:** Gặp mặt trực tiếp ký kết hợp đồng chính thức  
  * Khách hàng liên kết: Đặng Minh Quân (Vingroup)  
  * Mức độ ưu tiên: Cao  
  * Hạn chót hoàn thành: 29.06.2026

#### **5.3. Định nghĩa 3 danh sách khách hàng phân nhóm chuẩn mẫu**

* **Danh sách 1: Khách hàng Doanh nghiệp VIP trọng điểm**  
  * Tiêu chí lọc: Các tài khoản được gắn nhãn VIP, tổng giá trị các cơ hội bán hàng lớn hơn 100.000.000 VND.  
  * Đối tượng chứa mẫu: Nguyễn Hoàng Nam (Vinamilk), Lê Phan Anh (Hòa Phát), Phạm Hồng Đăng (Masan), Đặng Minh Quân (Vingroup).  
* **Danh sách 2: Đối tác Hệ thống Đại lý phân phối**  
  * Tiêu chí lọc: Các tài khoản đối tác pháp nhân được gắn nhãn Đại lý.  
  * Đối tượng chứa mẫu: Trần Tuyết Mai (FPT).  
* **Danh sách 3: Khách hàng Tiềm năng Khách lẻ**  
  * Tiêu chí lọc: Các tài khoản cá nhân hoặc tổ chức quy mô nhỏ được gắn nhãn Khách lẻ.  
  * Đối tượng chứa mẫu: Hoàng Thục Quyên (Vietjet).

Ban lãnh đạo đánh giá thế nào về cách phân bổ tỷ lệ hiển thị thông tin và hệ thống dữ liệu mẫu được chuẩn hóa theo mô hình doanh nghiệp lớn của Việt Nam trong bản định hướng thiết kế này?