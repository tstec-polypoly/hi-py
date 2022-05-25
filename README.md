# hi-py

Learn to deploy a simple Python "Hello, World!" script into Kubernetes.

## Prerequisites

### Docker Desktop (All Platforms)

https://www.docker.com/products/docker-desktop/

### MacOS

1. Install homebrew. https://brew.sh/
1. `brew install kind`
1. `kind create cluster --name k8s-hello-world --config kind.yml`

### Windows

1. Install chocolatey. https://chocolatey.org/install
1. `choco install kind`
1. `kind create cluster --name k8s-hello-world --config kind.yml`

## Inspecting the Cluster

```
# kubectl get nodes -A
NAME                            STATUS   ROLES           AGE   VERSION
k8s-hello-world-control-plane   Ready    control-plane   63s   v1.24.0
k8s-hello-world-worker          Ready    <none>          41s   v1.24.0
k8s-hello-world-worker2         Ready    <none>          42s   v1.24.0
```

```
# kubectl get pods -A
NAMESPACE            NAME                                                    READY   STATUS    RESTARTS   AGE
kube-system          coredns-6d4b75cb6d-89n7g                                1/1     Running   0          33s
kube-system          coredns-6d4b75cb6d-lbtsn                                1/1     Running   0          33s
kube-system          etcd-k8s-hello-world-control-plane                      1/1     Running   0          49s
kube-system          kindnet-8tzjz                                           1/1     Running   0          33s
kube-system          kindnet-d9tvn                                           1/1     Running   0          29s
kube-system          kindnet-lcp6t                                           1/1     Running   0          28s
kube-system          kube-apiserver-k8s-hello-world-control-plane            1/1     Running   0          48s
kube-system          kube-controller-manager-k8s-hello-world-control-plane   1/1     Running   0          49s
kube-system          kube-proxy-lnqvv                                        1/1     Running   0          28s
kube-system          kube-proxy-mxpx6                                        1/1     Running   0          29s
kube-system          kube-proxy-pxvs2                                        1/1     Running   0          33s
kube-system          kube-scheduler-k8s-hello-world-control-plane            1/1     Running   0          47s
local-path-storage   local-path-provisioner-9cd9bd544-2dm9t                  1/1     Running   0          33s
```

## Enable Deployment

`kubectl apply -f hi-py-deployment.yml`

## Inspect Deployment

```
# kubectl get deployments
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
hi-py-deployment   0/2     2            0           10s
```

## Enable NodePort Service

```
kubectl apply -f hi-py-service.yml
```

## Inspect Service

```
# kubectl get services
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
hi-py-service   NodePort    10.96.40.242   <none>        8080:30000/TCP   17s
kubernetes      ClusterIP   10.96.0.1      <none>        443/TCP          2m4s
```

## Test Service

```
# curl localhost:30000
Hello, world!%
```

## Modify Deployment

In `hi-py-deployment.yml` edit the following:

From: `command: [ "python", "hi.py", "-pworld" ]`

To: `command: [ "python", "hi.py", "-ppolypoly" ]`

Then, re-apply the deployment with `kubectl apply -f hi-py-deployment.yml`

## Test Service

```
# curl localhost:30000
Hello, polypoly!%
```

## Cleanup

`kind delete cluster --name k8s-hello-world`
