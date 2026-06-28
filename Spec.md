Dưới đây là tài liệu đặc tả chức năng (Functional Specifications) chi tiết cho từng tính năng của hệ thống CRM Myan Corp (Giai đoạn 1). Mỗi chức năng được cấu trúc thành một bảng đặc tả riêng biệt, cung cấp đầy đủ thông tin về giao diện, logic dữ liệu và quy tắc phân quyền để đội ngũ kỹ thuật có thể tiến hành lập trình và cài đặt được ngay.

## **PHÂN HỆ 1: XÁC THỰC VÀ QUẢN LÝ QUYỀN TRUY CẬP**

### **1\. Chức năng: Đăng ký và Đăng nhập bằng Email \+ Mật khẩu**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Cho phép người dùng khởi tạo tài khoản mới hoặc truy cập vào hệ thống bằng tài khoản email doanh nghiệp cá nhân. |
| **Giao diện người dùng** | Biểu mẫu nằm giữa màn hình gồm: Ô nhập Địa chỉ Email, ô nhập Mật khẩu, ô nhập Họ và tên (chỉ có ở màn hình đăng ký), nút bấm "Thực hiện", dòng chữ liên kết "Chuyển sang Đăng nhập/Đăng ký" và "Quên mật khẩu". |
| **Logic xử lý dữ liệu** | Kiểm tra định dạng Email phải đúng cấu trúc doanh nghiệp. Mật khẩu bắt buộc có độ dài từ 8 ký tự trở lên. Hệ thống tiến hành mã hóa mật khẩu trước khi lưu trữ vào bảng bảo mật của Supabase. Nếu thông tin đăng nhập sai, hiển thị thông báo lỗi trực tiếp dưới ô nhập liệu. |
| **Quy tắc phân quyền** | Tài khoản tự đăng ký bên ngoài sẽ mặc định rơi vào trạng thái "Chờ duyệt" và chưa được gán vai trò truy cập dữ liệu cho đến khi được Admin phê duyệt. |

### **2\. Chức năng: Đăng nhập tài khoản nội bộ và Hợp nhất định danh trùng Email**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Cho phép nhân sự sử dụng tài khoản do Admin khởi tạo sẵn trong cơ sở dữ liệu SQL để đăng nhập, đồng thời tự động hợp nhất nếu trùng email. |
| **Giao diện người dùng** | Sử dụng chung biểu mẫu đăng nhập bằng Email và Mật khẩu của hệ thống. |
| **Logic xử lý dữ liệu** | Khi người dùng đăng ký hoặc đăng nhập, hệ thống thực hiện truy vấn kiểm tra trường Email trong cơ sở dữ liệu. Nếu Email này đã được Admin khởi tạo từ trước trong bảng dữ liệu SQL kèm theo vai trò (Role), hệ thống sẽ tự động liên kết phương thức đăng nhập bằng mật khẩu với mã định danh (User ID) đã có sẵn. Tuyệt đối không tạo ra bản ghi nhân sự mới, tránh việc nhân bản tài khoản rác. |
| **Quy tắc phân quyền** | Quyền hạn kinh doanh và phạm vi tiếp cận dữ liệu được giữ nguyên vẹn hoàn toàn theo cấu hình cũ của Email đó, không bị ảnh hưởng bởi hành động thay đổi phương thức đăng nhập. |

### **3\. Chức năng: Quên mật khẩu và Đặt lại mật khẩu**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Hỗ trợ người dùng tự phục hồi quyền truy cập hệ thống khi quên thông tin mật khẩu cá nhân. |
| **Giao diện người dùng** | Màn hình "Quên mật khẩu" gồm ô nhập Email và nút "Gửi yêu cầu". Màn hình "Đặt lại mật khẩu" gồm ô nhập Mật khẩu mới và ô Xác nhận mật khẩu mới. |
| **Logic xử lý dữ liệu** | Khi người dùng nhấn gửi yêu cầu, hệ thống kiểm tra sự tồn tại của Email. Nếu hợp lệ, một đường dẫn chứa mã xác thực (Token) có thời hạn hiệu lực 15 phút sẽ được gửi tự động về email của nhân sự. Người dùng nhấp vào đường dẫn để truy cập giao diện đặt lại mật khẩu. Hệ thống ghi nhận mật khẩu mới, cập nhật vào Supabase và hủy bỏ hiệu lực của mã Token cũ. |
| **Quy tắc phân quyền** | Áp dụng chung cho cả ba cấp bậc người dùng (Admin, Trưởng nhóm, Sales). |

