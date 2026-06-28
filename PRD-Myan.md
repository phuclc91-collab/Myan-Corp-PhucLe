TÀI LIỆU YÊU CẦU SẢN PHẨM (PRODUCT REQUIREMENT DOCUMENT \- PRD)  
DỰ ÁN: HỆ THỐNG QUẢN TRỊ QUAN HỆ KHÁCH HÀNG (CRM) \- MYAN CORP  
GIAI ĐOẠN 1: CHUẨN HÓA NỀN TẢNG VÀ VẬN HÀNH KINH DOANH CỐT LÕI

### **1\. BỐI CẢNH VÀ MỤC TIÊU SẢN PHẨM**

#### **1.1. Bối Cảnh Kinh Doanh Hiện Tại Của Myan Corp**

Myan Corp đang bước vào giai đoạn tăng trưởng quy mô kinh doanh một cách mạnh mẽ. Lượng khách hàng tiềm năng và tệp dữ liệu đối tác tăng trưởng với tốc độ nhanh chóng đòi hỏi cấu trúc quản trị phải thay đổi toàn diện để đáp ứng yêu cầu vận hành hiện đại. Trong thời gian qua, các quy trình quản lý thông tin khách hàng tại doanh nghiệp vẫn phụ thuộc phần lớn vào các công cụ thủ công như bảng tính Excel, hệ thống ghi chú cá nhân và các ứng dụng nhắn tin rời rạc.  
Thực trạng này dẫn đến việc dữ liệu khách hàng bị phân mảnh nghiêm trọng, không có tính kế thừa khi nhân sự có sự thay đổi. Sự thiếu hụt một nền tảng quản trị tập trung khiến các bộ phận kinh doanh gặp khó khăn trong việc chia sẻ thông tin, theo dõi lịch sử tương tác và quản lý tiến độ các cơ hội bán hàng. Ngoài ra, việc lưu trữ phân tán cũng tiềm ẩn nguy cơ cao về việc rò rỉ thông tin kinh doanh cốt lõi, chồng chéo đối tượng tiếp cận giữa các nhân viên bán hàng, làm giảm trải nghiệm của khách hàng và ảnh hưởng trực tiếp đến uy tín thương hiệu của Myan Corp trên thị trường.

#### **1.2. Vấn Đề Cốt Lõi Hệ Thống CRM Cần Giải Quyết**

Hệ thống CRM giai đoạn 1 được xây dựng nhằm giải quyết triệt để các bài toán vận hành cấp bách sau:

* Xóa bỏ tình trạng cát cứ dữ liệu thông qua việc số hóa và tập trung hóa 100% hồ sơ khách hàng vào một cơ sở dữ liệu duy nhất, an toàn và có tính bảo mật cao.  
* Loại bỏ hiện tượng tranh chấp, chồng chéo khách hàng giữa các nhân viên kinh doanh bằng cơ chế phân quyền truy cập dữ liệu nghiêm ngặt theo mô hình tổ chức.  
* Khắc phục sự đứt gãy thông tin trong quy trình bán hàng bằng cách trực quan hóa các giai đoạn tiếp cận thông qua mô hình quản lý cơ hội bán hàng hiện đại.  
* Tối ưu hóa việc quản lý dòng tiền và tiến độ thanh toán của từng hợp đồng kinh doanh, giảm thiểu nợ đọng hoặc chậm trễ trong khâu đối soát tài chính.  
* Đồng nhất định danh người dùng nội bộ trên hệ thống, xử lý triệt để bài toán một nhân sự sử dụng nhiều phương thức đăng nhập khác nhau dẫn đến việc nhân bản tài khoản không kiểm soát.

#### **1.3. Mục Tiêu Chiến Lược Của Sản Phẩm**

Mục tiêu tối thượng của dự án CRM Myan Corp trong giai đoạn 1 là xây dựng một nền tảng công nghệ vững chắc, chuẩn hóa toàn bộ quy trình tương tác với khách hàng, tạo tiền đề cho các hoạt động tự động hóa và phân tích thông minh trong tương lai. Hệ thống phải đảm bảo tính dễ sử dụng để nhân viên kinh doanh sẵn sàng thích nghi, đồng thời cung cấp đầy đủ các báo cáo số liệu chính xác theo thời gian thực để Ban Giám đốc và các Trưởng nhóm đưa ra quyết định kinh doanh kịp thời.

#### **1.4. Chỉ Số Đánh Giá Hiệu Quả (KPI) Trong 90 Ngày Đầu Tiên**

Sau khi hệ thống CRM được chính thức đưa vào vận hành, sự thành công của giai đoạn 1 sẽ được đo lường bằng các chỉ số định lượng cụ thể sau trong vòng 90 ngày:

* Tỷ lệ số hóa dữ liệu: Đạt 100% khách hàng mới và toàn bộ lịch sử tương tác, giao dịch phát sinh được cập nhật đầy đủ lên hệ thống CRM, không sử dụng bảng tính cá nhân bên ngoài.  
* Mức độ áp dụng hệ thống (User Adoption Rate): Đạt tối thiểu 95% tổng số nhân viên kinh doanh thuộc các phòng ban tương tác tích cực và thực hiện báo cáo hàng ngày trên hệ thống CRM.  
* Tỷ lệ dữ liệu sạch (Data Accuracy Rate): Đảm bảo tỷ lệ trùng lặp thông tin khách hàng hoặc sai sót các trường dữ liệu cốt lõi (Số điện thoại, Email, Mã số thuế) dưới mức 2%.  
* Thời gian phản hồi khách hàng (Response Time): Giảm 35% thời gian xử lý và liên hệ lần đầu với khách hàng tiềm năng kể từ khi hệ thống tiếp nhận thông tin đầu vào.  
* Tỷ lệ chuyển đổi giai đoạn bán hàng: Tăng trưởng 15% tỷ lệ chuyển đổi từ giai đoạn tiếp cận ban đầu sang giai đoạn thương thảo hợp đồng nhờ quy trình theo dõi trực quan và nhắc nhở công việc liên tục.

### **2\. CHÂN DUNG NGƯỜI DÙNG (USER PERSONAS)**

#### **2.1. Quản Trị Viên Hệ Thống (Admin)**

* Quyền hạn tối cao: Xem, sửa, xóa toàn bộ dữ liệu trên hệ thống CRM của Myan Corp mà không bị giới hạn bởi bất kỳ bộ lọc truy cập nào.  
* Hành vi và trách nhiệm cốt lõi: Khởi tạo và quản lý tài khoản người dùng nội bộ, thiết lập vai trò (Role) và cấu hình chính sách truy cập dữ liệu cho các phòng ban. Giám sát hoạt động vận hành chung của hệ thống, xử lý các sự cố liên quan đến đồng bộ dữ liệu, nhập/xuất báo cáo tổng hợp cho Ban Giám đốc và bảo trì cấu hình danh mục sản phẩm, nhãn phân khúc khách hàng.  
* Mục tiêu trên CRM: Đảm bảo hệ thống hoạt động ổn định, dữ liệu được bảo mật tuyệt đối, việc phân quyền diễn ra chính xác theo đúng sơ đồ tổ chức của doanh nghiệp và không có tài khoản rác hoặc tài khoản bị trùng lặp định danh.

#### **2.2. Trưởng Nhóm Kinh Doanh (Team Lead)**

