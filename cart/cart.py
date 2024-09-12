class Cart:  # this cart class is in the context processor; been made available everywhere
    # for sessions

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')  # for existing/returning user to get existing session key

        # new user: generate session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            # ensure cart remembers if user has products in cart.Uses session key to confirm

        self.cart = cart

    def add(self, product, product_qty):

        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty

        else:

            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())  # loop through the items in the cart and sum up
