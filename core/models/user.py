from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import uuid
from core.models.rankme import Rankme


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(
        _('address'), max_length=100, blank=True, null=True)
    city = models.CharField(_('city'), max_length=60, blank=True, null=True)
    zipcode = models.CharField(
        _('zip code'), max_length=12, blank=True, null=True)
    phonenumber = models.CharField(
        _('first name'), max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=False, auto_now=True)
    steam_id = models.CharField(_('steam id'), max_length=40, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), unique=True,
                              help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                          '@/./+/-/_ only.'),
                              validators=[
        validators.RegexValidator(r'^[\w.@+-]+$',
                                  _('Enter a valid email address. '
                                    'This value may contain only letters, numbers '
                                    'and @/./+/-/_ characters.'), 'invalid'),
    ],
        error_messages={
            'unique': _("A user with that email already exists."),
    })
    dark_theme = models.BooleanField(default=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_customer = models.BooleanField(_('staff status'), default=False,
                                      help_text=_('Designates whether the user is a customer '
                                                  'site.'))
    is_admin = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user is a customer admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    class Meta:
        app_label = "core"

    def save(self, *args, **kwargs):
        print("FAKKING BEAVER!!!", self)
        try:
            # check if players has logged in with username on the server to find steam id
            player = Rankme.objects.get(name=self.username)
            self.steam_id = player.steam
            print(player)
        except:
            print("No user was found")
        super(CustomUser, self).save(*args, **kwargs)
