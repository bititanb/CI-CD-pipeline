#!/bin/sh -e

IMAGE_PATH="$(dirname "$0")/../packer/taskmngr1-images/taskmngr1.qcow2"
virt-install \
	-n taskmngr1 \
	--ram=2048 \
	--vcpus=2 \
	--os-variant=centos7.0 \
	--os-type=Linux \
	--graphics vnc,password=1,port=5900 \
  --import \
	--boot hd \
	--disk path="${IMAGE_PATH}",bus=virtio,size=100 \
	--network=bridge:br0 \
	--mac='64:DC:B5:5E:38:10'
