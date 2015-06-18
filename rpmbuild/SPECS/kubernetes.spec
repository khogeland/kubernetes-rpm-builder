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
export KUBE_GIT_VERSION=v0.19.0

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