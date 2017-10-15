# Образы для KVM
> Сборка и установка .qcow2-образов для импорта в QEMU-KVM с Packer

## Подготовка
### Зависимости

* [Packer](https://github.com/hashicorp/packer)
* QEMU-KVM
* virt-install

### Подготовка сети

Гость *taskmngr1* по умолчанию использует bridge на хосте с именем **br0** и MAC-адрес **64:DC:B5:5E:38:10** (меняется [здесь](../scripts/taskmngr1-virtinstall.sh)).  

Гость *taskmngr2* использует bridge **br0** и MAC **64:DC:B5:5E:38:11** (меняется [здесь](../scripts/taskmngr2-virtinstall.sh)).  

Создать bridge и сделать обе виртуальные машины доступными из сети по доменным именам **taskmngr1** и **taskmngr2** потребуется самостоятельно.  

#### Конфигурация DHCP и DNS

Если DHCP-сервер содержит записи вида
```
192.168.1.150   64:DC:B5:5E:38:10
192.168.1.151   64:DC:B5:5E:38:11
```
, то DNS должны быть
```
taskmngr1   A 192.168.1.150
taskmngr2   A 192.168.1.151
```

#### Без конфигурации

Теоретически можно обойтись без bridge, но на практике пропускной способности сети может не хватить. Хотите проще, без настройки bridge и DNS — используйте [Vagrant + VirtualBox](../vagrant).

## Сборка

```shell
packer-io build taskmngr1.json
packer-io build taskmngr2.json
```

SSH handshake errors в процессе — это норма, ждите до конца.

## Установка

Импорт образов в KVM:
```shell
../scripts/taskmngr1-virtinstall.sh
../scripts/taskmngr2-virtinstall.sh
```

## Дебаг

Выполните перед сборкой:
```shell
export PACKER_LOG=1   # детальный build output
sed -i 's/headless\": true/headless\": false/' taskmngr*.json   # GUI (требуется virt-viewer)
```
