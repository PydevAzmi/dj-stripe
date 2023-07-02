import stripe
from project import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
YOUR_DOMAIN = 'http://localhost:5000'

class Home(TemplateView):
    template_name = "payment.html"

class CreateCheckoutSession(View):

    def post(self, request, *args, **kwargs):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': '{{PRICE_ID}}',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
                automatic_tax={'enabled': True},
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)