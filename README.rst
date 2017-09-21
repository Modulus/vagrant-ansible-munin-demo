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


Plugins needed
---------------
- Server
  - ansible-galaxy install geerlingguy.munin
  - ansible-galaxy install jpnewman.apache
- Node
  - ansible-galaxy install geerlingguy.munin-node

Setup nodes
--------------
ansible-playbook munin_server.yml --skip-tags ssl  

Running tests
-----------------
.. code:: bash
testinfra  --sudo --sudo-user=vagrant --hosts=vagrant@192.168.13.102,vagrant@192.168.13.103 tests/munin_node.py

NB!
----------------
*on controller run*
.. code:: bash
ssh-keygen -t rsa -b 2048 -C "controller"

copy this key to the nodes