### **4\. Chức năng: Cơ chế phân quyền dữ liệu bảo mật 3 lớp**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Kiểm soát phạm vi hiển thị dữ liệu của toàn bộ các phân hệ trong CRM dựa trên vai trò hành chính của tài khoản đang đăng nhập. |
| **Giao diện người dùng** | Hệ thống tự động ẩn hoặc hiện các thanh thực đơn, các nút chức năng và các dòng dữ liệu trên màn hình làm việc tương ứng với từng vai trò. |
| **Logic xử lý dữ liệu** | Kích hoạt tính năng bảo mật mức dòng (Row-Level Security) của Supabase. Khi có yêu cầu truy xuất dữ liệu, hệ thống tự động chèn thêm điều kiện lọc: \- **Lớp 1 (Admin):** Mở toàn bộ dữ liệu. \- **Lớp 2 (Trưởng nhóm):** Chỉ hiển thị dữ liệu có mã nhóm trùng với mã nhóm của Trưởng nhóm. \- **Lớp 3 (Sales):** Chỉ hiển thị dữ liệu có mã người phụ trách trùng với mã định danh cá nhân của chính nhân viên đó. |
| **Quy tắc phân quyền** | Quyền hạn này gắn chặt với mã định danh tài khoản, người dùng không thể can thiệp hoặc thay đổi bằng các thao tác trên trình duyệt. |

## **PHÂN HỆ 2: QUẢN LÝ DANH SÁCH KHÁCH HÀNG CỐT LÕI**

### **5\. Chức năng: Thêm, Sửa, Xóa mềm hồ sơ khách hàng**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Thực hiện các tác vụ cập nhật và lưu trữ thông tin của từng khách hàng vào kho dữ liệu tập trung. |
| **Giao diện người dùng** | Màn hình danh sách dạng bảng dữ liệu. Biểu mẫu thêm/sửa hiển thị dạng cửa sổ Pop-up gồm các trường: Tên khách hàng, Số điện thoại, Email, Tên công ty, Địa chỉ, Phân khúc, Sản phẩm quan tâm, Ghi chú. Nút "Xóa" nằm ở thanh thao tác cuối mỗi dòng. |
| **Logic xử lý dữ liệu** | Trường Tên khách hàng và Số điện thoại là bắt buộc. Hệ thống tự động đối chiếu Số điện thoại trên toàn hệ thống; nếu phát hiện trùng lặp, lập tức chặn tiến trình và thông báo lỗi. Khi bấm "Xóa", hệ thống đổi trạng thái ẩn (is\_deleted \= true) để loại bỏ khỏi màn hình làm việc, dữ liệu gốc vẫn lưu trong database để phục vụ hậu kiểm. |
| **Quy tắc phân quyền** | Nhân viên Sales chỉ được xử lý khách hàng của mình. Trưởng nhóm được quyền xử lý khách hàng của toàn nhóm. Chỉ duy nhất Admin mới có nút chức năng xóa vĩnh viễn dữ liệu khỏi database. |

### **6\. Chức năng: Gắn nhãn phân khúc và Sản phẩm quan tâm**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Phân loại nhóm đối tượng khách hàng và ghi nhận nhu cầu sản phẩm cụ thể để tối ưu hóa chiến lược tư vấn. |
| **Giao diện người dùng** | Trong biểu mẫu chi tiết khách hàng, trường "Phân khúc" hiển thị dạng trình thả chọn một phương án (Khách lẻ, Đại lý, VIP). Trường "Sản phẩm quan tâm" hiển thị dạng danh sách tích chọn nhiều phương án (Multi-select). |
| **Logic xử lý dữ liệu** | Hệ thống ghi nhận các nhãn phân khúc và mảng mã sản phẩm được chọn vào các trường dữ liệu tương ứng trong bảng dữ liệu khách hàng. Các dữ liệu này liên kết trực tiếp với bộ lọc tìm kiếm nhanh trên thanh công cụ của màn hình danh sách khách hàng. |
| **Quy tắc phân quyền** | Tất cả các cấp người dùng (Admin, Trưởng nhóm, Sales) được quyền sử dụng tính năng này khi cập nhật hồ sơ khách hàng thuộc phạm vi quản lý của mình. |

