ENV = 'production'
PORT = __PORT__
DOMAIN = 'https://__DOMAIN__'
SECRET_KEY = '__SECRET__'
SECRET_CSRF_KEY = '__CSRF_KEY__'
LANGUAGES = ['en', 'fr']
BABEL_TRANSLATION_DIRECTORIES = 'locales'

# Customization
CUSTOM = {}
CUSTOM['name'] = '__PROJECT_NAME__'
CUSTOM['contact_url'] = '__CONTACT_URL__'
CUSTOM['logo'] = '__LOGO__'
CUSTOM['favicon'] = '__FAVICON__'
CUSTOM['currencies'] = [
    ('EUR', '€'),
    ('USD', '$')
]

# Stripe keys
CUSTOM['stripe_publishable_key'] = '__PUBLISHABLE_KEY__'
STRIPE_SECRET_KEY = '__SECRET_KEY__'

# Stripe subscription data
DONATION={'one_time':{}, 'recuring': {}}
