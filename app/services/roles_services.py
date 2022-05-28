from dbmodels import Roles
from .services_base import BaseService


class RolesService(BaseService[Roles]):
    pass

roles_services = RolesService(Roles) 

#1