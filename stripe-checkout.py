#!/usr/bin/env python3
"""
Stripe payment script for LeadForge.
Creates checkout sessions for products.
"""

import stripe
import json
import sys
import os

def load_credentials():
    cred_path = os.path.expanduser("~/.openclaw-seldon/credentials/stripe.json")
    with open(cred_path, 'r') as f:
        return json.load(f)

def create_checkout_session(price_id, success_url, cancel_url):
    creds = load_credentials()
    stripe.api_key = creds['secret_key']
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session

def create_checkout_from_product(product_name, amount_cents, success_url, cancel_url):
    """Create checkout session with inline product."""
    creds = load_credentials()
    stripe.api_key = creds['secret_key']
    
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product_name,
                },
                'unit_amount': amount_cents,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session

if __name__ == "__main__":
    # LeadForge pricing
    products = {
        'starter': ('LeadForge Starter', 29700),  # $297
        'growth': ('LeadForge Growth', 79700),    # $797
        'scale': ('LeadForge Scale', 199700),    # $1997
    }
    
    if len(sys.argv) > 1:
        plan = sys.argv[1].lower()
        if plan in products:
            name, amount = products[plan]
            session = create_checkout_from_product(
                name, amount,
                'https://example.com/success',
                'https://example.com/cancel'
            )
            print(f"Created {name} checkout:")
            print(session.url)
        else:
            print(f"Unknown plan: {plan}")
            print(f"Available: {list(products.keys())}")
    else:
        # Default: create starter checkout
        session = create_checkout_from_product(
            'LeadForge Starter', 29700,
            'https://example.com/success',
            'https://example.com/cancel'
        )
        print(f"LeadForge Starter checkout:")
        print(session.url)
