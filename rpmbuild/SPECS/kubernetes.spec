#debuginfo not supported with Go
%global debug_package	%{nil}
%global provider	github
%global provider_tld	com
%global project		GoogleCloudPlatform
%global repo		kubernetes
%global import_path	%{provider}.%{provider_tld}/%{project}/%{repo}
%global commit          6b0d4ffed36adb0e2585333f01a553ab3e0970fd
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

#I really need this, otherwise "version_ldflags=$(kube::version_ldflags)"
# does not work
%global _buildshell	/bin/bash
%global _checkshell	/bin/bash

Name:		kubernetes
Version:        v0.19.0
Release:	git%{shortcommit}%{?dist}
Summary:	Container cluster management
License:	ASL 2.0
URL:		https://github.com/GoogleCloudPlatform/kubernetes
ExclusiveArch:	x86_64
Source0:	https://github.com/GoogleCloudPlatform/kubernetes/archive/%{commit}/kubernetes-%{shortcommit}.tar.gz
#Patch0:		No-Nicer-error-msg-if-stdlib-pkg-with-cgo-flag-is-no.patch

# cadvisor is integrated into kubelet
Obsoletes:      cadvisor

%if 0%{?fedora} >= 21 || 0%{?rhel}
Requires:	docker
%else
Requires:	docker-io
%endif

Requires(pre):	shadow-utils

BuildRequires:	golang >= 1.2-7
BuildRequires:	systemd
BuildRequires:	etcd >= 2.0.8
BuildRequires:	hostname
BuildRequires:	rsync

%if 0%{?fedora}
# needed for go cover.  Not available in RHEL/CentOS (available in Fedora/EPEL)
BuildRequires:	golang-cover
%endif

%description
%{summary}

%if 0%{?fedora}
%package devel
Summary:	%{summary}
BuildRequires:	golang >= 1.2.1-3

%description devel
%{summary}

Provides: golang(%{import_path}/cmd/kube-apiserver/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kube-controller-manager/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kube-proxy/app) = %{version}-%{release}
Provides: golang(%{import_path}/cmd/kubelet/app) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/admission) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/endpoints) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/errors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/errors/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/meta) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/resource) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/rest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/rest/resttest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/testapi) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/testing) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/v1beta1) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/v1beta2) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/v1beta3) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/api/validation) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/apiserver) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authenticator) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authenticator/bearertoken) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authorizer) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/authorizer/abac) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/handlers) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/auth/user) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/capabilities) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/cache) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/clientcmd/api/v1) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/portforward) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/record) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/remotecommand) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/client/testclient) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/clientauth) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/aws) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/fake) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/gce) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/openstack) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/ovirt) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/rackspace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/cloudprovider/vagrant) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/controller/framework) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/conversion) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/credentialprovider) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/credentialprovider/gcp) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/fields) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/healthz) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/httplog) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/hyperkube) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/cmd/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubectl/resource) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/cadvisor) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/container) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/dockertools) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/envvars) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/leaky) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/network) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/kubelet/network/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/labels) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/master) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/master/ports) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/namespace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/http) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/probe/tcp) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/proxy) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/proxy/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/controller) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/controller/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/endpoint) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/endpoint/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/event) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/generic/rest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/limitrange) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/minion) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/minion/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/namespace) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/namespace/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolume) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolume/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolumeclaim) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/persistentvolumeclaim/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/pod) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/pod/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/registrytest) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/resourcequota/etcd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/secret) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/registry/service) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/runtime) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/scheduler) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/service) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/tools) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/types) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ui) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/config) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/errors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/exec) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/fielderrors) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/flushwriter) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/httpstream) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/httpstream/spdy) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/iptables) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/mount) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/slice) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/strategicpatch) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/wait) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/util/yaml) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/version) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/version/verflag) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/empty_dir) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/gce_pd) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/git_repo) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/glusterfs) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/host_path) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/iscsi) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/nfs) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/volume/secret) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/watch) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/watch/json) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/cmd/kube-scheduler/app) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/admit) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/deny) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/limitranger) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/autoprovision) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/exists) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/namespace/lifecycle) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/admission/resourcequota) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/password) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/password/allow) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/basicauth) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/union) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/request/x509) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/token/tokenfile) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/auth/authenticator/token/tokentest) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithmprovider) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/algorithmprovider/defaults) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/latest) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/v1) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/api/validation) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/factory) = %{version}-%{release}
Provides: golang(%{import_path}/plugin/pkg/scheduler/metrics) = %{version}-%{release}
Provides: golang(%{import_path}/test/e2e) = %{version}-%{release}
Provides: golang(%{import_path}/test/integration) = %{version}-%{release}
Provides: golang(%{import_path}/third_party/forked/json) = %{version}-%{release}
Provides: golang(%{import_path}/third_party/forked/reflect) = %{version}-%{release}
Provides: golang(%{import_path}/third_party/golang/netutil) = %{version}-%{release}

