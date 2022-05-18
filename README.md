***

Mỗi hồ sơ cần những thông tin sau: Mã nhân viên, tên nhân viên, ngày sinh, nơi sinh, trong đó các nhân viên sẽ được phân biệt nhau bởi mã nhân viên. Yêu cầu sử dụng cấu trúc dữ liệu cây nhị phân tìm kiếm (Binary Search Tree - BST) để lưu trữ và quản lý dữ liệu.

Hãy viết chương trình gồm các chức năng sau:

1. Đưa dữ liệu từ 1 text file vào 1 BTS.

2. Thêm  hồ sơ nhân viên mới vào cây BST

3. Duyệt cây BST theo thứ tự giữa (Inorder)

4. Duyệt cây BST theo chiều rộng

5. Tìm kiếm thông tin của nhân viên theo mã nhân viên trong cây BST

6. Xóa đi một hồ sơ nhân viên dựa vào mã nhân viên trong cây BST

***

Hướng dẫn

Trong bài này chúng ta cần:

- Tạo nên một cấu trúc dữ liệu cây nhị phân tìm kiếm của riêng mình để quản lý hồ sơ nhân viên, trong đó sẽ chứa các thao tác như thêm, xóa, tìm kiếm, duyệt, cân bằng cây, đếm số phần tử của cây.

- Thông tin của 1 người có 4 trường cơ bản: ID, Name, Day of Birth, Birthplace (lưu trữ ở dạng string).

Trong bài này chúng ta cần:

Tạo nên một cấu trúc dữ liệu cây nhị phân tìm kiếm của riêng mình để quản lý hồ sơ nhân viên, trong đó sẽ chứa các thao tác như thêm, xóa, tìm kiếm, duyệt, cân bằng cây, đếm số phần tử của cây.
Chức năng và yêu cầu cơ bản

1. Thiết kế Menu

Có ít nhất 6 chức năng để lựa chọn
Mỗi chức năng tương ứng với một câu hỏi
Không hạn chế số lần lựa chọn
2. Chức năng và yêu cầu 

1- Xây dựng BST từ dữ liệu load vào từ file.

2- Thêm  hồ sơ nhân viên mới vào cây BST:

Khi thêm hồ sơ mới, nếu có ID trùng với ID cũ thì không cho thêm, cây mới nhận được phải là cây nhị phân tìm kiếm.

3 - Duyệt cây BST theo thứ tự Inorder.

Sử dụng đệ quy để duyệt cây theo thứ tự duyệt Inorder.

4- Duyệt cây BST theo chiều rộng.

Sử dụng cấu trúc lưu trữ Queue và các thao tác trên Queue để duyệt.

5- Tìm kiếm thông tin của nhân viên theo mã nhân viên trong cây BST.

Sử dụng cấu trúc lưu trữ Queue và các thao tác trên Queue để tìm kiếm.

6-  Xóa đi một hồ sơ nhân viên dựa vào mã nhân viên trong cây BST.

Tổ chức code

Dưới đây là gợi ý tham khảo về cách thức tổ chức code cho ứng dụng. Bạn hoàn toàn có thể tổ chức code theo cách riêng của mình.

 - Lớp Person1 chứa thông tin và hành vi cần thiết cho mỗi hồ sơ nhân viên - Lớp Node để quản lý thông tin và hành  của vi mỗi node trong cây nhị phân tìm kiếm

- Lớp MyQueue chứa các thông tin và các thao tác cơ bản của Queue, lớp này sử dụng để phục vụ cho một số nhiệm vụ trong lớp MyBSTree hoặc có thể cả MyPerson

- Lớp MyBSTree chứa thông tin và  các hành vi cơ bản của một cây nhị phân tìm kiếm - Lớp MyPerson sẽ chứa các phương thức thức biểu diễn các yêu cầu chức năng từ a đến f

- Lớp Main chứa code để tạo ra menu và thực hiện các chức năng của bài toán. Một số phương thức quan trọng của các lớp. (Ngoài các lớp, phương thức này sinh viên có thể thêm các lớp và phương thức nữa nếu cảm thấy cần thiết).

 4. Kết quả khi chạy chương trình

run:

+-------------------Menu------------------+

Person Tree:

1. Load the data from the file.

2. Insert a new Person.

3. Inorder traverse

4. Breadth-First Traversal traverse

5. Search by Person ID

6. Delete by Person ID

Exit:

0. Exit

+-----------------------------------------.+

Nếu bấm 1, màn hình sẽ hiện ra:

Choice 1: Load data from file and display

Hướng dẫn nhập vào đường dẫn file:

Please enter the find path: ...

Nếu file hợp lệ, hiển thị: 

The file is loaded successfully!

Load toàn bộ dữ liệu người dùng vào BST, nếu đã có 1 BST thì load dữ liệu vào BST 

Nếu file không hợp lệ, hiển thị:

File-path is not correct!

Nếu bấm 2, màn hình sẽ hiện ra:

Choice 2: Insert a new Person.

Hướng dẫn nhập vào New ID:

Please insert the New ID:

VD về new ID: 1

Nếu ID đã bị trùng, hiển thị:

This ID has been chosen, please choose another ID!

Sau đó quay lại yêu cầu nhập New ID.

Hướng dẫn nhập vào Name:

Please insert the Name:

VD về Input Name: Ha

Hướng dẫn nhập vào Birthplace:

Please insert the Birthplace:

VD về Birthplace: Hanoi

Hướng dẫn nhập vào Birth of Date:

Please insert the Birth of Date:

VD về Birth of Date: 12/09/90

Sau khi nhập hết, các thông tin vừa khai báo sẽ được hiển thị:

New ID: 1

Name: Ha

Birthplace: Ha

Day of birth: 12/09/90

Please type anything to come back to the main menu!

Nếu bấm 3, màn hình sẽ hiện ra:

Choice 3: Inorder traverse

ID | Name | Day of Birth | Birthplace

1          Ha         12/09/90             Ha         

2          An         ?inh                 Nam        

3          Binh       01/05/92             TH         

4          Lan        04/04/87             Ha         

5          Tuan       02/02/89             TB    

Please type anything to come back to the main menu!

Nếu bấm 4, màn hình sẽ hiện ra:

Choice 4: Breadth-First Traversal traverse

ID | Name | Day of Birth | Birthplace

1          Ha         12/09/90             Ha         

4          Lan        04/04/87             Ha         

2          An         ?inh                 Nam        

5          Tuan       02/02/89             TB         

3          Binh       01/05/92             TH         

Please type anything to come back to the main menu!

Nếu bấm 5, màn hình sẽ hiện ra:

Choice 5: Search by Person ID

Please insert the ID:

VD về ID nhập vào: 3

Nếu ID nhập vào có trong BST, in ra:

Search for ID = 3

ID | Name | Day of Birth | Birthplace

3          Binh       01/05/92             TH         

Please type anything to come back to the main menu!

VD về ID nhập vào: 6

Nếu ID nhập vào không có trong BST, in ra:

Search for ID = 6

"The searched ID is not valid".

Please type anything to come back to the main menu!

Nếu bấm 6, màn hình sẽ hiện ra:

Choice 6: Delete by Person ID

Please insert the ID:

VD về ID nhập vào: 3

Nếu ID nhập vào có trong BST, in ra:

Delete the person with ID = 3

ID | Name | Day of Birth | Birthplace

3          Binh       01/05/92             TH         

Please type anything to come back to the main menu!

VD về ID nhập vào: 6

Nếu ID nhập vào không có trong BST, in ra:

Delete the person with ID = 6

"The searched ID is not valid".

Please type anything to come back to the main menu!