* Quyền hạn mở rộng theo phạm vi: Xem và quản lý toàn bộ dữ liệu khách hàng, các cơ hội bán hàng, tiến độ công việc và dòng tiền thanh toán thuộc phạm vi phụ trách của tất cả các nhân viên nằm trong nhóm do mình quản lý. Hoàn toàn không có quyền xem hoặc can thiệp vào dữ liệu của các đội nhóm kinh doanh khác trên hệ thống.  
* Hành vi và trách nhiệm cốt lõi: Theo dõi bảng điều khiển để đánh giá hiệu suất làm việc của từng nhân viên dưới quyền. Điều phối, phân bổ khách hàng tiềm năng cho các nhân viên bán hàng một cách hợp lý. Duyệt các đề xuất kinh doanh, hỗ trợ nhân viên giải quyết các điểm nghẽn trong quá trình thương thảo hợp đồng trên bảng Kanban. Đánh giá tỷ lệ đạt KPI doanh số của nhóm để báo cáo lên Ban Giám đốc.  
* Mục tiêu trên CRM: Nắm bắt chính xác năng suất làm việc của đội ngũ theo thời gian thực, phát hiện sớm các cơ hội bán hàng có rủi ro thất bại để can thiệp kịp thời, đảm bảo nhóm hoàn thành chỉ tiêu doanh số được giao.

#### **2.3. Nhân Viên Kinh Doanh (Sales Representative)**

* Quyền hạn giới hạn cá nhân: Chỉ có quyền xem, thêm mới, chỉnh sửa và quản lý các dữ liệu khách hàng, cơ hội bán hàng, danh sách công việc và thông tin thanh toán do chính tài khoản của mình tạo ra hoặc được Trưởng nhóm/Admin phân phối chỉ định phụ trách. Tuyệt đối không thể nhìn thấy bất kỳ thông tin nào của đồng nghiệp khác trên hệ thống.  
* Hành vi và trách nhiệm cốt lõi: Tiếp nhận thông tin khách hàng tiềm năng được phân bổ, thực hiện các hoạt động gọi điện, gửi email, gặp gỡ và ghi chú chi tiết lịch sử tương tác lên CRM. Cập nhật tiến độ cơ hội bán hàng bằng thao tác kéo thả trên bảng Kanban. Lập lịch công việc, thời hạn chăm sóc và theo dõi tiến độ thanh toán của khách hàng nhằm thúc đẩy quá trình nghiệm thu, quyết toán hợp đồng.  
* Mục tiêu trên CRM: Quản lý công việc hàng ngày một cách khoa học, không bỏ sót khách hàng, rút ngắn chu kỳ bán hàng và tối đa hóa doanh số cá nhân để đạt được các mức thưởng hiệu suất.

### **3\. DANH SÁCH VÀ MÔ TẢ CHI TIẾT CÁC PHÂN HỆ (MODULES)**

#### **3.1. Phân Hệ Tổng Quan (Dashboard)**

Phân hệ Tổng quan là màn hình đầu tiên hiển thị sau khi người dùng đăng nhập thành công, đóng vai trò cung cấp một cái nhìn toàn diện, trực quan và cô đọng nhất về toàn bộ hoạt động kinh doanh của Myan Corp dựa trên phạm vi phân quyền của từng tài khoản.

##### **3.1.1. Các Khối Số Liệu Cốt Lõi (Key Metrics Cards)**

Giao diện phía trên cùng của Dashboard bao gồm các thẻ số liệu động hiển thị các chỉ số tài chính và vận hành quan trọng:

* Doanh thu thực tế: Tổng số tiền đã thu được từ các hóa đơn/đợt thanh toán có trạng thái Đã thanh toán thành công trong chu kỳ thời gian được chọn.  
* Doanh thu dự kiến: Tổng giá trị của các cơ hội bán hàng đang nằm trong quy trình thương thảo (tính bằng cách lấy tổng giá trị các cơ hội nhân với tỷ lệ thành công dự kiến của từng giai đoạn tương ứng).  
* Tổng số khách hàng mới: Số lượng hồ sơ khách hàng được khởi tạo mới trên hệ thống trong khoảng thời gian truy vấn.  
* Tỷ lệ chuyển đổi cơ hội: Phần trăm các cơ hội bán hàng chuyển dịch thành công từ giai đoạn tiếp cận ban đầu đến khi chốt hợp đồng.

##### **3.1.2. Hệ Thống Biểu Đồ Trực Quan**

* Biểu đồ đường (Line Chart) xu hướng doanh thu: Hiển thị dòng tiền thực tế thu được theo từng mốc thời gian (ngày, tuần, tháng) nhằm giúp nhà quản trị đánh giá tốc độ tăng trưởng tài chính.  
* Biểu đồ hình phễu (Funnel Chart) chuyển đổi cơ hội bán hàng: Minh họa trực quan số lượng và tỷ lệ sụt giảm của các cơ hội bán hàng qua từng bước trong quy trình Pipeline (Tiếp cận, Tư vấn, Báo giá, Thương thảo, Thành công). Điều này giúp phát hiện ngay giai đoạn nào đang gặp tắc nghẽn.  
* Biểu đồ cột (Bar Chart) hiệu suất đội ngũ: So sánh doanh số thực tế giữa các phòng ban (đối với tài khoản Admin) hoặc giữa các cá nhân trong cùng một đội nhóm (đối với tài khoản Trưởng nhóm).

#### **3.2. Phân Hệ Danh Sách Khách Hàng (Customer Directory)**

Đây là phân hệ lưu trữ cốt lõi của hệ thống CRM Myan Corp, chịu trách nhiệm quản lý toàn bộ vòng đời thông tin của khách hàng từ lúc còn là đối tác tiềm năng cho đến khi trở thành khách hàng trung thành.

##### **3.2.1. Chức Năng Thêm, Sửa, Xóa Khách Hàng**

* Thêm mới khách hàng: Cho phép người dùng khởi tạo thủ công một hồ sơ khách hàng mới thông qua một biểu mẫu giao diện chuẩn hóa. Giao diện yêu cầu nhập đầy đủ thông tin bắt buộc và kiểm tra tính hợp lệ về mặt định dạng (ví dụ: số điện thoại phải đủ chữ số, email phải đúng cấu trúc chuẩn).  
* Chỉnh sửa khách hàng: Người dùng có thẩm quyền có thể bấm vào hồ sơ để thay đổi thông tin. Hệ thống tự động ghi nhận lịch sử chỉnh sửa bao gồm định danh người sửa và mốc thời gian chính xác để phục vụ công tác tra cứu, hậu kiểm dữ liệu.  
* Xóa khách hàng: Tính năng xóa hồ sơ khách hàng được kiểm soát nghiêm ngặt. Để tránh mất mát dữ liệu do sơ suất, hệ thống áp dụng cơ chế xóa mềm (Soft Delete \- chuyển trạng thái vào thùng rác nội bộ và chỉ có Admin mới có quyền xóa vĩnh viễn khỏi cơ sở dữ liệu Supabase).

##### **3.2.2. Gắn Nhãn Phân Khúc Khách Hàng**

Hệ thống cung cấp cơ chế phân loại khách hàng linh hoạt bằng hệ thống nhãn (Tagging System) cố định, bao gồm ba phân khúc chính:

* Khách lẻ: Dành cho các khách hàng cá nhân, quy mô giao dịch nhỏ, chu kỳ mua hàng ngắn và quy trình ra quyết định đơn giản.  
* Đại lý: Dành cho các tổ chức, đối tác phân phối hoặc các đơn vị mua sắm với số lượng lớn, có các chính sách chiết khấu thương mại và ràng buộc hợp đồng dài hạn.  
* VIP: Phân khúc khách hàng đặc biệt quan trọng, mang lại giá trị doanh thu lớn cho Myan Corp, đòi hỏi quy trình chăm sóc chuyên biệt và chế độ hậu mãi cao cấp nhất.

##### **3.2.3. Gắn Sản Phẩm Quan Tâm**

Trong hồ sơ khách hàng, nhân viên kinh doanh có thể lựa chọn một hoặc nhiều sản phẩm/dịch vụ từ danh mục cấu hình sẵn của Myan Corp để gắn vào mục Sản phẩm quan tâm. Việc này giúp doanh nghiệp hiểu rõ xu hướng nhu cầu của thị trường, hỗ trợ nhân viên sales chuẩn bị tài liệu tư vấn trúng đích và phục vụ cho các chiến dịch tiếp thị bán chéo (Cross-selling) ở các giai đoạn tiếp theo.

