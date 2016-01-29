#!/usr/bin/env python
#coding:utf8
#get system info from psutil
#required:psutil
import psutil
import platform
import socket
import json

def SysInfo():

    try:
        ip   = socket.gethostbyname(socket.gethostname())
    except Exception:
        ip   = "unknown"

    version  = platform.linux_distribution()
    hostname = platform.uname()[1]   #hostname,eg:localhost.localdomain
    kernel   = platform.uname()[2]   #kernel version
    arch     = platform.uname()[4]   #eg:x86_64 amd64 win32

    Cpus     = psutil.cpu_count(logical=False)

    mem      = psutil.virtual_memory()
    total    = mem.total
    free     = mem.free
    buffers  = mem.buffers
    cached   = mem.cached
    UsedPer  = 100 * int(total - free - cached - buffers) / int(total)
    mem_total= str(total / 1024 / 1024) + 'M'
    mem_free = str(free / 1024 / 1024) + 'M'
    memused  = str(UsedPer) + '%'

    pid_nums = len(psutil.pids())

    return json.dumps({
        "Hostname": hostname,
        "Ip": ip,
        "SysVersion": version,
        "KernelVersion": kernel,
        "Arch": arch,
        "Cpus": Cpus,
        "Memory": {"Total":mem_total, "Free":mem_free, "UsedPercent":memused},
        "Pids": pid_nums
    })
