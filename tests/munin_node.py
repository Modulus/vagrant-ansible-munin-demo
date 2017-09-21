def test_node_service(host):
    service = host.service("munin-node")

    assert service.is_enabled
    assert service.is_running


def test_log_files(host):
    log_file = host.file("/var/log/munin/munin-node.log")

    assert log_file.exists
    assert log_file.is_file

def test_pid_file(host):
    pid_file = host.file("/var/run/munin/munin-node.pid")

    assert pid_file.exists
    assert pid_file.is_file