This package contains library source intended for
building other packages which use %{project}/%{repo}.
%endif

%prep
%autosetup -n %{name}-%{commit} -p1

%build
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_COMMIT=%{commit}
export KUBE_GIT_VERSION=v0.15.0-123-g0ea87e48640729

%if 0%{?fedora}
#export KUBE_GIT_TREE_STATE="dirty"
#export KUBE_EXTRA_GOPATH=%{gopath}
#export KUBE_NO_GODEPS="true"
%endif

hack/build-go.sh --use_go_build

%check
%if 0%{?fedora}
#export KUBE_EXTRA_GOPATH=%{gopath}
#export KUBE_NO_GODEPS="true"
%endif

echo "******Testing the commands*****"
# run the test only if /fs/sys/cgroup is mounted
if [ -d /sys/fs/cgroup ]; then
	hack/test-cmd.sh
fi
echo "******Benchmarking kube********"
hack/benchmark-go.sh

# In Fedora 20 and RHEL7 the go cover tools isn't available correctly
%if 0%{?fedora} >= 21
echo "******Testing the go code******"
hack/test-go.sh
echo "******Testing integration******"
#hack/test-integration.sh --use_go_build
%endif

%install
. hack/lib/init.sh
kube::golang::setup_env

output_path="${KUBE_OUTPUT_BINPATH}/$(kube::golang::current_platform)"

binaries=(kube-apiserver kube-controller-manager kube-scheduler kube-proxy kubelet kubectl)
install -m 755 -d %{buildroot}%{_bindir}
for bin in "${binaries[@]}"; do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/${bin}
done

# install the bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
install -t %{buildroot}%{_datadir}/bash-completion/completions/ contrib/completions/bash/kubectl

