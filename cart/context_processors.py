from .cart import Cart


def cart(request):  # registered in context processors under templates in settings for availability throughout

    return {'cart': Cart(request)}
