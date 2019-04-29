import re
import sys


class PID:

    def __init__(self, pid, pname, tname):
        self.pid = pid
        self.pname = pname
        self.tname = tname


class PIDTool:

    def __init__(self, adb_device, name):

        self.adb_device = adb_device
        self.name = name
        self.mainPID = self._find_main_pid()
        self.app_pids = dict()
        self.app_pids[0] = PID(0, "idle_proc", "idle_thread")
        self.system_pids = dict()
        self.binder_pids = dict()

        self._find_all_pid()

    def find_child_binder_threads(self, PID):

        res = self.adb_device.command("busybox ps -T | grep Binder | grep " + str(PID))
        res = res.splitlines()

        child_pids = []
        for line in res:
            if line.isspace():
                continue
            child_pids.append(int(re.findall(" *(\d+)", line)[0]))
        return child_pids

    def is_relevant_pid(self, pid):
        if pid in self.app_pids:
            return True
        if pid in self.system_pids:
            return True
        if pid in self.binder_pids:
            return True
        return False

    def _find_main_pid(self):

        res = self.adb_device.command("ps | grep " + self.name)
        if res == "":
            sys.exit('Need valid application name')

        regex_line = re.findall(" +(\d+) +\d+ +\d+ .+ ([^ ]+)$", res)
        pid = int(regex_line[0][0])
        pname = regex_line[0][1]

        return PID(pid, pname, "main")

    def _find_system_server_pids(self):
        # Get all processes except the system_server itself
        res = self.adb_device.command("busybox ps -T | grep /system/bin")
        res = res.splitlines()

        for line in res:
            if re.search("(Binder)", line):
                continue
            if line.isspace():
                continue
            if re.search("(grep)", line):
                continue

            regex_line = re.findall("(\d+) \d+ +\d+:\d+ ?({(.*)})? (.+)", line)
            pid = int(regex_line[0][0])
            if regex_line[0][1] == "":
                tname = pname = regex_line[0][3]
            else:
                tname = regex_line[0][2]
                pname = regex_line[0][3]

            self.system_pids[pid] = PID(pid, pname, tname)

    def _find_binder_pids(self):
        # Get all processes except the system_server itself
        res = self.adb_device.command("busybox ps -T | grep {Binder:")
        res = res.splitlines()

        for line in res:
            if line.isspace():
                continue
            if re.search("(grep)", line):
                continue

            regex_line = re.findall("(\d+) \d+ +\d+:\d+ {(Binder:(\d+)_.+)} (.+)", line)
            pid = int(regex_line[0][0])
            tname = regex_line[0][1]
            pname = regex_line[0][3]

            self.binder_pids[pid] = PID(pid, pname, tname)

            # Check that parent threads are in system server threads. This catches threads
            # such as the media codec which is commonly used but is not a system service
            parent_pid = int(regex_line[0][2])
            # process will be first line as it's PID will be lower than child threads and as
            # such will be higher is list
            if not any(proc == parent_pid for proc in self.system_pids.keys()):
                parent_thread = self.adb_device.command("busybox ps -T | grep " + str(parent_pid))
                parent_thread = parent_thread.splitlines()
                for l in parent_thread:
                    if "grep" not in l:
                        regex_line = re.findall("(\d+) \d+ +\d+:\d+ ({(.*)}.* )?(.+)$", l)
                        pid = int(regex_line[0][0])
                        pname = regex_line[0][3]
                        if not regex_line[0][2]:
                            tname = pname
                        else:
                            tname = regex_line[0][2]

                        self.system_pids[pid] = PID(pid, pname, tname)

    def _find_all_app_pids(self):

        res = self.adb_device.command("busybox ps -T | grep " + self.name)
        res = res.splitlines()

        for line in res:
            if re.search("(Binder)", line):
                continue
            if line.isspace():
                continue
            # remove grep process
            if re.search("(grep)", line):
                continue

            regex_line = re.findall("(\d+) \d+ +\d+:\d* {(.+)} (.+)", line)

            pid = int(regex_line[0][0])
            tname = regex_line[0][1]
            pname = regex_line[0][2]

            self.app_pids[pid] = PID(pid, pname, tname)

    def _find_all_pid(self):
        self._find_main_pid
        self._find_all_app_pids()
        self._find_system_server_pids()
        self._find_binder_pids()