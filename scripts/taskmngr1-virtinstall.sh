#!/bin/sh -e

IMAGENAME="taskmngr1.qcow2"
IMAGE_ORIG_PATH="$(dirname "$0")/../packer/taskmngr1-images/${IMAGENAME}"
IMAGE_QEMU_PATH="/var/lib/libvirt/images/${IMAGENAME}"

sudo cp -v "${IMAGE_ORIG_PATH}" "${IMAGE_QEMU_PATH}"
virt-install \
	-n taskmngr1 \
	--ram=3800 \
	--vcpus=2 \
	--os-variant=centos7.0 \
	--os-type=Linux \
	--graphics vnc,password=1,port=5900 \
	--noautoconsole \
	--import \
	--boot hd \
	--disk path="${IMAGE_QEMU_PATH}",bus=virtio,size=8 \
	--network=bridge:br0 \
	--mac='64:DC:B5:5E:38:10'