##### **3.2.4. Tải Lên Danh Sách Khách Hàng Từ Tập Tin CSV (Bulk Import)**

* Cho phép người dùng tải lên hàng loạt hàng ngàn thông tin khách hàng từ một tập tin định dạng CSV theo biểu mẫu tiêu chuẩn hệ thống cung cấp.  
* Hệ thống sẽ thực hiện một quy trình quét kiểm tra dữ liệu trước khi nạp (Pre-validation process). Nếu phát hiện bất kỳ dòng dữ liệu nào sai định dạng hoặc bị trùng lặp Số điện thoại/Email với dữ liệu đã tồn tại trên Supabase, hệ thống sẽ dừng tiến trình và trả về một báo cáo lỗi chi tiết chỉ rõ số dòng và lỗi cụ thể để người dùng chỉnh sửa trước khi thử lại.

##### **3.2.5. Xuất Danh Sách Khách Hàng Ra Tập Tin CSV (Bulk Export)**

* Hỗ trợ kết xuất toàn bộ hoặc một phần danh sách khách hàng (dựa trên bộ lọc tìm kiếm hiện tại) ra tập tin CSV.  
* Tính năng này được kiểm soát chặt chẽ bằng quyền dữ liệu. Nhân viên sales chỉ xuất được danh sách do mình phụ trách, Trưởng nhóm xuất được danh sách của nhóm, Admin xuất được toàn bộ dữ liệu hệ thống. Mọi hành động xuất dữ liệu đều được lưu nhật ký hệ thống (Audit Log) để ngăn chặn hành vi đánh cắp tài nguyên của doanh nghiệp.

#### **3.3. Phân Hệ Cơ Hội Bán Hàng Với Bảng Kanban Kéo Thả (Sales Pipeline Kanban)**

Phân hệ này trực quan hóa toàn bộ hành trình chuyển đổi một khách hàng tiềm năng thành một giao dịch thành công. Giao diện được thiết kế theo dạng các cột tương ứng với các trạng thái kinh doanh, các cơ hội bán hàng hiển thị dưới dạng các thẻ thông tin (Cards).

##### **3.3.1. Các Giai Đoạn Trong Quy Trình Bán Hàng (Pipeline Stages)**

Bảng Kanban của Myan Corp được cấu hình cố định gồm 5 cột quy trình chuẩn mực:

* Tiếp cận: Khách hàng mới được khởi tạo hoặc phân bổ về, nhân viên đang trong quá trình thực hiện các cuộc gọi, email giới thiệu đầu tiên.  
* Tư vấn: Đã thiết lập được liên lạc, nhân viên sales đang đi sâu vào khai thác nhu cầu thực tế và tư vấn giải pháp phù hợp cho đối tác.  
* Báo giá: Doanh nghiệp đã gửi bảng báo giá chi tiết và các phương án tài chính cho khách hàng xem xét.  
* Thương thảo: Giai đoạn đàm phán sâu về các điều khoản hợp đồng, chính sách giảm giá, thời hạn thanh toán và cam kết dịch vụ.  
* Thành công: Hợp đồng chính thức được ký kết, cơ hội đóng lại với kết quả tích cực, chuẩn bị chuyển giao cho bộ phận vận hành và kế toán tài chính.

##### **3.3.2. Cơ Chế Tương Tác Kéo Thả Trực Quan**

* Nhân viên kinh doanh có thể dịch chuyển trạng thái của một cơ hội bán hàng bằng cách bấm giữ và kéo thẻ thông tin từ cột này sang cột khác trên giao diện chuột hoặc màn hình cảm ứng.  
* Khi một thẻ được thả vào cột mới, hệ thống tự động cập nhật trường trạng thái của cơ hội đó trong cơ sở dữ liệu Supabase theo thời gian thực, đồng thời tính toán lại tổng giá trị tiền tệ của cột nguồn và cột đích ngay lập tức mà không cần tải lại toàn bộ trang web.  
* Khi kéo một thẻ vào cột Thành công, hệ thống bắt buộc người dùng phải cập nhật tổng giá trị hợp đồng chính thức và tự động tạo ra một nhắc nhở liên kết sang phân hệ Thanh toán.

#### **3.4. Phân Hệ Quản Lý Công Việc (Task Management)**

Phân hệ này đóng vai trò như một trợ lý nhắc việc thông minh cho đội ngũ nhân sự của Myan Corp, đảm bảo mọi cam kết với khách hàng đều được thực hiện đúng thời hạn.

##### **3.4.1. Tạo Và Quản Lý Nhiệm Vụ Liên Kết**

* Mỗi nhân viên kinh doanh có thể tạo ra các đầu việc cụ thể (ví dụ: Gọi điện lại cho khách hàng A, Gửi bản thảo hợp đồng cho đối tác B, Đi gặp khách hàng VIP C).  
* Mọi nhiệm vụ bắt buộc phải liên kết trực tiếp với một hồ sơ khách hàng cụ thể hoặc một cơ hội bán hàng cụ thể trên hệ thống để đảm bảo tính mạch lạc của dữ liệu.

##### **3.4.2. Quản Lý Trạng Thái Và Mức Độ Ưu Tiên**

* Trạng thái công việc bao gồm: Chưa thực hiện, Đang xử lý, Đã hoàn thành, Hoàn thành muộn.  
* Mức độ ưu tiên được phân chia rõ ràng: Cao, Trung bình, Thấp. Hệ thống sẽ tự động gửi thông báo đẩy trên giao diện web hoặc tô màu cảnh báo đối với các công việc có mức độ ưu tiên Cao và sắp đến ngày hết hạn (Due Date) nhưng chưa được chuyển trạng thái sang Đã hoàn thành.

#### **3.5. Phân Hệ Quản Lý Thanh Toán (Payment Tracking)**

Quản lý tài chính và dòng tiền chặt chẽ là yếu tố sống còn đối với hoạt động của Myan Corp. Phân hệ Thanh toán trong CRM phối hợp chặt chẽ với quy trình bán hàng để theo dõi các giai đoạn thu tiền của từng hợp đồng.

##### **3.5.1. Theo Dõi Tiến Độ Thanh Toán Theo Giai Đoạn**

Đối với các hợp đồng có giá trị lớn hoặc quy định chia nhỏ nghĩa vụ tài chính thành nhiều đợt (ví dụ: Tạm ứng 30%, Thanh toán đợt hai 40%, Nghiệm thu quyết toán 30%), phân hệ này cho phép lập lịch thu tiền cụ thể cho từng đợt bao gồm Số tiền cần thu và Ngày hạn định thu tiền.

##### **3.5.2. Quản Lý Trạng Đơn Hàng Và Hóa Đơn**

* Các trạng thái thanh toán được cập nhật rõ ràng: Chưa thanh toán, Đã thanh toán một phần, Đã thanh toán toàn bộ, Quá hạn thanh toán.  
* Hệ thống hiển thị danh sách các đợt thanh toán sắp đến hạn trong tuần hoặc trong tháng để nhân viên kinh doanh chủ động liên hệ nhắc nợ khách hàng, tránh việc phát sinh nợ xấu hoặc làm chậm tiến độ dòng tiền của công ty.

#### **3.6. Phân Hệ Cài Đặt Hệ Thống (System Settings)**

Môi trường quản trị dành riêng cho tài khoản Admin nhằm thiết lập các tham số vận hành hệ thống toàn cục.

* Quản lý danh mục: Cho phép thêm, sửa, cấu hình danh sách sản phẩm của Myan Corp, định nghĩa các nhãn phân khúc khách hàng.  
* Quản lý tài khoản: Màn hình hiển thị toàn bộ danh sách nhân sự trong công ty. Admin có thể tạo tài khoản mới, cấp mật khẩu ban đầu, thay đổi vai trò công tác của nhân sự (từ Nhân viên lên Trưởng nhóm) hoặc thực hiện khóa tài khoản ngay lập tức khi nhân sự nghỉ việc để bảo vệ dữ liệu tối mật.

