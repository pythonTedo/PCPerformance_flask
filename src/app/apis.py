from flask import jsonify, Blueprint, current_app as app
import psutil

api_blueprint = Blueprint("api", __name__, static_folder="static", template_folder="templates")

olddata = {}
olddata["disk_write"] = 0
olddata["disk_read"] = 0
olddata["net_send"] = 0
olddata["net_recv"] = 0


@api_blueprint.route("/api/process", methods=["GET"])
def api_process():
    apidata = {}

    try:
        apidata["processes"] = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(
                    attrs=["pid", "name", "memory_percent", "num_threads", "cpu_times"]
                )
            except psutil.NoSuchProcess:
                pass
            
            else:
                apidata["processes"].append(pinfo)

    except Exception:
        pass
    return jsonify(apidata)

@api_blueprint.route("/api/monitor")
def api_monitor():
    apidata = {}
    apidata["cpu"] = psutil.cpu_percent(interval=0.9)
    apidata["mem"] = psutil.virtual_memory().percent
    apidata["disk"] = psutil.disk_usage("/").percent

    try:
        netio = psutil.net_io_counters()
        apidata["net_send"] = (0 if olddata["net_send"] == 0 else netio.bytes_sent - olddata["net_send"])
        olddata["net_send"] = netio.bytes_sent
        apidata["net_recv"] = (0 if olddata["net_recv"] == 0 else netio.bytes_sent - olddata["net_recv"])
        olddata["net_recv"] = netio.bytes_recv

    except Exception:
        apidata["net_send"] = -1
        apidata["net_recv"] = -1

    try:
        diskio = psutil.disk_io_counters()
        apidata["disk_write"] = (
            0
            if olddata["disk_write"] == 0
            else diskio.write_bytes - olddata["disk_write"]
        )
        olddata["disk_write"] = diskio.write_bytes
        apidata["disk_read"] = (
            0 if olddata["disk_read"] == 0 else diskio.read_bytes - olddata["disk_read"]
        )
        olddata["disk_read"] = diskio.read_bytes
    except Exception:
        apidata["disk_write"] = -1
        apidata["disk_read"] = -1

    return jsonify(apidata)
