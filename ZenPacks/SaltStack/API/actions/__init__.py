

from Products.ZenModel.actions import IActionBase, TargetableAction

import logging
log = logging.getLogger('zen.SaltStack')


class SaltStackAPI(IActionBase, TargetableAction):
    implements(IAction)

    id = 'saltstack'
    name = 'SaltStack'
    actionContentInfo = 