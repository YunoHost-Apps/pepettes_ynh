#!/usr/bin/env python3

ENV = "production"
PORT = __PORT__
DOMAIN = "https://__DOMAIN__"
SECRET_KEY = "__SECRET__"
SECRET_CSRF_KEY = "__CSRF_KEY__"
LANGUAGES = ["en", "fr"]
BABEL_TRANSLATION_DIRECTORIES = "locales"

# Customization
CUSTOM = {
    "name": "__PROJECT_NAME__",
    "contact_url": "__CONTACT_URL__",
    "logo": "__LOGO__",
    "favicon": "__FAVICON__",
    "currencies": [("EUR", "€"), ("USD", "$")],
}

# Stripe keys
CUSTOM["stripe_publishable_key"] = "__PUBLISHABLE_KEY__"
STRIPE_SECRET_KEY = "__SECRET_KEY__"

# Stripe subscription data
DONATION = {"one_time": {}, "recuring": {}}
