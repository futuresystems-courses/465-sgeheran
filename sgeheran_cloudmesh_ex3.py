In [3]: print cloudmesh.shell("cloud on india")
sgeheran
cloud 'india' activated.


In [4]: vmname = "sgeheran_cloudmesh_ex3"

In [5]: print cloudmesh.shell("vm start --cloud=india --image=futuresystems/ubuntu-14.04 --flavor=m1.small --name={0}".format(vmname))
