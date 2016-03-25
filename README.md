Build kubernetes rpm binaries
-------------

- git clone --recursive https://github.com/khogeland/kubernetes-rpm-builder
- sudo yum install rpm-build golang etcd
- sudo yum groupinstall "Development Tools"
- cd kubernetes-rpm-builder; ./build_latest_stable_kubernetes.sh v1.2.0;
