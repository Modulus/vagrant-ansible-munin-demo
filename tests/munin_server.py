import pytest

def test_node_service_should_not_run(host):
    service = host.service("munin")

    assert service.is_enabled
    assert service.is_running == False

@pytest.mark.parametrize("folder", [
("/var/lib/munin"),
('/var/cache/munin/www')
# ("/var/www/html/munin"),
("/var/log/munin"),
("/var/run/munin"),
("/etc/munin/munin-conf.d")
])
def test_munin_folders_present(host, folder):
    folder = host.file(folder)

    assert folder.exists
    assert folder.is_directory


def test_apache_running(host):
    apache = host.service("apache")

    assert apache.is_enabled
    assert apache.is_running
