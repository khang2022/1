from fastapi import HTTPException
from dbmodels import Staffs, Users,Roles
from .services_base import BaseService, Session
from .users_services import  users_services
from .roles_services import  roles_services
from schemas import  UserCreate ,StaffCreate, RoleCreate, StaffInfo,\
     RoleUpdate,UserUpdate,SignUp,StaffUpdate



class StaffsService(BaseService[Staffs]):
    
    def get_staff_by_user_id(self,session: Session,id: int):
        return session.query(self.model).filter(self.model.users_id == id).first()
 
    def get_staffs(self,session: Session): #Get all data from a table
       
        query = session.query(Users,Staffs,Roles).\
               join(Staffs,Users.id == Staffs.users_id ).\
               join(Roles,Roles.id == Users.roles_id )
        
        result = query.all()
        staffs_list = []  
        for user,staff,position in result:
            
            staffinfo = StaffInfo(
                staff_id    = staff.id,
                role        = position.title, 
                email       = user.email,
                password    = user.password,
                first_name  = user.first_name,
                last_name   = user.last_name,
                tel_no      = user.tel_no,
                address     = user.address           
                )
            
            staffs_list.append(staffinfo)    
        return staffs_list
    
    def get_staff(self,session : Session, id : int):
            staff_instance =  self.get_one(session,id)
            user_instance =  users_services.get_one(session,staff_instance.users_id)
            role_instance =  roles_services.get_one(session,user_instance.roles_id)
            
        
            staffinfo = StaffInfo(
                staff_id    = staff_instance.id,
                role        = role_instance.title, 
                email       = user_instance.email,
                password    = user_instance.password,
                first_name  = user_instance.first_name,
                last_name   = user_instance.last_name,
                tel_no      = user_instance.tel_no,
                address     = user_instance.address           
            )
            
            return staffinfo

    def add_staff(self,session : Session, body_form : SignUp):
        account = users_services.get_by_email(session,body_form.email) # check sự tồn tại của account
        if account:
            raise HTTPException(status_code= 403,  detail="This account created already !")
        
        
        # role  = users_services.save_role_db(body_form.role)
        
        # saving to role table 
        role_form = RoleCreate( title = body_form.role)
        role_instance = roles_services.create_one(session,role_form)
        
        # saving to user table
        user_from =  UserCreate(
                email       = body_form.email,
                password    = body_form.password,
                first_name  = body_form.first_name,
                last_name   = body_form.last_name,
                tel_no      = body_form.tel_no,
                address     = body_form.address,
                roles_id    = role_instance.id
            )
        user_instance = users_services.create_one2(session, user_from)
        
        # saving to staff table
        staff_form = StaffCreate(users_id = user_instance.id)
        staff_instance = self.create_one(session, staff_form)
        
        
        # response_model 
      
        return self.get_staff(session,staff_instance.id)
    
    def modify_staff(self, session : Session,id : int,body_form : StaffUpdate):      
        account = self.get_one(session,id) # check sự tồn tại của account
        if not account:
            raise HTTPException(status_code= 403,  detail="This account is not available !")
        
        staff_check=  self.get_one(session,id)  # read users_id

        # update to user table      
        user_read = users_services.get_one(session,staff_check.users_id)
          
        user_from =  UserUpdate(
                email       = body_form.email,
                password    = body_form.password,
                first_name  = body_form.first_name,
                last_name   = body_form.last_name,
                tel_no      = body_form.tel_no,
                address     = body_form.address,
                roles_id    = user_read.roles_id
            )
        
        user_check = users_services.update(session,staff_check.users_id, user_from) # read & write data to users table
        
    
   #1     
        # update to role table
        role_form = RoleCreate( title = body_form.role)
        role_check = roles_services.update(session,user_check.roles_id,role_form)
        
        print(role_check.__dict__)
        
        # response_model 
    
        return self.get_staff(session,id)
     
    def delete_staff (self,id : int ,session : Session):
        staff_instance =  self.get_one(session,id) # read next id
        self.delete_one(session,id) # delete staff
        
        # print(staff_instance.users_id)  
        user_instance =  users_services.get_one(session,staff_instance.users_id)  # read next id  
        users_services.delete_one(session,staff_instance.users_id) # delete
        
        # print(user_instance.roles_id)  
        roles_instance =  roles_services.get_one(session,user_instance.roles_id) # read next id  
        roles_services.delete_one(session,user_instance.roles_id) # delete
        session.close()
        
        

staffs_services = StaffsService(Staffs) 

