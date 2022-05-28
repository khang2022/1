# lỗi thứ tự đường dẫn !
### case 1
app.get("\book\{id}")
app.get("\book\me")

fastapi sẽ nhận diện me là id => báo lỗi 422  

phải đảo ngược lại thứ tự!

### case 2
app.get("\book\{id}")
app.get("\book")
app.get("\book\{id}\abc") => fastapi sẽ nhận diện {id}\abc là id => báo lỗi 422  

do trong hàm main  app = FastAPI()  chỉ khởi tạo 1 lần 
thứ tự đúng là 

app.get("\book")
app.get("\book\{id}")
app.get("\book\{id}\abc") 


# 


