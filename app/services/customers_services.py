from fastapi import   HTTPException
from dbmodels import Customers,Users
from .services_base import BaseService,Session
from .users_services import users_services
from schemas import CustomerInfor,SignUpBase,UserCreate,CustomerCreate,\
     CustomerUpdate,UserUpdate


class CustomersService(BaseService):
    def get_customer_by_user_id(self,session: Session,id: int):
        return session.query(self.model).filter(self.model.users_id == id).first()
      
    
    def get_customers(self,session: Session): #Get all data from a table
       
        # C1 mất nhiều thời gian xử lý  hơn
        result = session.query(Users,Customers).\
                join(Customers,Users.id == Customers.users_id )
        
        # C2 lấy  dữ liệu customer qua relationship của users
        # sqlalchemy tự xử lý tự tạo câu các câu lệnh con truy vấn tới sql, liên quan đến bảo mật / chống tấn công sql injection
        # result = session.query(Users)
        
        # result.all() 
        
        customers_list = []  
        # for c in user.customer:
        #     ...
        for user,customer in result:
            
            customerinfor = CustomerInfor(
                customer_id = customer.id,
                email       = user.email,
                password    = user.password,
                first_name  = user.first_name,
                last_name   = user.last_name,
                tel_no      = user.tel_no,
                address     = user.address           
                )
            
            customers_list.append(customerinfor)    
        return customers_list
    
    def get_customer(self,session: Session,id: int):
       customer_instance =  self.get_one(session,id)
       user_instance =  users_services.get_one(session, customer_instance.users_id)
            
       customerinfo = CustomerInfor(
            customer_id    = customer_instance.id,
            email          = user_instance.email,
            password       = user_instance.password,
            first_name     = user_instance.first_name,
            last_name      = user_instance.last_name,
            tel_no         = user_instance.tel_no,
            address        = user_instance.address           
        )
        
       return customerinfo
    
    def add_customer(self,session: Session,body_form : SignUpBase):
        account = users_services.get_by_email(session,body_form.email) # check sự tồn tại của account
        if account:
            raise HTTPException(status_code= 403,  detail="This account created already !")
        
        
        # saving to user table
        user_from =  UserCreate(
                email       = body_form.email,
                password    = body_form.password,
                first_name  = body_form.first_name,
                last_name   = body_form.last_name,
                tel_no      = body_form.tel_no,
                address     = body_form.address,
            )
        user_instance = users_services.create_one2(session, user_from)
        
        # saving to customer table
        customer_form = CustomerCreate(users_id = user_instance.id)
        customer_instance = self.create_one(session, customer_form)
        
        # response_model read from db 
        return self.get_customer(session,customer_instance.id)



    def modify_customer(self,session: Session, id : int ,body_form : CustomerUpdate ):
        
       account = customers_services.get_one(session,id) # check sự tồn tại của account
       if not account:
            raise HTTPException(status_code= 403,  detail="This account is not available !")
        
        
       customer_check = self.get_one(session,id)  # read users_id
        # update to user table   
       user_from =  UserUpdate(
                email       = body_form.email,
                password    = body_form.password,
                first_name  = body_form.first_name,
                last_name   = body_form.last_name,
                tel_no      = body_form.tel_no,
                address     = body_form.address
            )
        
       users_services.update(session,customer_check.users_id, user_from) #  write data to users table
            
        # response_model 
     # response_model read from db 
       return self.get_customer(session,id)
   

    def remove_customer( self,session: Session,id: int):
        customer_instance =  self.get_one(session,id) # read next id
        self.delete_one(session,id) # delete customer id 
        print(customer_instance.__dict__)
        print(customer_instance.users_id)
        users_services.delete_one(session,customer_instance.users_id) # delete user
        session.close()

customers_services = CustomersService(Customers) 

#1