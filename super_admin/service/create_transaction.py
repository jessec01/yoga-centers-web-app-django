from django.db import transaction
from userYC.models import UserYogaCenter
from super_admin.models import SuperAdminProfile as SuperAdmin
from django.db import IntegrityError 
class CreateTransactionService:
    @staticmethod
    def receiver_data(self,data):
        with transaction.atomic():
            user_yc=UserYogaCenter.objects.create_user(username=data['username'],first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone=data['phone'],
            password=data['password'])
            sid=transaction.savepoint()                        
            try:
                super_admin_profile = SuperAdmin.objects.create(
                    user=user_yc,
                    is_active=True,
                    is_super_admin=True
                )
                transaction.savepoint_commit(sid)
                return super_admin_profile.user        
            except IntegrityError as e:
                transaction.savepoint_rollback(sid)
                raise e