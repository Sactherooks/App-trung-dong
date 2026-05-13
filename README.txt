================================================================
        ANCIENT CHINA EVADE - HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY
================================================================

GIỚI THIỆU
-----------
Ancient China Evade là game né đạn phong cách hành động 2D được
viết bằng Python và thư viện Pygame.

Người chơi có thể:
- Chọn nhân vật với kỹ năng riêng
- Chọn bản đồ với loại obstacle khác nhau
- Né đòn, parry và kích hoạt trạng thái thức tỉnh
- Tăng điểm bằng cách sống sót lâu nhất có thể

================================================================
YÊU CẦU HỆ THỐNG
================================================================

- Windows 10/11
- Python 3.8 trở lên
- RAM tối thiểu: 4GB
- Độ phân giải khuyến nghị: 1920x1080
- Đã cài thư viện pygame

================================================================
CÀI ĐẶT PYTHON
================================================================

Bước 1:
Tải Python tại:
https://www.python.org/downloads/

Bước 2:
Khi cài đặt:
✓ Tick vào ô:
    Add Python to PATH

Bước 3:
Nhấn:
    Install Now

================================================================
CÀI ĐẶT PYGAME
================================================================

Sau khi cài Python:

1. Mở Command Prompt (cmd)

2. Nhập lệnh:

       pip install pygame

3. Chờ quá trình cài hoàn tất.

Nếu hiện:
       Successfully installed pygame
=> Đã cài thành công.

================================================================
CẤU TRÚC THƯ MỤC
================================================================

Đảm bảo toàn bộ file game nằm trong cùng thư mục project.

Ví dụ:

App-trung-dong/
│
├── app.py
├── Background.png
├── bg phật.png
├── bg thuyền.png
├── videoplayback.mp3
├── warning.png
├── baogay.png
│
├── nv2/
│   ├── Đứng.png
│   ├── Đỡ.png
│   ├── đứng_2.png
│   ├── đỡ_2.png
│   └── ...
│
├── bom/
│   └── ...
│
└── ...

================================================================
QUAN TRỌNG - CHỈNH ĐƯỜNG DẪN ASSET
================================================================

Trong file app.py có dòng:

    ASSET_PATH = "C:/Users/TBL/Documents/GitHub/App-trung-dong/"

Bạn PHẢI đổi đường dẫn này thành vị trí thư mục game trên máy bạn.

Ví dụ:

    ASSET_PATH = "D:/Game/App-trung-dong/"

Lưu ý:
- Phải có dấu / ở cuối
- Dùng dấu / thay vì \

================================================================
CHẠY GAME
================================================================

CÁCH 1 - DOUBLE CLICK
----------------------

Nhấp đúp vào file:

    app.py

Nếu Python đã được cài đúng, game sẽ tự chạy.

---------------------------------------------------------------

CÁCH 2 - COMMAND PROMPT
------------------------

1. Mở Command Prompt

2. Di chuyển tới thư mục game:

       cd "D:\Game\App-trung-dong"

3. Chạy game:

       python app.py

Hoặc:

       py app.py

================================================================
ĐIỀU KHIỂN
================================================================

DI CHUYỂN
-----------
← → hoặc A / D
Di chuyển trái/phải

NHẢY
------
↑ hoặc W

PARRY / ĐỠ ĐÒN
----------------
F

THOÁT / QUAY LẠI MENU
----------------------
ESC

CHƠI LẠI KHI THUA
------------------
R

================================================================
NHÂN VẬT
================================================================

1. MONK
--------
- Nhân vật cân bằng
- Dễ chơi
- Sau khi nhặt item:
    + Hiệu ứng toàn màn hình
    + Tăng tốc độ di chuyển

2. LIU XUANJI
--------------
- Nhân vật tốc độ cao
- Có trạng thái thức tỉnh

Khi nhặt item:
    + Chuyển sang awakened form
    + Được bất tử tạm thời
    + Thay đổi animation và sprite

================================================================
CÁC BẢN ĐỒ
================================================================

1. ELYSIUM OF CHERRY BLOSSOMS
--------------------------------
Obstacle:
- Katana từ nhiều hướng

2. ABYSS OF THE FORGOTTEN SHRINE
---------------------------------
Obstacle:
- Bùa talisman xoay tốc độ cao

3. THE GLORY OF CRIMSON BANNER
--------------------------------
Obstacle:
- Cannonball phát nổ giữa map

================================================================
MỤC TIÊU GAME
================================================================

- Né obstacle càng lâu càng tốt
- Sử dụng Parry để phá obstacle
- Nhặt item bất tử xuất hiện định kỳ
- Tăng điểm bằng cách sống sót lâu hơn

================================================================
TÍNH NĂNG ĐẶC BIỆT
================================================================

✓ Character Selection Screen
✓ Map Selection Screen
✓ Animation hệ thống
✓ Awakened Transformation
✓ Explosion Effects
✓ Particle Effects
✓ Parry System
✓ Speed Boost
✓ Dynamic Obstacles
✓ Sound Effects & Music

================================================================
LỖI THƯỜNG GẶP
================================================================

1. ModuleNotFoundError: No module named 'pygame'
--------------------------------------------------

Nguyên nhân:
Chưa cài pygame

Cách sửa:
    pip install pygame

--------------------------------------------------

2. FileNotFoundError
---------------------

Nguyên nhân:
Sai đường dẫn ASSET_PATH
hoặc thiếu file ảnh / âm thanh

Cách sửa:
- Kiểm tra ASSET_PATH
- Kiểm tra file có đúng vị trí không

--------------------------------------------------

3. Game mở rồi tự tắt
----------------------

Nguyên nhân:
Thiếu asset hoặc lỗi pygame

Cách sửa:
- Chạy bằng cmd để xem lỗi
- Kiểm tra toàn bộ file asset

================================================================
GỢI Ý
================================================================

- Nên chơi fullscreen hoặc màn hình lớn
- Dùng tai nghe để trải nghiệm âm thanh tốt hơn
- Archer phù hợp người chơi phản xạ nhanh
- Monk phù hợp người mới bắt đầu

================================================================
        CHÚC BẠN CHƠI GAME VUI VẺ!
================================================================