# install config files
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -t %{buildroot}%{_sysconfdir}/%{name} contrib/init/systemd/environ/*

# install service files
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 -t %{buildroot}%{_unitdir} contrib/init/systemd/*.service

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 docs/man/man1/* %{buildroot}%{_mandir}/man1

# install the place the kubelet defaults to put volumes
install -d %{buildroot}/var/lib/kubelet

# place contrib/init/systemd/tmpfiles.d/kubernetes.conf to /usr/lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %{buildroot}%{_tmpfilesdir}
install -p -m 0644 -t %{buildroot}/%{_tmpfilesdir} contrib/init/systemd/tmpfiles.d/kubernetes.conf

%if 0%{?fedora}
# install devel source codes
install -d %{buildroot}/%{gopath}/src/%{import_path}
for d in build cluster cmd contrib examples hack pkg plugin test; do
    cp -rpav $d %{buildroot}/%{gopath}/src/%{import_path}/
done
%endif

%files
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%{_mandir}/man1/*
%{_bindir}/kube-apiserver
%{_bindir}/kubectl
%{_bindir}/kube-controller-manager
%{_bindir}/kubelet
%{_bindir}/kube-proxy
%{_bindir}/kube-scheduler
%{_unitdir}/kube-apiserver.service
%{_unitdir}/kubelet.service
%{_unitdir}/kube-scheduler.service
%{_unitdir}/kube-controller-manager.service
%{_unitdir}/kube-proxy.service
%dir %{_sysconfdir}/%{name}
%{_datadir}/bash-completion/completions/kubectl
%dir /var/lib/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/config
%config(noreplace) %{_sysconfdir}/%{name}/apiserver
%config(noreplace) %{_sysconfdir}/%{name}/controller-manager
%config(noreplace) %{_sysconfdir}/%{name}/proxy
%config(noreplace) %{_sysconfdir}/%{name}/kubelet
%config(noreplace) %{_sysconfdir}/%{name}/scheduler
%{_tmpfilesdir}/kubernetes.conf

%if 0%{?fedora}
%files devel
%doc README.md LICENSE CONTRIB.md CONTRIBUTING.md DESIGN.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}
%endif

%pre
getent group kube >/dev/null || groupadd -r kube
getent passwd kube >/dev/null || useradd -r -g kube -d / -s /sbin/nologin \
        -c "Kubernetes user" kube
%post
%systemd_post kube-apiserver kube-scheduler kube-controller-manager kubelet kube-proxy

%preun
%systemd_preun kube-apiserver kube-scheduler kube-controller-manager kubelet kube-proxy

%postun
%systemd_postun

%changelog
* Fri Apr 17 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-0.3.git0ea87e4
- Obsolete cadvisor
  related: #1199219

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-0.2.git0ea87e4
- Bump to upstream 0ea87e486407298dc1e3126c47f4076b9022fb09
  related: #1199219

* Tue Apr 14 2015 jchaloup <jchaloup@redhat.com> - 0.15.0-0.1.gitd02139d
- Bump to upstream d02139d2b454ecc5730cc535d415c1963a7fb2aa
  related: #1211266

* Sun Apr 12 2015 jchaloup <jchaloup@redhat.com> - 0.14.2-0.2.gitd577db9
- Bump to upstream d577db99873cbf04b8e17b78f17ec8f3a27eca30

* Wed Apr 08 2015 jchaloup <jchaloup@redhat.com> - 0.14.2-0.1.git2719194
- Bump to upstream 2719194154ffd38fd1613699a9dd10a00909957e
  Use etcd-2.0.8 and higher

* Tue Apr 07 2015 jchaloup <jchaloup@redhat.com> - 0.14.1-0.2.gitd2f4734
- Bump to upstream d2f473465738e6b6f7935aa704319577f5e890ba

* Thu Apr 02 2015 jchaloup <jchaloup@redhat.com> - 0.14.1-0.1.gita94ffc8
- Bump to upstream a94ffc8625beb5e2a39edb01edc839cb8e59c444
  resolves: #1199219

* Wed Apr 01 2015 jchaloup <jchaloup@redhat.com> - 0.14.0-0.2.git8168344
- Bump to upstream 81683441b96537d4b51d146e39929b7003401cd5

* Tue Mar 31 2015 jchaloup <jchaloup@redhat.com> - 0.14.0-0.1.git9ed8761
- Bump to upstream 9ed87612d07f75143ac96ad90ff1ff68f13a2c67
- Remove [B]R from devel branch until the package has stable API

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.6.git8a7a127
- Bump to upstream 8a7a127352263439e22253a58628d37a93fdaeb2

* Fri Mar 27 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.5.git8d94c43
- Bump to upstream 8d94c43e705824f23791b66ad5de4ea095d5bb32
  resolves: #1205362

* Wed Mar 25 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.4.git455fe82
- Bump to upstream 455fe8235be8fd9ba0ce21bf4f50a69d42e18693

* Mon Mar 23 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.3.gitef75888
- Remove runtime dependency on etcd
  resolves: #1202923

* Sun Mar 22 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.2.gitef75888
- Bump to upstream ef758881d108bb53a128126c503689104d17f477

* Fri Mar 20 2015 jchaloup <jchaloup@redhat.com> - 0.13.2-0.1.gita8f2cee
- Bump to upstream a8f2cee8c5418676ee33a311fad57d6821d3d29a

* Fri Mar 13 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.9.git53b25a7
- Bump to upstream 53b25a7890e31bdec6f2a95b32200d6cc27ae2ca
  fix kube-proxy.service and kubelet
  resolves: #1200919 #1200924

* Fri Mar 13 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.8.git39dceb1
- Bump to upstream 39dceb13a511a83963a766a439cb386d10764310

* Thu Mar 12 2015 Eric Paris <eparis@redhat.com> - 0.12.0-0.7.gita3fd0a9
- Move from /etc/tmpfiles.d to %{_tmpfilesdir}
  resolves: #1200969

* Thu Mar 12 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.6.gita3fd0a9
- Place contrib/init/systemd/tmpfiles.d/kubernetes.conf to /etc/tmpfiles.d/kubernetes.conf

* Thu Mar 12 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.5.gita3fd0a9
- Bump to upstream a3fd0a9fd516bb6033f32196ae97aaecf8c096b1

* Tue Mar 10 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.4.gita4d871a
- Bump to upstream a4d871a10086436557f804930812f2566c9d4d39

* Fri Mar 06 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.3.git2700871
- Bump to upstream 2700871b049d5498167671cea6de8317099ad406

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.2.git8b627f5
- Bump to upstream 8b627f516fd3e4f62da90d401ceb3d38de6f8077

* Tue Mar 03 2015 jchaloup <jchaloup@redhat.com> - 0.12.0-0.1.gitecca426
- Bump to upstream ecca42643b91a7117de8cd385b64e6bafecefd65

* Mon Mar 02 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.5.git6c5b390
- Bump to upstream 6c5b390160856cd8334043344ef6e08568b0a5c9

* Sat Feb 28 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.4.git0fec31a
- Bump to upstream 0fec31a11edff14715a1efb27f77262a7c3770f4

* Fri Feb 27 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.3.git08402d7
- Bump to upstream 08402d798c8f207a2e093de5a670c5e8e673e2de

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.2.git86434b4
- Bump to upstream 86434b4038ab87ac40219562ad420c3cc58c7c6b

* Tue Feb 24 2015 jchaloup <jchaloup@redhat.com> - 0.11.0-0.1.git754a2a8
- Bump to upstream 754a2a8305c812121c3845d8293efdd819b6a704
  turn off integration tests until "FAILED: unexpected endpoints:
  timed out waiting for the condition" problem is resolved
  Adding back devel subpackage ([B]R list outdated)

* Fri Feb 20 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.3.git4c87805
- Bump to upstream 4c87805870b1b22e463c4bd711238ef68c77f0af

* Tue Feb 17 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.2.git6f84bda
- Bump to upstream 6f84bdaba853872dbac69c84d3ab4b6964e85d8c

* Tue Feb 17 2015 jchaloup <jchaloup@redhat.com> - 0.10.1-0.1.git7d6130e
- Bump to upstream 7d6130edcdfabd7dd2e6a06fdc8fe5e333f07f5c

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.7.gitc9c98ab
- Bump to upstream c9c98ab19eaa6f0b2ea17152c9a455338853f4d0
  Since some dependencies are broken, we can not build Kubernetes from Fedora deps.
  Switching to vendored source codes until Go draft is resolved

* Wed Feb 04 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.6.git7f5ed54
- Bump to upstream 7f5ed541f794348ae6279414cf70523a4d5133cc

* Tue Feb 03 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.5.git2ac6bbb
- Bump to upstream 2ac6bbb7eba7e69eac71bd9acd192cda97e67641

* Mon Feb 02 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.4.gite335e2d
- Bump to upstream e335e2d3e26a9a58d3b189ccf41ceb3770d1bfa9

* Fri Jan 30 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.3.git55793ac
- Bump to upstream 55793ac2066745f7243c666316499e1a8cf074f0

* Thu Jan 29 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.2.gitca6de16
- Bump to upstream ca6de16df7762d4fc9b4ad44baa78d22e3f30742

* Tue Jan 27 2015 jchaloup <jchaloup@redhat.com> - 0.9.1-0.1.git3623a01
- Bump to upstream 3623a01bf0e90de6345147eef62894057fe04b29
- update tests for etcd-2.0

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0.8.2-571.gitb2f287c
+- Bump to upstream b2f287c259d856f4c08052a51cd7772c563aff77

* Thu Jan 22 2015 Eric Paris <eparis@redhat.com> - 0.8.2-570.gitb2f287c
- patch kubelet service file to use docker.service not docker.socket

* Wed Jan 21 2015 jchaloup <jchaloup@redhat.com> - 0.8.2-0.1.git5b04640
- Bump to upstream 5b046406a957a1e7eda7c0c86dd7a89e9c94fc5f

* Sun Jan 18 2015 jchaloup <jchaloup@redhat.com> - 0.8.0-126.0.git68298f0
- Add some missing dependencies
- Add devel subpackage

* Fri Jan 09 2015 Eric Paris <eparis@redhat.com> - 0.8.0-125.0.git68298f0
- Bump to upstream 68298f08a4980f95dfbf7b9f58bfec1808fb2670

* Tue Dec 16 2014 Eric Paris <eparis@redhat.com> - 0.7.0-18.0.git52e165a
- Bump to upstream 52e165a4fd720d1703ebc31bd6660e01334227b8

* Mon Dec 15 2014 Eric Paris <eparis@redhat.com> - 0.6-297.0.git5ef34bf
- Bump to upstream 5ef34bf52311901b997119cc49eff944c610081b

* Wed Dec 03 2014 Eric Paris <eparis@redhat.com>
- Replace patch to use old googlecode/go.net/ with BuildRequires on golang.org/x/net/

* Tue Dec 02 2014 Eric Paris <eparis@redhat.com> - 0.6-4.0.git993ef88
- Bump to upstream 993ef88eec9012b221f79abe8f2932ee97997d28

* Mon Dec 01 2014 Eric Paris <eparis@redhat.com> - 0.5-235.0.git6aabd98
- Bump to upstream 6aabd9804fb75764b70e9172774002d4febcae34

* Wed Nov 26 2014 Eric Paris <eparis@redhat.com> - 0.5-210.0.gitff1e9f4
- Bump to upstream ff1e9f4c191342c24974c030e82aceaff8ea9c24

* Tue Nov 25 2014 Eric Paris <eparis@redhat.com> - 0.5-174.0.git64e07f7
- Bump to upstream 64e07f7fe03d8692c685b09770c45f364967a119

* Mon Nov 24 2014 Eric Paris <eparis@redhat.com> - 0.5-125.0.git162e498
- Bump to upstream 162e4983b947d2f6f858ca7607869d70627f5dff

* Fri Nov 21 2014 Eric Paris <eparis@redhat.com> - 0.5-105.0.git3f74a1e
- Bump to upstream 3f74a1e9f56b3c3502762930c0c551ccab0557ea

* Thu Nov 20 2014 Eric Paris <eparis@redhat.com> - 0.5-65.0.gitc6158b8
- Bump to upstream c6158b8aa9c40fbf1732650a8611429536466b21
- include go-restful build requirement

* Tue Nov 18 2014 Eric Paris <eparis@redhat.com> - 0.5-14.0.gitdf0981b
- Bump to upstream df0981bc01c5782ad30fc45cb6f510f365737fc1

* Tue Nov 11 2014 Eric Paris <eparis@redhat.com> - 0.4-680.0.git30fcf24
- Bump to upstream 30fcf241312f6d0767c7d9305b4c462f1655f790

* Mon Nov 10 2014 Eric Paris <eparis@redhat.com> - 0.4-633.0.git6c70227
- Bump to upstream 6c70227a2eccc23966d32ea6d558ee05df46e400

* Fri Nov 07 2014 Eric Paris <eparis@redhat.com> - 0.4-595.0.gitb695650
- Bump to upstream b6956506fa2682afa93770a58ea8c7ba4b4caec1

* Thu Nov 06 2014 Eric Paris <eparis@redhat.com> - 0.4-567.0.git3b1ef73
- Bump to upstream 3b1ef739d1fb32a822a22216fb965e22cdd28e7f

* Thu Nov 06 2014 Eric Paris <eparis@redhat.com> - 0.4-561.0.git06633bf
- Bump to upstream 06633bf4cdc1ebd4fc848f85025e14a794b017b4
- Make spec file more RHEL/CentOS friendly

* Tue Nov 04 2014 Eric Paris <eparis@redhat.com - 0.4-510.0.git5a649f2
- Bump to upstream 5a649f2b9360a756fc8124897d3453a5fa9473a6

* Mon Nov 03 2014 Eric Paris <eparis@redhat.com - 0.4-477.0.gita4abafe
- Bump to upstream a4abafea02babc529c9b5b9c825ba0bb3eec74c6

* Mon Nov 03 2014 Eric Paris <eparis@redhat.com - 0.4-453.0.git808be2d
- Bump to upstream 808be2d13b7bf14a3cf6985bc7c9d02f48a3d1e0
- Includes upstream change to remove --machines from the APIServer
- Port to new build system
- Start running %check tests again

* Fri Oct 31 2014 Eric Paris <eparis@redhat.com - 0.4+-426.0.gita18cdac
- Bump to upstream a18cdac616962a2c486feb22afa3538fc3cf3a3a

* Thu Oct 30 2014 Eric Paris <eparis@redhat.com - 0.4+-397.0.git78df011
- Bump to upstream 78df01172af5cc132b7276afb668d31e91e61c11

* Wed Oct 29 2014 Eric Paris <eparis@redhat.com - 0.4+-0.9.git8e1d416
- Bump to upstream 8e1d41670783cb75cf0c5088f199961a7d8e05e5

* Tue Oct 28 2014 Eric Paris <eparis@redhat.com - 0.4-0.8.git1c61486
- Bump to upstream 1c61486ec343246a81f62b4297671217c9576df7

* Mon Oct 27 2014 Eric Paris <eparis@redhat.com - 0.4-0.7.gitdc7e3d6
- Bump to upstream dc7e3d6601a89e9017ca9db42c09fd0ecb36bb36

* Fri Oct 24 2014 Eric Paris <eparis@redhat.com - 0.4-0.6.gite46af6e
- Bump to upstream e46af6e37f6e6965a63edb8eb8f115ae8ef41482

* Thu Oct 23 2014 Eric Paris <eparis@redhat.com - 0.4-0.5.git77d2815
- Bump to upstream 77d2815b86e9581393d7de4379759c536df89edc

* Wed Oct 22 2014 Eric Paris <eparis@redhat.com - 0.4-0.4.git97dd730
- Bump to upstream 97dd7302ac2c2b9458a9348462a614ebf394b1ed
- Use upstream kubectl bash completion instead of in-repo
- Fix systemd_post and systemd_preun since we are using upstream service files

* Tue Oct 21 2014 Eric Paris <eparis@redhat.com - 0.4-0.3.gite868642
- Bump to upstream e8686429c4aa63fc73401259c8818da168a7b85e

* Mon Oct 20 2014 Eric Paris <eparis@redhat.com - 0.4-0.2.gitd5377e4
- Bump to upstream d5377e4a394b4fc6e3088634729b538eac124b1b
- Use in tree systemd unit and Environment files
- Include kubectl bash completion from outside tree

* Fri Oct 17 2014 Eric Paris <eparis@redhat.com - 0.4-0.1.gitb011263
- Bump to upstream b01126322b826a15db06f6eeefeeb56dc06db7af
- This is a major non backward compatible change.

* Thu Oct 16 2014 Eric Paris <eparis@redhat.com> - 0.4-0.0.git4452163
- rebase to v0.4
- include man pages

* Tue Oct 14 2014 jchaloup <jchaloup@redhat.com> - 0.3-0.3.git98ac8e1
- create /var/lib/kubelet
- Use bash completions from upstream
- Bump to upstream 98ac8e178fcf1627399d659889bcb5fe25abdca4
- all by Eric Paris

* Mon Sep 29 2014 Jan Chaloupka <jchaloup@redhat.com> - 0.3-0.2.git88fdb65
- replace * with coresponding files
- remove dependency on gcc

* Wed Sep 24 2014 Eric Paris <eparis@redhat.com - 0.3-0.1.git88fdb65
- Bump to upstream 88fdb659bc44cf2d1895c03f8838d36f4d890796

* Tue Sep 23 2014 Eric Paris <eparis@redhat.com - 0.3-0.0.gitbab5082
- Bump to upstream bab5082a852218bb65aaacb91bdf599f9dd1b3ac

* Fri Sep 19 2014 Eric Paris <eparis@redhat.com - 0.2-0.10.git06316f4
- Bump to upstream 06316f486127697d5c2f5f4c82963dec272926cf

* Thu Sep 18 2014 Eric Paris <eparis@redhat.com - 0.2-0.9.gitf7a5ec3
- Bump to upstream f7a5ec3c36bd40cc2216c1da331ab647733769dd

* Wed Sep 17 2014 Eric Paris <eparis@redhat.com - 0.2-0.8.gitac8ee45
- Try to intelligently determine the deps

* Wed Sep 17 2014 Eric Paris <eparis@redhat.com - 0.2-0.7.gitac8ee45
- Bump to upstream ac8ee45f4fc4579b3ed65faafa618de9c0f8fb26

* Mon Sep 15 2014 Eric Paris <eparis@redhat.com - 0.2-0.5.git24b5b7e
- Bump to upstream 24b5b7e8d3a8af1eecf4db40c204e3c15ae955ba

* Thu Sep 11 2014 Eric Paris <eparis@redhat.com - 0.2-0.3.gitcc7999c
- Bump to upstream cc7999c00a40df21bd3b5e85ecea3b817377b231

* Wed Sep 10 2014 Eric Paris <eparis@redhat.com - 0.2-0.2.git60d4770
- Add bash completions

* Wed Sep 10 2014 Eric Paris <eparis@redhat.com - 0.2-0.1.git60d4770
- Bump to upstream 60d4770127d22e51c53e74ca94c3639702924bd2

* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1-0.4.git6ebe69a
- prefer autosetup instead of setup (revert setup change in 0-0.3.git)
https://fedoraproject.org/wiki/Autosetup_packaging_draft
- revert version number to 0.1

* Mon Sep 08 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.3.git6ebe69a
- gopath defined in golang package already
- package owns /etc/kubernetes
- bash dependency implicit
- keep buildroot/$RPM_BUILD_ROOT macros consistent
- replace with macros wherever possible
- set version, release and source tarball prep as per
https://fedoraproject.org/wiki/Packaging:SourceURL#Github

* Mon Sep 08 2014 Eric Paris <eparis@redhat.com>
- make services restart automatically on error

* Sat Sep 06 2014 Eric Paris <eparis@redhat.com - 0.1-0.1.0.git6ebe69a8
- Bump to upstream 6ebe69a8751508c11d0db4dceb8ecab0c2c7314a

* Wed Aug 13 2014 Eric Paris <eparis@redhat.com>
- update to upstream
- redo build to use project scripts
- use project scripts in %check
- rework deletion of third_party packages to easily detect changes
- run apiserver and controller-manager as non-root

* Mon Aug 11 2014 Adam Miller <maxamillion@redhat.com>
- update to upstream
- decouple the rest of third_party

* Thu Aug 7 2014 Eric Paris <eparis@redhat.com>
- update to head
- update package to include config files

* Wed Jul 16 2014 Colin Walters <walters@redhat.com>
- Initial package
