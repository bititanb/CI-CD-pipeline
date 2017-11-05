## Быстрый старт

### Требования
* Vagrant 2.0 (https://releases.hashicorp.com/vagrant/2.0.0/)
* VirtualBox 5.1 (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* 4.6 ГБ свободной оперативной памяти

### Развертывание

#### Windows

```shell
git clone https://github.com/bititanb/CI-CD-pipeline
cd .\CI-CD-pipeline

.\scripts\hosts.bat         # от администратора, обновляет hosts

cd .\vagrant
vagrant up --provider=virtualbox

vagrant ssh taskmngr1                                # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml     # пароль: 1
```

#### Linux

```shell
git clone https://github.com/bititanb/CI-CD-pipeline
cd ./CI-CD-pipeline

sudo ./scripts/hosts.sh         # обновляет hosts

cd ./vagrant
vagrant up --provider=virtualbox

vagrant ssh taskmngr1                                # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml     # пароль: 1
```

### Проверка

Когда Ansible завершит работу, за сборкой/тестированием/развертыванием приложения в Kubernetes можно следить в Jenkins (http://taskmngr1:8080/job/taskmngr).

По окончанию будут доступны:

| Сервис | Доступ | Пользователь | Пароль |
| ----- | ----- | :-----: | :-----: |
| Приложение (production) | [taskmngr1:443](https://taskmngr1) | - | - |
| Приложение (testing) | [testing.taskmngr1:80](http://testing.taskmngr1) | - | - |
| Jenkins | [taskmngr1:8080](http://taskmngr1:8080/job/taskmngr) | admin | admin |
| Kibana | [taskmngr1:8085](http://taskmngr1:8085/app/kibana#/settings/indices/filebeat-*?_g=%28time:%28from:now-24h%29%29)<br>(нажмите <img src="./res/defaultindexbutton.png" height="20px"/> и *Discover* для логов) | - | - |
| Zabbix | [taskmngr1:8088](http://taskmngr1:8088) | Admin | zabbix |
| Kubernetes | # ssh user1@taskmngr1<br># sudo kubectl get all --all-namespaces | user1 | 1 |

| Виртуальная машина | Доступ | Пользователь | Пароль |
| ----- | ----- | :-----: | :-----: |
| taskmngr1 | # ssh user1@taskmngr1 | user1 | 1 |
| taskmngr2 | # ssh user1@taskmngr2 | user1 | 1 |

## Подробнее

### Развертывание
#### Vagrant/VirtualBox (рекомендуется)

[Описано здесь.](#Развертывание)

#### Packer/KVM

[Подробнее здесь.](./packer/README.md)
