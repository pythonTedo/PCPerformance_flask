from flask import render_template, Blueprint

import cpuinfo
import psutil
import platform
import datetime

views_blueprint = Blueprint("views", __name__, template_folder="templates", static_folder="static")

@views_blueprint.route("/")
@views_blueprint.route("/home")
def index():
    return render_template("base.html")


@views_blueprint.route("/info")
def info():
    osinfo = {}
    osinfo["plat"] = platform
    osinfo["cpu"] = cpuinfo.get_cpu_info()
    osinfo["mem"] = psutil.virtual_memory()
    osinfo["net"] = psutil.net_if_addrs()
    osinfo["boottime"] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return render_template("info.html", info=osinfo)


@views_blueprint.route("/monitor")
def monitor():
    return render_template("monitor.html")
