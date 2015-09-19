umount -lf ../chroot/dev
rm -rf ../chroot/root/workspace
rm ../chroot/install.sh
rm ../chroot/done.sh
rm '../chroot/eclipse installs'
mkdir -p ../image/{live,isolinux}
mksquashfs ../chroot ../image/live/filesystem.squashfs -e boot
cp ../chroot/boot/vmlinuz-* ../image/live/vmlinuz1
cp ../chroot/boot/initrd.img-* ../image/live/initrd1
cp isolinux.cfg ../image/isolinux/isolinux.cfg
cp /usr/lib/syslinux/isolinux.bin ../image/isolinux/
cp /usr/lib/syslinux/menu.c32 ../image/isolinux/
cp /usr/lib/syslinux/hdt.c32 ../image/isolinux/
cp /usr/share/misc/pci.ids ../image/isolinux/
cp /boot/memtest86+.bin ../image/live/memtest
cd ../image
genisoimage -rational-rock -volid "Debian Live" -cache-inodes -joliet -full-iso9660-filenames -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -output ../debian-live.iso . && cd ..
mv debian-live.iso $SF/debwini.iso
rm -rf image
