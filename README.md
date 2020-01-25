---

### 2020 UPDATE:
This was done back in 2017 as part of the [CI/CD demo](https://github.com/search?q=user:ilya-lesikov+topic:ci-cd-pipeline+fork:true&type=Repositories), before looking for a job as a Junior Automation Engineer. \
Now unmantained and left here for purely historical purposes.

---

How and why explained [here](https://old-demo.ilya-lesikov.com).

Repositories that are part of this demo:
* https://github.com/ilya-lesikov/ansible-taskmngr
* https://github.com/ilya-lesikov/taskmngr

## Быстрый старт с Vagrant/VirtualBox
> Развертывание с Packer/KVM [описано здесь](./packer#Развертывание-с-packerkvm) (требуется дополнительная конфигурация)

### Требования
* Vagrant 2.0 (https://releases.hashicorp.com/vagrant/2.0.0/)
* VirtualBox 5.1 (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* 4.9 ГБ свободной оперативной памяти

### Развертывание

#### Windows

```shell
git clone https://github.com/ilya-lesikov/CI-CD-pipeline
cd .\CI-CD-pipeline

.\scripts\hosts.bat         # от администратора, обновляет hosts

cd .\vagrant
vagrant up --provider=virtualbox

vagrant ssh taskmngr1                                # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml     # пароль: 1
```

#### Linux

```shell
git clone https://github.com/ilya-lesikov/CI-CD-pipeline
cd ./CI-CD-pipeline

sudo ./scripts/hosts.sh         # обновляет hosts

cd ./vagrant
vagrant up --provider=virtualbox

vagrant ssh taskmngr1                                # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml     # пароль: 1
```

### Доступные сервисы

Когда Ansible завершит работу, за сборкой/тестированием/развертыванием приложения в Kubernetes можно следить в Jenkins (http://taskmngr1:8080/job/taskmngr).

По окончанию будут доступны:

| Сервис | Доступ | Пользователь | Пароль |
| ----- | ----- | :-----: | :-----: |
| Приложение (production) | [https://taskmngr1:443](https://taskmngr1:443) | - | - |
| Приложение (testing) | [testing.taskmngr1:80](http://testing.taskmngr1) | - | - |
| Jenkins | [taskmngr1:8080](http://taskmngr1:8080/job/taskmngr) | admin | admin |
| Kibana | [taskmngr1:8085](http://taskmngr1:8085/app/kibana#/settings/indices/filebeat-*?_g=%28time:%28from:now-24h%29%29)<br>(нажмите <img src="./res/defaultindexbutton.png" height="20px"/> и *Discover* для логов) | - | - |
| Zabbix | [taskmngr1:8088](http://taskmngr1:8088) | Admin | zabbix |
| Kubernetes | # ssh user1@taskmngr1<br># sudo kubectl get all --all-namespaces | user1 | 1 |

| Виртуальная машина | Доступ | Пользователь | Пароль |
| ----- | ----- | :-----: | :-----: |
| taskmngr1 | # ssh user1@taskmngr1 | user1 | 1 |
| taskmngr2 | # ssh user1@taskmngr2 | user1 | 1 |

### Дополнительно
* Развертывание с [Packer/KVM](./packer#Развертывание-с-packerkvm)
* Ansible-роль для развертывания приложения [taskmngr-kubernetes](https://github.com/ilya-lesikov/ansible-taskmngr/tree/master/roles/taskmngr-kubernetes)

### Changelog

#### 1.0.1 — 27.11.17
##### Updated
* ./scripts/hosts.bat rewritten (fixed some bugs as well)
#### 1.0.0 — 26.11.17