### **7\. Chức năng: Tải lên danh sách khách hàng hàng loạt từ tập tin CSV (Bulk Import)**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Hỗ trợ nạp số lượng lớn dữ liệu khách hàng từ file bảng tính sẵn có vào hệ thống CRM để giảm thiểu thời gian nhập liệu thủ công. |
| **Giao diện người dùng** | Nút "Nhập từ CSV" nằm phía trên bảng danh sách khách hàng. Khi bấm vào sẽ mở giao diện chọn file từ máy tính và cung cấp đường dẫn tải xuống file CSV mẫu của công ty. |
| **Logic xử lý dữ liệu** | Hệ thống đọc toàn bộ tệp tin CSV được tải lên. Trước khi lưu vào cơ sở dữ liệu Supabase, hệ thống thực hiện quét kiểm tra tính toàn vẹn: Nếu có bất kỳ dòng dữ liệu nào thiếu thông tin bắt buộc hoặc trùng Số điện thoại/Email với dữ liệu hiện có, toàn bộ tiến trình sẽ bị dừng lại (Rollback). Hệ thống xuất thông báo lỗi hiển thị rõ số dòng và nguyên nhân lỗi cho người dùng. Nếu file hợp lệ 100%, hệ thống ghi dữ liệu hàng loạt và gán quyền phụ trách cho tài khoản thực hiện. |
| **Quy tắc phân quyền** | Chức năng này chỉ mở cho tài khoản thuộc vai trò Admin và Trưởng nhóm kinh doanh. |

### **8\. Chức năng: Kết xuất danh sách khách hàng ra tập tin CSV (Bulk Export)**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Cho phép trích xuất dữ liệu khách hàng từ hệ thống ra file bảng tính phục vụ công tác lưu trữ nội bộ hoặc báo cáo độc lập. |
| **Giao diện người dùng** | Nút chức năng "Xuất dữ liệu CSV" nằm ở thanh công cụ phía trên bảng danh sách. |
| **Logic xử lý dữ liệu** | Khi người dùng nhấn nút, hệ thống sẽ đóng gói toàn bộ các dòng dữ liệu khách hàng đang hiển thị trên màn hình (bao gồm cả kết quả sau khi áp dụng các bộ lọc phân khúc hoặc từ khóa tìm kiếm hiện tại) thành một tệp tin định dạng CSV và tự động tải xuống thiết bị cá nhân. |
| **Quy tắc phân quyền** | Tuân thủ nghiêm ngặt quy tắc bảo mật 3 lớp: Sales chỉ xuất được dữ liệu cá nhân phụ trách; Trưởng nhóm xuất được dữ liệu của toàn nhóm; Admin xuất được toàn bộ dữ liệu công ty. Hệ thống tự động ghi nhật ký (Audit Log) đối với mọi hành động xuất file để ngăn chặn thất thoát tài nguyên. |

## **PHÂN HỆ 3: QUẢN LÝ CƠ HỘI BÁN HÀNG (SALES PIPELINE)**

### **9\. Chức năng: Giao diện bảng Kanban và Kéo thả cập nhật trạng thái**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Trực quan hóa quy trình bán hàng theo các giai đoạn tiến độ, giúp nhân sự quản lý các thương vụ kinh doanh một cách khoa học. |
| **Giao diện người dùng** | Màn hình hiển thị dạng 5 cột dọc cố định: Tiếp cận, Tư vấn, Báo giá, Thương thảo, Thành công. Mỗi cơ hội bán hàng là một thẻ thông tin độc lập nằm trong các cột, chứa các chữ hiển thị: Tên khách hàng, Giá trị dự kiến, Người phụ trách. |
| **Logic xử lý dữ liệu** | Người dùng thực hiện thao tác bấm, giữ và di chuyển thẻ cơ hội từ cột này sang cột khác. Ngay khi thả thẻ vào cột mới, hệ thống gửi lệnh API ngầm cập nhật trường trạng thái (stage) của cơ hội đó vào Supabase theo thời gian thực và ghi nhận nhật ký lịch sử dịch chuyển quy trình. |
| **Quy tắc phân quyền** | Nhân viên Sales chỉ nhìn thấy và tương tác với các thẻ do mình phụ trách. Trưởng nhóm xem và điều phối được toàn bộ thẻ của các thành viên trong nhóm. |

