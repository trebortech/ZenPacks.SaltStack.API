
from Products.ZenModel.ZenPack import ZenPackBase

import logging
log = logging.getLogger('zen.SaltStack')


MODULE_NAME = {}
CLASS_NAME = {}

for product_name in productNames:
    ZP_NAME = 'ZenPacks.SaltStack.API'
    MODULE_NAME[product_name] = '.'.join([ZP_NAME, product_name])
    CLASS_NAME[product_name] = '.'.join([ZP_NAME, product_name, product_name])


class ZenPack(ZenPackBase):

    def install(self, app):
        super(Zenpack, self).install(app)

    def remote(self, app, leaveObjects=False):
        """
        Remove SaltStack API
        """
        super(ZenPack, self).remove(app, leaveObjects=leaveObjects)