### **4\. LUỒNG TRẢI NGHIỆM NGƯỜI DÙNG CHÍNH (USER FLOWS)**

#### **4.1. Luồng Đăng Nhập Và Hợp Nhất Tài Khoản Trùng Email**

Luồng xử lý này đảm bảo trải nghiệm đăng nhập thông suốt của người dùng trong khi vẫn duy trì tính duy nhất của hồ sơ dữ liệu bảo mật nội bộ.

1. Người dùng truy cập trang đăng nhập của hệ thống CRM Myan Corp.  
2. Người dùng lựa chọn một trong hai hình thức xác thực: Nhập Email \+ Mật khẩu thủ công, hoặc click vào nút Đăng nhập bằng tài khoản Google (Google OAuth).  
3. Hệ thống tiếp nhận thông tin xác thực từ phía client gửi lên.  
4. Hệ thống tiến hành kiểm tra trường Email trong cơ sở dữ liệu xác thực của Supabase.  
5. Nếu Email này chưa từng tồn tại trên hệ thống: Hệ thống thực hiện quy trình khởi tạo một hồ sơ người dùng mới trong bảng Profiles, mặc định gán vai trò có cấp độ thấp nhất (Nhân viên sales) và chuyển hướng vào màn hình cập nhật thông tin cá nhân.  
6. Nếu Email này đã tồn tại trong cơ sở dữ liệu từ trước nhưng được tạo bởi phương thức đăng nhập khác (ví dụ: Tài khoản do SQL khởi tạo sẵn trước đó, bây giờ người dùng chọn đăng nhập bằng Google OAuth): Hệ thống không tạo hồ sơ mới. Cơ chế kích hoạt hàm Trigger trên cơ sở dữ liệu Supabase sẽ thực hiện liên kết phương thức xác thực mới này vào UID (User ID) hiện tại của người dùng.  
7. Hồ sơ định danh cá nhân, mã phân quyền (Role) và toàn bộ quyền truy cập dữ liệu cũ gắn liền với Email đó được giữ nguyên vẹn hoàn toàn.  
8. Hệ thống cấp mã Token xác thực hợp lệ và chuyển hướng người dùng vào màn hình Dashboard phù hợp với phân quyền của họ.

#### **4.2. Luồng Vận Hành Cơ Hội Bán Hàng Trên Bảng Kanban**

1. Nhân viên kinh doanh truy cập vào Phân hệ Cơ hội bán hàng (Sales Pipeline). Hệ thống mặc định tải giao diện dạng bảng Kanban trực quan.  
2. Nhân viên chọn xem một thẻ cơ hội bán hàng hiện có để xem nhanh tóm tắt thông tin (Tên khách hàng, Giá trị dự kiến, Ngày cập nhật cuối cùng).  
3. Nhân viên thực hiện hành động tương tác: Nhấp và giữ thẻ, di chuyển thẻ theo chiều ngang từ cột trạng thái hiện tại (ví dụ: Báo giá) sang cột trạng thái tiếp theo (ví dụ: Thương thảo) và thả chuột.  
4. Trình duyệt gửi một yêu cầu API bất đồng bộ (Asynchronous API Request) về phía Backend của Supabase để cập nhật trạng thái mới của cơ hội bán hàng.  
5. Cơ sở dữ liệu lưu trữ thành công trạng thái mới. Hệ thống tự động ghi nhận một dòng nhật ký hệ thống ghi rõ: "Cơ hội X đã được chuyển từ giai đoạn Báo giá sang giai đoạn Thương thảo bởi Người dùng Y vào lúc Z".  
6. Giao diện frontend cập nhật lại số liệu tổng giá trị tiền tệ của cả hai cột liên quan mà không làm gián đoạn trải nghiệm người dùng trên màn hình làm việc.

#### **4.3. Luồng Nhập Liệu Khách Hàng Hàng Loạt Từ Tập Tin CSV**

1. Người dùng có thẩm quyền (Admin hoặc Trưởng nhóm) truy cập phân hệ Danh sách khách hàng và nhấn chọn chức năng Tải lên từ CSV.  
2. Hệ thống hiển thị một cửa sổ thông báo yêu cầu người dùng chọn file và cung cấp liên kết tải xuống tệp tin CSV mẫu có cấu trúc chuẩn của Myan Corp.  
3. Người dùng chọn tệp tin CSV từ máy tính cá nhân và nhấn nút Thực hiện tải lên.  
4. Hệ thống tại phía client đọc tệp dữ liệu và thực hiện bước kiểm tra cú pháp sơ bộ (Client-side validation).  
5. Tệp tin được đẩy lên bộ xử lý trung tâm. Hệ thống phân tích từng dòng dữ liệu và thực hiện đối chiếu kiểm tra tính hợp lệ sâu (Deep validation): Kiểm tra tính bắt buộc của các trường Tên, Số điện thoại; Kiểm tra xem Số điện thoại hoặc Email có bị trùng lặp với dữ liệu thực tế đang lưu trong cơ sở dữ liệu Supabase hay không.  
6. Trường hợp phát hiện lỗi dữ liệu: Hệ thống lập tức hủy bỏ toàn bộ tiến trình nhập liệu (Rollback transaction) để bảo vệ tính toàn vẹn của database, đồng thời xuất ra một thông báo lỗi màu đỏ kèm theo danh sách chi tiết các dòng bị lỗi và nguyên nhân cụ thể để người dùng biết cách xử lý.  
7. Trường hợp toàn bộ dữ liệu hợp lệ: Hệ thống thực hiện ghi hàng loạt (Bulk Insert) dữ liệu vào cơ sở dữ liệu Supabase, tự động gán trường Người tạo chính là tài khoản đang thực hiện tác vụ và thông báo số lượng hồ sơ đã được số hóa thành công lên màn hình.

### **5\. CẤU TRÚC DỮ LIỆU CHI TIẾT (DATA FIELDS)**

Dưới đây là thiết kế chi tiết các bảng dữ liệu cốt lõi sẽ được triển khai trên nền tảng Supabase cho giai đoạn 1 của dự án CRM Myan Corp.

#### **5.1. Bảng Thông Tin Người Dùng (Profiles)**

Bảng này lưu trữ thông tin định danh và phân quyền của toàn bộ nhân sự thuộc Myan Corp sử dụng hệ thống CRM.

| Tên trường dữ liệu | Kiểu dữ liệu | Ràng buộc | Mô tả chức năng |
| :---- | :---- | :---- | :---- |
| id | uuid | Primary Key, references auth.users | Mã định danh duy nhất của người dùng, liên kết trực tiếp với phân hệ xác thực của Supabase. |
| email | varchar(255) | Unique, Not Null | Địa chỉ email chính thức của nhân sự dùng để đăng nhập và nhận thông tin từ hệ thống. |
| full\_name | varchar(255) | Not Null | Họ và tên đầy đủ của nhân sự. |
| role | varchar(50) | Not Null | Vai trò trên hệ thống, nhận một trong ba giá trị cố định: admin, manager, sales. |
| team\_id | uuid | Foreign Key | Mã định danh nhóm kinh doanh mà nhân sự này đang thuộc về (bỏ trống nếu là Admin). |
| status | varchar(50) | Not Null, Default 'active' | Trạng thái tài khoản trên hệ thống, bao gồm các giá trị: active (hoạt động), inactive (bị khóa). |
| created\_at | timestamptz | Default now() | Mốc thời gian tài khoản người dùng được khởi tạo trên hệ thống. |

#### **5.2. Bảng Danh Sách Khách Hàng (Customers)**

Bảng lưu trữ thông tin chi tiết về các đối tác, khách hàng của doanh nghiệp.

