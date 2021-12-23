# marlb
Một ngôn ngữ lập trình nho nhỏ nhưng có võ, được dùng để viết một giai điệu đơn giản. Tên được đề xuất bởi bạn của tôi LOLLLLLLL.
<br>
Xây dựng dựa trên ngôn ngữ `brainfuck` AKA `đ*t não`
<br>
# Tải trình thông dịch
```
Điều kiện:
Python: 3.10
Windows: 10

Trình thông dịch này chỉ chạy được trên Windows do tôi không tìm thấy
gói phần mềm hỗ trợ nào để kêu một tiếng beep trên Linux và MacOSX :(
```

```
Định dạng tệp tin: *.marble

chú ý: Trình thông dịch sẽ không thực thi các câu lệnh có trong một file có định dạng tệp tin khác *.marble 
```

Dùng `git` để clone cái repo này về
<br>
`git clone https://github.com/bennett-nguyen/marlb.git`
<br>
hoặc tải file zip về rồi giải nén mà xài :v

# Hướng dẫn sử dụng
Có 2 phiên bản, bản mã nguồn và bản executable (kiểm tra `./bin/README.md` để xem thêm thông tin). Nếu bạn lười tải Python để chạy trình thông dịch này
thì dùng bản executable còn nếu có Python và muốn chỉnh sửa mã nguồn thì dùng bản mã nguồn
<br>
<br>
Bản mã nguồn:
Chạy trên terminal emulator (command prompt, powershell): `python marlb.py -m MODE -f đường/dẫn/tới/file`
<br>
Bản executable: 
Chạy: `marlb -m MODE -f đường/dẫn/tới/file`
<br>
muốn xem thêm thông tin về tham số thì gõ `--help` vào phía sau câu lệnh, vd: `marlb --help`
<br>
<br>
Có một file lệnh tên `hello_world.marble` mà tôi đã viết sẵn trong cái repo này, để thông dịch nó thì cần chạy `marlb -m interpret -f ./hello_world.marble`.
<br>
<br>
**Chế độ (MODE)**
```
interpret: thông dịch thông thường
debug: thông dịch nhưng in ra thông tin về những gì đang diễn ra, 
vd như dòng đang dịch, độ cao của âm hiện tại, độ dài của âm hiện tại, v.v
```
<br>

# Cú pháp
Comment được ký hiệu bằng dấu `"`, những ký tự nào đứng sau `"` sẽ bị trình thông dịch bỏ qua. Mặc dù những kí tự mà trình thông dịch
này không nhận dạng được cũng sẽ bị xem là một comment, sử dụng comment bằng dấu `"` vẫn là một lựa chọn tốt nhất!
<br><br>

Trình thông dịch sẽ chơi một nốt ứng với ký tự đại diện cho nốt đó, các ký tự bao gồm:
<br>
`q`: C
<br>
`a`: C#
<br><br>
`w`: D
<br>
`s`: D#
<br><br>
`e`: E
<br><br>
`r`: F
<br>
`d`: F#
<br><br>
`u`: G
<br>
`j`: G#
<br><br>
`i`: A
<br>
`k`: A#
<br><br>
`o`: B
<br><br>
`p`: C (âm cao hơn nốt C của `q`)

<br>
Để thay đổi cao độ hay độ dài của một nốt thì sử dụng những ký tự sau đây:

```
mặc định:
  độ cao của nốt (pitch_level): 2
  độ dài của nốt (duration): 200ms
```

`+`: Tăng cao độ lên `1` (cao nhất: `16`)
<br>
`-`: Giảm cao độ xuống `1` (thấp nhất: `1`)
<br>
`>`: Tăng độ dài của nốt lên `100ms` (cao nhất: `15s`)
<br>
`<`: Giảm độ dài của nốt xuống `100ms` (thấp nhất: `0ms`)
<br>
`!`: Ngừng việc thực thi lệnh trong `0.5s`
<br>
`:`: Reset cao độ và độ dài của nốt xuống mức mặc định

# Update
- (2021/12/23): Thêm hỗ trợ `utf-8` encoding. Tách nhỏ code thành 2 phần.
- (2021/12/20): Thêm vào [language support extension](https://marketplace.visualstudio.com/items?itemName=bennett-nguyen.marble) cho ngôn ngữ này trong VS Code, tải về để làm nổi bật cú pháp cho đẹp và dễ nhìn
- (2021/12/16): Thêm vào mode `debug`
- (2021/12/16): Thêm vào tính năng xử lí những thứ thừa thải có trong file script (vd: newline character, comment, whitespaces)
