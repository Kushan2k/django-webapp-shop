from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About, name='about'),
    path('product/', views.Products, name='products'),
    path('products/new-posted', views.NewItems, name='new-posted'),
    path('products/trending', views.Trending, name='trending'),
    path('item/<int:id>', views.Items, name='item'),
    path('add/', views.AddItem.as_view(), name='additem'),
    path('user/<int:pid>', views.Profile, name='user'),

    path('add-to-basket/<int:id>', views.addtobasket, name='basket'),
    path('cart/<int:uid>', views.Cart, name='cart'),
    path('remove-from-cart/<int:iID>', views.RMCart, name='rm-cart'),
    path('buy-now/<int:id>', views.BuyNow, name='buy-now'),
    path('edit/<int:id>', views.EditItem.as_view(), name='edit'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
