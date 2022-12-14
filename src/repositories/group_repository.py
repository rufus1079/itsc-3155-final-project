from src.models import db, Group
class group_repository:

    def get_all_groups(self):
        groups = Group.query.all()
        return groups

    def get_group_by_id(self, group_id):
        group = Group.query.get(group_id)
        return group

    def create_group(self, name, descript):
        group = Group(name, descript)
        db.session.add(group)
        db.session.commit()
        return group

    def search_groups_by_name(self, name):
        group = Group.query.filter(Group.name.ilike(f'%{name}%')).all()
        return group
    
    def search_groups_by_descript(self, descript):
        group = Group.query.filter(Group.name.ilike(f'%{descript}%')).all()
        return group
    
    def delete_group(self, id):
        group = Group.query.filter(Group.id == id)
        db.session.delete(group)
        db.session.commit()
        return group
    
    def update_group(self, id, name, descript):
        group = Group.query.filter(Group.id == id)
        group.name = name
        group.decript = descript
        db.session.commit

# Singleton to be used in other modules
group_repository_singleton = group_repository()