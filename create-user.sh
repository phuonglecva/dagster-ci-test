USERNAME=admin
openssl genrsa -out ${USERNAME}.key 4096 &&
openssl req -new -key ${USERNAME}.key -out ${USERNAME}.csr -subj "/CN=${USERNAME}/O=example:masters" &&
crs=$(cat ${USERNAME}.csr | base64 | tr -d '\n')
cat > ${USERNAME}.yaml << EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
    name: ${USERNAME}-csr
spec:
    groups:
    - system:authenticated
    request: ${crs}
    signerName: kubernetes.io/kube-apiserver-client
    usages:
    - digital signature
    - key encipherment
    - client auth
EOF

kubectl apply -f ${USERNAME}.yaml &&
kubectl certificate approve ${USERNAME}-csr
