from dbmodels import Categorys
from .services_base import BaseService


class CategorysService(BaseService[Categorys]):
    pass

categorys_services = CategorysService(Categorys) 

#1