| Tên trường dữ liệu | Kiểu dữ liệu | Ràng buộc | Mô tả chức năng |
| :---- | :---- | :---- | :---- |
| id | uuid | Primary Key | Mã định danh duy nhất của mỗi hồ sơ khách hàng. |
| name | varchar(255) | Not Null | Tên của khách hàng cá nhân hoặc tên người đại diện tổ chức. |
| company\_name | varchar(255) | Nullable | Tên công ty hoặc tổ chức đối tác (dành cho khách hàng doanh nghiệp). |
| phone | varchar(20) | Unique, Not Null | Số điện thoại liên hệ chính thức, dùng làm trường khóa để kiểm tra trùng lặp dữ liệu. |
| email | varchar(255) | Unique, Nullable | Địa chỉ email của khách hàng phục vụ gửi tài liệu, báo giá. |
| segment | varchar(50) | Not Null, Default 'khach\_le' | Phân khúc khách hàng, nhận các giá trị cố định: khach\_le, dai\_ly, vip. |
| interested\_products | text\[\] | Nullable | Mảng chứa danh sách các mã sản phẩm dịch vụ mà khách hàng đang thể hiện sự quan tâm. |
| assigned\_to | uuid | Foreign Key, references profiles.id | Mã định danh của nhân viên kinh doanh được giao chịu trách nhiệm chăm sóc trực tiếp khách hàng này. |
| created\_by | uuid | Foreign Key, references profiles.id | Mã định danh của nhân sự thực hiện hành động tạo hồ sơ khách hàng lên hệ thống. |
| notes | text | Nullable | Các ghi chú đặc biệt về đặc điểm, thói quen hoặc yêu cầu riêng biệt của khách hàng. |
| is\_deleted | boolean | Not Null, Default false | Trường đánh dấu trạng thái xóa mềm phục vụ quản trị an toàn dữ liệu. |
| created\_at | timestamptz | Default now() | Thời gian hồ sơ khách hàng được đưa vào hệ thống CRM. |

#### **5.3. Bảng Cơ Hội Bán Hàng (Opportunities)**

Bảng theo dõi các thương vụ kinh doanh đang được triển khai với khách hàng.

| Tên trường dữ liệu | Kiểu dữ liệu | Ràng buộc | Mô tả chức năng |
| :---- | :---- | :---- | :---- |
| id | uuid | Primary Key | Mã định danh duy nhất của một cơ hội bán hàng. |
| customer\_id | uuid | Foreign Key, references customers.id | Liên kết trực tiếp cơ hội này với một khách hàng cụ thể trong cơ sở dữ liệu. |
| title | varchar(255) | Not Null | Tên gọi gợi nhớ của cơ hội bán hàng (ví dụ: Hợp đồng cung ứng thiết bị quý 3). |
| stage | varchar(50) | Not Null, Default 'tiep\_can' | Giai đoạn hiện tại trên Kanban, nhận các giá trị: tiep\_can, tu van, bao\_gia, thuong\_thao, thanh\_cong. |
| expected\_value | numeric(15,2) | Not Null, Default 0 | Giá trị tiền tệ dự kiến của thương vụ bán hàng này. |
| actual\_value | numeric(15,2) | Nullable | Giá trị hợp đồng chính thức được ký kết khi chuyển sang trạng thái thành công. |
| probability | integer | Not Null | Tỷ lệ phần trăm thành công dự kiến tương ứng với từng giai đoạn phục vụ tính toán doanh thu dự kiến trên Dashboard. |
| closed\_at | timestamptz | Nullable | Thời điểm thương vụ kết thúc (thành công hoặc thất bại). |
| created\_at | timestamptz | Default now() | Ngày khởi tạo cơ hội bán hàng. |

#### **5.4. Bảng Quản Lý Công Việc (Tasks)**

Bảng lưu trữ danh sách các tác vụ chăm sóc khách hàng của đội ngũ sales.

| Tên trường dữ liệu | Kiểu dữ liệu | Ràng buộc | Mô tả chức năng |
| :---- | :---- | :---- | :---- |
| id | uuid | Primary Key | Mã định danh duy nhất của nhiệm vụ. |
| customer\_id | uuid | Foreign Key, references customers.id | Liên kết nhiệm vụ này với hồ sơ một khách hàng cụ thể. |
| opportunity\_id | uuid | Foreign Key, references opportunities.id | Liên kết trực tiếp với cơ hội bán hàng liên quan (nếu có). |
| title | varchar(255) | Not Null | Tiêu đề ngắn gọn mô tả đầu việc cần làm. |
| description | text | Nullable | Mô tả chi tiết các bước cần thực hiện hoặc nội dung cần trao đổi. |
| due\_date | timestamptz | Not Null | Hạn chót bắt buộc phải hoàn thành nhiệm vụ được giao. |
| priority | varchar(50) | Not Null, Default 'trung\_binh' | Mức độ cấp thiết của công việc: cao, trung\_binh, thap. |
| status | varchar(50) | Not Null, Default 'chua\_lam' | Trạng thái tiến độ: chua\_lam, dang\_lam, da\_xong, qua\_han. |
| assigned\_to | uuid | Foreign Key, references profiles.id | Người chịu trách nhiệm thực thi nhiệm vụ này. |
| created\_at | timestamptz | Default now() | Ngày tạo nhiệm vụ nhắc việc trên hệ thống. |

#### **5.5. Bảng Quản Lý Thanh Toán (Payments)**

Bảng theo dõi dòng tiền và tiến độ thanh toán của các hợp đồng.

| Tên trường dữ liệu | Kiểu dữ liệu | Ràng buộc | Mô tả chức năng |
| :---- | :---- | :---- | :---- |
| id | uuid | Primary Key | Mã định danh duy nhất của đợt thanh toán / hóa đơn. |
| opportunity\_id | uuid | Foreign Key, references opportunities.id | Liên kết đợt thanh toán với thương vụ bán hàng thành công tương ứng. |
| amount\_due | numeric(15,2) | Not Null | Số tiền cụ thể cần phải thu trong đợt thanh toán này theo điều khoản hợp đồng. |
| amount\_paid | numeric(15,2) | Default 0 | Số tiền thực tế khách hàng đã chuyển khoản và được xác nhận thành công. |
| payment\_stage | varchar(100) | Not Null | Tên gọi của đợt thanh toán (ví dụ: Tạm ứng đợt 1, Thanh toán quyết toán đợt cuối). |
| due\_date | timestamptz | Not Null | Ngày hạn định cuối cùng khách hàng phải thực hiện nghĩa vụ thanh toán đợt này. |
| status | varchar(50) | Not Null, Default 'chua\_thanh\_toan' | Trạng thái: chua\_thanh\_toan, thanh\_toan\_mot\_phan, da\_thanh\_toan, qua\_han. |
| paid\_at | timestamptz | Nullable | Thời điểm chính thức nhận được tiền từ khách hàng. |
| created\_at | timestamptz | Default now() | Thời gian khởi tạo đợt thu tiền trên hệ thống CRM. |

### **6\. QUY TẮC PHÂN QUYỀN VÀ CHÍNH SÁCH TRUY CẬP DỮ LIỆU**

Hệ thống CRM Myan Corp áp dụng mô hình kiểm soát truy cập dựa trên vai trò kết hợp kiểm soát dữ liệu theo cấp bậc (Hierarchical Row-Level Security) một cách chặt chẽ. Quyền hạn xử lý dữ liệu được quy định cụ thể thông qua ma trận chức năng dưới đây:

#### **6.1. Ma Trận Phân Quyền Chức Năng Hệ Thống**

