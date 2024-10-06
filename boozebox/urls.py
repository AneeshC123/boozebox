from django.urls import path
from .views import home, signup, show, edit, update, destroy, login_view, cart

urlpatterns=[
        path('', home,name='home'),
        path('signup/', signup, name='signup'),
        path('login/', login_view, name='login'),
        path('show/',show,name='show'),
        path('edit/<int:id>', edit ,name='edit'),
        path('update/<int:id>',update, name='update'),
        path('delete/<int:id>', destroy, name='destroy'),
        path('cart/', cart, name='cart')
]