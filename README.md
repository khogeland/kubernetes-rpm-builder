Build kubernetes rpm binaries
-------------

- git clone --recursive git@github.com:JohnTheodore/kubernetes-rpm-builder.git
- sudo yum install rpm-build golang etcd
- sudo yum groupinstall "Development Tools"
- cd kubernetes-rpm-builder; ./build_latest_stable_kubernetes.sh;