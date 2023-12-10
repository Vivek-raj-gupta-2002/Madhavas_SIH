from django.contrib.auth.base_user import BaseUserManager

# Handeling the user creations 

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):

        # check if username is not null
        if not username:
            raise ValueError("username require")
        
        
        # normalise the email
        if extra_fields['email']:
            extra_fields['email'] = self.normalize_email(extra_fields['email'])

        user = self.model(self, username, **extra_fields)
        

        # set the password
        user.set_password(password)

        # save the user
        user.save(using=self.db)
        return user
    

    # Super User Creation
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, **extra_fields)