### **10\. Chức năng: Tự động tính toán giá trị Pipeline và Chốt hợp đồng thành công**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Tự động cập nhật tổng giá trị tiền tệ của từng giai đoạn bán hàng và bắt buộc ghi nhận doanh thu thực tế khi thương vụ hoàn thành. |
| **Giao diện người dùng** | Phía trên tiêu đề của từng cột dọc Kanban hiển thị một dòng số tổng tiền lũy kế. Một cửa sổ Pop-up thông báo sẽ hiển thị khi thẻ được thả vào cột "Thành công". |
| **Logic xử lý dữ liệu** | Hệ thống tự động cộng tổng giá trị dự kiến của các thẻ trong cùng một cột và hiển thị lại con số này ngay lập tức sau mỗi thao tác kéo thả mà không cần tải lại trang. Khi thẻ được kéo vào cột "Thành công", cửa sổ Pop-up bắt buộc người dùng nhập vào "Giá trị hợp đồng chính thức" và "Ngày ký kết". Nếu người dùng không nhập hoặc hủy bỏ, thẻ sẽ tự động trả về vị trí cột cũ. |
| **Quy tắc phân quyền** | Áp dụng đồng nhất cho tất cả các tài khoản có quyền tương tác trên bảng Kanban. |

## **PHÂN HỆ 4: QUẢN LÝ CÔNG VIỆC VÀ LỊCH NHẮC**

### **11\. Chức năng: Tạo lập nhiệm vụ liên kết và Cập nhật trạng thái tiến độ**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Quản lý các đầu việc cần thực hiện đối với từng khách hàng, đảm bảo nhân sự thực hiện đúng cam kết và thời hạn. |
| **Giao diện người dùng** | Màn hình danh sách công việc hiển thị dạng bảng. Biểu mẫu tạo việc gồm: Tiêu đề việc, Nội dung chi tiết, Ô chọn khách hàng liên kết, Hạn chót hoàn thành, Mức độ ưu tiên (Cao, Trung bình, Thấp), Trạng thái (Chưa làm, Đang làm, Đã xong). |
| **Logic xử lý dữ liệu** | Trường Tiêu đề và Hạn chót là bắt buộc. Mọi nhiệm vụ khi khởi tạo bắt buộc phải chọn liên kết trực tiếp với hồ sơ của một khách hàng cụ thể trên CRM. Khi nhân sự tích chọn chuyển trạng thái sang "Đã xong", hệ thống khóa chỉnh sửa và ghi nhận mốc thời gian hoàn thành thực tế. |
| **Quy tắc phân quyền** | Nhân viên Sales tự tạo và quản lý danh sách việc của cá nhân. Trưởng nhóm có quyền tạo việc và gán trực tiếp người thực hiện cho các nhân viên dưới quyền trong nhóm của mình. |

### **12\. Chức năng: Cơ chế tự động cảnh báo công việc quá hạn**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Hệ thống tự động rà soát thời gian để đưa ra cảnh báo trực quan đối với các đầu việc bị chậm tiến độ. |
| **Giao diện người dùng** | Trên màn hình danh sách công việc và bảng điều khiển tổng quan, các nhiệm vụ có mức độ ưu tiên Cao hoặc đã vượt quá mốc thời gian Hạn chót nhưng Trạng thái vẫn là "Chưa làm" hoặc "Đang làm" sẽ tự động được thay đổi màu chữ và màu nền sang màu đỏ đậm. |
| **Logic xử lý dữ liệu** | Hệ thống thực hiện việc đối chiếu liên tục giữa thời gian thực tế của máy chủ với giá trị của trường Hạn chót (due\_date) trong bảng dữ liệu công việc để tự động thay đổi thuộc tính hiển thị giao diện của dòng dữ liệu đó theo thời gian thực. |
| **Quy tắc phân quyền** | Hiển thị cảnh báo cho cả nhân sự trực tiếp phụ trách công việc và cấp quản lý (Trưởng nhóm/Admin) để phục vụ công tác đôn đốc, giám sát. |

