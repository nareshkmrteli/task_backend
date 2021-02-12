from rest_framework.authentication import SessionAuthentication


class CsrExemptSessionAuthentiation(SessionAuthentication):
    def enforce_csrf(self,request):        
        pass  