| Vai Trò (Role) | Module Khách Hàng | Module Kanban | Module Công Việc | Module Thanh Toán | Module Cài Đặt |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Admin** | Toàn quyền (Thêm, Sửa, Xóa mềm, Xem toàn công ty, Import/Export toàn bộ dữ liệu). | Toàn quyền (Tạo, Xem, Xóa, Dịch chuyển tất cả cơ hội bán hàng trên toàn hệ thống). | Toàn quyền (Giao việc, Theo dõi và Cập nhật trạng thái công việc của mọi nhân sự). | Toàn quyền (Tạo đợt thu, Xác nhận thanh toán, Xem toàn bộ dòng tiền của công ty). | Toàn quyền (Quản lý cấu hình danh mục sản phẩm, Phân quyền tài khoản, Khóa user). |
| **Trưởng Nhóm** | Quyền phạm vi nhóm (Thêm, Sửa, Xem dữ liệu của các nhân viên trong nhóm, Export dữ liệu nhóm). Tuyệt đối không có quyền Xóa. | Quyền phạm vi nhóm (Xem, Tạo, Dịch chuyển trạng thái các thẻ cơ hội thuộc thành viên trong nhóm mình). | Quyền phạm vi nhóm (Tạo công việc, Giao việc cho nhân viên trong nhóm, Giám sát tiến độ công việc của nhóm). | Quyền phạm vi nhóm (Xem tiến độ thanh toán của các hợp đồng do nhóm mình thực hiện, không có quyền xóa đợt thu). | Không có quyền truy cập (Giao diện bị ẩn hoặc hiển thị thông báo từ chối truy cập). |
| **Nhân Viên Sales** | Quyền cá nhân (Thêm, Sửa, Xem các khách hàng do mình tạo hoặc được chỉ định phụ trách, Export dữ liệu cá nhân). | Quyền cá nhân (Xem, Tạo, Tương tác kéo thả các thẻ cơ hội do mình phụ trách). | Quyền cá nhân (Tự tạo việc, Thực hiện và Cập nhật trạng thái các công việc được giao). | Quyền cá nhân (Theo dõi lịch sử đợt thu và cập nhật số tiền đề xuất xác nhận cho khách hàng mình phụ trách). | Không có quyền truy cập (Giao diện bị ẩn hoàn toàn khỏi thanh điều hướng thanh thực đơn). |

#### **6.2. Cơ Chế Bảo Mật Dữ Liệu Mức Dòng (Row-Level Security \- RLS) Trên Supabase**

Để đảm bảo nhân viên không thể phá vỡ quy tắc phân quyền bằng cách thay đổi mã script hoặc gọi trực tiếp API từ phía client, toàn bộ các bảng dữ liệu trên Supabase (Customers, Opportunities, Tasks, Payments) đều bắt buộc phải kích hoạt tính năng Row-Level Security (RLS). Các chính sách bảo mật (RLS Policies) được cấu hình bằng ngôn ngữ PL/pgSQL như sau:

* Chính sách đối với vai trò Admin: auth.uid() IN (SELECT id FROM profiles WHERE role \= 'admin') \-\> Cho phép thực hiện tất cả các thao tác SELECT, INSERT, UPDATE, DELETE trên mọi dòng dữ liệu.  
* Chính sách đối với vai trò Trưởng nhóm (Manager): Cho phép thực hiện các thao tác SELECT, INSERT, UPDATE trên các dòng dữ liệu thỏa mãn điều kiện nhân viên phụ trách thuộc cùng một nhóm kinh doanh: assigned\_to IN (SELECT id FROM profiles WHERE team\_id \= (SELECT team\_id FROM profiles WHERE id \= auth.uid())).  
* Chính sách đối với vai trò Nhân viên Sales: Chỉ cho phép thao tác trên các dòng dữ liệu mà mã định danh trùng khớp hoàn toàn với tài khoản đang đăng nhập: assigned\_to \= auth.uid().

### **7\. YÊU CẦU GIAO DIỆN VÀ PHONG CÁCH THIẾT KẾ (UI/UX)**

#### **7.1. Định Hướng Thẩm Mỹ Và Màu Sắc Chủ Đạo**

Giao diện của ứng dụng web CRM Myan Corp phải tuân thủ nghiêm ngặt tính chuyên nghiệp, hiện đại, tối giản và tập trung cao độ vào khả năng hiển thị dữ liệu rõ ràng, dễ đọc.