## **PHÂN HỆ 5: THEO DÕI TIẾN ĐỘ THANH TOÁN VÀ DÒNG TIỀN**

### **13\. Chức năng: Lập lịch thu tiền theo đợt và Cảnh báo công nợ**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Chia nhỏ giá trị hợp đồng thành các đợt thanh toán cụ thể và theo dõi sát sao tình hình thu hồi công nợ của doanh nghiệp. |
| **Giao diện người dùng** | Giao diện danh sách đợt thanh toán gồm bảng dữ liệu và thanh bộ lọc trạng thái (Chưa thanh toán, Thanh toán một phần, Đã thanh toán toàn bộ, Quá hạn). Biểu mẫu lập lịch thu gồm các trường: Tên đợt thu, Số tiền cần thu, Ngày hạn định thu tiền. |
| **Logic xử lý dữ liệu** | Khi một cơ hội bán hàng đạt trạng thái "Thành công", hệ thống cho phép khởi tạo lịch thu tiền. Nếu đợt thu tiền chưa hoàn thành (amount\_paid \< amount\_due) và ngày hiện tại đã vượt quá ngày hạn định, hệ thống tự động đổi trạng thái đợt thu sang "Quá hạn", đồng thời đẩy thông tin vào danh sách cảnh báo công nợ trên Dashboard. |
| **Quy tắc phân quyền** | Nhân viên Sales lập lịch thu và theo dõi đợt thu của khách hàng mình phụ trách. Trưởng nhóm và Admin kiểm soát danh sách công nợ toàn cục. |

### **14\. Chức năng: Lưu trữ dữ liệu chứng từ thanh toán bảo mật trên Supabase**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Cho phép đính kèm và lưu trữ an toàn các tệp tin chứng từ, biên lai thanh toán của khách hàng trực tiếp lên kho dữ liệu đám mây. |
| **Giao diện người dùng** | Trong giao diện chi tiết của từng đợt thanh toán, xuất hiện một khu vực bấm chọn hoặc kéo thả file chứng từ (hỗ trợ định dạng hình ảnh hoặc tệp PDF). |
| **Logic xử lý dữ liệu** | Tệp tin khi tải lên sẽ được chuyển thẳng vào một thư mục bảo mật (Bucket) riêng biệt trên Supabase Storage. Hệ thống tự động mã hóa lại tên file để tránh xung đột hệ thống. Đường dẫn tải file (URL) được cấu hình chế độ bảo mật nghiêm ngặt (Signed URL), chỉ cấp quyền xem tạm thời trong vòng 5 phút cho những tài khoản có đủ thẩm quyền dữ liệu đối với hợp đồng đó. |
| **Quy tắc phân quyền** | Nhân viên Sales có quyền tải lên chứng từ cho đợt thu mình phụ trách. Quyền bấm nút duyệt xác nhận trạng thái đợt thu sang "Đã thanh toán toàn bộ" được giới hạn riêng cho tài khoản vai trò Admin. |

## **PHÂN HỆ 6: BẢNG ĐIỀU KHIỂN TỔNG QUAN (DASHBOARD)**

### **15\. Chức năng: Tổng hợp số liệu động và Hệ thống biểu đồ hiệu suất**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Trung tâm hiển thị toàn bộ các chỉ số tài chính, vận hành kinh doanh và biểu đồ phân tích hiệu suất theo thời gian thực. |
| **Giao diện người dùng** | Màn hình gồm 4 thẻ số liệu lớn phía trên (Doanh thu thực tế, Doanh thu dự kiến, Tổng khách hàng mới, Số việc quá hạn) và 2 khối biểu đồ phía dưới (Biểu đồ hình phễu chuyển đổi quy trình bán hàng, Biểu đồ cột so sánh hiệu suất doanh số). Thanh công cụ chọn khoảng thời gian nằm trên cùng. |
| **Logic xử lý dữ liệu** | Hệ thống tự động thực hiện các câu lệnh tính toán tổng hợp (Aggregation) dữ liệu từ các phân hệ Khách hàng, Cơ hội, Thanh toán để xuất số liệu lên màn hình. Số liệu và các đường nét biểu đồ tự động thay đổi tương ứng ngay khi người dùng thay đổi bộ lọc khoảng thời gian (ví dụ: tuần này, tháng này, quý này). |
| **Quy tắc phân quyền** | Hệ thống áp dụng bộ lọc quyền từ khóa gốc: Màn hình của Sales chỉ hiện số liệu cá nhân; màn hình của Trưởng nhóm hiện tổng số liệu và biểu đồ cột so sánh giữa các nhân viên trong nhóm; màn hình của Admin hiển thị số liệu toàn công ty và biểu đồ cột so sánh doanh số giữa các nhóm kinh doanh với nhau. |

