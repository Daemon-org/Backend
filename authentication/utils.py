import arrow
from django.http import JsonResponse
from authentication.models import Profile
import jwt
from decouple import config
from django.contrib.auth.hashers import make_password, check_password
import random
import logging
from CRMS.settings import REDIS
from CRMS.notif import Notify

notify = Notify()
logger = logging.getLogger(__name__)


class Authenticate:
    def generate_access_token(self, email):
        user = Profile.objects.get(email=email)
        payload = {
            "user_id": user.uid,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_id": user.uid,
            "username": user.username,
            "exp": arrow.utcnow().shift(minutes=15).timestamp(),
            "iat": arrow.utcnow().timestamp(),
        }
        return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")

    def generate_refresh_token(self, email):
        user = Profile.objects.get(email=email)
        payload = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_id": user.uid,
            "username": user.username,
            "exp": arrow.utcnow().shift(days=7).timestamp(),
            "iat": arrow.utcnow().timestamp(),
        }
        return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")

    def generate_otp(self):
        # Generate a random 5-digit OTP
        return random.randint(10000, 99999)

    def send_otp(self, recipient):
        try:
            otp = self.generate_otp()
            context = {
                "email": recipient,
                "template": "otp-verification",
                "context": dict(
                    email=recipient,
                    otp=otp,
                ),
            }
            REDIS.set(f"{recipient}", otp)
            notify.send_sms_or_email(
                medium="email", recipient=recipient, context=context
            )
            return JsonResponse({"success": True, "info": "OTP sent successfully"})
        except Exception as e:
            logger.warning(f"SMTPException: {str(e)}")
            return JsonResponse(
                {"success": False, "info": "Error sending OTP via email"}
            )

    def verify_otp(self, email, user_entered_otp):
        stored_otp = REDIS.get(f"{email}")
        logger.warning(stored_otp)
        if stored_otp and int(stored_otp) == int(user_entered_otp):
            return JsonResponse(
                {"success": True, "info": "OTP verification successful"}
            )

        else:
            # Invalid OTP
            return JsonResponse({"success": False, "info": "Invalid OTP"})

    def register_user(
        self, username, email, first_name, last_name, phone_number, password
    ):
        try:
            if len(username) < 5 or len(first_name) < 5 or len(last_name) < 5:
                return JsonResponse({"success": False, "info": "input  too short"})

            if password < 10:
                return JsonResponse(
                    {
                        "success": False,
                        "info": "password must contain at least 10 characters",
                    }
                )

            if Profile.objects.get(email=email):
                return JsonResponse({"success": False, "info": "Email already exists"})

            if Profile.objects.get(username=username):
                return JsonResponse(
                    {"success": False, "info": "Username already exists"}
                )

            user = Profile.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                password=make_password(password),
            )
            if user:
                return JsonResponse(
                    {"success": True, "info": "User created successfully"}
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "An error ocurred,try again later"}
                )

        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "An error ocurred,try again later"}
            )

    def login_user(self, email, password):
        try:
            user = Profile.objects.get(email=email)

            if not user:
                return JsonResponse(
                    {"success": False, "info": "User with this email does not exist."},
                )

            if check_password(password, user.password):
                access_token = self.generate_access_token(user.email)
                refresh_token = self.generate_refresh_token(user.email)

                return JsonResponse(
                    {
                        "success": True,
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }
                )
            else:
                return JsonResponse(
                    {"success": False, "info": "Invalid email or password."}
                )
        except Exception as e:
            logger.warning(str(e))
            return JsonResponse(
                {"success": False, "info": "Kindly try again --p2prx2--"}
            )

    def get_user_info_from_token(token):
        decoded_token = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
        user_email = decoded_token["email"]

        # Retrieve additional user info using the email
        user = Profile.objects.get(email=user_email)

        # Extract the necessary user info
        user_info = {
            "uid": user.uid,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone": user.phone_number,
            "username": user.username,
        }

        return user_info
