from django.urls import path

from shop.store.views import show_contact_info, index, redirect_to_home, show_about, show_articles, \
    show_single_article_by_id, checkout_basket

urlpatterns = (
    path("", index, name="index"),
    path("go-to-home/", redirect_to_home, name="redirect to home"),
    path("contacts/", show_contact_info, name="contacts"),
    path("about/", show_about, name="about"),
    path("articles/", show_articles, name="articles"),
    path("articles/<int:article_id>/", show_single_article_by_id, name="single article"),
    path("basket/", checkout_basket, name="checkout")
)
