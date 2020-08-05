from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView, 
    DetailView
)

from django.views.generic.edit import (
    FormView
)

from .forms import UserRegisterForm, ConnectionRegisterForm

from .models import User, Connection

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-list')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        User.objects.create(
            name = name
        )
        return super(UserRegisterView, self).form_valid(form)


class ConnectionRegisterView(FormView):
    template_name = 'users/add-connections.html'
    form_class = ConnectionRegisterForm
    success_url = '.'

    def form_valid(self, form):
        user1 = form.cleaned_data['user1']
        user2 = form.cleaned_data['user2']
        Connection.objects.create(
            user1 = user1,
            user2 = user2
        )
        return super(ConnectionRegisterView, self).form_valid(form)



class UserListView(ListView):
    template_name = 'users/list_users.html'
    paginate_by = 5
    ordering = 'id'
    context_object_name = 'users'
    model = User

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = User.objects.filter(
            name__icontains=palabra_clave
        )
        return lista

class UserConnectionsListView(ListView):
    template_name = 'users/user-connections.html'
    paginate_by = 5
    ordering = 'id'
    context_object_name = 'connections'
    model = Connection

    def get_context_data(self, **kwargs):
        context = super(UserConnectionsListView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context["pk"] = pk
        context["user"] = User.objects.get( id = pk)
        return context

    def get_queryset(self):
        pk = self.kwargs['pk']

        u = User.objects.get( id = pk)
        con = Connection.objects.filter(
            Q(user1 = u) | Q(user2 = u) 
        )
        users= []

        for c in con:
            if c.user1 == u:
                users.append(c.user2)

            else:
                users.append(c.user1)
                
        return users 


