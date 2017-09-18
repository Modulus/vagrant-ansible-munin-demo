=======================
Ansible multinode setup
=======================

This setup has 3 nodes, 1 controller and 2 remote notes.


Tested with
-----------
Ansible 2.0.0 downloaded from .. vagrant: https://www.vagrantup.com/


How to use this
---------------
1. Open shell
2. vagrant up
3. vagrant ssh controller
4. cd /vagrant
5. ansible -i local -a "echo hello" all
