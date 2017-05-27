from app.models import User,MenuAuth
import json

class Auth(object):
    def __init__(self, user):
        self.user = user

    def auth_menus(self):
        menus = MenuAuth.query.order_by('sort').all()
        if str(self.user.group_id) == '1':
            return self.tree(menus)
        rules_str = self.user.group.rules
        rules = []
        if rules_str :
            rules = json.loads(rules_str)
        auth_menus = []
        for menu in menus:
            for rule in rules:
                if str(menu.id) == rule['id']:
                    auth_menus.append(menu)
        auth_menus = self.tree(auth_menus)
        return auth_menus

    def tree(self,data,pid = 0):
        tree_list = []
        for da in data:
            if str(da.parent) == str(pid):
                tmp = self.tree(data,da.id)
                if tmp :
                    da.child = tmp
                tree_list.append(da)
        return tree_list


