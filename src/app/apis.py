from flask import jsonify, current_app as app
import psutil


olddata = {}
olddata["disk_write"] = 0
olddata["disk_read"] = 0
olddata["net_send"] = 0
olddata["net_recv"] = 0


@app.route("/api/process", methods=["GET"])
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