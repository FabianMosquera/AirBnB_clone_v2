#!/usr/bin/python3
"""distributes an archive to your web servers, using the function deploy """
from datetime import datetime
from fabric.api import *
from os import path

env.hosts = ['34.73.23.33', '34.236.145.76']


def do_pack():
    """Packs web_static into tgz"""
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + current_time + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        return file_path
    else:
        return None

def do_deploy(archive_path):
    """ Distributes an archive to the web servers """
    if not path.exists(archive_path):
        return False
    # split the path and get the second element in the list
    file_path = archive_path.split("/")[1]
    serv_folder = "/data/web_static/releases/" + file_path

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p " + serv_folder)
        run("sudo tar -xzf /tmp/" + file_path + " -C " + serv_folder + "/")
        run("sudo rm /tmp/" + file_path)
        run("sudo mv " + serv_folder + "/web_static/* " + serv_folder)
        run("sudo rm -rf " + serv_folder + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + serv_folder + " /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """distributes an archive to your web servers, using the function deploy"""
    file_path = do_pack()
    if file_path is None:
        return False

    return (do_deploy(file_path))
