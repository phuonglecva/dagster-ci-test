namespace=default
sa=test2
role=role-test2
# echo ${namespace}
kubectl -n ${namespace} create serviceaccount ${sa} &&
    kubectl -n ${namespace} create rolebinding ${role} --clusterrole=cluster-admin --serviceaccount=${namespace}:${sa} &&
    kubectl -n ${namespace} get serviceaccount ${sa}
# kubectl -n ${namespace} get secrets jenkins-robot-token-d6d8z -o go-template --template '{{index .data "token"}}' | base64 -d
