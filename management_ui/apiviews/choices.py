from django.utils.translation import gettext as _

STATUS_CHOICES = (
    ("New", _("New")),
    ("Alpha", _("Alpha")),
    ("Beta", _("Beta")),
    ("Active", _("Active")),
    ("Down", _("Down")),
    ("Retired", _("Retired"))
)

STATE_CHOICES = (
    ("ACT", _("ACT")),
    ("NSW", _("NSW")),
    ("NT", _("NT")),
    ("QLD", _("QLD")),
    ("TAS", _("TAS")),
    ("VIC", _("VIC")),
    ("WA", _("WA"))
)
