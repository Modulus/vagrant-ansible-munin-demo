# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  config.vm.define :controller do |controller|
    controller.vm.box = "bento/ubuntu-16.04"
    if Vagrant.has_plugin?("vagrant-cachier")
    	config.cache.scope = :box
    end

    controller.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "/vagrant/controller.yml"
    end
    controller.vm.network "private_network", ip: "192.168.13.101"

  end


  config.vm.define :node1 do |node1|
    node1.vm.box = "bento/ubuntu-16.04"
    node1.vm.network "private_network", ip: "192.168.13.102"
    if Vagrant.has_plugin?("vagrant-cachier")
    	config.cache.scope = :box
    end
  end

  config.vm.define :node2 do |node2|
    node2.vm.box = "bento/ubuntu-16.04"
    node2.vm.network "private_network", ip: "192.168.13.103"
    if Vagrant.has_plugin?("vagrant-cachier")
    	config.cache.scope = :box
    end
  end

end
