

from ZenPacks.zenoss.Microsoft.Windows.zope_utils import BaseDevice

import logging
log = logging.getLogger('zen.SaltStack')


class Device(BaseDevice):
    """
    Add property to all devices
    """

    minionid = ''

    _properties = BaseDevice._properties + (
        {'id': 'minionid', 'label': 'SaltStack minion id', 'type': 'string', 'mode': 'w'},
    )
