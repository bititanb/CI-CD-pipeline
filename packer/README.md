# Развертывание с Packer/KVM

## Образы для KVM
> Сборка .qcow2-образов для импорта в QEMU-KVM с Packer

> Для развертывания без какой-либо дополнительной конфигурации используйте [Vagrant/Virtualbox](https://github.com/bititanb/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox)

### Подготовка
#### Зависимости

* [Packer](https://github.com/hashicorp/packer)
* QEMU-KVM
* virt-install
* 4.9 ГБ свободной оперативной памяти

#### Подготовка сети

Гость *taskmngr1* по умолчанию использует bridge на хосте с именем **br0** и MAC-адрес **64:DC:B5:5E:38:10** (меняется [здесь](../scripts/taskmngr1-virtinstall.sh)).  

Гость *taskmngr2* использует bridge **br0** и MAC **64:DC:B5:5E:38:11** (меняется [здесь](../scripts/taskmngr2-virtinstall.sh)).  

Создать bridge и убедиться, что обе виртуальные машины доступны из сети по доменным именам **taskmngr1** и **taskmngr2** потребуется самостоятельно.  

##### Конфигурация DHCP и DNS

Если потребуется ручная конфигурация, DHCP-сервер должен содержать записи вида
```
192.168.1.150   64:DC:B5:5E:38:10
192.168.1.151   64:DC:B5:5E:38:11
```
тогда DNS должны быть
```
taskmngr1   A 192.168.1.150
taskmngr2   A 192.168.1.151
```

##### Без конфигурации

Теоретически можно обойтись без bridge, но на практике пропускной способности сети может не хватить. Хотите проще, без настройки bridge и DNS — используйте [Vagrant + VirtualBox](../vagrant).

### Сборка

```shell
packer-io build taskmngr-common.json
packer-io build taskmngr1.json
packer-io build taskmngr2.json
```

SSH handshake errors в процессе — это норма, ждите до конца.

### Дебаг

```shell
export PACKER_LOG=1   # детальный build output
sed -i 's/headless\": true/headless\": false/' taskmngr*.json   # GUI (требуется virt-viewer)

packer-io build --force taskmngr-common.json
packer-io build --force taskmngrN.json
virsh shutdown taskmngrN
virsh undefine taskmngrN
../scripts/taskmngrN-virtinstall.sh
```

## Развертывание, используя полученные образы

### Импорт образов в KVM

```shell
../scripts/taskmngr1-virtinstall.sh
../scripts/taskmngr2-virtinstall.sh
```

### Развертывание

```shell
ssh user1@taskmngr1                                  # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml     # пароль: 1
```

### Доступные сервисы
[Описано здесь.](https://github.com/bititanb/CI-CD-pipeline#Доступные-сервисы)
