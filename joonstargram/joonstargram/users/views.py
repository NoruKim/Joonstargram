from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import SignUpForm
from .models import User


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage, send_mail
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text

from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

# ViewSets define the view behavior.
class HelloWorldAPI(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(data={"greeting": "Hello World"}, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/main.html')

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()

        return render(request, 'users/signup.html', {'form': form})

    elif request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.get(username=username)
            current_site = get_current_site(request)

            message = render_to_string('users/activation_email.html',
                {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                }
            )

            mail_title = "【Joonstargram】アカウント認証確認"
            mail_to = user.email
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()

            return HttpResponseRedirect(reverse('users:main'))


            # if user is not None:
            #     login(request, user)
            #     # Redirect to a success page.
            #     return HttpResponseRedirect(reverse('posts:index'))

        return render(request, 'users/main.html')

def logout(request):
    request.session.flush()

    return render(request, 'users/main.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse("posts:index"))
    else:
        return render(request, 'users/main.html', {'error' : '계정 활성화 오류'})