* Màu sắc chủ đạo (Primary Color): Sử dụng màu xanh dương đậm (Deep Blue, mã màu dự kiến \#1E3A8A hoặc tương đương) để thể hiện sự chuẩn mực, tin cậy và vững chắc của một hệ thống quản trị doanh nghiệp. Màu chủ đạo được áp dụng cho thanh điều hướng chính, các nút hành động quan trọng và tiêu đề phân hệ lớn.  
* Màu sắc bổ trợ (Secondary/Accent Color): Sử dụng màu xám sáng hoặc xanh nhạt cho các vùng nền nội dung nhằm tạo độ tương phản dịu mắt, giảm mỏi mắt cho nhân viên khi phải thao tác liên tục nhiều giờ liền. Các trạng thái cảnh báo sử dụng màu sắc chuẩn mực: Màu xanh lá cho trạng thái hoàn thành/thành công, Màu vàng cho trạng thái đang xử lý/chờ duyệt, Màu đỏ cho trạng thái quá hạn/thất bại.  
* Không sử dụng các biểu tượng đồ họa (icon) trang trí tự do hoặc các ký hiệu cảm xúc (emoji) trong văn bản tài liệu và giao diện cấu trúc để đảm bảo tính trang trọng, chuẩn mực cao nhất của môi trường cơ quan doanh nghiệp. Các nút bấm và thanh thực đơn sử dụng nhãn chữ hiển thị rõ ràng, trực diện với chức năng tương ứng.

#### **7.2. Bố Cục Giao Diện Tổng Thể (Layout Architecture)**

Hệ thống CRM áp dụng cấu trúc bố cục hai khối cố định chuẩn mực:

* Thanh điều hướng bên trái (Sidebar Navigation): Nằm cố định ở rìa trái màn hình, chứa danh sách chữ liên kết trực tiếp đến 6 phân hệ cốt lõi gồm: Tổng quan, Danh sách khách hàng, Cơ hội bán hàng, Quản lý công việc, Quản lý thanh toán, Cài đặt hệ thống. Thanh điều hướng này có thể thu gọn lại để tối ưu hóa không gian làm việc hiển thị trên các thiết bị có màn hình nhỏ.  
* Vùng hiển thị nội dung trung tâm (Main Content Area): Chiếm toàn bộ không gian còn lại của màn hình, hiển thị nội dung chi tiết của phân hệ đang được chọn. Phía trên cùng của vùng này luôn có một thanh công cụ chứa thông tin tài khoản đang đăng nhập, nút Đăng xuất và bộ lọc khoảng thời gian áp dụng toàn cục cho trang dữ liệu.

#### **7.3. Thiết Kế Đáp Ứng Kỹ Thuật Số (Responsive Design)**

* Hệ thống CRM phải được tối ưu hóa hiển thị giao diện mượt mà trên tất cả các loại màn hình thiết bị phổ biến hiện nay bao gồm Máy tính để bàn (Desktop), Máy tính xách tay (Laptop) và Máy tính bảng (Tablet) có độ phân giải từ 1024px trở lên để phục vụ các Trưởng nhóm và Admin làm việc tại văn phòng.  
* Đối với giao diện dành cho điện thoại di động thông minh (Smartphone), hệ thống yêu cầu tối ưu hóa đặc biệt cho phân hệ Danh sách khách hàng và Quản lý công việc để nhân viên sales có thể tra cứu thông tin nhanh chóng và ghi chú lịch sử làm việc ngay khi đang đi gặp gỡ đối tác ở bên ngoài văn phòng. Các bảng dữ liệu nhiều cột khi hiển thị trên di động phải tự động chuyển đổi sang dạng thẻ (Card Layout) cuộn dọc để tránh hiện tượng vỡ khung hình.

### **8\. YÊU CẦU KỸ THUẬT MỨC CAO VÀ KIẾN TRÚC DỮ LIỆU**

#### **8.1. Mô Hình Kiến Trúc Và Công Nghệ Sử Dụng**

Hệ thống CRM cho Myan Corp được xây dựng theo kiến trúc Single Page Application (SPA) hiện đại nhằm mang lại trải nghiệm tương tác tốc độ cao, không gián đoạn cho người dùng cuối.

* Công nghệ Frontend: Sử dụng mã nguồn tối ưu hóa, đảm bảo thời gian tải trang ban đầu dưới 1.5 giây và các thao tác chuyển đổi phân hệ diễn ra ngay lập tức mà không phải tải lại toàn bộ tài nguyên trang web.  
* Nền tảng Backend và Lưu Trữ Dữ Liệu: Toàn bộ hệ thống cơ sở dữ liệu quan hệ, phân hệ quản lý xác thực tài khoản và cơ chế lưu trữ tập tin chứng từ thanh toán được chuẩn bị tích hợp đồng bộ và lưu trữ dữ liệu thật bằng nền tảng điện toán đám mây Supabase.

#### **8.2. Kiến Trúc Lưu Trữ Thực Tế Bằng Supabase**

* Supabase Database (PostgreSQL): Dữ liệu được tổ chức chặt chẽ theo mô hình dữ liệu quan hệ (Relational Database) với các ràng buộc khóa ngoại (Foreign Keys) nghiêm ngặt để đảm bảo không xảy ra tình trạng dữ liệu mồ côi (orphan data). Toàn bộ các bảng dữ liệu đều được thiết lập chỉ mục (Indexes) trên các trường thường xuyên tìm kiếm và truy vấn như phone, email, assigned\_to để tối ưu tốc độ phản hồi của hệ thống dưới 200ms đối với các truy vấn quy mô lớn.  
* Supabase Auth: Quản lý toàn bộ tiến trình đăng ký, đăng nhập, cấp phát và thu hồi mã Token JWT (JSON Web Token) bảo mật. Hệ thống cấu hình thời gian hết hạn của Access Token là 1 giờ và tự động làm mới bằng Refresh Token nhằm cân bằng giữa tính tiện dụng và an toàn hệ thống.  
* Supabase Storage: Tạo riêng một Bucket lưu trữ bảo mật có tên payment-proofs để chứa các tệp tin hình ảnh hoặc tài liệu PDF chứng từ, biên lai thanh toán do nhân viên sales tải lên. Bucket này được cấu hình quyền RLS chỉ cho phép những nhân sự có quyền xem đợt thanh toán tương ứng mới có thể lấy được đường dẫn URL tạm thời (Signed URL) để xem tài liệu, tuyệt đối không công khai ra môi trường internet ngoài.

#### **8.3. Yêu Cầu Xử Lý Dữ Liệu Lớn Và Hiệu Năng (CSV Processing)**

* Tiến trình nhập liệu hàng loạt (Bulk Import) từ tệp CSV phải được thực hiện thông qua cơ chế thực thi giao dịch cơ sở dữ liệu (Database Transaction). Nếu có bất kỳ lỗi nào xảy ra ở dòng thứ 500 của tệp CSV có 1000 dòng, toàn bộ 499 dòng trước đó đã nạp tạm thời phải được rút gọn xóa bỏ hoàn toàn khỏi bộ nhớ (Rollback), đưa hệ thống về trạng thái nguyên bản để tránh làm bẩn dữ liệu thật.  
* Hệ thống áp dụng kỹ thuật Phân trang dữ liệu (Pagination) ở tất cả các danh sách hiển thị lớn (như Danh sách khách hàng, Danh sách thanh toán). Mỗi trang chỉ tải tối đa 50 dòng dữ liệu. Khi người dùng cuộn xuống hoặc nhấn chuyển trang, hệ thống mới gọi API lấy khối dữ liệu tiếp theo, giúp giảm tải băng thông internet và tăng tốc độ kết xuất đồ họa của trình duyệt.

### **9\. YÊU CẦU XÁC THỰC VÀ LIÊN KẾT TÀI KHOẢN CHUYÊN SÂU**

Một trong những yêu cầu kỹ thuật cốt lõi và quan trọng nhất của hệ thống CRM Myan Corp trong giai đoạn 1 là xây dựng một cơ chế định danh người dùng thông minh, an toàn và có khả năng hợp nhất tài khoản linh hoạt nhằm giải quyết bài toán đa phương thức đăng nhập.

#### **9.1. Hỗ Trợ Đồng Thời Song Song Hai Phương Thức Xác Thực**

Hệ thống CRM bắt buộc phải cung cấp hai giải pháp xác thực có giá trị ngang nhau tại màn hình đăng nhập:

* Phương thức truyền thống (Email/Password): Người dùng nhập địa chỉ email doanh nghiệp và mật khẩu cá nhân tự đặt để xác thực quyền truy cập. Hệ thống áp dụng chính sách mật khẩu an toàn tối thiểu 8 ký tự, bao gồm chữ hoa, chữ thường và chữ số.  
* Phương thức hiện đại (Google OAuth): Người dùng click vào nút Đăng nhập bằng Google để hệ thống chuyển hướng xác thực qua dịch vụ Identity Provider của Google. Phương thức này yêu cầu người dùng phải sử dụng tài khoản Google có đuôi email trùng khớp với email đã được định danh trên hệ thống của Myan Corp.

#### **9.2. Quy Định Xử Lý Xung Đột Và Hợp Nhất Tài Khoản Trùng Email**

Hệ thống CRM Myan Corp áp dụng nguyên tắc tối thượng: **Một địa chỉ Email duy nhất chỉ tương ứng với một Thực thể Người dùng duy nhất (Single Unique User Identity) trong hệ thống dữ liệu.** Quy trình xử lý logic được thiết lập tự động tại tầng cơ sở dữ liệu như sau:

* Khi một nhân sự tiến hành đăng nhập bằng Google OAuth, hệ thống sẽ bóc tách trường thông tin email trả về từ API của Google.  
* Hệ thống thực hiện câu lệnh truy vấn tìm kiếm trong bảng auth.users của Supabase xem email này đã tồn tại hay chưa.  
* Nếu email này đã tồn tại dưới dạng một tài khoản được tạo trước đó bằng phương thức Email/Password (hoặc do quản trị viên Admin khởi tạo sẵn tài khoản SQL nội bộ trong cơ sở dữ liệu), hệ thống **tuyệt đối không được phép khởi tạo thêm một bản ghi người dùng mới** trong bảng Profiles.  
* Thay vào đó, hệ thống sẽ tự động gọi hàm liên kết định danh (Identity Linking Function). Phương thức xác thực Google OAuth mới sẽ được bổ sung vào danh sách các nhà cung cấp xác thực (Identities Array) của chính User ID hiện tại.  
* Hệ thống coi hai cách thức đăng nhập này là hai chìa khóa khác nhau để mở cùng một cánh cửa tài khoản duy nhất. Người dùng có thể linh hoạt chuyển đổi giữa việc gõ mật khẩu hoặc click chọn Google OAuth trong các phiên làm việc tiếp theo mà không gặp bất kỳ sự gián đoạn hay sai lệch nào về mặt trải nghiệm giao diện.

#### **9.3. Độc Lập Hoàn Toàn Giữa Phương Thức Xác Thực Và Cơ Chế Phân Quyền**

* Quyền hạn thao tác tính năng và phạm vi tiếp cận dữ liệu kinh doanh của một nhân sự được gắn chặt hoàn toàn vào mã định danh người dùng (profiles.id) và vai trò hành chính (profiles.role), tuyệt đối không phụ thuộc vào con đường hay cách thức mà người dùng đó lựa chọn để đăng nhập vào hệ thống CRM.  
* Dù nhân viên sales đăng nhập bằng cách gõ Email \+ Mật khẩu trên máy tính bàn hay sử dụng tính năng bấm chọn tài khoản Google OAuth trên máy tính bảng, hệ thống sau khi xác thực thành công đều phải trả về chính xác cùng một mã Token JWT chứa các thông tin phân quyền giống nhau. Toàn bộ các chính sách RLS bảo mật mức dòng tại Supabase sẽ hoạt động đồng nhất, đảm bảo nhân viên đó chỉ thấy đúng tệp khách hàng cá nhân do mình phụ trách, giữ nguyên tính toàn vẹn và an toàn của hệ thống thông tin.

### **10\. TIÊU CHÍ NGHIỆM THU GIAI ĐOẠN 1 (ACCEPTANCE CRITERIA)**

Để dự án CRM Myan Corp giai đoạn 1 được xác nhận hoàn thành và đủ điều kiện bàn giao đưa vào vận hành thực tế, hệ thống phải vượt qua toàn bộ các kịch bản kiểm thử nghiệm thu (UAT \- User Acceptance Testing) cốt lõi dưới đây với kết quả đạt 100%, không tồn tại lỗi nghiêm trọng (Critical Bug).

#### **10.1. Kịch Bản Nghiệm Thu Phân Hệ Xác Thực Và Hợp Nhất Dữ Liệu (UAT-01)**

* Điều kiện đầu vào: Đã khởi tạo sẵn một tài khoản trong hệ thống bằng phương thức Email/Password với email là nhanvien@myancorp.com và được Admin cấp vai trò là sales, đã gán phụ trách 50 khách hàng.  
* Hành động thực hiện: Người dùng đăng xuất khỏi hệ thống, sau đó quay lại màn hình đăng nhập và nhấn chọn nút Đăng nhập bằng Google, tiến hành chọn tài khoản Google có email chính xác là nhanvien@myancorp.com.  
* Kết quả kỳ vọng đạt được: Hệ thống đăng nhập thành công, chuyển hướng vào màn hình Dashboard. Khi kiểm tra cơ sở dữ liệu, không có bản ghi mới nào bị tạo trùng lặp trong bảng profiles. Tài khoản của nhân viên này vẫn giữ nguyên vai trò là sales và hiển thị đầy đủ, chính xác danh sách 50 khách hàng cũ được giao phụ trách, không bị mất mát hay sai lệch quyền dữ liệu.

#### **10.2. Kịch Bản Nghiệm Thu Phân Quyền Dữ Liệu Mức Dòng (UAT-02)**

* Điều kiện đầu vào: Nhân viên Sales A và Nhân viên Sales B cùng thuộc Đội kinh doanh 1\. Trưởng nhóm C là người quản lý Đội kinh doanh 1\.  
* Hành động thực hiện:  
  1. Sử dụng tài khoản của Nhân viên Sales A để truy cập phân hệ Danh sách khách hàng và thực hiện tìm kiếm mã khách hàng do Sales B đang phụ trách bằng cách nhập trực tiếp URL định danh của hồ sơ đó.  
  2. Sử dụng tài khoản của Trưởng nhóm C để truy cập xem danh sách khách hàng và báo cáo doanh thu trên hệ thống.  
* Kết quả kỳ vọng đạt được:  
  1. Hệ thống của Nhân viên Sales A lập tức chặn quyền truy cập, hiển thị thông báo từ chối quyền xem dữ liệu (Error 403 Forbidden) hoặc tự động chuyển hướng về trang chủ cá nhân để đảm bảo tính bảo mật nghiêm ngặt.  
  2. Tài khoản của Trưởng nhóm C hiển thị đầy đủ dữ liệu của cả Sales A và Sales B, tổng hợp chính xác doanh thu của toàn đội nhóm, nhưng hoàn toàn không thể thấy dữ liệu của các Đội kinh doanh 2 hoặc 3 trên hệ thống.

#### **10.3. Kịch Bản Nghiệm Thu Tương Tác Kéo Thả Trên Bảng Kanban (UAT-03)**

* Điều kiện đầu vào: Đang có 5 thẻ cơ hội bán hàng nằm ở cột Báo giá trong phân hệ Cơ hội bán hàng.  
* Hành động thực hiện: Người dùng chọn một thẻ cơ hội bán hàng, thực hiện thao tác giữ và kéo thẻ di chuyển sang cột Thương thảo và thả ra.  
* Kết quả kỳ vọng đạt được: Thẻ nằm ổn định ở cột Thương thảo. Không có hiện tượng giật lag giao diện hay thẻ tự động nhảy ngược lại cột cũ. Hệ thống tự động gửi yêu cầu cập nhật ngầm về cơ sở dữ liệu Supabase thành công. Dòng tổng giá trị tiền tệ của cột Báo giá tự động trừ đi giá trị của thẻ vừa chuyển, và cột Thương thảo tự động cộng thêm giá trị tương ứng theo thời gian thực mà không cần tải lại toàn bộ giao diện trang web.

#### **10.4. Kịch Bản Nghiệm Thu Nhập/Xuất Dữ Liệu CSV Hàng Loạt (UAT-04)**

* Điều kiện đầu vào: Chuẩn bị một tệp CSV gồm 200 dòng thông tin khách hàng mới, trong đó dòng số 150 cố tình để trống trường Số điện thoại (trường bắt buộc) và dòng số 180 có số điện thoại bị trùng lặp hoàn toàn với một khách hàng đang có sẵn trên hệ thống CRM.  
* Hành động thực hiện: Thực hiện đăng nhập bằng tài khoản Admin, truy cập phân hệ Danh sách khách hàng, nhấn chọn chức năng Tải lên từ CSV, chọn tệp tin lỗi đã chuẩn bị và nhấn Thực hiện.  
* Kết quả kỳ vọng đạt được: Hệ thống thực hiện quét dữ liệu, phát hiện ra các lỗi tại dòng 150 và dòng 180\. Tiến trình nạp dữ liệu bị dừng lại ngay lập tức. Hệ thống không ghi bất kỳ một dòng khách hàng nào của tệp CSV này vào cơ sở dữ liệu thực tế (Rollback hoàn toàn). Màn hình hiển thị thông báo lỗi chi tiết, chỉ rõ dòng 150 thiếu thông tin bắt buộc và dòng 180 bị trùng lặp dữ liệu để người dùng thực hiện chỉnh sửa.

### **KẾT LUẬN VÀ KHUYẾN NGHỊ HÀNH ĐỘNG**

#### **Kết Luận Ngắn**

Tài liệu PRD chi tiết này định hình toàn bộ cấu trúc tính năng, luồng trải nghiệm người dùng, quy tắc bảo mật phân quyền 3 cấp và kiến trúc dữ liệu tích hợp trên nền tảng Supabase cho giai đoạn 1 của hệ thống CRM Myan Corp. Việc tuân thủ chặt chẽ tài liệu này sẽ đảm bảo sản phẩm phần mềm đầu ra đáp ứng hoàn hảo nhu cầu số hóa dữ liệu tập trung, siết chặt an toàn thông tin kinh doanh và tối ưu hóa năng suất vận hành của đội ngũ sales trong doanh nghiệp.

#### **Khuyến Nghị Hành Động**

1. Ban Giám đốc và đại diện các phòng ban kinh doanh của Myan Corp cần tiến hành xem xét, đánh giá và ký duyệt chính thức bản tài liệu PRD này để làm căn cứ pháp lý và kỹ thuật duy nhất cho quá trình nghiệm thu sản phẩm sau này.  
2. Đội ngũ kỹ sư phát triển phần mềm (Development Team) dựa trên cấu trúc các bảng dữ liệu đã được định nghĩa chi tiết tại Mục 5 để tiến hành khởi tạo cơ sở dữ liệu, thiết lập hệ thống khóa ngoại và cấu hình các chính sách bảo mật RLS trực tiếp trên môi trường Supabase Production.  
3. Bộ phận IT phối hợp với Phòng Nhân sự chuẩn bị sẵn danh sách định danh toàn bộ cán bộ nhân viên trong công ty (bao gồm Họ tên, Email doanh nghiệp chính thức, Vai trò phân bổ) để sẵn sàng nạp vào hệ thống ngay khi phân hệ xác thực hoàn thành, phục vụ cho công tác chạy thử nghiệm hệ thống (Beta Testing).