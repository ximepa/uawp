__author__ = 'ximepa'
from fabric.api import lcd, local


def prepare_deployment(branch_name):
    #local('python manage.py test django_project')
    local('git add -p && git commit') #


def deploy():
    with lcd('/path/to/my/prod/area/'):

        # With git...
        local('git pull ~/PycharmProjects/uawp/')

        # With both
        local('python manage.py migrate web')
        #local('python manage.py test myapp')
        #local('/my/command/to/restart/webserver')