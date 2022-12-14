from src.models import db, Group
class group_repository:

    def get_all_groups(self):
        groups = Group.query.all()
        return groups

    def get_group_by_id(self, movie_id):
        group = Group.query.get(movie_id)
        return group

    def create_group(self, name, descript):
        group = Group(name, descript)
        db.session.add(group)
        db.session.commit()
        return group

    def search_groups(self, title):
        movie = Group.query.filter(Group.name.ilike(f'%{title}%')).all()
        return movie


# Singleton to be used in other modules
group_repository_singleton = group_repository()