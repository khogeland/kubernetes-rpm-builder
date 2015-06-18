#!/bin/bash

# sudo yum install rpm-build golang etcd -y
# sudo yum groupinstall "Development Tools" -y

# Find the latest tagged stable release in the master branch
cd kubernetes; git checkout master &> /dev/null; git reset --hard &> /dev/null; git pull &> /dev/null;
latest_stable_kubernetes_version=`git describe --abbrev=0 --tags|cut -c 2-`
latest_stable_kubernetes_commit="`git rev-list v${latest_stable_kubernetes_version}  | head -n 1`"
short_commit=`echo $latest_stable_kubernetes_commit | cut -c1-7`
cd ..;

# update the rpm spec file with the latest stable version and commit
sed -i "s/^Version:.*/Version:        ${latest_stable_kubernetes_version}/" rpmbuild/SPECS/kubernetes.spec
sed -i "s/^%global commit.*/%global commit          ${latest_stable_kubernetes_commit}/" rpmbuild/SPECS/kubernetes.spec
sed -i "s/^export KUBE_GIT_VERSION=.*/KUBE_GIT_VERSION=${latest_stable_kubernetes_version-${short_commit}}/" rpmbuild/SPECS/kubernetes.spec

# clean up any old builds. tar up the latest stable commit, and throw it into rpmbuild/SOURCES, and prepare for the build
cd kubernetes; git checkout $latest_stable_kubernetes_commit &> /dev/null; cd ..;
mkdir -p rpmbuild/SOURCES
rm -rf rpmbuild/BUILD rpmbuild/BUILDROOT rpmbuild/RPMS rpmbuild/SRPMS rpmbuild/SOURCES/kubernetes-*.tar.gz
tar -c kubernetes --transform s/kubernetes/kubernetes-$latest_stable_kubernetes_commit/ | gzip -9 &> "rpmbuild/SOURCES/kubernetes-${short_commit}.tar.gz"

# start compiling kubernetes
echo -e "Starting the compilation of kubernetes version: $latest_stable_kubernetes_version \n\n\n"
rpmbuild -ba --define "_topdir `pwd`/rpmbuild" rpmbuild/SPECS/kubernetes.spec

if [ $? -eq 0 ]
then
  rpm_file=`ls rpmbuild/RPMS/*/kubernetes*`
  echo -e "\n\n\nFinished compiling kubernetes version: $latest_stable_kubernetes_version \nThe file is located here: ./$rpm_file"
else
  echo -e "\n\n\nKubernetes compilation failed.\n" 
fi