## **PHÂN HỆ 7: CÀI ĐẶT VÀ CẤU HÌNH HỆ THỐNG (DÀNH RIÊNG DÀNH CHO ADMIN)**

### **16\. Chức năng: Quản lý danh mục sản phẩm và Khóa tài khoản nhân sự**

| Thành phần đặc tả | Nội dung chi tiết |
| :---- | :---- |
| **Mô tả tổng quan** | Cấu hình các tham số vận hành hệ thống toàn cục và quản lý danh sách tài khoản nhân sự nội bộ công ty. |
| **Giao diện người dùng** | Giao diện gồm 2 tab nội dung tách biệt: Tab "Danh mục sản phẩm" hiển thị bảng danh sách các mặt hàng, đơn giá quy chuẩn; Tab "Quản lý nhân sự" hiển thị danh sách toàn bộ nhân viên công ty kèm nút thao tác "Chỉnh sửa quyền" và "Khóa tài khoản". |
| **Logic xử lý dữ liệu** | \- **Danh mục sản phẩm:** Dữ liệu sản phẩm cấu hình tại đây sẽ làm nguồn cấp dữ liệu cho tính năng gắn sản phẩm quan tâm ở hồ sơ khách hàng. \- **Quản lý nhân sự:** Khi nhân viên nghỉ việc, Admin bấm nút "Khóa tài khoản", hệ thống lập tức thay đổi trạng thái thành inactive và vô hiệu hóa toàn bộ mã Token xác thực của tài khoản đó ngay tại thời điểm thao tác. Người dùng bị khóa sẽ bị đẩy ra khỏi hệ thống ngay lập tức và không thể đăng nhập lại. Toàn bộ lịch sử dữ liệu cũ của nhân sự này được giữ nguyên vẹn trên cơ sở dữ liệu để Admin thực hiện điều phối chuyển giao cho nhân sự khác. |
| **Quy tắc phân quyền** | Phân hệ này được ẩn hoàn toàn khỏi thanh điều hướng của tài khoản Trưởng nhóm và Nhân viên Sales. Chỉ duy nhất tài khoản vai trò Admin mới có quyền truy cập và thao tác. |

### **KẾT LUẬN VÀ KHUYẾN NGHỊ HÀNH ĐỘNG**

#### **Kết luận ngắn**

Bộ tài liệu đặc tả chức năng chi tiết dạng bảng trên đã làm rõ toàn bộ các yêu cầu vận hành, cấu trúc giao diện, logic xử lý dữ liệu và cơ chế bảo mật 3 lớp cho hệ thống CRM Myan Corp Giai đoạn 1\. Việc loại bỏ các kết nối bên ngoài phức tạp giúp tài liệu này đạt được tính khả thi kỹ thuật tối đa, sẵn sàng chuyển giao cho đội ngũ phát triển xây dựng mã nguồn mà không gặp phải các điểm mờ về mặt nghiệp vụ.

#### **Khuyến nghị hành động**

1. **Phê duyệt kỹ thuật:** Ban dự án Myan Corp thực hiện ký duyệt bộ đặc tả chi tiết này để làm căn cứ kỹ thuật duy nhất cho đội ngũ lập trình triển khai xây dựng cấu trúc cơ sở dữ liệu và viết mã nguồn giao diện.  
2. **Khởi tạo môi trường Supabase:** Đội ngũ kỹ sư căn cứ trực tiếp vào phần "Logic xử lý dữ liệu" của các bảng đặc tả để tiến hành bật tính năng RLS, cấu hình các hàm liên kết định danh người dùng và thiết lập cấu trúc bảng lưu trữ dữ liệu thật trên môi trường Supabase Production.